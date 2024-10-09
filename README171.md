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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83e07c94-fb4f-380b-a437-9a9f0856c251 | -10.89735 | -49.14207 | 2024-10-09 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5890521-bc70-39f0-b39a-605315b5d8b2 | -10.89254 | -49.14158 | 2024-10-09 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 679a0c3b-0bcf-33f7-a70a-62a4d2cc6d43 | -13.6256 | -48.48627 | 2024-10-09 05:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6066f1ca-f0b3-35f5-bcd6-25e57c9a1cf0 | -13.62049 | -48.48484 | 2024-10-09 05:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64d81872-db61-33c5-a656-97fb5a6353d8 | -13.56363 | -48.65272 | 2024-10-09 05:04:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e2db1ca-e3a2-3e9d-9e8c-c3aa0764ecd5 | -13.56125 | -48.65153 | 2024-10-09 05:04:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28fac960-2958-3ec9-88e4-850e1dc46a27 | -13.56096 | -48.65389 | 2024-10-09 05:04:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fd71047-8e9b-3629-a696-c7198496e2d9 | -13.5582 | -48.6545 | 2024-10-09 05:04:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69dcf66e-1366-3fd3-998a-99493886efc7 | -13.55585 | -48.653 | 2024-10-09 05:04:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16b649fe-fcea-395e-b924-74e177b791d8 | -13.55553 | -48.65555 | 2024-10-09 05:04:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba3f2e27-922c-3ac6-b51c-1eba360a5171 | -15.07988 | -48.94496 | 2024-10-09 05:04:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e501f471-db9a-3d3b-b888-12c17d3ec229 | -15.07947 | -48.94839 | 2024-10-09 05:04:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ff32a73e-e840-340b-aa5c-3c1e8d9de74a | -14.79746 | -49.98789 | 2024-10-09 05:04:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8523815d-15d8-3175-bf3c-c0724898ad01 | -14.5618 | -49.8491 | 2024-10-09 05:04:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5bbd95c-ea2c-3d12-9e3a-3fc5d4620ce5 | -14.52975 | -49.16446 | 2024-10-09 05:04:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b6703bc-94cd-3a2b-90b8-7e72eb5fe25d | -14.5294 | -49.16732 | 2024-10-09 05:04:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc223888-2411-3e0b-b5f0-9662dff8312b | -9.33953 | -49.85119 | 2024-10-09 05:04:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d35ec95-f001-33ae-ac66-653556d1ddf1 | -9.12074 | -50.29529 | 2024-10-09 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 3682508d-a0b6-39a9-a4a3-3918a077bb3a | -9.12016 | -50.2994 | 2024-10-09 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 68e465a9-ef0c-3918-8735-989f2153ffcc | -9.11643 | -50.2947 | 2024-10-09 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d973e17e-78eb-3112-8d35-0c12ab6d9388 | -9.444 | -48.89043 | 2024-10-09 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65758797-68dc-368c-95b8-a5da174dfac7 | -9.44362 | -48.8893 | 2024-10-09 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e35eb29-9625-31ae-979e-816fceb2d233 | -10.54136 | -49.46471 | 2024-10-09 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28692aaf-307c-3109-81f4-6c9042ac244b | -10.52665 | -49.10827 | 2024-10-09 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ed64a68-18a5-3530-9396-38ae75f3449e | -10.52186 | -49.1077 | 2024-10-09 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db1b49c9-793a-3ac4-a08e-d83855668504 | -10.51708 | -49.10707 | 2024-10-09 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23a9e3bb-cb30-3f69-826c-01f999401d72 | -11.69759 | -49.96362 | 2024-10-09 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2655ef9f-be37-3c7d-a4a1-36ba046f1726 | -11.56044 | -49.90609 | 2024-10-09 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4059e23e-d796-39e3-9b96-cb0d780521e5 | -11.55521 | -49.91024 | 2024-10-09 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99a66890-e227-3d19-9abc-52f9e924f8fb | -11.55062 | -49.90962 | 2024-10-09 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d2399a0-469e-33fe-9346-132ccc48650e | -11.47096 | -49.48764 | 2024-10-09 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6db308b3-39b7-3da5-8f1d-8e624e0d848c | -11.4703 | -49.49269 | 2024-10-09 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f6fe51b-9b1b-3f31-ac18-c90ddbcab3ff | -13.18608 | -51.17391 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39298296-f805-39e1-9c9a-1ce8f694c5d9 | -13.18553 | -51.17806 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdc722d7-b4c2-3eb8-bdfa-b89d34cdd286 | -14.09847 | -51.08532 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f968d09a-bb6f-3815-9d48-73ed9b180f4c | -14.09797 | -51.08658 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 288f15c7-a51c-31e7-9be1-f1c7dffcfd3b | -14.09792 | -51.08969 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 514934f7-1d5d-3c3d-ac69-2857d90a01bc | -14.09739 | -51.09093 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af37d21f-6897-330f-9b65-15cab0f41098 | -14.09243 | -51.09468 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e312234-4d36-3304-b9db-9bae4dcebb92 | -14.09185 | -51.09903 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23aa0ecc-2fb2-3a13-ab32-e39b0f83d9d9 | -14.09127 | -51.10337 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c11ea76-8765-3c38-9156-a3c1050e971b | -14.09069 | -51.10772 | 2024-10-09 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e844007f-fca5-30b1-87b0-765d11af668d | -16.40387 | -51.888 | 2024-10-09 05:04:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0cfe724-5c84-39a1-b21a-9462d7906bf7 | -16.40336 | -51.892 | 2024-10-09 05:04:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d955e5b9-7f6c-3335-8bba-ada74662446f | -16.40012 | -51.88306 | 2024-10-09 05:04:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c10419e-2a2b-31d7-ad25-f4347e27e3d8 | -9.25185 | -50.36519 | 2024-10-09 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3344d12c-7998-3556-94b7-c7457a4bd590 | -9.24899 | -50.36657 | 2024-10-09 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe809a7c-7ee0-339a-af0e-298f0f072233 | -9.49231 | -50.98357 | 2024-10-09 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2562ede9-b73b-37a0-ac6e-a3bb6c1e0907 | -10.66584 | -51.81504 | 2024-10-09 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7b9943b-62f0-36ac-b71c-77cacd309d15 | -10.664 | -51.81306 | 2024-10-09 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0408c7c-d389-31cd-91fc-652984bf1a7e | -10.66325 | -51.81824 | 2024-10-09 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f076b968-662e-31c1-b7b5-5c409180dccb | -10.66295 | -50.91592 | 2024-10-09 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 79b01566-43be-3fe3-a8ce-e454b0cee1b5 | -10.66239 | -50.91989 | 2024-10-09 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b66aca4-08d1-35d6-941a-eaa317b82128 | -10.66126 | -51.81879 | 2024-10-09 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2583f037-85a5-39a3-8c4f-be2e845c6aa0 | -10.65816 | -50.91929 | 2024-10-09 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a37e6cf4-cab7-3ecd-a7ab-e80f4096a64e | -10.65394 | -50.91869 | 2024-10-09 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba994f79-6c30-3408-b67e-34e535465ee1 | -10.64916 | -50.92206 | 2024-10-09 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9e7e871-0c14-3fd6-b080-c36c6a05680d | -10.61482 | -50.92124 | 2024-10-09 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 349485af-f899-36ab-9294-610546e27acc | -12.01095 | -51.04596 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dba4579-0a9a-398f-99fa-0dc89839d2af | -12.00668 | -51.04536 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23193d88-638b-3030-a5b4-09f6fe43edfa | -12.00241 | -51.04477 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afba6c58-54cc-31c6-8f59-76db93ff4b41 | -12.00228 | -51.07791 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0851ea2a-3171-3c2b-ba05-1490164abf70 | -11.48013 | -51.86129 | 2024-10-09 05:04:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a72f0830-c06e-3dbe-be9c-3516a0506559 | -11.37547 | -51.09397 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3da0a39-1260-3abb-a901-b417a0e1ea34 | -11.37125 | -51.09338 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88c218cc-71d6-3bac-b804-833b6e2468bc | -11.35305 | -51.00562 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28858685-8a93-3db7-bbcd-c0d508a0ee6f | -11.35251 | -51.00962 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed220dd3-61d3-3b50-9af6-e2f6eb53c5e1 | -11.35196 | -51.01363 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 967a0642-21e4-30f9-a1e3-982558372be4 | -11.34772 | -51.01302 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c600f81a-77b6-357b-8853-5a117bf7dff7 | -11.32422 | -50.96648 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a758981-f127-3c73-8872-3b60ea263c0f | -11.32391 | -50.96468 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 436547ef-314b-3eec-b9ff-2ca14d3d268a | -11.32337 | -50.96871 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee92eba9-7f34-3ed4-9f5f-f00d1e6c67ff | -11.31876 | -51.31974 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c20811f2-45af-326b-b413-84de99065bcd | -11.31565 | -51.31152 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1d08c75-a224-3203-b796-51717d974d1d | -11.31513 | -51.31533 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc991575-d9b7-390d-8533-e971421d4a6f | -11.31097 | -51.31473 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5883d527-2cc4-39ef-91cf-16ceff0efba5 | -11.30933 | -51.41889 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47e05cdb-3fe8-353a-926e-bb458e886805 | -11.30882 | -51.42266 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46056b57-53ba-39a0-8ec0-3a3471af78dc | -11.29475 | -51.08413 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 415fdc1e-cb2d-3cfe-b96c-b906ad54fd49 | -11.2942 | -51.08806 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90fcec56-0fef-3a09-bb06-e67eacf5c7e3 | -11.24917 | -51.28776 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 762c18c8-1404-39c8-9199-0bbb356ef50c | -11.24714 | -51.27188 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4ad3f7a-282e-3383-b5a5-dbff2ad34b9f | -11.24501 | -51.28716 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16732d05-a9a5-3589-9f26-b24653c223f6 | -11.20182 | -51.35475 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f4d3bdf-2075-3cce-9a0c-18dd462a7a65 | -11.19717 | -51.35791 | 2024-10-09 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 958e590d-da87-393a-8ed0-ea609164d064 | -11.18529 | -51.38317 | 2024-10-09 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a63197d1-ccea-36be-8582-460c2ebd4207 | -13.15301 | -51.67266 | 2024-10-09 05:04:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef8b205a-7b63-37b5-bda8-15a6a0b30a99 | -13.15248 | -51.67654 | 2024-10-09 05:04:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76dfe3db-e4cd-3f9f-b84c-e89f7649cd3b | -16.00238 | -53.07594 | 2024-10-09 05:04:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eee35a96-bbf0-3a50-bd2a-b60036c03f66 | -15.99971 | -53.07342 | 2024-10-09 05:04:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d22e4e2-3237-3142-a826-d85836f89b98 | -15.67722 | -52.52035 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 343393de-82f8-3f5b-8a34-401e7906ed56 | -15.67509 | -52.50487 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5691c279-cead-30d4-8f0f-d72d6cb5d4c5 | -15.6746 | -52.50857 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 48ce346e-cec9-304e-aaf5-c8ea30206e99 | -15.67412 | -52.51226 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4458f793-6052-3099-a806-d9f62e1a3073 | -15.67363 | -52.51597 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6308406f-604f-37e3-b4c3-bb3d37af3154 | -15.67005 | -52.5116 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b83bc8d3-f8c9-30fa-81af-141653263563 | -15.66956 | -52.5153 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6ad02607-5f4d-3dc4-add3-25af1e534797 | -9.47383 | -52.10185 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e7358a1-ad64-32a1-b45c-0bc57227d4ea | -9.46613 | -52.10072 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61ed1b9d-830d-3cd0-8bc9-bb8191aaf94b | -8.98558 | -52.79646 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README172.md)
