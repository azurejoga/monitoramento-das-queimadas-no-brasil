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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82575720-8944-3aac-83a6-39965709ae76 | -7.19506 | -42.96754 | 2026-08-01 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 473d88a1-95b5-3b13-9938-f01fbe5acee0 | -7.19999 | -42.97928 | 2026-08-01 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e65d7c1d-89a5-389d-ae2b-07cfc694d739 | -3.05556 | -39.92866 | 2026-08-01 03:34:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 19998004-d15b-3b23-a4ac-87fea9c5cb1d | -6.54096 | -41.86738 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8e986e63-cbdb-3027-a6ea-ec36b6117311 | -6.54496 | -41.84533 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d35f3b4a-db23-3f4b-9e51-1724fc7767ea | -4.26399 | -38.03738 | 2026-08-01 03:34:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0fffcd8e-74cd-3283-add8-bb3568a6a541 | -6.54058 | -41.86974 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bed32567-2327-3b28-b483-beaf2ea48bdd | -7.24739 | -42.13722 | 2026-08-01 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| f8a1ae49-3740-32ed-8cdb-7b9632adab17 | -7.19585 | -42.96329 | 2026-08-01 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e205555b-037b-3361-89c8-27ffd02bdd3b | -4.25959 | -38.03664 | 2026-08-01 03:34:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 5315c1a4-274b-3673-9e57-4b4b5450c83a | -4.52466 | -38.54778 | 2026-08-01 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fcd5e5f0-2c84-337a-b60d-5a44b7fc394c | -5.7535 | -43.26853 | 2026-08-01 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b96334f-44db-3675-a86d-3b34a1ed610d | -6.76493 | -41.01058 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 73d0031e-e1cf-35f7-acac-5b89b200aaea | -6.27334 | -41.87418 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5dd11af7-e56c-3339-9669-c6532092feb4 | -6.54122 | -41.86608 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53133083-a61e-345b-96a9-b77808d379db | -5.55177 | -43.96836 | 2026-08-01 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c0ff4303-ffc2-3307-9d57-849519a767c5 | -3.06115 | -39.92662 | 2026-08-01 03:34:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0b26c101-7268-30ed-b7cd-ccbf2f91f1dd | -6.67015 | -42.56836 | 2026-08-01 03:34:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c787b758-6fbc-3bac-b821-13542d9c45e3 | -6.75866 | -41.01596 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3694e8f0-28f0-39c0-af43-b050d058435d | -7.32022 | -43.0038 | 2026-08-01 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a0fd897-5412-38fa-a0ff-d0d2c7eb9ad4 | -6.64546 | -43.91834 | 2026-08-01 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a536603b-6754-31f2-8021-f2fa02560544 | -5.55081 | -43.97369 | 2026-08-01 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2a0d3790-b87c-37b8-8b0f-5bc66d595733 | -6.53949 | -41.84429 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c139032d-4b2f-3427-a5a3-3c06cac54da0 | -7.20075 | -42.97505 | 2026-08-01 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da1fb7c8-1eac-3c71-b083-4ca492dac99f | -6.66944 | -42.57229 | 2026-08-01 03:34:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6352e43d-d61e-3a1f-9366-5774234fe6a6 | -4.26469 | -38.03308 | 2026-08-01 03:34:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| dcf8e5d0-1d4c-3e92-96e0-8c3613246b01 | -3.05045 | -39.9278 | 2026-08-01 03:34:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9ebfd0a4-3f95-39f9-8de6-0baaedfbb5b1 | -4.26478 | -38.03191 | 2026-08-01 03:34:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c82703b3-7848-3a83-a944-838fbfc57f8a | -6.76086 | -41.00338 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20b010c8-6fa6-3fd8-836f-c9a044181775 | -7.24684 | -42.13762 | 2026-08-01 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c1a3a910-4b77-33ce-8782-3b48b455135f | -6.27887 | -41.87508 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 73c2014f-1f1f-3884-9e03-c64155105388 | -4.652 | -42.43233 | 2026-08-01 03:34:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| aa6aedf3-6c86-3092-bce7-92743c6fa813 | -6.75976 | -41.00967 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf9c534e-6ef8-3320-ab33-14580f9036a7 | -6.22707 | -38.25887 | 2026-08-01 03:34:00 | NOAA-20 | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ba3f52ce-06ea-3814-b1cd-446a162913cc | -6.27271 | -41.87776 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 928b8420-253e-326c-bd62-716e03c0b2a2 | -6.75348 | -41.01509 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0486cd9-cdfe-3713-bc4e-ede0fc90d0ee | -5.55717 | -43.9749 | 2026-08-01 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 872c9f99-2fcb-31e9-9033-788ef6916e79 | -7.62527 | -38.80012 | 2026-08-01 03:34:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 94ea59d7-bf4c-35c8-addd-930664b3e3e7 | -7.94097 | -37.16795 | 2026-08-01 03:34:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 908e7323-d665-366f-9ac0-12593f278f2c | -6.75458 | -41.0088 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 29f01ed1-dd3a-340c-8f6e-ba7ae0101719 | -6.54506 | -41.84395 | 2026-08-01 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfb8c332-069a-3026-8d72-b5260f596f63 | -6.76438 | -41.01371 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87e662a7-b00c-3eca-a241-cd067a7a0b76 | -3.79832 | -41.60919 | 2026-08-01 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb6794ff-664d-3112-b786-c86322ff0a4c | -4.65126 | -42.43657 | 2026-08-01 03:34:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 88d84ba7-6dc7-3a5b-bf19-f01b88e70209 | -5.04156 | -43.26517 | 2026-08-01 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5b6d4b8-90a1-332d-8262-9874af29c460 | -7.6073 | -42.58485 | 2026-08-01 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48ce93bb-12fe-3f36-8681-bec7fdda792a | -6.42309 | -43.71668 | 2026-08-01 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9810de4-2b00-3d73-bf4e-80d625f21850 | -7.60657 | -42.58881 | 2026-08-01 03:34:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7d50d785-ab1b-3504-b975-b286406dcb75 | -3.79899 | -41.60534 | 2026-08-01 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 60114dcd-e7cf-3157-ab50-1c82a9f1c36f | -4.25519 | -38.03591 | 2026-08-01 03:34:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 49e3ea20-39e7-3d1a-bda5-49de7c1f04fe | -6.42398 | -43.71189 | 2026-08-01 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ad01ad0-0c75-33c2-9b3b-7fd69628be18 | -5.01136 | -38.67244 | 2026-08-01 03:34:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1860667e-b531-3413-a2a5-3e8596db12b0 | -3.05606 | -39.92567 | 2026-08-01 03:34:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f23b1b64-f3d0-3c3d-b901-285bbe135d1d | -7.24751 | -42.13393 | 2026-08-01 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 13340ffe-f0bb-3d2d-9a49-7a07ed55638b | -4.2559 | -38.0316 | 2026-08-01 03:34:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 1a27d2e2-da4b-30ec-8ab9-ddbb7b53b0e7 | -6.76031 | -41.00653 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2267094-b3ef-397c-bb1e-684508899ab0 | -7.31944 | -43.00801 | 2026-08-01 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a8d6211-8c77-301c-853f-9d71e5d6bbf5 | -5.75392 | -43.26975 | 2026-08-01 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c206df72-52e7-3ab0-8bc9-b6b74e74ebf9 | -6.42488 | -43.71533 | 2026-08-01 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0bb1796e-e07f-34dc-8182-10f7329ae9fd | -5.8105 | -44.76246 | 2026-08-01 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5253a53-82a5-3db9-9b95-b772b630f243 | -4.26405 | -38.0362 | 2026-08-01 03:34:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 9cac2d54-92b7-320e-bc17-19633b5be43d | -6.75921 | -41.01282 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 73934631-f55c-3640-bc0f-7cfc91f44d31 | -6.72178 | -44.01666 | 2026-08-01 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c6ec191-f13e-3a29-b9ba-f46d80a6a960 | -6.76383 | -41.01685 | 2026-08-01 03:34:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 421d3c66-bf0d-3ead-a0ce-a4d092489e90 | -7.19004 | -42.96217 | 2026-08-01 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd7d48be-5a10-3132-a2a2-a3adc76f7a64 | -5.55814 | -43.96954 | 2026-08-01 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8f2c6122-b6d6-3bab-8227-55a1eda5f0d5 | -6.71556 | -44.01522 | 2026-08-01 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dd9cbc61-193b-3f1f-9ae3-78f5bc976d42 | -12.30623 | -43.72835 | 2026-08-01 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b3e09f0-eb47-3b6e-9049-6d439bedcc22 | -8.96588 | -46.64542 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cd83be6-cc21-35ee-97da-0ef60637de33 | -8.34563 | -45.98888 | 2026-08-01 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 506cfafb-9697-37a7-855f-9f33d28d0739 | -12.60958 | -44.61823 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbf42565-a74d-31ee-b47b-d3626d588564 | -12.41454 | -40.92517 | 2026-08-01 03:36:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa957bf5-1cac-3c4d-9be4-ae1dce4a75d5 | -7.64033 | -45.05048 | 2026-08-01 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13a1738a-84d6-3661-9d59-801a2f96c9fc | -7.49859 | -45.8388 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccb44a1e-db66-39cd-b5c8-a80d97b0affa | -12.30696 | -43.72458 | 2026-08-01 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59171bf1-7236-3645-b23f-2d9895ff41b7 | -12.6105 | -44.61376 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bea9c9b5-4ce0-39c3-bdcb-31b6d783f863 | -7.49685 | -45.84519 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c9bf9acf-4720-3d3e-8855-4df6f36aa80e | -11.95355 | -40.60434 | 2026-08-01 03:36:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e25aa4e6-f3c6-35d0-8f9d-f3250b5a3d5c | -12.61903 | -44.60192 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25ec5e42-e821-395d-a4ac-11f382f91117 | -7.5055 | -45.84001 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a413f21-ab21-3474-b9bb-40ae951363c1 | -12.69774 | -44.74549 | 2026-08-01 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 601f5c39-e3f2-35a0-9ec7-f32ee0aece2f | -12.61814 | -44.60632 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e645191f-c343-3311-968d-420ef1c495dc | -7.64689 | -45.05181 | 2026-08-01 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e8944ab-e7f7-3fd2-815c-341ca88306eb | -8.96989 | -46.64757 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32ba0750-8c0f-383d-b428-cfe4d3d96d5c | -11.93648 | -43.43534 | 2026-08-01 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbd97564-eaca-30c1-b027-8af3021de4b9 | -7.49736 | -45.84525 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be58d5a7-da33-3b4b-858f-3bd9a15db2a2 | -8.97295 | -46.64673 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c68ba37-4dac-3e13-b8ce-7cfabe2911a4 | -7.50503 | -45.83994 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ae1f69b7-7c1e-35d1-9ce4-383481c67b3d | -13.8531 | -41.33959 | 2026-08-01 03:36:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9958683c-090f-3e0f-8cbd-b2ca49bf347b | -9.90431 | -45.74673 | 2026-08-01 03:36:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 856a270d-88b5-3851-bbd0-4e6654cbcc7e | -12.69683 | -44.74995 | 2026-08-01 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f18339ab-953b-3791-81a6-5fcba4552f85 | -11.9547 | -40.60251 | 2026-08-01 03:36:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4cae8877-d46d-33f4-ab92-6c9f983c518d | -12.60653 | -44.61373 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf183951-1f1b-3f45-a2ee-6255d2b721d5 | -11.95446 | -40.59951 | 2026-08-01 03:36:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c253bd0-afde-314a-b3c1-90093d55b317 | -7.64484 | -45.05231 | 2026-08-01 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c42538b8-0711-3b2f-822f-a6a113802bad | -13.05756 | -42.02339 | 2026-08-01 03:36:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a10a8137-df9d-3810-83d9-61cdc0b40cd2 | -7.55286 | -43.99261 | 2026-08-01 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3dbe2c7-77f7-3ff6-9a69-151ff50d3ef9 | -8.33811 | -45.99097 | 2026-08-01 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 726ef540-4ded-309b-9319-e1e5fa2d8d73 | -8.34498 | -45.99225 | 2026-08-01 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02f9c8f9-5c63-3446-b44c-7ce57ea3de61 | -12.6114 | -44.60933 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
