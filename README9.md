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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7232d89-0182-317a-9d0e-1800f388686f | -10.43747 | -49.59367 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cbdc18b-1ffd-31ab-b726-4e18d2558162 | -8.59926 | -48.01443 | 2026-07-01 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 1ece7c7e-fa8f-328a-ac96-17a84828cbd9 | -10.37957 | -49.58954 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8b8ed82-5040-35d1-baf7-4493daea67d0 | -10.79703 | -53.54514 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53873821-0f66-39fb-bb2c-9e334e89556c | -11.49835 | -47.42558 | 2026-07-01 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6432925d-eba0-396a-b298-094d26566720 | -7.74839 | -44.19257 | 2026-07-01 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe6ffe80-a62c-34ac-8c27-1b1d2ced697e | -10.66944 | -54.56261 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6847ea9-3672-3e29-8b7c-02026ef39bcd | -11.24078 | -41.89145 | 2026-07-01 04:02:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ef91f8eb-6403-32d1-9372-3d4769f37663 | -10.91967 | -43.04961 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 87dd1ad4-9eb7-37ff-a25a-498e3a5e5a46 | -9.69978 | -47.69434 | 2026-07-01 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5af098b-b5a5-3864-967c-99da5a323703 | -8.34752 | -46.81839 | 2026-07-01 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b719f758-c0b3-3c93-af6d-313e1e3c3224 | -5.80048 | -45.04805 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae4836a5-d143-3449-b985-b76fa2451a45 | -7.7425 | -45.92086 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b129a011-74f4-387a-9640-9878458fd1a2 | -10.76369 | -53.54912 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 17133333-148c-3332-ba92-8ff02977eaff | -10.67477 | -54.53604 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 295f168b-0081-3971-983a-afd4b8fae9b7 | -10.44014 | -49.58869 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79731fbd-dc7d-3016-afe5-9dee39ca4cd8 | -10.91906 | -43.05344 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ac899cac-2207-3371-9f69-abf992e6d882 | -9.1963 | -45.32327 | 2026-07-01 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc5fa2f2-6225-31b8-b1d0-cab023bc5ba6 | -9.69948 | -47.69319 | 2026-07-01 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85738def-2ea5-3912-a537-5d8bb7d988a4 | -10.38015 | -49.58638 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac80be45-1d4c-3dfd-9421-bc98e43de3ee | -7.47516 | -44.74741 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c77afb3-1272-315a-93fd-68ef6c813e7c | -10.67495 | -54.57124 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b02f1a6-5d59-306d-9783-ae2fc5bdf4a4 | -5.80299 | -45.05229 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21e2102e-9bd4-36bb-a758-31f589e222e4 | -10.44192 | -49.57928 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9646510-2077-3984-9775-c37eaa323450 | -7.91406 | -48.238 | 2026-07-01 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4de0dc3-1d34-379c-a9ae-237e6abbc159 | -5.80237 | -45.05593 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ca7b78c-91f0-3b20-829f-940e6d0c639f | -9.88705 | -50.3972 | 2026-07-01 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 32f39928-0240-3409-b836-92b8c0208b75 | -10.763 | -53.54494 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2617139c-7f9a-3c70-a299-13e914909a34 | -5.80782 | -43.7975 | 2026-07-01 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c4171e11-a13f-3aba-8a38-d6db1342d0bb | -5.29375 | -45.30924 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05efbda8-3fca-32b4-8b1b-a576954f9735 | -11.92118 | -43.39468 | 2026-07-01 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 827a0c8b-e138-3357-809f-c4b4b77e0f4c | -7.00115 | -42.76893 | 2026-07-01 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a071f1db-34d5-3d73-b784-48bb4d6e14c1 | -7.75215 | -44.19327 | 2026-07-01 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eff901b-ce87-3bdf-8d2a-a8fa9df6ce93 | -10.43677 | -49.57831 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27b0f4f2-cfbd-3fb3-9764-39bc4b11023c | -10.67608 | -54.52954 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 8cfaf1f1-b7d7-3d44-a4c9-828fab393151 | -6.95958 | -44.55158 | 2026-07-01 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e88a67e4-0a7f-370b-a9a0-19413d97a5ed | -5.79812 | -45.06261 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e235ad0-086a-3dce-ab59-f9574a917fa9 | -10.13193 | -52.10223 | 2026-07-01 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e674749-2569-3908-b177-e5f398c29d49 | -8.59524 | -50.97647 | 2026-07-01 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd03f182-27ac-328d-ba9f-b217cf9a62fa | -4.35191 | -47.76602 | 2026-07-01 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 202a2c7c-3992-3ef7-98a4-3d4b4f572b66 | -8.78126 | -44.82423 | 2026-07-01 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12e67352-ba60-3911-90ed-fc7200ba1425 | -6.85909 | -38.35289 | 2026-07-01 04:02:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99920737-af2e-313d-bdf1-c10ca149606e | -10.92532 | -43.05395 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| bb73f74c-ccc2-308c-9093-8aaf159ef83c | -8.59447 | -50.98056 | 2026-07-01 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c98e6055-7f02-39a5-aa93-0546e0e293ca | -10.77253 | -53.53879 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 91be9f33-a3df-36e2-8a6f-d8401bd697cc | -8.60019 | -48.00918 | 2026-07-01 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9675274d-3930-3fe0-bb71-578442163e7d | -5.80114 | -45.06321 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea988fdb-bd25-3216-91b3-1aa5625930e8 | -11.91253 | -43.78094 | 2026-07-01 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a665f7db-d45c-37a5-a7db-010892a83baf | -10.92595 | -43.05012 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| e4c1b5b6-fc17-37bb-ad82-0ed0851db569 | -5.86089 | -46.25317 | 2026-07-01 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8dc7e85-0136-3562-ba40-6f64cf9b0af0 | -5.80281 | -45.05967 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67b793a0-8839-319d-9ea9-434e367875ea | -5.81161 | -43.79808 | 2026-07-01 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 393c2400-a71f-347a-9612-df7325094177 | -10.48292 | -47.09417 | 2026-07-01 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9bfc74b-61b2-3b84-ba16-a778834d3fed | -5.80222 | -45.06332 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecaa5156-8cdd-3e54-9bfd-cb99a304c6df | -5.81084 | -43.80275 | 2026-07-01 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b0af43d8-f5a7-3287-a3c6-2335ba6cbcf4 | -4.34683 | -47.76527 | 2026-07-01 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79bc1d2a-fcc2-3970-ae98-9d21c5cb32eb | -9.69517 | -47.69356 | 2026-07-01 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da5f52ef-05eb-32f8-b9c3-f68078b73f8a | -10.12767 | -52.09171 | 2026-07-01 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe458d9e-e5df-3b09-b504-c97c96010aac | -11.48961 | -47.39602 | 2026-07-01 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de5f0dc3-e914-362a-b65a-2a3253e87bcc | -5.55205 | -43.96621 | 2026-07-01 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a841766-5341-3d41-bf4d-92a6416fac2e | -7.0018 | -42.76491 | 2026-07-01 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5907331-397d-37db-b716-ef90a37a0a61 | -9.27551 | -48.7651 | 2026-07-01 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c98d63e1-4c07-3795-91df-346f5df4ecd3 | -10.68173 | -54.53736 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3d77cf6f-d242-33a5-bec4-1cb5fa844527 | -10.12157 | -52.09062 | 2026-07-01 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1aa9af4d-d665-391f-9180-2b3bf4f800b0 | -8.50922 | -50.15339 | 2026-07-01 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b14e7803-f9d4-334f-8319-3411e55eda3e | -9.75205 | -49.04341 | 2026-07-01 04:02:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 258c5dec-5e98-3c06-add8-fb647cd77cf5 | -10.75947 | -42.11065 | 2026-07-01 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0508b1e2-01fa-3e04-8389-e2f975c430de | -5.71359 | -43.23175 | 2026-07-01 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd515d3b-889e-3d40-ae09-2e2db03d70bb | -6.15812 | -44.64967 | 2026-07-01 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06d9c9de-b264-3652-83d2-f1968d489046 | -8.78307 | -44.82737 | 2026-07-01 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85a218d0-d493-3d92-b402-21ead28c7a34 | -11.91082 | -43.39292 | 2026-07-01 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e665269-7c33-30aa-8f40-01471dd82f16 | -10.43954 | -49.59184 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32d3734d-833d-323d-9061-066659c1473e | -10.57064 | -44.80612 | 2026-07-01 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 495aaecf-14ad-3511-9629-bbb38c206eaf | -7.74915 | -44.18798 | 2026-07-01 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53e56fe6-37aa-3461-9132-0fe3a0805bb6 | -9.67887 | -47.0275 | 2026-07-01 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aba7c16-b03d-353d-b923-b5da99881f61 | -11.54683 | -47.45771 | 2026-07-01 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1e6164ff-1e38-37fa-bf86-b7c48d6b33fc | -7.73474 | -45.91552 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e736a3c7-5c24-3e1d-a578-ba4cfbcda049 | -10.43919 | -49.58419 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec283c94-28db-379a-8683-d32a0f588978 | -7.91308 | -48.24354 | 2026-07-01 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 542ea0c0-fd67-3b7b-b9e7-38c61b8d226f | -7.29014 | -46.25541 | 2026-07-01 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06e2303a-4df0-334f-bfde-a3e99e344d32 | -9.75258 | -49.04044 | 2026-07-01 04:02:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a24a201-ff96-3590-b97a-19a88178270b | -10.76418 | -53.53916 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 614edf76-5840-315a-97cf-a7d0ca39ec6c | -7.7138 | -45.93616 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a6bf52c-1d61-305d-b444-0a343289750a | -7.21794 | -34.9563 | 2026-07-01 04:02:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 127df449-3ad3-314a-899e-d34c19ab5d64 | -4.34732 | -47.76234 | 2026-07-01 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 100cae97-0bf8-3b27-8b74-ab87b86fe0cc | -10.91562 | -43.05287 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fd96c3a-99e6-3a2f-8806-9816e0bf16b1 | -8.60113 | -48.00394 | 2026-07-01 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 97b822ae-717d-3a05-ad38-3e8b7c755e4d | -9.20026 | -45.32395 | 2026-07-01 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd077b50-8d7e-3db1-9b29-b56902e384a5 | -11.53368 | -47.45532 | 2026-07-01 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d731e41b-351b-324f-909c-f4372083f739 | -10.76005 | -42.10705 | 2026-07-01 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d05ed74-1a0e-32cc-9a71-20b3ea3d800c | -5.5584 | -43.96478 | 2026-07-01 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d579f8b6-265a-3d6c-8e7f-ba9d71e82b57 | -8.06173 | -46.7189 | 2026-07-01 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c367edcd-5a5d-3189-b4dd-4ab3ba499890 | -10.7714 | -53.54452 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0724e9a6-a83e-3e9d-8182-a541dc270707 | -10.38073 | -49.58324 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a1bdd40-5fc6-317c-af73-4189a4313607 | -10.43862 | -49.58733 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf1edf66-6946-3b64-9cb0-56b931c82ae8 | -8.34671 | -46.82296 | 2026-07-01 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6893dfce-0771-3db9-b649-c707b5c6bbef | -7.47488 | -44.74923 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7f77da5-5c58-3719-bb22-56d5ad04292c | -11.54321 | -47.45264 | 2026-07-01 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bcc76a09-a36c-3eed-b425-e38bc8e25750 | -5.54991 | -43.96838 | 2026-07-01 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03d01932-f895-3eb9-b97f-0a19970568e7 | -11.53086 | -47.44582 | 2026-07-01 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
