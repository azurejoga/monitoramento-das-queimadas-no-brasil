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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80afa583-b90c-3f29-8519-e3b927245858 | -8.071 | -48.01557 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c893bbca-97b3-3a4e-9c5b-1f55781133e3 | -7.85437 | -46.47112 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a2d3633-f5e8-3495-9afe-4d54c4ec51c5 | -7.77749 | -45.40403 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 183a400e-b02d-3dcf-9efa-5d7d51779cdb | -3.98402 | -55.74459 | 2025-10-27 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfc27eb5-c0cc-3970-98bf-13b34f08cc1f | -4.83058 | -45.34575 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf44f51e-3282-3de0-b671-65ae1b4e73f8 | -6.82625 | -41.20483 | 2025-10-27 04:32:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 02d63de8-9aa3-3d28-ade0-8660c6b6e613 | -9.95584 | -47.06596 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12c5cdad-0c8f-3492-ba14-835d77a7c886 | -7.89528 | -47.24348 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4edab675-fdec-3f20-b2c6-dfbbb2723a46 | -9.30272 | -45.21837 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eb2fd25-fc53-33ca-af7b-aa74eaa11369 | -8.6631 | -47.11706 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73175758-9d18-3049-97ea-27db315b9c3e | -7.59767 | -45.68847 | 2025-10-27 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c452b0d4-696e-3690-b893-26aa24555670 | -7.23615 | -44.98344 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa0f2b32-c33c-3a7c-b409-7a2a20660531 | -7.88756 | -47.24948 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff56029a-2eeb-3a99-905c-f936f952845a | -7.87749 | -47.24804 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8dd675-bc4b-3764-b705-f557d98000eb | -7.83629 | -46.45366 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0571740-c705-3757-8bd7-5f7380c4f583 | -5.64266 | -47.63671 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e7aa90e-689e-3533-af56-0a1738d047c9 | -8.58158 | -45.10701 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90eb6b65-a0f6-3be4-9212-bc6da8714f9e | -7.86498 | -46.4244 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1233fb2c-a30e-35bb-a543-b4cc5635fbb6 | -9.14539 | -45.84165 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3e08a1f-2e92-3495-833d-9106ad5c93e1 | -5.65531 | -41.10144 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 150f9b5b-5f9e-3885-b032-6a4970aa70fb | -6.26271 | -51.72459 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3e38b51-f200-3364-ba9c-3e609e227a2c | -4.46793 | -43.4265 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dffd9b80-4081-3d6f-bac7-12dfddc9d25c | -8.03047 | -46.76377 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c0e79c59-f042-39bf-9497-1f8a472d56ab | -8.69685 | -44.42529 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7768717-60bb-361d-a906-25d839e215dc | -6.39078 | -45.76554 | 2025-10-27 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e47b99f-d9e1-3ae0-b2ff-c8748adbaf5f | -3.24462 | -48.77506 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77ff6fb9-277d-3cdb-a071-e5f7ae085d3a | -5.81596 | -40.81858 | 2025-10-27 04:32:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1797c0a8-45fc-39fc-9078-c36539f9cc88 | -3.89701 | -42.67631 | 2025-10-27 04:32:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31c385a9-8909-34fc-8ecb-01c9ae757651 | -4.834 | -45.34627 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cdd66aa-6a2a-3cd4-9218-37cce931cfa4 | -6.18536 | -47.80419 | 2025-10-27 04:32:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8ef2e51-c6fd-34c1-bf78-e305dcf94646 | -5.30794 | -44.87514 | 2025-10-27 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76100ba2-fc17-3421-9946-b4af7ef31a92 | -4.86636 | -43.2495 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc07bb2d-b810-3dee-8583-d1258fc10e59 | -5.51951 | -41.71992 | 2025-10-27 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 313786a2-1a9d-3abc-a383-fedc7c672923 | -7.84805 | -46.4219 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c19a0a4-25cc-3aa0-a7a6-f663ad936716 | -7.82892 | -46.43392 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 150e8781-2ee3-3026-aca2-b145c63ab1be | -5.77627 | -51.56106 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 712423a3-a2e7-3cf2-ab40-3555b061cc01 | -7.94943 | -47.22314 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24a9b7ef-67e9-37bd-a9a1-8948759c1611 | -3.27165 | -50.04762 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ff8c0de-f1db-3ca1-84de-8f0741f0511f | -4.45582 | -45.45294 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 07ea6d8f-828c-39c7-b6c2-38326ff46a86 | -6.12797 | -42.44931 | 2025-10-27 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fc97ec8-7ee3-34e1-91d5-65ed0620528a | -3.42197 | -52.43568 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81207cfd-0d09-3a02-aaf4-93279e210cb3 | -7.24989 | -44.96503 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a2387d9d-6dd1-350b-8aa3-5f02cb4fbfef | -5.64636 | -41.09444 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| accf1329-828b-3d00-8cef-d4fde40d8f92 | -4.36074 | -48.66868 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa3f2c58-4aca-3546-a2c9-910f62390292 | -3.23945 | -50.65071 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e87d02c-5324-3188-bfef-756d54922a82 | -7.83753 | -46.49083 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2e7df50-9fee-3295-9e7e-67f1c97b45c1 | -5.71416 | -49.31135 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9feff1ee-2f28-3009-96d0-b74cc7c59b7a | -2.44575 | -49.03044 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b735314e-c0ae-38ce-8aa5-1225d6bc1821 | -4.25475 | -48.13179 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c60ac95a-ac59-328b-a9a8-43dff05a1d4c | -7.0753 | -47.35448 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5318ce97-e06b-3f26-95ed-a06e4fdf5459 | -6.85865 | -46.93124 | 2025-10-27 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdda39e2-d708-3322-9e8e-28b76827acf9 | -7.36554 | -42.43912 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f76b851e-33f1-32b3-bbec-8458c9504d15 | -3.46958 | -49.96512 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4d87379e-fdf1-3ec6-ba0d-883768bf1800 | -3.24244 | -50.65565 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 616af027-7591-36f1-8343-c25c75b5e1b8 | -2.78542 | -54.41964 | 2025-10-27 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b68f52b3-f80f-3e30-b17d-b32d111896d2 | -8.05125 | -46.95735 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2d9e7c7-21c9-3f2f-8573-93a57cfc3a3a | -5.53911 | -41.40492 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 966e8a87-ae48-35ac-bd5f-026c45372de8 | -7.41799 | -46.38951 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9506a352-7a7e-3052-8417-a9eddc2e914c | -9.21204 | -46.35365 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec744894-6aaf-32b7-a2c2-fffe30471d41 | -6.61161 | -38.63813 | 2025-10-27 04:32:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 71c796b1-dbcc-3d79-964e-90f5f84da8b4 | -3.23112 | -48.75061 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab08f604-acf0-36c2-9db4-62b5b89d9680 | -8.70129 | -50.81186 | 2025-10-27 04:32:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64885cca-8f6c-3c11-83b5-4f696584eb39 | -7.83685 | -46.45001 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 470b0a71-e3e5-3d4d-aff6-e33e7fdaf0a6 | -9.48372 | -46.85615 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2320ca5f-998f-3d51-aa5d-b1e397de6e54 | -5.60387 | -42.77856 | 2025-10-27 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64a2180d-650e-3985-9de3-26a290fff88e | -3.04817 | -53.02424 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4e13c26e-7a36-300f-8166-ac3ec567e9eb | -7.15367 | -44.49005 | 2025-10-27 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3f78218-4159-3b3e-af88-698930b19eea | -9.71809 | -48.92705 | 2025-10-27 04:32:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cbc9f45-1c92-3fc1-aba1-40cb9b8a052a | -8.02821 | -46.75612 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 489164f5-c671-32df-b528-658a33db03b8 | -3.05313 | -53.02095 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0bfa8e4-3994-34c7-bba1-2ee7be80b126 | -5.33925 | -44.71374 | 2025-10-27 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6e7ba29-832f-35fd-9ecd-a644f8de7cd3 | -7.95059 | -47.23769 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8db3895c-ec4e-335d-aad7-d3e1eaa27277 | -3.89567 | -42.67937 | 2025-10-27 04:32:00 | NOAA-21 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3796267b-c589-36d6-81d2-24c09890b8b3 | -2.77576 | -54.56948 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7a66fbd-2c37-30c9-8431-afd0d6772ecb | -4.65229 | -46.33007 | 2025-10-27 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caffcca1-97e8-38af-be06-066b9817d086 | -7.94286 | -47.24368 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cea086a-e56a-3ac9-ade2-b16bb6f23923 | -9.78697 | -46.98442 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19221c90-e794-306b-affd-1b917094ce84 | -5.25303 | -42.48439 | 2025-10-27 04:32:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c0da541e-e5a6-3b7e-916b-0d540fe4d1d2 | -4.37115 | -46.80565 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9992dda7-3f53-3a93-9634-7513cc89e4b0 | -7.93051 | -47.19145 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5db0725f-60ac-3e97-81cf-58eb171ca6eb | -2.93317 | -51.94504 | 2025-10-27 04:32:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4147d1f8-a414-3f9f-b4cb-7e37168427aa | -9.22281 | -50.75658 | 2025-10-27 04:32:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 469c3c96-3d57-3969-ad9a-15450904fe73 | -7.77107 | -45.39892 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e4f8577-9ed2-353a-9dae-f3b579b92a47 | -4.42793 | -48.91109 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 397df9c4-f48b-3016-96b9-c7d365e345f0 | -6.17113 | -41.57786 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44dc26cf-a4ac-359f-8e7c-b087ab9e566a | -7.68575 | -46.65928 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5682c46a-f15e-3cf8-8591-81a9073fce21 | -7.23434 | -46.943 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b44d284e-3342-3b69-90a7-5108375164d1 | -5.47525 | -37.85303 | 2025-10-27 04:32:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 89d893e0-e8d8-3fcb-a7cd-6c176488ce79 | -3.72372 | -47.6578 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3807096c-4c8a-3aa5-906a-a8d58848f1be | -7.13005 | -47.02396 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ec494dd-88fb-37b7-9f86-fbdfd52c713c | -4.73685 | -41.48442 | 2025-10-27 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10ea3c8e-5d1c-3fa4-8959-f4cab2579bf3 | -7.86816 | -45.7125 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10705505-d366-3ecc-9e85-f66f6d85b7bb | -8.03156 | -46.75664 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06a16b20-0a30-393e-8d6e-590402aea8d8 | -9.57956 | -45.18787 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7baa1455-9775-3a0f-87de-2e97b362b7c8 | -6.78795 | -41.00343 | 2025-10-27 04:32:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d3b285f1-c01a-3520-a371-20fad2df8a44 | -6.23798 | -44.63454 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 254afe66-c05b-3c74-bc08-9ca1cb5e283f | -9.55867 | -46.93114 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a334a2f-a8af-368a-b043-2814349a25a0 | -7.15602 | -43.73901 | 2025-10-27 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cd247a2-477d-3edc-91b3-a4f3f622dd07 | -2.79733 | -48.89351 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80461159-b4e1-3cbc-8176-851e9551dcfd | -7.0416 | -45.72749 | 2025-10-27 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
