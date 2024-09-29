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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faaa6fba-b16d-3010-bc08-879de406157f | -18.82776 | -41.97159 | 2024-09-29 04:29:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| cd3ec251-b582-3c01-977e-ec0a6a3311b6 | -18.78856 | -41.90039 | 2024-09-29 04:29:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| bc59afcb-f010-3283-8b2b-36c5729cdc97 | -3.96554 | -41.48928 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f92638d2-5961-3d8a-8ccf-614ac6cf4278 | -3.95972 | -41.48835 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 76ba6598-a285-3b2f-867e-1a3ce2e920ea | -3.95852 | -41.49656 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 5be83d9c-72eb-3e6d-8d10-4eb5fb9465f8 | -3.95791 | -41.50068 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 64fbc233-3ebd-385b-b4a5-9e1525947675 | -3.9549 | -41.52111 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5bbda6d4-dd48-3f68-9cfe-c30cbb15b97f | -3.9527 | -41.49561 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ab00bde5-1df0-399e-9481-dfd3c04c9128 | -3.9521 | -41.49972 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 26ad25be-2dcf-36e3-9548-0ec8df05f7b2 | -3.95149 | -41.50384 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 930b3469-ad44-3230-b02d-b16a925de36f | -3.95029 | -41.51207 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bb11038e-bdea-391d-89ee-1718fa92f731 | -3.94969 | -41.51614 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 762798c3-1677-30f3-bd2e-ddd00fdd8723 | -3.94909 | -41.5202 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b86c6741-c5f1-30b8-bb22-bc1cc756ed80 | -3.9485 | -41.52424 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 25740ebb-050a-30aa-a1bd-d39b35556b7f | -3.94568 | -41.50291 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 395c3132-e897-325e-a2a1-3b0d12db64e2 | -3.94508 | -41.50703 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5835b5b7-9133-3015-979d-ee6b3ab299f0 | -3.94447 | -41.51117 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 66012389-78a9-3368-9631-d015abfdaa79 | -3.94387 | -41.51525 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7fc9fe4d-8ce5-345a-99b9-c19e26e31760 | -3.79627 | -41.59111 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b06fa500-63fa-382e-8bf1-1adf22afdae4 | -3.79569 | -41.59517 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07df2cad-5e2f-3ab2-808c-f297d4b06993 | -3.79511 | -41.59917 | 2024-09-29 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0b816879-eca4-3331-9bfc-d6e4ccf6c215 | -4.8095 | -43.02652 | 2024-09-29 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06c5b1b5-d9b0-3c76-a6f2-d8a46b5aab4f | -4.80901 | -43.02987 | 2024-09-29 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acce437a-faff-35a1-a17d-72d99840f341 | -4.80416 | -43.02576 | 2024-09-29 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05a2f424-b6cf-3da7-9a1e-70c83cef629f | -4.80368 | -43.02909 | 2024-09-29 04:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23d65515-ccdc-36de-b39c-5e7fcb7fc8ab | -5.01131 | -43.80949 | 2024-09-29 04:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bb598298-f6cf-398a-a952-9f4470fb4c67 | -5.01089 | -43.81241 | 2024-09-29 04:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4b244133-196a-30c1-81d8-dd52b8a7d1df | -5.01045 | -43.81541 | 2024-09-29 04:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a6bd2a48-65b7-31a2-9774-19104b5da7f2 | -4.99945 | -43.81984 | 2024-09-29 04:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cb7c48e4-64ec-3cb5-ac28-9cdd1e989bab | -4.99903 | -43.82277 | 2024-09-29 04:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3bff7d5b-deff-3e63-a928-1fb5cd3fe77e | -4.71631 | -45.9251 | 2024-09-29 04:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c11b70e-2f1f-386a-bf85-a6eb3b00151c | -4.57881 | -46.06316 | 2024-09-29 04:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58b17349-18fa-3c09-a90b-396312f71496 | -4.44906 | -46.11952 | 2024-09-29 04:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19933053-9dae-3c45-b113-a4e771e24bb3 | -4.4448 | -46.11876 | 2024-09-29 04:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15a1750a-4e91-3a05-a805-979f9d86aa5a | -4.44419 | -46.12284 | 2024-09-29 04:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c123e9a-855e-3fd3-9476-ee9c46740bb2 | -1.1761 | -46.71709 | 2024-09-29 04:46:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade6fb1f-b2ae-3d52-80e7-9cf3e8826dc7 | -1.17218 | -46.7165 | 2024-09-29 04:46:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6146d0af-aeeb-3773-ba9e-a870581ae56d | -3.4698 | -47.53295 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee01bacf-2e10-3db1-8cdb-e30667b5f479 | -3.46905 | -47.53785 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f62c22d1-9d86-35ed-a469-9990a6d76faf | -3.21767 | -46.00382 | 2024-09-29 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2865ad45-273d-3dfc-a45c-2723f670a41c | -2.96079 | -47.3709 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f1c27a8-3d42-3208-8e11-4872b62a7711 | -2.72273 | -46.72716 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 230dbe49-d923-37e9-8940-3e9b823f5282 | -2.71925 | -46.72307 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f054d7-ba5b-3b40-9525-5ef8d9b7e6d1 | -2.71872 | -46.72656 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe59eb55-ea15-35f5-bcc2-d5dab8fecfc7 | -2.7147 | -46.72597 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77f42fc1-7132-32fe-8c09-77c33812c502 | -2.3761 | -46.54594 | 2024-09-29 04:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bafa95f5-7354-36a9-8a18-94e80cc9553a | -3.70199 | -47.6113 | 2024-09-29 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a49b2979-07bc-31d1-8505-ec32b1917405 | -4.3794 | -47.61343 | 2024-09-29 04:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c211a27a-6e5f-39f9-bae2-0fc2d6bcebbe | -4.3762 | -47.61518 | 2024-09-29 04:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08a874be-8511-33c6-8668-acc2d2bd432d | -4.37551 | -47.61292 | 2024-09-29 04:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31ae5d62-3a78-3e5e-aeaf-3bc08e312f72 | -3.91857 | -46.4621 | 2024-09-29 04:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9481956c-0346-305e-bb8a-b939b1b0d910 | -3.91441 | -46.46152 | 2024-09-29 04:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdcd6645-019f-34e2-a68d-eae27660735b | -3.91388 | -46.46516 | 2024-09-29 04:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66257149-2a04-3272-8f57-80eebfaaaccd | -3.91334 | -46.46878 | 2024-09-29 04:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41b41b2a-d7c2-355b-b35f-f6570ce85af7 | -3.91026 | -46.46089 | 2024-09-29 04:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 783014d5-a209-32f7-8795-63145ded4e6f | -2.0266 | -47.65583 | 2024-09-29 04:46:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32938216-7017-3a3c-9198-a7b2ff742d82 | -1.87209 | -47.90656 | 2024-09-29 04:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75a80dd3-d368-38b8-8e0c-92170c636e85 | -1.79047 | -48.0714 | 2024-09-29 04:46:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf87b44e-d1b3-31da-b80d-cd24411ed177 | -1.63369 | -48.6772 | 2024-09-29 04:46:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7697b069-e70e-30b8-aa93-2873b5d6af9c | -3.33346 | -49.03178 | 2024-09-29 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 348e3c22-7b04-3ff3-a6ce-868c7c1a2edb | -3.22252 | -48.92999 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24700755-62c4-30b8-9c85-b3347b114f96 | -2.92116 | -48.89058 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54568f77-5678-3b89-a00d-8e69ce029ff0 | -2.91761 | -48.89005 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6af8dfb1-0af3-3d84-9696-5f6070bf636b | -3.70126 | -47.61605 | 2024-09-29 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3463090a-5f4f-34ba-af04-3e3334f5da8e | -3.70052 | -47.6208 | 2024-09-29 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddaccdbf-ae79-36d4-8178-d8ed642742a4 | -3.69667 | -47.62028 | 2024-09-29 04:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d4bffe9-2544-36d5-b4bb-855f1656a0fc | -3.47011 | -47.65881 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24234a63-9b6f-31ae-b70b-cca7236f2416 | -3.46938 | -47.66356 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0937b82-8bd0-38e7-8048-e19c6276b662 | -3.41048 | -47.58741 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d87d4411-d96c-327c-95b4-670f1f3edddc | -3.40977 | -47.59214 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98c7fd19-3242-382e-a94c-a55c1a25710d | -3.40694 | -47.59386 | 2024-09-29 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2094726b-7292-3b5e-b44b-db5c81b68cae | -2.95048 | -48.60411 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e659b4a5-ccb2-3835-8f18-3eba3bd9f6b3 | -2.90024 | -47.88803 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79e4dc10-4d24-3c39-90b7-207052888487 | -2.80231 | -48.69669 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6ab67a3-b51d-3ea9-9d75-e810435710b6 | -2.80169 | -48.70076 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db943d11-6cd4-3243-b291-9ca98feaa597 | -2.79983 | -48.69713 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 089108e7-cf50-31d2-8df8-fc315c7e1e49 | -2.79919 | -48.7012 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bd80a0d-c15d-3e81-bc6b-17af530344ce | -2.79204 | -48.7001 | 2024-09-29 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27a7d999-0dde-3696-be6a-1400ef159306 | -2.63762 | -48.25329 | 2024-09-29 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0bf861b7-5f15-3b92-ab9a-2360ca0dd550 | -2.62335 | -48.32062 | 2024-09-29 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9aca502-0d9e-30a5-99c3-a23211536280 | -2.59163 | -47.6572 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 606ac253-e0a6-355d-b38a-2495e61e51c7 | -2.59092 | -47.66178 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1c22caa-61c3-30ec-ad52-fae9832cd08c | -2.58786 | -47.65659 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 216bf611-3ac1-3158-9869-22913897adce | -2.46333 | -47.8343 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cefe1bb1-d1d1-3e33-b722-b0d1e4c036f3 | -2.46264 | -47.83875 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bc4708d-d11c-374b-add7-0a116af50633 | -2.42393 | -48.59723 | 2024-09-29 04:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6da360c-3cb5-385c-bfb6-bef203be9412 | -2.41725 | -48.44901 | 2024-09-29 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22f62fa5-1ed2-36c9-b1b1-c399a2306c06 | -2.41661 | -48.45316 | 2024-09-29 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc05551-f475-3560-bce8-153aca655277 | -2.36369 | -47.60414 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 80645932-b5c4-38e3-ac65-91c322ccbf51 | -2.36299 | -47.60868 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| d995fce3-6650-3a71-8e59-5ebc410e72ef | -2.35991 | -47.60357 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1c594fab-cf1b-3005-a966-53517ffc53b3 | -2.35922 | -47.60811 | 2024-09-29 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 949645bc-2dce-33e5-bcc8-450150d5ec19 | -2.35544 | -47.60754 | 2024-09-29 04:46:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 797291c2-a013-3b81-907c-760c256f0764 | -2.35097 | -47.61152 | 2024-09-29 04:46:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72b83b33-67d4-39ce-92aa-025a3abfd087 | -2.25785 | -48.29123 | 2024-09-29 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc8fbced-cfe9-3ce1-99f8-38262326337e | -1.37578 | -49.34921 | 2024-09-29 04:46:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc1df95d-88ec-37f3-b747-73997dd32a96 | -4.23268 | -48.57994 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da7c4e4c-9535-3ada-993d-8287293b4f8e | -4.22774 | -48.58788 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5afcff3a-9291-3b71-a85e-d931035b18b6 | -4.22772 | -48.58949 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d86b28f9-57b1-3295-a6b1-55af4807110c | -4.22711 | -48.59213 | 2024-09-29 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
