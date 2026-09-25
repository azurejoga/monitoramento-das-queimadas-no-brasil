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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c2f059d-b704-3b68-b00e-baa447b7f990 | -15.98854 | -42.99583 | 2026-09-25 03:51:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8a53ce2-9b96-3b75-861a-0e2003a00ecc | -13.21928 | -51.55702 | 2026-09-25 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07c12c06-cf47-307b-bc94-3149238d60c6 | -14.6767 | -48.76348 | 2026-09-25 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c49ddcf4-ffe2-38cf-b304-d5c66d03fdbe | -12.19727 | -50.74516 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c5daa338-46b2-3b4e-94e7-972742ace49d | -12.18163 | -50.75184 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8f7e7a4a-e01a-3d4c-a21f-f9a72f58e82b | -16.69874 | -50.66714 | 2026-09-25 03:51:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a06cfc3b-f1b8-3f33-9895-ee642c1c77f3 | -12.19357 | -50.72591 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aaea7290-1c62-38b9-8555-9107603b3fcb | -12.1954 | -50.72207 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3d7d3086-48a3-3b12-bff4-4d514f45db18 | -14.72816 | -46.22133 | 2026-09-25 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 360c4d0e-c488-3f5d-9121-0376485c2bed | -19.18807 | -47.36162 | 2026-09-25 03:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8e06ea5-6102-35a8-9c3d-9b1a450e2b2c | -14.73278 | -46.22219 | 2026-09-25 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7a4d9d1-2d1b-377c-bfb0-6f9c7ff4dd26 | -12.17385 | -50.79023 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d2399001-203d-3b0f-989c-787f050d9197 | -12.19085 | -50.74384 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5a119218-a622-33f0-b96c-a03d858138ea | -14.06567 | -44.06285 | 2026-09-25 03:51:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21eaa2f2-29e0-3301-a46c-ef95e91b7d0e | -12.17502 | -50.72357 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9a806101-5686-3bf2-93b1-c0bc16c3c05c | -13.24232 | -43.83768 | 2026-09-25 03:51:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9f9a037-5ea5-35b9-9ee0-776b2f79c4a2 | -14.51937 | -48.33963 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29ebe531-0715-3bf1-bf0f-9dedba14cb50 | -12.18284 | -50.78211 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| bb9bffc4-213c-3e1b-b60a-e1aae24a01bc | -12.19312 | -50.73296 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 13acd0f9-a8f6-3bdf-a2b9-8f154f6f6aae | -17.34495 | -46.93502 | 2026-09-25 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15396410-e9ea-3436-91d3-108d251b03e5 | -14.72432 | -46.22318 | 2026-09-25 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbd4d117-424a-319b-9b9e-4bcc2549087f | -12.18029 | -50.73032 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a7ba9f78-5deb-3d30-8aa8-7ce5abf5c352 | -12.19649 | -50.77778 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| eceed329-cc67-36c4-a1be-7761fffe7111 | -18.95621 | -46.95008 | 2026-09-25 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29603568-61f5-3214-b0ab-868a50970470 | -12.16007 | -50.79462 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16b69510-706c-3b00-9b05-8ebad8a5055e | -12.17434 | -50.72187 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 607f165b-9840-38d7-a89f-ee3e48d34b28 | -12.20029 | -50.76281 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e8dcba2f-9a10-392c-b2b1-a1e673c5be30 | -12.195 | -50.75606 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cef88f6f-ceb7-31f2-b51b-f073d960d74b | -12.1814 | -50.78608 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a8586928-aed3-3e1d-bb60-e280a6cd837d | -12.20369 | -50.74648 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 66a202a1-bee1-3308-9bb1-6ae6696ea193 | -14.77151 | -45.59024 | 2026-09-25 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed3bd562-6343-3f8f-90d3-6ba49f78b3be | -12.1987 | -50.7668 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| b182390f-3320-3b2e-9c70-ba4041af5d05 | -15.81276 | -53.10867 | 2026-09-25 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 394910a1-c6c1-3edc-8d32-caeb92aba036 | -12.19915 | -50.76828 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2b0d0867-67a7-3de7-b9ef-788a48b970b3 | -12.18258 | -50.71944 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a802821c-748a-35f2-beaa-edd62ebc382f | -13.84272 | -49.68407 | 2026-09-25 03:51:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5527e89-e1eb-3812-bf94-2dd427d3bab5 | -12.18857 | -50.75475 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 16650173-806b-3ad3-aedd-acc0800afcac | -13.55402 | -43.51577 | 2026-09-25 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce01239e-9e37-3b7a-9316-95d55192cfb8 | -14.93997 | -41.33186 | 2026-09-25 03:51:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b55e8d3b-c00b-37a3-a6fb-9e7418b50d19 | -12.18716 | -50.72455 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4303c411-505a-365c-ab04-7612b636b461 | -14.76881 | -48.47372 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7b42f7d-dc22-3968-ac2b-9a557c9c9333 | -12.18443 | -50.74252 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5db65f81-70ed-3e4b-a2ce-3aa8e59acd1c | -19.87826 | -47.06002 | 2026-09-25 03:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e2c2f6c-8964-3427-bcbd-d383e2cb1006 | -15.51575 | -40.01209 | 2026-09-25 03:51:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c15c19b6-093a-378f-ac1b-ec31cbb3cdf5 | -12.19467 | -50.72044 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4fd7ef4a-72d4-3f05-94f5-6dc4f96bc3cb | -15.98483 | -42.99524 | 2026-09-25 03:51:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84b4c2ef-3d8b-3d14-a5f8-393d1387a14a | -12.18895 | -50.78192 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e8655fa7-1677-3aae-b5a2-858be721ea94 | -17.14782 | -44.78675 | 2026-09-25 03:51:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dae2d04-7b53-341b-94ce-f23c6c3906da | -12.1663 | -50.79439 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 06163efb-8269-3188-b338-cc337a8447d6 | -12.16651 | -50.79594 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2f5b6960-17a2-3520-924b-1744d05952c8 | -14.70661 | -48.75582 | 2026-09-25 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a3c9c1c-fd36-3282-93d4-48d21890b3ae | -12.19448 | -50.75453 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 13850a4e-c8fc-3818-a91d-0c979e1bcfab | -18.96069 | -46.95098 | 2026-09-25 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a05fd5c-be70-3400-9126-9594c145baca | -14.70603 | -48.75869 | 2026-09-25 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93e2f7cc-a4af-33a9-83f2-c0757f01cd5c | -12.17964 | -50.72866 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3675be1f-8ac4-3111-95ad-dd6aab7cb29a | -12.19668 | -50.74361 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 027e95b2-fe74-3f75-9b3b-83e6084b74f9 | -12.20143 | -50.75735 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8b45ba2f-1d8f-3bdd-abb1-749f7bd6af2e | -12.16766 | -50.79045 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 551c06cb-0fff-396c-8565-3eb58e709090 | -14.76277 | -48.47615 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 184d1bee-fe6e-3c0d-b4a9-6d75470609ff | -12.18169 | -50.78761 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 84bed2b9-e15b-3db6-bfd4-31a5c99aa880 | -13.7298 | -48.97514 | 2026-09-25 03:51:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8f9aef5-f2aa-3eee-a07d-11d1c5a069da | -12.18805 | -50.75319 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 281ffec6-ad9c-382b-95ad-ce11eeb16e2c | -12.19199 | -50.7384 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9a00fa99-954a-35c2-9a34-b002851f58b9 | -12.18385 | -50.74092 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d0d87883-ea2e-3ffe-ae0d-1020abe95b81 | -12.19778 | -50.73815 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 22c74718-6138-32aa-9627-20d0dca02402 | -12.17411 | -50.79176 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 0f1d671e-ea24-37c5-ab66-971f383edece | -12.19426 | -50.72752 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e825a024-b4df-3096-ad6b-b5981a4f5947 | -12.19043 | -50.77794 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 462d6238-bfe5-3bff-90bd-a1b5326750eb | -19.87386 | -47.05893 | 2026-09-25 03:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2cb8b59-e336-31e9-bfcc-2e4e605b0451 | -12.198 | -50.77378 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| febb26c8-722d-396b-a61d-8938f0625eef | -12.19613 | -50.75061 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 765faf15-0e26-3aa1-b90f-178d4343108d | -12.18029 | -50.79157 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d11c46c9-5531-35b6-9faf-6c9fa0d8ac79 | -14.51396 | -48.33903 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6f34deb-f747-377d-8b7d-4126fd01b002 | -16.11482 | -49.94866 | 2026-09-25 03:51:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e884f27-ecb9-3620-b304-9114fd1ca49c | -12.18928 | -50.78342 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ca881254-7f83-3939-81dd-2062434cc556 | -14.51219 | -48.33728 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92c26bd0-c047-34a9-9633-26695c36cd6b | -12.18971 | -50.74929 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c1a846a3-c4a3-3b3b-95f2-765ac02457f6 | -12.19841 | -50.73972 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 31da9172-6657-3ff1-b99e-a751efc7f046 | -12.19006 | -50.77642 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 62cf90e3-f663-38d0-aab9-6c80a5f71094 | -17.10258 | -46.47307 | 2026-09-25 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b732a107-d12a-3848-bdee-9fae562fe593 | -15.08241 | -40.85818 | 2026-09-25 03:51:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 777f3e36-5c30-3fe2-88c1-0865d892a777 | -15.05296 | -43.62193 | 2026-09-25 03:51:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9de509a2-9891-395e-bc10-a6522abf82cd | -12.19558 | -50.74907 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1788b8cb-6fd4-3529-a154-36b6f5b18190 | -14.52075 | -48.33259 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a4463ab-f46b-30c2-8bc3-1dcf998ab643 | -12.2031 | -50.74496 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d12736a7-870c-3be8-850b-ef857f9c4336 | -12.18916 | -50.74771 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b4c14e7a-c933-36b4-95ab-1b9f75c5034a | -12.18826 | -50.7191 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 28b219ae-2856-363b-b5fb-d30136736c06 | -14.51291 | -48.33375 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52318cf2-f867-35fe-a22e-8b0171019f1e | -15.95835 | -42.95964 | 2026-09-25 03:51:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcecbc10-ad28-322d-9b4d-1b9b818f48b9 | -14.73181 | -46.22723 | 2026-09-25 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| acd68774-4e69-3ae0-a676-c1baad20a791 | -15.10921 | -40.43952 | 2026-09-25 03:51:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3282534-af5e-30e8-860e-44a9246d10ed | -12.18899 | -50.72076 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 015fb362-925c-39cc-926a-dcb891e42dd2 | -12.1998 | -50.76132 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1ca34136-85de-365e-896b-17f83ae33f7f | -12.19759 | -50.77229 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9e4d3a38-2fd2-3aa0-9bd9-f39a3623b111 | -18.95715 | -46.94535 | 2026-09-25 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f3e0e1-7538-39e5-94b9-2ea73334b568 | -12.20256 | -50.7519 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2ad2ce08-f8ad-351d-a879-b63ab7a1d3a2 | -12.19954 | -50.73428 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0fa4fdc7-7f9e-39b2-b9ae-71ba804196bd | -14.2239 | -48.51117 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91dddb9e-327a-3d23-b41a-19fd30ec89b5 | -14.51687 | -48.34153 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b774b550-bf2d-3955-abea-493d6f07471b | -12.19137 | -50.7368 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |


[Clique aqui para ver as próximas entradas](README14.md)
