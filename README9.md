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
| 4a5609aa-74a6-3af2-ba1a-ab399ca7704a | 1.00342 | -59.47798 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6508692-3266-3ce7-bf9e-2303d87509c1 | 0.30319 | -60.44797 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37b52c63-472c-3489-a335-f943427463bb | 1.10943 | -59.20068 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b078348-f47a-3919-b57f-cf4b22bc159e | 0.31324 | -60.4464 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d23f93fc-3c9d-3b5d-a256-0a4eabe28636 | 1.16775 | -60.37178 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2038000-ddbe-3a0c-8279-d0bcf2967294 | -6.72591 | -69.04118 | 2026-03-04 05:25:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf87c92d-ef44-3182-91bd-87a8ca6b30f7 | 0.47982 | -56.01845 | 2026-03-04 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3ea00adc-2351-3b04-9d8a-c5eb3a49ea39 | 0.8929 | -59.78914 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ed4e32-f609-3db7-8396-6953ea509259 | 0.31268 | -60.44285 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da2fc293-6d9f-3c1f-bb63-38262fc66448 | 0.16086 | -60.68486 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9e2d5ef-4b9d-312d-b0dd-6671bedbd4e1 | 0.06302 | -60.99627 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b716d744-eb01-3386-8acb-4be6170a24a4 | 1.01109 | -59.50499 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a940bc68-a4b1-3f52-a7d6-9fc3c05f2114 | 0.49437 | -60.51252 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdd428b3-4470-3c6e-8922-5d97db1f97ae | 1.08622 | -59.24645 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e811c54e-35c7-3cbc-bf86-dcda2ef47ec1 | 1.08291 | -59.25088 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d99f3ec-91a0-393d-942c-6cd65cddc7ec | 0.67016 | -60.35767 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6aa7e1e1-1fbf-33b2-bde9-8ef2e83c9154 | -0.15346 | -60.75941 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab59b364-7bea-3681-8a06-ea0fde2df9e2 | 0.04685 | -60.98754 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 9da0b9e4-290c-300c-bd64-b6f7a4ddd069 | 0.09173 | -60.62954 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d26679bd-1d0f-32c5-98c9-68d048abc9cb | 0.04346 | -60.98808 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| e2fc9881-cfa5-3fc7-bf11-2ec7d719632c | 0.46184 | -60.39391 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f1215ff-3def-397f-8d96-3945d30b75fe | 0.05422 | -60.9901 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0f95afd3-3c16-335e-9a55-5614268c2c8c | 0.05676 | -60.97846 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 418ec4fd-1d23-327f-8317-b164b1ac03b6 | 1.11328 | -59.20359 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76bec4a3-0519-393e-b79d-b269fce6de92 | 0.99866 | -60.41642 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cbf9a0b-284e-3dc6-a949-29908cbf98e1 | 0.04627 | -60.98389 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 672ceb33-ed02-318f-b303-936088ae9fd5 | 0.45458 | -60.39141 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad36aa5a-fa30-3271-bafe-6fe85a13caf3 | 0.95064 | -59.44395 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c4094db-b606-32a6-b2e6-41f1d50ae896 | 0.49158 | -60.51662 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2edaccf7-3699-383b-b44e-adffb5a3441a | 0.87411 | -60.46851 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ec8b69b-2304-3828-9f94-350c7d5daa69 | 0.05132 | -60.97192 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7d52dbfc-ab6f-3841-b8b0-43f9bbede1c6 | 0.70122 | -60.08261 | 2026-03-04 05:25:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4a118c4-55b1-31b9-8cac-3250064f535a | 0.27709 | -60.6226 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4758a0b3-e3a3-3628-8294-474f8bc0c238 | 1.07686 | -59.25534 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7951c97-c040-369a-a541-995372f74c84 | 0.96501 | -60.53164 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 909861e8-80cd-3a26-ab7e-53f42b8e5d76 | 0.27653 | -60.61903 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24712e29-355a-34ef-b78e-f3ae6c26ba52 | 0.05025 | -60.98698 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cd5ade74-63e2-321a-a945-79636869e439 | 1.21946 | -60.61394 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da94ab5e-ba48-3e20-a0f7-4644f820b3ec | 0.3043 | -60.45506 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c82fc88-9964-3611-8f3c-9e9dd47a7c48 | 0.05451 | -60.98628 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8c1bfe7-2e50-339b-9e6c-2acc3579778e | -8.60746 | -64.7747 | 2026-03-04 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 921a9180-ba1e-3b5c-856a-ca6ff18120aa | 0.30598 | -60.4439 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ac8cd9e-9940-3481-95f7-44a7724f0e6a | 0.65459 | -60.00045 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 831535b8-6be9-3629-92bb-99de20c33213 | 0.30986 | -60.49053 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97b6f7ca-ee56-3d40-b12d-6b4b59384bab | 0.77008 | -60.47696 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d2a7067-ac56-3abc-a1d3-f23726457128 | 1.06591 | -59.48574 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a2c93e-c5de-3f91-be84-4cf45cf01977 | 1.06369 | -59.49313 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 622fe38e-dd88-354e-a9c2-19894c149a8a | 0.88475 | -59.41595 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d4e0775-1cd7-37e1-ad86-5a2dd9e70df0 | -13.2476 | -53.86056 | 2026-03-04 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 016f3fc0-59a3-3bec-839f-5b99d4380f6a | 0.05223 | -60.97175 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51c623d9-15e3-3cfb-8f08-8e85aba6b445 | 0.49547 | -60.49775 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0916e3f0-0846-3fe7-bb55-fa15f4b5d9ac | 0.08037 | -60.53652 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 428aa2df-7e1c-39dd-a005-f46bcbf05c71 | 0.08041 | -60.55835 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7da87b70-5e2a-3e1d-8801-4247734cdae2 | 0.28662 | -60.61746 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e883a56b-c09f-3960-84df-43ef29ae4628 | -0.15009 | -60.75889 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1979a43-4d20-3aa4-8bce-7725f8b812aa | 1.03182 | -59.46286 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eed40178-88a2-3009-9af1-3e723ee9ba1f | 0.45012 | -60.40662 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 826a1594-061e-3595-8c02-9e4dd03a5883 | 1.20648 | -60.61966 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec04f24a-81f6-3bbe-bbc5-97277a264df0 | 1.02388 | -59.80018 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1f342c8-57d5-3bba-a883-a03e1a2695b0 | 0.0389 | -60.98131 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 02105909-a1fe-3cd7-82d3-334ea321c89e | 0.4624 | -60.39746 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b087a7af-c114-3db5-aeae-ea704c9e2598 | 1.0593 | -59.48677 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 654d573b-120b-3484-9f21-44c935e1e59e | 0.0519 | -60.97553 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 721ce389-2c83-39d2-8968-3435adeb1117 | 0.76013 | -59.89518 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7182cc47-24a3-328a-a948-37e8ea32a2ba | 1.13019 | -60.51673 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947e6c7f-0368-3e3f-9288-17b89e784ee2 | 0.27933 | -60.61493 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3557cb5c-6977-321c-b10d-341e3610dfb7 | 0.93029 | -60.54041 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97ab32bf-ea38-3e01-aa68-2e7a1715d966 | 0.16694 | -60.5924 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe9f8692-6969-329a-b310-7f0e4d55aa18 | 0.45905 | -60.39797 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 066024a3-c376-3080-b80b-00fb4ba0ccf3 | 0.92635 | -60.53735 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59908a8d-7dbb-364e-9f6e-bc14fddfbd76 | 0.16704 | -60.68023 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2940652-bf17-3b9b-9006-aeeea03adafe | 1.19977 | -59.96885 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9b0d94a-b492-30f2-b71e-9d0e3d6be441 | -0.15573 | -60.74506 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a8e0e4d-c92e-3e72-b5f7-db5de51f6153 | 0.73079 | -59.90302 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 051e83d2-fbf1-3521-affb-0567f2073203 | 0.65503 | -59.61726 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fd4efed-199f-3b48-9f73-ccb2f9528dab | 0.31213 | -60.4393 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 315bf8cc-aa80-3091-8a43-38908825f8c0 | 0.30208 | -60.44088 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c47232c-31cd-30c6-a978-df5d9e1ec188 | 1.11165 | -59.19331 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 246437ad-dd7d-3e9c-9ba3-0cd69d625f0a | 1.35299 | -60.03532 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7821a66a-e51c-3b0e-854c-8ff8b914618e | 0.4966 | -60.50487 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e993927d-c0f5-3596-b68e-732d75bd2ef7 | 0.28326 | -60.61798 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 904d807a-4287-3481-9fb8-0b3cfcb8ccb4 | 0.05481 | -60.99378 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82a48c45-797d-3bcf-80e3-ec8b3419e7cb | 0.49829 | -60.51556 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5961710-a626-3739-9222-e7c0669f81b4 | 0.30706 | -60.49459 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cc8ac5b-5579-3104-9757-ed700cb700d6 | 0.53436 | -60.46999 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70b7671d-1a52-394a-b4b4-90f8869a943b | 0.21709 | -60.59174 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a17241b6-0bcf-397e-b2cd-a158462e4639 | 0.03667 | -60.98915 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| cff242c8-bdec-353b-80fa-440c9546adf3 | 1.11549 | -59.19622 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c8bb6c5-1642-3c0b-86f6-62eb2a92d84c | 0.80001 | -59.8676 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6c92126-b6d5-3010-b2f1-4a306c3ec5a6 | 0.92183 | -60.50872 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecff6283-993b-3f32-a4c5-c7e280d91d3b | 0.6931 | -59.94451 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a87fcf8-4a4c-3845-89bc-fa132a9ea9c9 | 0.45849 | -60.39443 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f68cb49b-374f-3901-9d51-faf80db80fe5 | 0.96343 | -60.23644 | 2026-03-04 05:25:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 361f85f6-bdc6-3cad-9536-314944bbab71 | -10.24541 | -69.33214 | 2026-03-04 05:25:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf83c91a-3557-3eea-8c1c-c59ef2c81b89 | 1.02001 | -59.79722 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 729e2bb0-81f5-3b1a-b12c-bdeff6ef63bf | 0.16367 | -60.68075 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 064f38b1-58a1-3336-a827-a0295025463a | 0.96445 | -60.52804 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39a38370-9787-334d-86ab-32150dfba3a3 | 1.07356 | -59.25585 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1a850db-28ed-3fdc-9232-96cce93c6d2d | -0.15516 | -60.74865 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3519e835-2082-3a5e-bfe7-11e941cecaa8 | 1.00172 | -59.50998 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
