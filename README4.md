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
| 510a1372-1766-3880-80eb-35fd2a76ff3f | -16.57853 | -57.79839 | 2026-03-17 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0bb86c09-e395-3cac-995e-93134a91276b | -16.44326 | -58.17684 | 2026-03-17 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ce768e1d-a7b7-3da2-8fbb-801b73de1a5f | -17.91048 | -54.65223 | 2026-03-17 04:44:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71d0dde8-4bf8-3c35-872a-0edeab2eb352 | -16.44754 | -58.17773 | 2026-03-17 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ee728aa0-6c5b-3bd6-a1e0-6b8a45765d27 | -19.98986 | -54.73979 | 2026-03-17 04:44:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96a0701a-1127-3627-b811-98850fec5748 | -16.57437 | -57.7975 | 2026-03-17 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d2c9a90e-82a6-3373-a160-490b6d3e80a2 | -16.44832 | -58.17355 | 2026-03-17 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 966cab38-ee54-3f7e-944e-505b3f03795c | -17.90702 | -54.65157 | 2026-03-17 04:44:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31ff7441-4a11-3123-9bd7-c327005a433e | -16.44558 | -58.17562 | 2026-03-17 04:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b355e1c1-536b-31f4-bf47-f2f05b54dda6 | -21.3597 | -47.06593 | 2026-03-17 04:46:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b946036c-252a-308c-b320-4ce104de35a1 | -21.36441 | -47.06239 | 2026-03-17 04:46:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5210aa3c-bb42-3f1e-8294-1b15706d8313 | -21.70859 | -48.43479 | 2026-03-17 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ebcc41d0-359e-3b46-a3a5-e6fc2a6d2108 | -21.70555 | -48.43073 | 2026-03-17 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dad10c93-4383-3f18-b15c-2dd40b448766 | -22.65405 | -47.64407 | 2026-03-17 04:46:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d14211e8-9a02-3462-98fa-3988766ecff9 | -23.03107 | -52.67637 | 2026-03-17 04:46:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 69de6cd5-2ff5-302a-994d-459567db5038 | -21.70945 | -48.43121 | 2026-03-17 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c330786-2654-3e79-b580-440dca34b67a | -21.7049 | -48.43594 | 2026-03-17 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cbfe3d16-bdf3-3584-8470-685e477faa0b | -21.3532 | -48.0964 | 2026-03-17 04:46:00 | NOAA-20 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c544ecd5-e698-34e6-a864-4b4d5ef4f536 | -22.65454 | -47.64014 | 2026-03-17 04:46:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6c08f3b0-0fa0-3811-a4a7-535713a438d6 | -21.70537 | -48.4291 | 2026-03-17 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 203bf07c-0833-3ebb-8432-eedbe4f563f1 | -21.70468 | -48.4343 | 2026-03-17 04:46:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96227f56-8f2b-3b00-8508-819c3b5925da | -22.03412 | -56.30594 | 2026-03-17 04:46:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2de32d55-bcc9-3594-b540-bfc57c41acc6 | 1.69046 | -60.22635 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67dab7ea-310d-334c-b6c0-a1c50ffcbf1b | 3.12199 | -60.7613 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4556f4b0-c4e5-3b92-91e6-1d375c590a47 | 3.12535 | -60.7395 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8069be96-6de9-3b40-81a6-9e9032e0abf1 | 3.17151 | -60.11872 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5909e92-4a4f-3c3c-88cd-36d3644b055a | 3.12009 | -60.8575 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58c2fe48-4a09-3233-975f-daefbb9f73b8 | 3.12064 | -60.86097 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41dd9063-3c8b-3cd4-b841-b1aa29adba61 | 3.78715 | -61.32009 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87b9f384-b3fc-36b9-929b-b99a37f5156c | 0.83907 | -60.33207 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0aa050a7-4c75-3ba1-9325-5c9ca32d03fb | 3.13351 | -60.79146 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae91adc0-43c1-36b1-9621-2b61cf5525aa | 2.02051 | -59.98851 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43a7acb7-b435-3053-bdd1-aaa259836341 | 1.17743 | -59.14958 | 2026-03-17 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff304ba8-327e-3e83-85b3-481b758f00fb | 0.85286 | -59.31571 | 2026-03-17 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1677165-a09e-302e-a82a-dcaa8d4e0617 | 2.07927 | -60.18558 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e307da5-6d7b-34bf-b727-ee8899407d11 | 3.14392 | -60.72536 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f906ac5e-5ddb-33c1-9a5b-529f85cb060d | 2.21042 | -60.15469 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 558e8831-0e66-33f3-b8e6-b7e502b4a180 | 1.32865 | -60.69699 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f709dcf3-a48e-3b22-bbfb-9d9e507feea2 | 3.7509 | -61.32195 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdfc95a2-1145-3e12-b7b7-2a5ae7aea881 | 3.1209 | -60.75437 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 02b4381a-051a-36a0-ad13-57c91d985251 | 0.63526 | -59.66191 | 2026-03-17 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0dc7794-8e0c-3b16-8d6e-e419bc14e295 | 1.64116 | -60.28322 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f0363ba-5bae-32e4-9414-435326644e1b | 1.01075 | -60.23161 | 2026-03-17 05:27:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d40aa27e-aba8-3fe8-b89f-3a5a6a7fc655 | 3.14231 | -60.71497 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60051ee-f538-34d9-99ad-b119799a4586 | 3.14285 | -60.71843 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fcefa2f-edad-351d-bbfb-ca0f0f26d734 | 3.12145 | -60.75783 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ccc8472c-a897-3799-b12d-ff2082f70a61 | 1.63786 | -60.28373 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1106549d-9739-3593-9ae5-a668364b98b7 | 0.99439 | -59.82575 | 2026-03-17 05:27:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cde3dfe8-e8a9-311e-89dc-37a68bdedc1f | 0.83355 | -60.33994 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58312cf0-4767-3897-a0a3-4e041c2d4994 | 0.95565 | -60.2298 | 2026-03-17 05:27:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a37e8a60-9aa3-3365-917f-0e68a58be3d4 | 3.13122 | -60.73087 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5bf25031-58e3-399b-b1f8-b22eccde4084 | 0.83631 | -60.33601 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0cd82705-01d7-3f8e-93f1-d2c6783c83c4 | 0.90927 | -60.30006 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e90bddd7-a471-3e23-845d-b5ff9e9c1d4d | 0.90543 | -60.29715 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47f0a830-ab09-3a69-b62a-18159e7136c7 | 3.78379 | -61.32061 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6867d910-5a37-3042-a885-2f709f207f22 | 3.19604 | -60.31856 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9ca3139-b31e-3b6e-ae52-0802633f6d23 | 3.08056 | -60.77832 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e532cc4-80b9-359a-8e20-5b90b4a3a64a | 3.145 | -60.73229 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0ce911be-4a22-3ae2-a4ac-b4387a6e8ff2 | 3.87535 | -60.1167 | 2026-03-17 05:27:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5e91121-ce2e-3a86-93b5-8d2d942b5061 | 3.12698 | -60.74989 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cd941105-867d-3c94-8ad2-2a671705c386 | 0.83577 | -60.33258 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4107f0e-b488-3ff6-a1b6-5fe1ec981d04 | 3.72964 | -61.29591 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aede52a6-cdea-360d-b05b-aa30acba9b8d | 3.12367 | -60.75039 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9f2b1fac-c4d0-33ef-808a-d4b82654aabe | 3.08664 | -60.77383 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 700035e8-aae2-3993-b9cd-31b72f2b35a1 | 2.85602 | -60.73518 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60d792c1-408a-3f9b-8053-de16d8f467d8 | 0.83961 | -60.33549 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ec26715-8a37-3136-9e85-569d600a5e7c | 1.55334 | -60.28278 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 487fd699-9e0d-31b4-9592-1097c1bd8b39 | 3.13405 | -60.79492 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7ce4135-6059-34c1-8dfb-2ad6227b1c9b | 2.25142 | -60.20093 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db8b864c-836d-3b11-8be1-ab29ab8a77ff | 0.99691 | -59.47289 | 2026-03-17 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bbe7286-d434-3944-8211-d608d589a1e8 | 3.72684 | -61.30001 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16ea1416-541a-38e5-b5e1-a4426a6eff88 | 2.30863 | -60.23744 | 2026-03-17 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6932b1b3-dae0-3b7a-b510-a0d096dc80b3 | 1.09053 | -59.89516 | 2026-03-17 05:27:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50391ee4-1b54-3d13-bfca-4fe351058596 | 0.99493 | -59.8292 | 2026-03-17 05:27:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa7972f-542b-34c3-b686-69ad770a400d | 1.00746 | -60.23211 | 2026-03-17 05:27:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e60349c-cd0c-32c5-a98a-94fd595dceb2 | 3.19396 | -60.13279 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec354d34-ad41-31ec-bf56-fa4a81c8a34f | 3.139 | -60.71548 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2d4853c-050a-3e65-b21e-48efe5c84102 | 3.19288 | -60.12594 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ad0b222-ba7f-38c3-80c0-cff89524914d | 1.81382 | -61.14344 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5320175-200c-3837-b7c0-677fc4e5ed4e | 3.13954 | -60.71895 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ca8ce1c-4f71-39fb-a9bd-bfdc1f981ce3 | 1.32972 | -60.70384 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdd4e2b9-710c-3b24-b187-e0f2d00c1393 | 3.14339 | -60.7219 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82210c1c-e09a-37bd-8c74-ae9b18e284bf | 0.90597 | -60.30057 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e80b3ab1-6e5b-3e2c-bb7d-72dc3ade7a11 | 1.08999 | -59.89171 | 2026-03-17 05:27:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 984fc1c7-14f8-3fb8-ab30-8ec2e8a27b94 | 3.13507 | -60.73382 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 26cefe8d-f60d-3b80-8e9a-d4d8544cc737 | 2.23763 | -60.22059 | 2026-03-17 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23b74ddf-0385-36d6-862c-43458e4d0db0 | 3.08387 | -60.7778 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f152fd99-a7d8-36c1-8e77-c82befaf9fa9 | 2.52154 | -60.98966 | 2026-03-17 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd96190f-03ec-3ddc-b420-0abd81027bf7 | 0.83194 | -60.32967 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02b985c6-d39a-3598-84c9-0bbca5f596f7 | 3.78604 | -61.31293 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1395f39f-6c46-3961-955f-1b7479a4e66c | 3.72853 | -61.28878 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c52535ef-edd2-383c-87fe-937ca0534296 | 3.18522 | -60.1201 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a99144a-d9df-35d6-b436-edf50eada6bf | 3.13623 | -60.71945 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c09dd8f4-6f00-3313-8a4b-9ec8ac4ca2c9 | 1.63733 | -60.28031 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30b988b2-4888-3480-96a5-f09f54543a96 | 0.83301 | -60.33651 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3236e908-845f-3262-ab1d-dbfce44a4489 | 2.25089 | -60.19751 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1d2132e-0c3a-3df4-85af-c900a9619aee | 0.84015 | -60.33892 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9f3466a-7ace-34e0-804f-13c21869d794 | 2.74424 | -60.43592 | 2026-03-17 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d11feb1f-b50a-3fe0-967b-75fd037d7a01 | 1.64062 | -60.2798 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 046d9108-747d-3a80-82ea-eafb09e2f983 | 3.12812 | -60.73553 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README5.md)
