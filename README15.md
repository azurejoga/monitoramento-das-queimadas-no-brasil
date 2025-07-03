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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceb351b8-5251-3177-a3a0-0a9be7af3fec | -8.81724 | -43.92766 | 2025-07-03 04:34:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a06578c8-8815-3e14-ba3d-168abaa64dc3 | -7.19323 | -43.10041 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d5f32679-7d07-3464-a804-f5159373fd7f | -6.73222 | -47.37652 | 2025-07-03 04:34:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fac2e9d8-924d-3a78-8a4c-b9836141d2e8 | -6.83209 | -47.83734 | 2025-07-03 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb3cbd81-25a9-3059-a610-718058bfa63f | -7.20318 | -43.09078 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f92d6506-1a29-3476-880b-7799795d541f | -4.48699 | -50.50228 | 2025-07-03 04:34:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a98b5b8d-cbbe-32da-bab6-d1df48965760 | -7.21984 | -43.06074 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 2a1320a3-c864-38f6-89e8-a4834e8d5648 | -6.95209 | -42.88364 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 935804ba-2e86-32bf-85e0-37cd502866df | -6.68736 | -43.16608 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4fbd4f3d-6164-342e-ac65-9f381579ce10 | -5.87214 | -50.14881 | 2025-07-03 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ffe45d6c-2519-38c6-ad06-a42029cdc740 | -5.49777 | -44.39025 | 2025-07-03 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa401750-cb0f-3130-bae1-e6a9c7ac3db2 | -7.09054 | -44.39297 | 2025-07-03 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2394d86f-4731-3be2-8641-b574150defb9 | -7.21573 | -43.17476 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5dab219e-a92e-324c-83b9-cb71d54b06bd | -8.8596 | -46.14125 | 2025-07-03 04:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2381f8d-f05f-3baa-a8f7-d877710a9ae6 | -7.85689 | -47.88229 | 2025-07-03 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9432c9c2-2bb8-3cd0-a8d8-3fbfbf779525 | -5.91514 | -43.44826 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85b431ed-e440-3827-a59b-9b35a2f04ec6 | -3.51175 | -47.22226 | 2025-07-03 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71f4a1f5-50fd-314d-b11a-a33ced1e48a2 | -8.15375 | -45.90071 | 2025-07-03 04:34:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8aa89b2e-e2c8-3115-af87-b962e59d6d60 | -7.19778 | -43.09752 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8e1fe274-e670-397d-a228-ffbc08712461 | -7.06039 | -44.3658 | 2025-07-03 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b5958b5-c3a8-33cf-808d-f91d1d8ea8f8 | -7.43861 | -44.4422 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff56006c-8b93-3df2-9668-217e298a78ca | -6.80147 | -43.9342 | 2025-07-03 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3f10cf1-f091-33f1-bba8-ab8450d8e7a4 | -6.72626 | -43.15076 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80aab9c1-77b3-3271-a2ea-b7bec27cbf06 | -6.0191 | -49.23112 | 2025-07-03 04:34:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 058f6c96-54f4-35d1-8386-4a7395c5ee46 | -5.99913 | -43.73832 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b68c205a-5483-3211-bdc5-75fde0c1049c | -8.58368 | -48.21144 | 2025-07-03 04:34:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7783408-5daf-3ba0-a477-97fb8b19054d | -4.10561 | -47.93586 | 2025-07-03 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2d93e17-046c-3c2d-9e26-9a889f922dcd | -6.6976 | -43.15174 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ebdea06f-fb00-342e-9545-e80185533df8 | -6.96891 | -42.88239 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0db20ffe-9837-373a-b399-c456addbcd3b | -6.94855 | -42.87938 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| acb5dc7b-102f-33bc-a4c6-a84c7748ba6f | -5.99984 | -43.73363 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ebb1eabe-8239-376f-b879-88cca107fde9 | -2.91391 | -48.24099 | 2025-07-03 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| afea2621-fa7f-3289-a21b-370868a1be14 | -3.5123 | -47.21882 | 2025-07-03 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7b7c672-cf40-320e-825b-18c720330142 | -6.96838 | -42.88597 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bee2052f-c970-3500-8b56-9dd593ff3e34 | -7.43739 | -44.44362 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e908b843-4dfe-3659-bd13-6a329dd38749 | -7.67784 | -44.66719 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3614f845-67b1-3776-a706-f258c95a2706 | -6.58969 | -43.03965 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a646714c-e855-3623-9cbb-5a580f476844 | -5.72418 | -49.10675 | 2025-07-03 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e009b2f-e5b0-3763-b15c-479c9e8e6cca | -9.0397 | -49.72088 | 2025-07-03 04:34:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6886cce0-c221-3ece-849a-7efe972ed522 | -2.91447 | -48.23745 | 2025-07-03 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ff5a3e2-503a-357c-b7a8-c6fc3a4ac56b | -5.62756 | -44.26696 | 2025-07-03 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9ca1252-4821-3fb0-aad0-216ee0adb1e3 | -7.23144 | -43.06615 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ea44f918-d6d2-31b1-a705-bc918000ff15 | -4.53537 | -48.02172 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03ce269b-7471-3157-bb79-739794a5b3d2 | -6.96181 | -42.874 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9bb6d27d-7aac-347c-b903-b664862bb8a0 | -6.96536 | -42.87822 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7566c46d-237f-3d45-9eb0-07b08153c020 | -6.00222 | -43.74361 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a8fd807-08f4-30ee-a1db-7341b508b89e | -7.22689 | -43.06908 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2075188b-2764-379c-b0b7-25b95563433d | -6.95721 | -42.87703 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d7faa3eb-f7f2-30be-8495-9eda8f39385b | -5.92243 | -43.47867 | 2025-07-03 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ae52ba0-8fed-3e0a-b435-b53f93e4e9cf | -5.42817 | -49.08242 | 2025-07-03 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f744bf71-b359-3228-adce-3b0e79986efa | -6.17501 | -48.05685 | 2025-07-03 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b502faa7-9c79-3c82-ada0-76f52912f132 | -7.10798 | -47.84915 | 2025-07-03 04:34:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3d39fb0-487f-3087-ae60-c06cc8662adb | -6.6921 | -43.16149 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b5852613-31ed-3906-8b4e-0db5af8d745e | -9.112 | -47.63695 | 2025-07-03 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b440b7a1-455a-3da6-8ce9-c28bd8cf4d8c | -4.89825 | -37.37125 | 2025-07-03 04:34:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 901951e6-f1dd-3d64-8fa3-6f153b8598de | -5.72756 | -49.10728 | 2025-07-03 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2aeb2ce-5690-31e7-b8b0-4b61c039e1dd | -6.33176 | -43.75397 | 2025-07-03 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 205b5055-4114-3596-9dbf-c5a927711557 | -7.85744 | -47.87881 | 2025-07-03 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a80a732-a3e9-3f9a-ab79-269fd4b246e7 | -6.60224 | -43.03789 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45e33358-d855-3a95-9adc-2d861ee4fe74 | -8.49625 | -47.42151 | 2025-07-03 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6e394f0-6d26-3a98-bce3-5a1b461fbd0a | -7.43795 | -44.44674 | 2025-07-03 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca4d12de-c84e-3c81-ae22-30d2738f772c | -7.86354 | -47.88335 | 2025-07-03 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 573ed0d8-e81e-3bec-bd7d-d0d259ac61c4 | -5.6251 | -44.26414 | 2025-07-03 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97665ba5-1d92-3631-9637-f97484e0f85c | -2.89165 | -48.03505 | 2025-07-03 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58dd11c2-cd13-302c-8799-97a1e7aee13f | -6.96589 | -42.87459 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 186996ae-8857-3355-815d-eac0fae9ec11 | -9.17087 | -48.7737 | 2025-07-03 04:34:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d68ea48a-9651-3ea7-9f56-2898e3e67f01 | -4.32307 | -48.08065 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a51063ca-1e0d-3fe5-8bcf-c5791d0a4708 | -4.53592 | -48.01825 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb51ecdc-75ff-306c-a42c-8c5e753ba4a9 | -6.60768 | -43.89189 | 2025-07-03 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 823f81ff-637a-3298-b0ce-a995435507c2 | -7.09784 | -49.17051 | 2025-07-03 04:34:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 764d033f-44b2-3f7f-9e9f-194cea9315ad | -6.96076 | -42.88124 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 08236f9b-5da3-3c4e-bb03-45502298e91f | -7.02397 | -44.04409 | 2025-07-03 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a896a51-9c21-33ea-a167-701fb291d390 | -8.43582 | -49.19912 | 2025-07-03 04:34:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59cee734-510f-3e07-a683-f2a96d118234 | -6.68812 | -43.1609 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6b61e905-fac2-390a-b5bf-482db389e382 | -6.61149 | -43.89243 | 2025-07-03 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 466dde71-da6b-3941-998d-3bc42c281555 | -6.7137 | -43.18054 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf2ff282-80e9-3eff-a118-6863e0ce12b4 | -6.72381 | -43.13987 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae9b1d89-8346-3e8a-b0d9-2319be21bd9d | -7.06104 | -44.36141 | 2025-07-03 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f082cc4-b391-395f-ad30-14b2d61dc3e6 | -4.5387 | -48.02223 | 2025-07-03 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6aeac55e-d468-33e6-bce9-fa96b5c7c882 | -8.63169 | -50.03937 | 2025-07-03 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14fa6bb0-61d6-303b-b7da-60ed85616380 | -7.20368 | -43.08727 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8d31e8b-c056-33a6-b38b-8e0da284b254 | -6.29257 | -43.67617 | 2025-07-03 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cadcaa29-d38b-32ea-8307-7cadaf68cb8c | -5.39478 | -43.24557 | 2025-07-03 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4e393847-4ce3-30d1-880a-b63b27621c4d | -6.59709 | -43.04509 | 2025-07-03 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38e5f2b4-9b27-30bb-8bb4-94b754d9da23 | -6.96023 | -42.88483 | 2025-07-03 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| ca96ac21-92c1-3f10-b946-be532ea61f67 | -6.17556 | -48.0534 | 2025-07-03 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 95e0340c-fbc0-343c-bea1-44b2d5feb4f3 | -6.53748 | -55.03613 | 2025-07-03 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c40889db-de47-350e-858e-ebdcf56220e7 | -7.09256 | -44.37962 | 2025-07-03 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f97e6e8a-2853-3105-a200-f937a799a3bd | -6.17833 | -48.05738 | 2025-07-03 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6ee1fe69-a95d-371f-81d4-2fb9deed5343 | -14.85725 | -48.3353 | 2025-07-03 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bfe55a63-291c-3cfc-8f30-250ca60349ad | -15.62007 | -46.45936 | 2025-07-03 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dafb0808-b2cd-3dae-94ac-cdd0fdc8bfbd | -13.22758 | -57.13548 | 2025-07-03 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d15a919e-824e-3630-926f-7d47271054f3 | -13.38751 | -47.84322 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40610ccd-a793-3a07-a11c-40912050f33b | -12.43275 | -50.028 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15829b09-f5cb-3163-86bc-a9aecf48b50e | -12.42999 | -50.02387 | 2025-07-03 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9c5279b-f9d2-35d8-9996-8e6dc1228af2 | -15.35594 | -49.23091 | 2025-07-03 04:36:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29a0f53d-be48-34ff-b582-1b2b2478d368 | -15.07898 | -48.94527 | 2025-07-03 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9a39ccc-3439-3238-ae03-4a75c8746eb0 | -13.44814 | -47.83276 | 2025-07-03 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5864e59d-4281-34c6-b138-4a4f6575e81e | -13.65362 | -46.81435 | 2025-07-03 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebcc872d-a859-3064-ab0f-ca54861fdd0b | -14.6308 | -53.88268 | 2025-07-03 04:36:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
