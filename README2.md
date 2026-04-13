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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 780b7797-ed43-3190-b0fa-2843da456f43 | 1.121 | -60.5413 | 2026-04-13 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d895a1f7-0968-361a-a007-9d7edf355bb1 | 1.1028 | -60.5414 | 2026-04-13 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 195.5 |
| 96da0da9-ceb7-3a41-8977-6e26133a3078 | -11.8105 | -43.637 | 2026-04-13 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ab3d52a3-ef1b-393e-849c-148781c65fa2 | 1.1028 | -60.5225 | 2026-04-13 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 182.9 |
| 38287f65-4fb0-3184-b99a-1e50f048e624 | 1.121 | -60.5224 | 2026-04-13 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| dc825192-38db-3b85-9ba6-c53f1ca25f8e | 1.121 | -60.5413 | 2026-04-13 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 81f1c0c8-6338-3942-8f4b-f756c4d0ab89 | 1.1028 | -60.5414 | 2026-04-13 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 9fbb4c21-d587-33b5-8208-307d639a162f | 1.1028 | -60.5225 | 2026-04-13 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.4 |
| c42eb800-effe-3627-b900-52aedc4f4f1e | 1.1028 | -60.5225 | 2026-04-13 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 5548099a-3c70-39dd-9eae-82e42b24be78 | 1.1028 | -60.5414 | 2026-04-13 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 156b35bc-a289-378d-af67-9a7585ca11af | 1.121 | -60.5413 | 2026-04-13 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5250460e-f341-3be2-b458-5079b50f68fb | 1.121 | -60.5224 | 2026-04-13 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7ee2c951-a206-3a46-9530-8ebc67b40d55 | 1.1028 | -60.5225 | 2026-04-13 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 2b72f19e-2090-3195-a399-a58a7c3bb159 | 1.121 | -60.5413 | 2026-04-13 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c6621d8b-ebc7-3119-a1c3-d273b2751079 | 1.121 | -60.5224 | 2026-04-13 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| edc0705a-6f16-3ab9-b43e-92e27468c495 | 1.1028 | -60.5414 | 2026-04-13 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 32259315-e8c7-3e44-a2fd-315b58009f1f | -11.80486 | -43.62952 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ee60bda9-6738-3454-9b18-8a59b6658006 | -11.80619 | -43.63258 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d135c09d-8db6-3721-8eff-55ff999265b8 | -11.81085 | -43.63341 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 219aaed2-fbeb-317c-881f-8809b192e0d6 | -11.80243 | -43.62683 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dc1c0654-92f3-3438-b433-398a37b25e6b | -11.80114 | -43.62379 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41440079-196b-3573-838f-487cbac9695e | -11.80154 | -43.63175 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c73470a9-c155-3e45-9d68-7981cba02961 | -11.80997 | -43.63832 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 0ae51bec-2d1f-3438-b02d-83639a109828 | -9.82162 | -37.75743 | 2026-04-13 03:45:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 427366a2-4ded-3ea7-a328-c202b9e03103 | -11.8086 | -43.63524 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 768276ee-887c-30bf-a6b9-dac1e32b438f | -11.79929 | -43.63361 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5e83aee-328e-377b-a57c-196acbf0a2f7 | -9.80133 | -37.46928 | 2026-04-13 03:45:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4decd709-0d4e-3417-b4f3-b7e4b4e3bf4c | -11.80021 | -43.62869 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4feb7cbc-e1d7-3ce1-b899-23b6bd32f9b6 | -9.70462 | -37.1996 | 2026-04-13 03:45:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f00eadb9-70ab-3c2e-8a02-42d5c2c2f4fb | -10.62403 | -37.40541 | 2026-04-13 03:45:00 | NOAA-21 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29b53e5f-d70f-3a20-a7cf-727265ea38a8 | -9.80413 | -37.4735 | 2026-04-13 03:45:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 03ed7fa9-476a-37b8-84ce-2c6c88202ad0 | -11.80952 | -43.63034 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 74b294ab-a70f-3e17-8fb9-904e4e73cadb | -11.80065 | -43.63668 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c8a22db7-151b-3097-8c13-bf2621fa4c40 | -9.80074 | -37.47294 | 2026-04-13 03:45:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ddefa83f-46b1-30f0-bddf-5f8f5150b5b6 | -9.70798 | -37.20016 | 2026-04-13 03:45:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 48f3a18d-4401-3f4a-bab4-4740e67c92f9 | -11.80531 | -43.63749 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ea5e56b6-626a-34d9-9fb5-542709563599 | -11.79599 | -43.63585 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 23afebeb-d6ae-3248-82cb-58c1e3c9c451 | -9.82504 | -37.758 | 2026-04-13 03:45:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf139a5a-08fe-38f1-a41b-af17f15ca737 | -11.03312 | -44.67274 | 2026-04-13 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 071f1dc6-a8ed-3de0-a461-c53b88baca32 | -11.79836 | -43.63853 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d57c1110-b33f-36cf-a32c-8595173ace69 | -11.80394 | -43.63442 | 2026-04-13 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3e59a11d-13e8-3fc1-b900-0b75113dd6d5 | -20.13525 | -46.76582 | 2026-04-13 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72abbd3c-555d-311f-b1c2-cd8686cbd09a | -20.13444 | -46.75567 | 2026-04-13 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2753e88-a612-3252-a8f7-b6cdb684be82 | -20.13324 | -46.76134 | 2026-04-13 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8be417ae-d317-3caf-84f2-5a4c8c06cd34 | -23.42924 | -46.75663 | 2026-04-13 03:47:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 61eab179-14f2-3388-81cc-5901dc65f94a | -20.13642 | -46.76007 | 2026-04-13 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 521b7391-e5c1-3007-85e9-4ffe6916cdb9 | -23.42814 | -46.76184 | 2026-04-13 03:47:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9407938-6f25-33ee-9980-f9a80333eff6 | 1.1028 | -60.5225 | 2026-04-13 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.5 |
| de201e4c-20fe-35e8-8633-d9c7578fc805 | 1.121 | -60.5413 | 2026-04-13 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 0ad9a50c-1dce-38d5-a9ce-1a44074cdf9e | 1.121 | -60.5224 | 2026-04-13 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| d9470987-e55b-3fc5-b017-d2a86586421f | 1.1028 | -60.5414 | 2026-04-13 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 29e856ea-086e-35e4-bcf4-2425944c33f0 | 1.1028 | -60.5225 | 2026-04-13 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 51fc31d5-da65-36b3-8855-1bf8904aeca1 | 1.121 | -60.5413 | 2026-04-13 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c76b9e9d-316b-3d66-8938-9d355dcd1cd7 | 1.1028 | -60.5414 | 2026-04-13 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e1d238f3-06ad-3473-983e-d48654fdae03 | 1.121 | -60.5224 | 2026-04-13 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 26ec7e32-e81e-3ecb-9704-53aafce511b9 | 1.121 | -60.5224 | 2026-04-13 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 61c6ba44-ef3a-323c-8770-4966a00fe8a5 | 1.1028 | -60.5225 | 2026-04-13 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 149.3 |
| dfbce148-dc01-3a00-b58b-68731a556ccf | 1.1028 | -60.5414 | 2026-04-13 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 151.0 |
| ec703d74-0ccc-339b-907a-41dd1c0d7be1 | 1.121 | -60.5413 | 2026-04-13 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 32727439-c29b-3857-9611-d4e6ef1c7f8a | -11.02949 | -44.67197 | 2026-04-13 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcda4261-efa6-3f59-a9ad-85c579db78b4 | -19.49366 | -44.27747 | 2026-04-13 04:17:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3bccb32-2c3e-3f8b-9d13-9e6cf5598011 | -11.80732 | -43.63318 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 166563f9-5416-33ea-8ab3-b27cb506290a | -11.81065 | -43.63373 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5f00baa3-42a1-3c31-8b9c-ee6c2a5d69c0 | -11.79673 | -43.63509 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d15f4bc-a431-3471-84d0-84fe62fe6e80 | -20.1353 | -46.75545 | 2026-04-13 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4be248ca-9b34-3fb4-9cc4-1cb6252dd17c | -20.13754 | -44.82522 | 2026-04-13 04:17:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20bef7e8-cf0e-353f-bfe9-a4b809dd36eb | -20.13665 | -46.74757 | 2026-04-13 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74bb06d1-7023-33ed-88d5-1f06eb5e5f08 | -11.79454 | -43.62741 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580ebb56-409d-3b67-90f9-1a30440e076c | -11.80007 | -43.63564 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19618c87-a59f-3624-9245-4db28e83e8df | -12.69322 | -38.58273 | 2026-04-13 04:17:00 | NPP-375D | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0a9c1410-9241-3bf2-b058-dbf7a9e24f6f | -11.03189 | -44.67131 | 2026-04-13 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23f8825e-4e44-3636-9a9c-0d38a2eccd60 | -18.78848 | -51.93985 | 2026-04-13 04:17:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb464ffe-df7a-3178-8b73-315363dfad52 | -11.02955 | -45.13544 | 2026-04-13 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de18fa86-e27b-3935-a704-9ca1dca8fa8b | -11.80179 | -43.62495 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b176c45f-26f6-3eb6-9648-e61017d14ee2 | -11.80513 | -43.62551 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1468916a-0359-39ed-bcbd-5d6ee4257b3d | -20.13397 | -46.76325 | 2026-04-13 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d53b999a-238c-3a97-9fc7-3b199184e0f4 | -11.03293 | -44.67255 | 2026-04-13 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3546fcce-1512-3bcf-af75-eded19eb0cf0 | -20.13463 | -46.75935 | 2026-04-13 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c3cd726-8120-3511-981e-032bfea051aa | -20.96376 | -42.77297 | 2026-04-13 04:17:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c191df8e-0b19-3d4e-b0a2-d25fc6269e34 | -9.80282 | -37.47072 | 2026-04-13 04:17:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c0be9d05-4f3d-3a7a-ab2b-236a5182c9b9 | -11.80789 | -43.62962 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 34121c4e-4267-38ca-95af-89f8c1e48e48 | -9.80206 | -37.47598 | 2026-04-13 04:17:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 27e89d3c-8fca-3ec6-b5a5-19b31a5bf511 | -11.80398 | -43.63263 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f7e8e84-4913-3791-b841-c4de18a54364 | -9.82209 | -37.75706 | 2026-04-13 04:17:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 117cfd56-8bfb-359e-9679-e8c6c4812f82 | -9.82125 | -37.7588 | 2026-04-13 04:17:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1abfd0d-7705-3b2b-a844-b674fcfdf581 | -11.80064 | -43.63208 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44eb40a6-3f48-33d1-a28e-eb5ece078aff | -11.80455 | -43.62907 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5245ee39-4c62-3190-b7fb-c9166f2b15f3 | -11.8034 | -43.63619 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b790fb7-656a-3c12-a9b2-0433c7c30044 | -11.81008 | -43.63729 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ffcf13c6-7efd-3c40-a244-b16fbafa8f92 | -9.79881 | -37.47013 | 2026-04-13 04:17:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 998f880b-0371-3217-b28f-02eea1c4e447 | -11.80121 | -43.62851 | 2026-04-13 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0453ff4e-e93b-36d3-a537-b7bb2ecb66a8 | -23.42799 | -46.75874 | 2026-04-13 04:19:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc1b6a63-b332-301e-8493-a851dcd0a075 | -21.25273 | -48.57983 | 2026-04-13 04:19:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fef3bf42-ebd8-3a1b-99f2-3a2ba32155e4 | 1.1028 | -60.5414 | 2026-04-13 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 4a0ba21c-4283-3ecf-a531-d85820c78bd9 | 1.1028 | -60.5035 | 2026-04-13 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.0 |
| f5f196d5-9470-3311-90a6-0b3fd8ab0d93 | 1.121 | -60.5224 | 2026-04-13 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 598634a1-8328-3ffb-b551-e6becd54058a | 1.1028 | -60.5225 | 2026-04-13 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 143.8 |
| ee3fa10f-6561-3e49-ba16-c96e53997594 | 1.121 | -60.5413 | 2026-04-13 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 034934a9-3add-3b3b-b60e-3e10d7fe4b47 | -9.80136 | -37.47102 | 2026-04-13 04:36:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4f7eac48-80c0-3f26-a748-724f39f2e89b | -11.79644 | -43.63635 | 2026-04-13 04:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
