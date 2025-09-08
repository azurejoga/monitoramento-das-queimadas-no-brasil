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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63276bf4-ce53-3ff8-9bfc-fdc6fa68b387 | -7.82556 | -45.4239 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ecd3427-5667-3f63-8f7d-912d51888fa9 | -6.37981 | -42.6095 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a406bb5d-8664-3023-bfc4-93e552b72f31 | -5.88456 | -43.96135 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27de6be6-e24b-3e71-bf3e-e84122d898dc | -6.22618 | -45.03159 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19172c86-248b-3ede-b9cf-84b523e48911 | -6.20331 | -42.64764 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 83c996cd-db05-3f30-bacb-4b3aa9c308aa | -6.87469 | -44.2568 | 2025-09-08 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d83a3c1-469a-336c-8fbe-c2c4d4274a5f | -6.28061 | -53.42297 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7d6aac7-4db9-3d55-9fb3-dda5b534753a | -6.30261 | -43.32765 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72901264-db23-3e79-a65a-e7aa4fed480b | -6.87853 | -44.25735 | 2025-09-08 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d243acd4-4a59-36e1-9792-77e96d78e058 | -7.35388 | -43.9458 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a0aa5f0-8d00-31cd-8016-a6ff4c954671 | -6.19713 | -43.61096 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a685de5b-b81d-3325-b9a2-3f923f18b91b | -6.63196 | -53.37351 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 254f5fd6-f9bf-384c-9c28-33cd994120e7 | -6.83282 | -52.80854 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47d85239-7caf-3b4e-bbd2-f16d210760d3 | -7.9754 | -44.84062 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9392bd05-ff18-34c8-8bc3-6cc0be35f0fc | -6.00314 | -46.19548 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42853566-a31a-3aa5-9045-c238c11e1275 | -7.03789 | -43.25578 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea3b7847-c99d-36cd-bfa9-057c658e3649 | -6.21415 | -43.31851 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2b22661-8578-3d6c-bf6f-3d67e51a59da | -6.19042 | -43.37186 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a801399-8303-3264-8d9e-77877ee1419e | -4.82553 | -42.73904 | 2025-09-08 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e46698a-bef1-305f-8b20-3940d6750613 | -5.08174 | -42.4141 | 2025-09-08 04:00:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d00db10-ef82-3063-a73a-8e8a66d76feb | -6.56083 | -42.94239 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ea9c72d-e40d-3b51-8099-809b6a215216 | -8.10532 | -39.51234 | 2025-09-08 04:00:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ea2ba08-8fcb-36c8-9976-ad660a14049e | -6.78181 | -43.42081 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d1631f5-f7e7-3961-9d0b-ffc814a98823 | -6.8408 | -52.85849 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d897cab1-2fb1-3671-9307-04ece26a895e | -6.26459 | -41.39746 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9a5c16f-1ff7-39dd-a9c0-575a96a9066a | -6.84322 | -44.87984 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2da2375c-decd-3a55-a3f6-74aaf99cea3f | -5.79044 | -45.66311 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f907c0dd-ae8e-30d2-a42c-d75111ec3f69 | -5.62841 | -42.61678 | 2025-09-08 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 955cbd50-a1c5-310c-a451-a82e87f658f6 | -6.48447 | -41.7728 | 2025-09-08 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 88651bb5-4876-3df6-8d50-ecef8052d2ef | -4.5446 | -40.70455 | 2025-09-08 04:00:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8669a8c-a2f4-3c54-b726-9aade720d43a | -6.36151 | -42.58678 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 114e58b6-91a4-3e3b-b113-71ee6358eac3 | -6.40378 | -42.98958 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6aff7fff-2aa5-3d34-9e51-b31c90f09000 | -6.23904 | -43.5076 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03f8f2fa-b9f5-3e09-ad64-ec9ded291f2a | -6.19545 | -41.00174 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 694d029a-e04e-3fba-b494-4315be6c4d9a | -6.40156 | -42.98077 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d5615a3-92c7-3956-9a2c-e20d51e5091e | -6.46072 | -43.94796 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89146dd2-de7b-3a45-8894-44798187719e | -6.94202 | -43.35873 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6fb01355-483e-39ac-962a-91f20ecbd715 | -8.04156 | -44.05368 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b3aeec8-e966-3f6b-9bd8-7f11ae4dc6a5 | -6.60969 | -44.00911 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a026d0c9-35cb-3344-9b3c-1c7334104464 | -5.86881 | -44.17868 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32ebbb29-3b49-3cd4-87fe-43e62b25dd95 | -6.81643 | -52.80377 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a17c5dec-5a7f-30cd-a590-31a0a9cd0e93 | -5.95002 | -46.16205 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f338a138-3437-398c-b741-74add3e407a1 | -6.71263 | -45.14259 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f19dd606-c766-3077-aba6-6d005bd228ba | -7.7548 | -44.00211 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fd33409-40bc-38aa-8132-a8eb2438c3fc | -6.21941 | -42.59291 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 53f89009-4a97-366b-9896-cb8aa7e35958 | -5.73152 | -45.36902 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7fe7648-bdca-3542-afe9-0bc09a4954e9 | -6.77816 | -43.42025 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cf042205-2c1a-3da2-9346-8eb8a6b749de | -5.79111 | -45.65913 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccddb0af-4b89-3c07-b924-f63e51403b9c | -3.79001 | -48.87755 | 2025-09-08 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b89dc126-c265-3d67-a706-c78e89e24239 | -5.45252 | -42.80268 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 12cd300e-a084-35d2-b434-1f34da5949cd | -6.91634 | -43.80237 | 2025-09-08 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ca9c5c2-5f1e-318d-86a7-72f73bdc4666 | -4.80787 | -46.8242 | 2025-09-08 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0449636-163d-3e20-8a69-a11b1c25ce51 | -7.55153 | -45.3418 | 2025-09-08 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d3dd25c-284e-39c8-b916-bcd12c77ffcd | -5.87494 | -46.09848 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e21d2952-f943-3de4-9321-7e0f5b026c10 | -6.63885 | -53.37479 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2937f48d-f591-337b-a387-3b1908b21d06 | -6.20547 | -41.00336 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43c00543-d192-3fc2-86be-54595eb76fc0 | -6.851 | -44.82512 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66a1f2ef-d0f7-3e88-b8ec-b81db8926855 | -5.91245 | -49.66886 | 2025-09-08 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0497e7b-82cd-3782-809f-ab7b05c5ecad | -7.829 | -45.42824 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3810aab0-f7f3-3c6b-90aa-877202ee3761 | -5.6704 | -44.16198 | 2025-09-08 04:00:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eebb37a5-6417-3d7c-b71a-6d7c6624c9ac | -6.24703 | -44.83315 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e62773dc-82a2-3783-823a-5a3aa0d46ade | -8.44362 | -45.02175 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1d127b65-a92b-331b-9aeb-deca475fa235 | -6.56241 | -42.95517 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0e55cb9-adf0-3a74-9d41-738f4cf3a8d8 | -6.60611 | -43.96064 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1aaf2bb-026e-3b3c-96a3-f7ce62f32840 | -5.86709 | -43.44987 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f30aada6-979d-3bfb-9a1a-9de2e1a62fad | -7.61828 | -44.66549 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56ecd065-36ff-39a3-a91a-5c0f3d00118a | -3.30731 | -48.72239 | 2025-09-08 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ff20afb-adc9-392a-ab59-ac857b233b84 | -6.83938 | -52.84641 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5da2f79-63d9-3b58-bef2-d157ae910864 | -6.19608 | -40.97644 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c6e1481-2838-37d7-b9da-5a3815391f3c | -5.96253 | -45.77219 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53fd013d-ee01-367b-9c04-d5d33c1dc52f | -6.25522 | -42.57336 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af396621-e414-3c3f-9dff-78a2c946b2b7 | -6.5035 | -42.17901 | 2025-09-08 04:00:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05e9fc4f-112d-3715-ba65-2daafd6c1385 | -7.82836 | -45.43207 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15d39989-7b3d-3b38-a1dc-8605c2bc03f0 | -6.62923 | -53.35096 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 759a0025-ac8c-3535-8fe5-ca45a57425fb | -6.2939 | -44.38616 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc13730f-bbe0-3562-b850-707df011ef5f | -5.71634 | -43.90116 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7ce583e-0423-39ae-a8d8-75e841b81916 | -6.67115 | -44.55704 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16196ebd-6883-36ef-9e31-e168e01740b6 | -6.02886 | -45.88988 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59917135-1f92-38f7-b6f3-82625634b002 | -5.91732 | -49.67365 | 2025-09-08 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 99f703e8-540a-347f-9a87-c9e685048a01 | -8.62224 | -40.20181 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 00d5f5db-ff3d-3dd3-9d22-86d0a3e038eb | -3.76104 | -41.66102 | 2025-09-08 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1eef5847-c975-30c0-91ac-7ae22ab5af01 | -6.2027 | -40.99928 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ebc6364e-eae2-3c31-af69-4df9387b6cdd | -6.08999 | -43.11675 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4528355-cbdc-3cbd-a1d1-182e58132224 | -6.4649 | -43.94624 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9296e5ec-5a40-377f-9979-c48c680cf4a2 | -6.07456 | -43.55667 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01090a9d-dde5-32f4-be36-805e3ffce32c | -6.36639 | -43.53172 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adff59bd-c8c3-3113-b851-6c61b95e0344 | -6.20213 | -53.27755 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d476cb-9dff-32e1-8c03-430f240a01cf | -8.04082 | -44.05811 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7de8c354-331e-3567-9116-953f754babfc | -5.75528 | -42.75286 | 2025-09-08 04:00:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dfcef992-7eda-3871-a18d-eb97717723e9 | -6.17161 | -44.24593 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 45e9201b-1a73-3cb4-8848-90e12ea532f7 | -4.90452 | -42.21308 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b66dfd2c-df12-3975-ac82-07f47055124c | -6.35278 | -46.3704 | 2025-09-08 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae6f471-2ae5-31f7-85a2-64fbf0cd6cd3 | -7.59749 | -37.80606 | 2025-09-08 04:00:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 529b7dc9-9340-3414-9bf1-80be09848880 | -6.85497 | -44.82576 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d36138-234d-39fe-95bc-56e6bef587de | -5.98577 | -44.1517 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab314d18-3cf7-34b0-adbb-00652626b888 | -5.8752 | -43.44669 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54a34437-f0c3-394b-a7a2-9f4e8a62e63c | -7.89543 | -45.26147 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efce9ea6-6bed-38dd-86f3-f29d1c74de7d | -7.99002 | -45.46397 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d67c600a-4ca0-3937-848a-3f470faa1887 | -5.22214 | -43.69576 | 2025-09-08 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4fc1a3e0-ae85-30b8-b342-702cb7e12781 | -6.46377 | -43.95288 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README35.md)
