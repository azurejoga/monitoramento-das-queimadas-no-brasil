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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 864b1e74-07e2-3e80-8d2c-09c059466928 | -11.7245 | -47.4543 | 2025-07-12 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 600f8adf-166e-3f01-8faf-bcf33ce92273 | -11.7241 | -47.4766 | 2025-07-12 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 072847a0-186e-350a-94cb-5c747f8dedf6 | -6.0923 | -47.3129 | 2025-07-12 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 4289cc1c-d075-397a-8260-ab8f09e03fd3 | -7.4733 | -47.5149 | 2025-07-12 00:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 2665b259-e8b9-3182-9b78-c4dffea6791b | -10.8429 | -49.1236 | 2025-07-12 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7ff93058-ca57-30c4-83da-8b9905596b92 | -11.7436 | -47.4518 | 2025-07-12 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| abe15c6e-f87f-3389-949e-752be6cd73c9 | -10.8432 | -49.1018 | 2025-07-12 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| afb9cd7d-8a28-3eb0-b3c3-cdccbc430baf | -7.4731 | -47.5369 | 2025-07-12 00:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a8941d3e-f8a6-3137-b4cb-5a20341ce2aa | -6.1112 | -47.2897 | 2025-07-12 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ac30b108-e90b-3c74-8fd9-77db92d12f41 | -11.7433 | -47.4741 | 2025-07-12 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 636b28d3-77c6-3571-a2cf-fb79243e19e6 | -6.0925 | -47.291 | 2025-07-12 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 42f5f3cd-e2c8-315e-8077-4b13013452a1 | -10.8986 | -49.204 | 2025-07-12 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| aa1029a5-5091-3e8f-a9aa-682787568753 | -6.111 | -47.3116 | 2025-07-12 00:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c81716fc-2f1b-364b-bf3e-353a3cbe20cd | -7.492 | -47.5134 | 2025-07-12 00:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 67ce920d-ee1b-326f-9d70-9f5e270e26e4 | -10.8622 | -49.0997 | 2025-07-12 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 60047548-c0a0-3020-80b2-3b489978eb1a | -8.4622 | -49.6193 | 2025-07-12 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 1a516d2a-f961-314b-9c74-7715aa246283 | -10.8619 | -49.1214 | 2025-07-12 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 55955a32-49bb-3c1b-8c91-043d12d9b0ef | -8.4622 | -49.6193 | 2025-07-12 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 51dae53b-aeba-3a7b-8f53-062cfd50208e | -7.4731 | -47.5369 | 2025-07-12 00:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e03a60b9-f569-3bdd-95ae-6e18944b3500 | -11.7241 | -47.4766 | 2025-07-12 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| dd7a46f3-c8bd-31a9-8088-2eee094692fe | -10.8429 | -49.1236 | 2025-07-12 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e4a7d798-660b-3101-9334-3e0d166bed21 | -10.8986 | -49.204 | 2025-07-12 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 69c87ecf-3173-3825-a09f-226af9f80fd3 | -10.8622 | -49.0997 | 2025-07-12 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b12eea10-4b84-351d-a166-7a65113c6f68 | -11.7436 | -47.4518 | 2025-07-12 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9c8b7f03-8bff-3fae-92e5-449582072a0d | -10.8432 | -49.1018 | 2025-07-12 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 1219b5df-4e72-3475-9018-b5f6b9a7f17a | -11.7433 | -47.4741 | 2025-07-12 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 41cd9b69-ea0c-38e8-9ab0-3a7986eb199d | -3.7686 | -47.1136 | 2025-07-12 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 12b619bb-bddf-3eeb-8b3f-adc34b924008 | -7.492 | -47.5134 | 2025-07-12 00:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2fa43834-0b2b-3539-97d7-7f722216d4c2 | -3.75 | -47.1144 | 2025-07-12 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 39de8d22-796f-3456-9de3-edb9077be331 | -10.8619 | -49.1214 | 2025-07-12 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4113b6b1-3d96-3abe-bf86-214e34a87d5f | -11.7245 | -47.4543 | 2025-07-12 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 9f9f62e3-0549-3118-9799-f49e41f35ffc | -23.6997 | -51.723 | 2025-07-12 00:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| 24a031fb-3db8-35c7-9edf-27fcff23a052 | -8.4809 | -49.6177 | 2025-07-12 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ccfb13e0-ef1f-3a22-82a3-38c85758eef5 | -7.4733 | -47.5149 | 2025-07-12 00:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 280.4 |
| caa1140d-222b-349b-a5c9-9a4d1a8d6770 | -7.4731 | -47.5369 | 2025-07-12 00:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 088d12bf-6c2c-37c2-9c9d-a52f81fb9696 | -10.8619 | -49.1214 | 2025-07-12 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 833bf3c9-c0bd-3b39-bc34-3b6e05fd41a0 | -8.4622 | -49.6193 | 2025-07-12 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| b954bfa8-4bf5-347e-a368-7d20781d7984 | -3.75 | -47.1144 | 2025-07-12 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 023acdca-be2c-388b-9a7a-fa75770f56cd | -7.992 | -46.406 | 2025-07-12 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 26d0c575-625d-3e90-bb13-4b9a3581964f | -8.4809 | -49.6177 | 2025-07-12 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 97526ee7-9046-35bd-9e6f-e2cddbfad043 | -7.4733 | -47.5149 | 2025-07-12 00:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 41334a3e-b26e-3d54-855b-c14649bb9275 | -7.4545 | -47.5165 | 2025-07-12 00:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 71754fee-7993-36a9-bd2a-aa8558ff01ea | -10.8986 | -49.204 | 2025-07-12 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| db4ecd20-005d-3769-a06f-6c2f155c85a1 | -10.8622 | -49.0997 | 2025-07-12 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| fdb52904-c716-394e-ba64-16a40f30751c | -11.7436 | -47.4518 | 2025-07-12 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 81e2450d-14d3-3d8f-a5ec-86f8f27d6c38 | -10.8432 | -49.1018 | 2025-07-12 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8def30ef-4d90-31e1-ade1-a4d330fcab65 | -11.7241 | -47.4766 | 2025-07-12 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3c789529-62de-33e5-abd2-13314edab907 | -7.492 | -47.5134 | 2025-07-12 00:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 5ffd5ac6-40d0-3e74-9171-6c16208edb46 | -11.7245 | -47.4543 | 2025-07-12 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 99696788-5bb4-3339-a862-10ea2382992c | -11.7433 | -47.4741 | 2025-07-12 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e7248922-a446-344f-8280-952495d1d667 | -10.8429 | -49.1236 | 2025-07-12 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6696d731-4c4e-30bd-bf09-03d9f55494af | -7.2271 | -43.099098 | 2025-07-12 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e719d975-7669-3a03-8696-5912ab7e4a75 | -7.2157 | -43.094299 | 2025-07-12 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 39de33ad-224d-3a42-8d2e-9e3c40eab4ff | -10.6565 | -49.496498 | 2025-07-12 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5069c462-ac1f-398b-8e48-434ce6ceab15 | -3.7599 | -47.1063 | 2025-07-12 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d41273-94df-311e-bb0b-c1d80a92c6c4 | -7.9904 | -46.428398 | 2025-07-12 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cbd2b9f-e215-3383-b362-26275c6e711f | -11.4126 | -46.398701 | 2025-07-12 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 697c7495-dff1-3397-8526-044360f362ff | -11.4404 | -45.1096 | 2025-07-12 00:24:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1df005b2-792b-39c1-b404-314fcf119fed | -11.8337 | -47.5116 | 2025-07-12 00:24:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d10ec993-b411-38de-97df-589a4cb3dd31 | -7.9375 | -49.662102 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f711b74-504c-330f-8316-98cef68707ed | -7.4609 | -47.518501 | 2025-07-12 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7462eda1-567f-3253-b206-31349e0a5842 | -4.0923 | -40.981701 | 2025-07-12 00:24:00 | METOP-C | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cf987198-d933-3065-8d29-89346c0e2ac8 | -6.8638 | -42.7766 | 2025-07-12 00:24:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2eb9c81e-fa24-35b0-9de8-7137187d1337 | -11.4387 | -45.102001 | 2025-07-12 00:24:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7332bdde-e653-3361-b1df-34bf15916696 | -11.7284 | -48.522701 | 2025-07-12 00:24:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42acd660-fc0c-3a58-85fb-76d94e9b08d5 | -8.9222 | -47.351101 | 2025-07-12 00:24:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e101939-2485-3e12-b209-b121c6802920 | -9.7976 | -48.5648 | 2025-07-12 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6336e790-b5e1-3bf1-8d62-139fde65b070 | -8.4683 | -49.6133 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09426c2c-1e62-37bc-a36c-2f54005a26bf | -8.4585 | -49.615299 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61353919-046c-3898-9fde-8cc664865421 | -7.2189 | -43.1082 | 2025-07-12 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85627dc2-fbe8-338c-bbfe-59def86cfdb0 | -10.8522 | -49.114899 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4a0c02c-2ce7-3057-bc63-98b3ac9645a9 | -7.4727 | -47.5252 | 2025-07-12 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06b13e56-9b9c-3139-a103-f612603aaaf0 | -4.6057 | -43.319698 | 2025-07-12 00:24:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a57fd278-13b9-344a-a8d2-4ba84a9fbb54 | -7.9447 | -49.6479 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3859d1a-1945-37e1-b7b4-cd81ad77f5b7 | -7.4805 | -47.514301 | 2025-07-12 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f04a0bc3-d03c-3fd2-9317-a4d2d3518bbe | -10.8399 | -49.104698 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45389121-e8eb-305a-ad45-9ae8247beefa | -12.4211 | -43.498901 | 2025-07-12 00:24:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9a5864-e74e-3bf5-ad06-429f4067459a | -5.8352 | -48.382599 | 2025-07-12 00:24:00 | METOP-C | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 214fa7b5-f5e9-37eb-8a76-f2a18732e12c | -3.7536 | -47.123699 | 2025-07-12 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9218574-c36a-3ebc-9c82-f9372e927fb1 | -7.9949 | -46.402699 | 2025-07-12 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1daea224-64de-3e10-aa7e-e0c1493d5721 | -7.9473 | -49.66 | 2025-07-12 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42acd1ab-6151-3b44-91eb-54ba3809bb43 | -11.4186 | -46.379299 | 2025-07-12 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86c944d1-c2cf-3b58-9a97-a7ca80f7feb1 | -11.7231 | -47.472301 | 2025-07-12 00:24:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f154c910-ebae-382f-ac97-3b346065b4da | -11.7308 | -47.460201 | 2025-07-12 00:24:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2267bce8-9c91-3372-9a66-6613687a8940 | -5.8373 | -48.391899 | 2025-07-12 00:24:00 | METOP-C | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25946fb6-46fa-3487-bc33-81e0df62bc1c | -6.8736 | -42.7743 | 2025-07-12 00:24:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2b4b65a-31e1-3d91-b643-bcbcac3a1cd3 | -11.719 | -47.4524 | 2025-07-12 00:24:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c0b313f-49a4-392e-8a6a-131146d028d7 | -7.4707 | -47.516399 | 2025-07-12 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdde1e17-b738-3315-b2ae-c91467d31454 | -12.4072 | -45.351601 | 2025-07-12 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dacf9788-5343-34ae-b2fa-3b4ccd0c1896 | -7.2255 | -43.092098 | 2025-07-12 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d30f99c6-2a6a-31ad-add4-7f15e8ff0a07 | -7.4688 | -47.507702 | 2025-07-12 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| feaed127-aaf9-31ab-9197-30d6b829dde9 | -7.0779 | -49.610001 | 2025-07-12 00:24:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da28ae4c-4ce2-3b74-9a88-d2a9f245e410 | -13.1183 | -47.303101 | 2025-07-12 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7559349c-d7ec-3b4f-b58f-905c1bf8c33e | -10.8424 | -49.116901 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8231206-68e0-3f60-8467-ff3df0252dc2 | -3.9979 | -43.234299 | 2025-07-12 00:24:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2b562b5-aba9-332a-9b3c-031713a1a772 | -13.1204 | -47.313301 | 2025-07-12 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 606d44e7-cbc9-3393-bbf2-e19380ac4cf1 | -10.8949 | -49.222099 | 2025-07-12 00:24:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d25df76e-9714-3683-8245-751139765c63 | -8.9124 | -47.353199 | 2025-07-12 00:24:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b542e327-7402-369b-a5a1-6872681b5967 | -12.4187 | -45.357399 | 2025-07-12 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d73bc92f-ab47-3977-adf3-85ac62af3f51 | -3.4112 | -43.374401 | 2025-07-12 00:24:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
