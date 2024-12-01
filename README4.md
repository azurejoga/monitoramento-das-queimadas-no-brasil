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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee8a0f2f-9212-301e-b3bf-a119fa16bc64 | -10.6657 | -44.50148 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a128a5b0-03cb-3333-be0f-67f5fb024206 | -4.49994 | -43.60866 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8545e32-654c-3279-8e16-e797af6c6123 | -5.91373 | -43.84233 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 80b14db3-edf3-384f-b7f8-ab702fcec90e | -4.70055 | -46.55391 | 2024-12-01 00:32:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b98d6699-9792-3a8c-a489-a22a27ed321b | -8.13583 | -44.47489 | 2024-12-01 00:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5e5e3afa-972f-369e-bbbb-571fb7c26ab2 | -4.26576 | -47.61861 | 2024-12-01 00:32:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3ffdaa1f-4f73-3f08-ad84-92cf5760adef | -4.41072 | -48.5951 | 2024-12-01 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e048e62a-7fe7-343f-8840-6960827a8276 | -4.8777 | -41.32748 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 56f5f0bd-3e83-3d0b-bab7-392e9da6fbf8 | -10.08108 | -36.38317 | 2024-12-01 00:32:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 046c205d-fc90-3543-aaaa-39ff9e8d706e | -4.26376 | -48.34817 | 2024-12-01 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e0f605c1-e524-3ba8-b557-0c50422bedc8 | -11.08077 | -44.31008 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4560db83-c206-31b9-a239-92cd1b0055a7 | -6.06065 | -41.92939 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 25ecc715-e1f0-3271-9e88-4ed0848745dc | -6.93311 | -43.5521 | 2024-12-01 00:32:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 4df00921-3577-35e9-99a7-fc7d943aa71b | -6.67437 | -39.33291 | 2024-12-01 00:32:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 49a4b7c2-f48e-35aa-941f-2d53c4275968 | -10.52244 | -42.41997 | 2024-12-01 00:32:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 463a7414-5baa-3056-be28-6481314ad95e | -4.69946 | -42.40108 | 2024-12-01 00:32:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a1faf74f-af38-3ac2-a3d1-8d352a10305e | -8.75039 | -38.78975 | 2024-12-01 00:32:00 | TERRA_M-M | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ae0e615e-33aa-3721-b643-7126e93dcb32 | -4.68387 | -44.07366 | 2024-12-01 00:32:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7352a388-3b1f-3479-9208-1fc5e3e11439 | -7.25125 | -39.84944 | 2024-12-01 00:32:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7d403870-bbfb-3aad-b16c-8969b827dc58 | -4.18377 | -43.98442 | 2024-12-01 00:32:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c4d0e740-2587-39fd-8c35-d9eb1f6e4f84 | -4.26394 | -47.6055 | 2024-12-01 00:32:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b899fb98-2c97-39ad-a013-cf468fdaa856 | -4.55854 | -45.71664 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 225.6 |
| e1691d06-4e30-3e2e-9afc-19ca034b4a73 | -4.03021 | -43.07736 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b808e0a-f8fa-3781-b539-b460e87c73f8 | -10.65489 | -44.4925 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| da56f1bc-d79d-3dc7-b01b-ace626686593 | -3.98287 | -46.75881 | 2024-12-01 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 63c661f5-99eb-376c-9601-f7e3a22894ee | -6.71395 | -47.2817 | 2024-12-01 00:32:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 04736d14-9f59-34f0-85ff-1833a79d443b | -6.92246 | -43.55085 | 2024-12-01 00:32:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d12fd3cd-b77e-3ad2-8aac-18382232faf9 | -4.55157 | -43.577 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| da51c0ab-4b65-38fe-9ba4-8591bc36f3db | -4.66653 | -44.94734 | 2024-12-01 00:32:00 | TERRA_M-M | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 02c94657-ff71-3a88-9b0d-11d193bda66c | -4.31901 | -48.08292 | 2024-12-01 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 77cc353f-70ae-38af-90c9-c483b28720a2 | -4.96847 | -41.31721 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f51b2f88-c77e-3490-8219-0a6f5587c74d | -9.5263 | -37.03055 | 2024-12-01 00:32:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 50.3 |
| f23521ec-8dd0-3d4d-bb7a-e0e8f151e66e | -5.7318 | -43.98997 | 2024-12-01 00:32:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 060d542b-cf40-3cf9-85e3-7cf4adb43b25 | -6.262 | -43.16441 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0bc50453-9678-3961-8695-cbcc270e2e0a | -6.93188 | -43.54315 | 2024-12-01 00:32:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 79d60b6c-bab2-34c0-a716-8b041463d59a | -6.75962 | -46.53027 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ed87bc4a-d511-3f44-942f-c007998c2547 | -4.52851 | -45.74742 | 2024-12-01 00:32:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7dcc5359-2d72-3357-9e52-0c2a5da22245 | -4.83097 | -41.30977 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 11dbdd32-5ec3-3235-aa71-8f1225d68877 | -3.98132 | -46.74724 | 2024-12-01 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fa59610a-15a7-37fd-a407-14d3e4d08d01 | -3.9658 | -45.73955 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f1ae0c5-ae8d-369f-8154-c28c3cdb7337 | -4.69047 | -42.40237 | 2024-12-01 00:32:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 06af3696-0d73-3546-837f-7246ff1257bc | -4.26474 | -48.35712 | 2024-12-01 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| ac8eaed1-1ccc-3504-bcd4-bf347bf90df4 | -4.05378 | -46.83019 | 2024-12-01 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 31b4a9fe-0160-3b9f-bb37-42c5adeca353 | -4.554 | -45.72306 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 1d62307a-c5c0-349e-a430-839de713b38e | -4.25916 | -47.6136 | 2024-12-01 00:32:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 45e7afb0-0011-3226-97fe-8651adeb5f0c | -6.91997 | -43.53296 | 2024-12-01 00:32:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 653ecdd8-ba50-30ec-9d44-52c44233fa4f | -5.61211 | -45.06529 | 2024-12-01 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 13e3844e-7b93-3046-bd99-72751f9eb694 | -5.26559 | -44.35004 | 2024-12-01 00:32:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 528a2972-eda8-3c66-9518-76ef9f867f3c | -4.53234 | -45.70543 | 2024-12-01 00:32:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ba23ba90-25d4-3bce-8b6d-97a8f4937861 | -4.88841 | -41.33557 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c1f2e41d-998f-39db-a97e-33b536760a9f | -4.74624 | -43.71759 | 2024-12-01 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf389bac-c8f0-3fcb-9a77-e9f1568b53ad | -4.14118 | -43.87304 | 2024-12-01 00:32:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f523d07b-2c55-3e85-90ed-fe04f1c4dbf0 | -8.28226 | -41.35691 | 2024-12-01 00:32:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8e1622dc-3de8-3956-a3b5-4cb263d8aca9 | -10.07821 | -36.365 | 2024-12-01 00:32:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 16.2 |
| e1379125-0088-3362-ba10-f4723bb43f61 | -4.5271 | -45.73717 | 2024-12-01 00:32:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 749c9a36-0ccf-3d0c-b14c-e96543e3db6d | -6.4218 | -35.17998 | 2024-12-01 00:32:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 40.8 |
| 08c632ab-f34a-3861-95bf-ddcca26f38c9 | -6.11775 | -42.20152 | 2024-12-01 00:32:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 90602aab-6af7-37bb-a019-a27d3325fa61 | -5.73057 | -43.98101 | 2024-12-01 00:32:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9d841603-107d-3a79-a63a-7156c3b46f9e | -4.55261 | -45.713 | 2024-12-01 00:32:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 391fa137-8962-37c9-8043-1a94b56740fd | -4.32169 | -48.09127 | 2024-12-01 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 093b52b2-73b9-3870-8dec-1b1e3695503c | -4.26985 | -47.61238 | 2024-12-01 00:32:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 388da3dc-e4a9-38d7-b18c-998dbd4ffe97 | -4.83233 | -41.31933 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b003a6c3-21a8-3a08-a7f5-03b0e7447132 | -4.90356 | -47.14587 | 2024-12-01 00:32:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b329b875-15c0-32c2-a992-edcdd40ec09e | -6.29294 | -43.85564 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0e554594-5f74-3b99-9d5c-f74f7fb36bc0 | -3.69522 | -43.12218 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cdd6dd65-fd4d-30ea-bcaa-42de6c9d0f86 | -4.68533 | -42.3659 | 2024-12-01 00:32:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3434aaac-59f4-331e-9c51-3de002eae000 | -6.92121 | -43.5419 | 2024-12-01 00:32:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 9c8f75c5-8c72-37e3-bdaf-4bfa0bc13506 | -6.71219 | -47.26808 | 2024-12-01 00:32:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f6eaeb99-7917-36e6-a7ef-cc7e25013488 | -4.55988 | -45.72664 | 2024-12-01 00:32:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 186.9 |
| 951d69c8-e791-3ab6-993c-546b472711b1 | -11.0761 | -44.317 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9296d7d5-388e-3e70-a753-9e33d127042c | -4.53096 | -45.6954 | 2024-12-01 00:32:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| eb9f431e-7022-312c-b51f-24e7f0e7abff | -4.54886 | -43.29819 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f1b63975-06d6-3776-9cc8-a10f42a8e603 | -4.09247 | -44.85542 | 2024-12-01 00:32:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| faa64b86-021d-3654-82e4-866c4ac46663 | -4.8684 | -41.32915 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 841dd7f8-8e99-3b7e-bf62-2f5ee39a6c5f | -4.21416 | -47.71956 | 2024-12-01 00:32:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 33924fd3-851f-3830-a48b-d9090a9500bd | -5.01889 | -43.23718 | 2024-12-01 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3df88b0b-2cc0-3875-b15b-0e7e930e1cad | -5.19288 | -43.95624 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fea99f41-6c0d-35fb-a0f2-3c710ca58b25 | -4.55034 | -43.56817 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0c76d13a-74b7-3f81-b70b-e346dfd04a58 | -3.22431 | -45.77 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 133.2 |
| f38adfb3-2ba8-39d4-949f-a2e314034eea | -2.68766 | -51.71787 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 3ba6b034-0f7c-3edc-aaf3-84d7499b6447 | -2.74867 | -46.1161 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 114ba313-e4e7-3f93-b289-044e0b227291 | -1.07628 | -47.0182 | 2024-12-01 00:34:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1e11902d-a095-3e47-a8b7-f0a642a855fd | -3.30537 | -50.02967 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 9844b8d5-3463-39fa-bb77-918696ea8f49 | -3.79505 | -48.09981 | 2024-12-01 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fb3b0f57-d5cf-33c6-b765-e688b75c707e | -3.46731 | -50.26432 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 248.8 |
| 8a1c57d1-e40b-3e8c-81c4-502a69364fae | -2.07963 | -46.66916 | 2024-12-01 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad29271e-158d-34a2-bc95-c2749e67df1b | -3.58895 | -45.07574 | 2024-12-01 00:34:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3697342c-e84e-38a7-b63f-fcd6ebc2aeef | -1.70342 | -46.15614 | 2024-12-01 00:34:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 36012f7f-ed14-3c3d-bd4e-59ca241c4000 | -2.66091 | -51.86039 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2fd3184f-9903-30f6-9246-75a8c277ea31 | -3.22838 | -45.1315 | 2024-12-01 00:34:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1320046c-53e7-32c4-883d-bcc2516f6f81 | -3.31811 | -50.02794 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| be898aec-c59d-3e42-9e04-e5c9ccdd1b33 | -3.21364 | -45.76147 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8417405a-1598-3ca4-a1f7-1cf4ce97920f | -2.92973 | -51.45474 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f22fff83-281b-35d3-b8ee-d0023c3b9aa9 | -3.05457 | -51.06395 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 40e84d2c-646c-3cc7-ae2c-b127bc04568e | -2.20649 | -45.66346 | 2024-12-01 00:34:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 1ce53558-02fc-3949-a5bb-984a21078b6b | -3.30881 | -43.52337 | 2024-12-01 00:34:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 612413b8-418c-3019-9f89-1b09b9ac5526 | -2.0983 | -46.2806 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3b23cc2b-2b9a-3f12-8e9c-9c41d44d89b1 | -2.92621 | -51.46023 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| b386d318-bf79-32f3-aa6f-b7a23309e2e2 | -3.14424 | -49.40707 | 2024-12-01 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| cb9d56dc-92fb-301e-9f95-8b2ac2539eb7 | -2.69124 | -51.74392 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |


[Clique aqui para ver as próximas entradas](README5.md)
