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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f6c3016-0755-3dd0-a0a9-8eddedf3d176 | -10.8505 | -49.9217 | 2025-10-09 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 53a6e5ee-36f3-3cd6-80e7-5124caed9c94 | -4.9894 | -45.3159 | 2025-10-09 01:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 92dc9a47-6acf-3b0b-b48c-cddf0fdf51c5 | -14.4717 | -52.8937 | 2025-10-09 01:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5082f3cf-7063-3eb3-960e-c9a5a56c25ba | -10.8558 | -44.6199 | 2025-10-09 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e042a34d-5a1e-39a5-8d9d-f3e4bd0105f5 | -10.8554 | -44.6431 | 2025-10-09 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d893aca2-12dd-3f97-bccf-a26eff76106b | -8.5398 | -46.2181 | 2025-10-09 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 79c5d686-594c-3f63-9aaf-724f23c51e0d | -7.7758 | -44.0164 | 2025-10-09 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c5110798-c887-3870-86c2-37f8d0a43eff | -4.305 | -44.5161 | 2025-10-09 01:20:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| f0c2fddf-56f4-3a10-aaa2-9402a32c14aa | -4.2864 | -44.5171 | 2025-10-09 01:20:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 2d526304-1bd6-3a02-8cb4-7d2fbb6c6583 | -18.9974 | -43.0805 | 2025-10-09 01:20:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| 32f93175-b879-3b46-9945-a1069c6b7b18 | -8.5021 | -46.222 | 2025-10-09 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c1d855b9-a015-3ece-ae35-e04497f29652 | -17.3771 | -46.6636 | 2025-10-09 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3b94ac98-3c88-3214-86ac-268ca4a0b28f | -18.1923 | -43.0648 | 2025-10-09 01:20:00 | GOES-19 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| 76e7b4d0-d9e1-3db3-b1ea-0a4bf83aab64 | -10.8749 | -44.6172 | 2025-10-09 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 97253a09-7cdc-390c-8d32-411c7c93c209 | -4.991 | -45.1124 | 2025-10-09 01:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 01f6daf5-8a31-39ae-b437-3c521ae1fccd | -9.1018 | -47.9575 | 2025-10-09 01:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| dac918e9-507d-3037-a64a-a83a44cea6f7 | -13.7921 | -43.9403 | 2025-10-09 01:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 2466e3f1-e46f-3958-8fb1-b8bf297d27cc | -13.7926 | -43.9165 | 2025-10-09 01:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a3727bc7-92d8-3db8-b40a-9ff9d316cfc9 | -14.4329 | -43.9874 | 2025-10-09 01:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 38dc8e68-6934-321a-8896-65e96f2479a0 | -13.8116 | -43.9367 | 2025-10-09 01:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 5151a3b3-5952-33ff-a4cc-de28a5d54105 | -8.5024 | -46.1995 | 2025-10-09 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c314bcd6-b425-337b-a6d4-fb676dc8db7b | -6.6806 | -46.3184 | 2025-10-09 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 565309b9-c6eb-3416-986e-fdecc0bdac6e | -13.8121 | -43.9129 | 2025-10-09 01:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| add73336-7f09-3b40-b2fb-72844bc2059e | -7.7755 | -44.0396 | 2025-10-09 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| c7e88223-9545-3605-8e24-4dd21075765f | -4.9708 | -45.317 | 2025-10-09 01:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 7245c5a4-88ed-3b46-8f71-db43f8c255c6 | -14.4133 | -43.9911 | 2025-10-09 01:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 136.7 |
| e33c8b60-e3d0-3453-895d-2dcaa056e335 | -6.6808 | -46.2961 | 2025-10-09 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 8096719e-e3cb-3616-a5c3-26a3812f4979 | -4.9908 | -45.1351 | 2025-10-09 01:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a4d96e96-06bd-3145-8845-94de89683dd4 | -17.8413 | -57.6459 | 2025-10-09 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| aaf3e76c-c5d8-3855-8773-56c13cf7d09e | -14.4138 | -43.9672 | 2025-10-09 01:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 179.4 |
| c163f0e6-9b40-3ea6-a4ae-51410edfaf19 | -6.6993 | -46.3169 | 2025-10-09 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 55140816-e06e-3ccd-8582-5c93549bf97a | -9.191 | -46.8881 | 2025-10-09 01:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1634e8c9-3096-3467-acaa-5b35657b0540 | -6.6995 | -46.2946 | 2025-10-09 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 1884505f-5828-3448-b066-9fd23a9a4bd0 | -10.8745 | -44.6404 | 2025-10-09 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f6f8f902-31a7-3def-929e-00446c1c5c51 | -18.4118 | -45.2394 | 2025-10-09 01:20:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 133.1 |
| fca5ca3a-18e9-3cc3-86a2-a300339f629d | -5.3999 | -40.9856 | 2025-10-09 01:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 8bd90054-39c8-315e-88d6-3d4f3ace813b | -19.47121 | -55.47963 | 2025-10-09 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| e4341563-c44d-3a55-8b30-c454c6657dad | -17.89068 | -57.66154 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 00903795-c874-39ce-a700-5c3a8b8194ec | -18.05791 | -57.55208 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 139d0116-6c21-34c2-ae56-48d65c241fab | -18.02829 | -57.56941 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| f41775f6-2bc6-3366-9a01-93875a518034 | -17.83432 | -57.64584 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.5 |
| d13398d1-bb4f-320f-9f24-dc97268608e6 | -17.84675 | -57.65603 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 3ccbbf9c-1465-3fd2-838b-57e60aad0b1d | -17.96873 | -57.50253 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8ae9ce6c-7633-356d-95aa-ea142d292f28 | -17.97517 | -57.50954 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| c57bdbf2-167b-3861-8973-c3c66177d63a | -17.98145 | -57.51428 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| da44cd42-84c8-3669-9f4a-4b6039a46018 | -17.85704 | -57.58604 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| ab5dbfc8-9017-37a6-a937-b601be1bf946 | -19.47613 | -55.4731 | 2025-10-09 01:28:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 7435b2fa-e438-35f3-9125-a09dd870f180 | -17.91622 | -57.51379 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| d58ff8e4-78e5-355b-87b0-af84446309f8 | -17.92662 | -57.51096 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| b97f5800-934c-3b26-991d-ed80001dfc69 | -17.90113 | -57.65967 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| b7b075d3-a531-310b-bad4-f23a9465e8a2 | -17.8802 | -57.6633 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 4734d020-8133-36f5-a576-90461aaeb42c | -17.85719 | -57.65399 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 3610f308-4785-3df3-b59e-2deef9d03f25 | -17.82394 | -57.64826 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| a45167c4-cc46-3d84-ba62-660e374f61a7 | -17.82592 | -57.66037 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 6db0189d-7861-3a87-a8fe-293500d941d4 | -17.84861 | -57.60085 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.4 |
| c468fa91-4a9e-3af9-9b8a-42012e7c49b6 | -17.84637 | -57.58694 | 2025-10-09 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 2740a9f1-431b-3d47-bbc1-46a305a06069 | -18.1923 | -43.0648 | 2025-10-09 01:30:00 | GOES-19 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 0a56279a-d0d2-33e0-8337-f2dcda3eb974 | -4.9708 | -45.317 | 2025-10-09 01:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 7b7b7922-2eed-32e5-9d62-5753e1a1dd79 | -5.4001 | -40.9613 | 2025-10-09 01:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| db8289a7-1de2-399f-a2bd-c0603a73ffdc | -12.9297 | -54.7127 | 2025-10-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 499cc35f-5066-3d5f-8541-c7e881e12b88 | -14.4329 | -43.9874 | 2025-10-09 01:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 132.9 |
| a6085f92-5329-305d-9242-7738036e7427 | -4.3049 | -44.5389 | 2025-10-09 01:30:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6f49a7fd-c210-30e6-8ac1-3f01a4fbd694 | -17.8413 | -57.6459 | 2025-10-09 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| b60ad90b-c848-3e00-9c47-97144351c4b7 | -4.991 | -45.1124 | 2025-10-09 01:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c29460de-3e53-3b86-be8b-0a51bd79c480 | -7.7569 | -44.0183 | 2025-10-09 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 69f7baa3-af9c-31aa-9a85-77677df1ac84 | -6.6806 | -46.3184 | 2025-10-09 01:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| f46e02bf-f416-3188-a8d4-bb4f66e34fab | -19.9363 | -44.8919 | 2025-10-09 01:30:00 | GOES-19 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0a900741-e12a-3f72-805c-23d44ee52ac2 | -4.9894 | -45.3159 | 2025-10-09 01:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| deb1f98e-b196-3e03-8f82-c733e5a0e52f | -9.191 | -46.8881 | 2025-10-09 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3519cec3-ed2e-3ca3-a734-9b29cf698f32 | -10.8558 | -44.6199 | 2025-10-09 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 343.6 |
| 59babaf5-d2a8-374f-9a88-eb95a3a16f91 | -12.8913 | -54.7372 | 2025-10-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 40785990-563a-3fbc-bd26-e4282551ef31 | -7.7755 | -44.0396 | 2025-10-09 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| acbbc5fa-1a87-3b8a-a5f0-90bf8ba3dccc | -13.8116 | -43.9367 | 2025-10-09 01:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| adf88b21-c51d-37a0-bfc0-b8728e510374 | -13.7909 | -45.8552 | 2025-10-09 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5c6ed1bf-afed-398b-b535-1146bb2d393a | -6.6995 | -46.2946 | 2025-10-09 01:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| e5470ece-610b-3298-95f7-a221099b9364 | -14.4133 | -43.9911 | 2025-10-09 01:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 188139b9-caa5-35bc-846f-85c5c8b62bcd | -14.4334 | -43.9635 | 2025-10-09 01:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 227.0 |
| ea6cdbc9-ddbe-3d62-9c40-67c913631eac | -10.8745 | -44.6404 | 2025-10-09 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| adcb8678-14e3-3572-afde-901920af04f6 | -8.1993 | -43.3424 | 2025-10-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 22f77377-9056-3cf2-9646-1d17f27f0d1b | -4.305 | -44.5161 | 2025-10-09 01:30:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 7de6288e-6813-3ca5-881d-69be88084c6d | -12.8916 | -54.7166 | 2025-10-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 04d32a52-7b6b-3656-967a-571b447570a5 | -10.8505 | -49.9217 | 2025-10-09 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b4fc3eca-e1e5-317f-9d6f-9d77d19afb74 | -12.9103 | -54.7352 | 2025-10-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e0913b74-3ac5-3469-844d-6e4c779700c9 | -17.3771 | -46.6636 | 2025-10-09 01:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 93562484-ffd3-32c3-808d-38ebda3e58be | -16.0042 | -50.8147 | 2025-10-09 01:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 393cd5ac-9d0f-3c02-a2fb-6414be90843b | -10.8554 | -44.6431 | 2025-10-09 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 0c3026ab-dbed-342a-81d4-aba86e91822c | -14.4138 | -43.9672 | 2025-10-09 01:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 190.3 |
| cba6fa6e-5904-3214-8b8d-80fa60c63050 | -6.6808 | -46.2961 | 2025-10-09 01:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 410fc61e-f50d-3925-b4b2-90124656c73d | -4.2864 | -44.5171 | 2025-10-09 01:30:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 77a47115-e3b0-33e2-89c6-fbad0dd57d43 | -7.7567 | -44.0415 | 2025-10-09 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 68db0385-c8d1-3600-bf3b-c9788376a811 | -16.3757 | -46.3779 | 2025-10-09 01:30:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1349886c-84f3-3392-b1a7-d5fbe9c21665 | -9.0829 | -47.9594 | 2025-10-09 01:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 125fa2d4-c3e9-36f8-9c0a-39987aa15107 | -4.2862 | -44.5399 | 2025-10-09 01:30:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| ac5ca7e9-0707-33f8-83d3-07223142c4b5 | -18.4118 | -45.2394 | 2025-10-09 01:30:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 149.8 |
| c59ab8d9-1832-3623-93bf-a5df88967d11 | -11.666 | -47.5288 | 2025-10-09 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9e2ade99-0774-345f-ad98-fe4c08265eaa | -12.9106 | -54.7147 | 2025-10-09 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ac0d0c74-bcc2-3b39-8a1d-8c9d6c6a3ad9 | -10.8749 | -44.6172 | 2025-10-09 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 52a13863-1725-3a63-a32f-fbee6ccd2e3d | -14.4717 | -52.8937 | 2025-10-09 01:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d69cd36c-78cb-353a-8845-a145d8ad7e49 | -6.6993 | -46.3169 | 2025-10-09 01:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 1bb2c8b0-d9ea-3258-8368-d443e5cf5833 | -5.3999 | -40.9856 | 2025-10-09 01:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 180.8 |


[Clique aqui para ver as próximas entradas](README6.md)
