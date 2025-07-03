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
| a1fb6ed8-4821-3a6a-a2a4-010917cae717 | -18.1995 | -51.3701 | 2025-07-03 00:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1bde7425-544c-35bd-9ec9-b86f803d490e | -9.1668 | -48.7794 | 2025-07-03 00:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 2b72e41d-a315-3e83-b1e7-0f488e8cdf37 | -6.2945 | -43.6659 | 2025-07-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| cb88f4f6-7da0-3ebc-bd3b-8924f484b9d5 | -7.184 | -43.0954 | 2025-07-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 5bb86466-5ce8-3836-997a-d3227a526018 | -14.6291 | -53.8809 | 2025-07-03 00:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 6b8da6a9-ec8b-3ccc-9491-00eebae0c145 | -7.2031 | -43.0701 | 2025-07-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 3cc05263-c3bc-355b-80d1-ac54f8d16ad6 | -6.1792 | -48.0494 | 2025-07-03 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 3a0c5491-598c-3517-b090-ecda6e3f9379 | -6.1791 | -48.0712 | 2025-07-03 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a5655906-556e-331c-be5a-d26cefa298be | -6.6112 | -43.8941 | 2025-07-03 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 709a1dff-33d6-3521-aa18-ae96fe4b2ada | -6.1792 | -48.0494 | 2025-07-03 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 203.8 |
| bc9b025d-0ba2-38e6-8a6a-0de41e4b05ea | -11.6379 | -48.0866 | 2025-07-03 00:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 713dde11-3f9f-3a54-b86f-d2b4d70ec11c | -6.9419 | -42.8598 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| c2c71b83-21eb-3c59-a220-a5a6bb92616a | -9.1668 | -48.7794 | 2025-07-03 00:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 93.4 |
| dd6315a5-a373-3ced-b050-34ee3ba608ea | -6.1791 | -48.0712 | 2025-07-03 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| a90a7418-deb0-3079-8307-03a2ceb7262b | -9.1857 | -48.7776 | 2025-07-03 00:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 53b1f4c1-8f42-30c2-86ca-9b03beac1a37 | -18.22 | -51.3446 | 2025-07-03 00:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 2c4145f1-2c05-3b06-826d-80dba3928d7d | -11.6396 | -44.6003 | 2025-07-03 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 01f1a4d6-5ef8-3737-8c92-020254ed9e89 | -6.2945 | -43.6659 | 2025-07-03 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 732201d7-4cba-303f-b7a8-73c9687c098e | -14.6287 | -53.9018 | 2025-07-03 00:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| c099cfc3-6673-3723-90dc-b5f52b7d20a3 | -6.9605 | -42.8816 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 384.9 |
| 15b8d7a5-c573-3ed8-b995-b3280b819e3d | -9.186 | -48.7559 | 2025-07-03 00:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 81.9 |
| ead1a032-a603-3edc-a487-1ea9a9202d90 | -6.9602 | -42.9052 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| b60be85f-9e58-38a5-a772-71af00fdd85b | -11.6592 | -44.5741 | 2025-07-03 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 209.2 |
| c7d226f8-cace-3b84-9b0d-d7e99f8c0f5b | -11.6588 | -44.5974 | 2025-07-03 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 67712cd6-f549-3f35-86d8-1fe9824dcc75 | -6.0206 | -49.2234 | 2025-07-03 00:30:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e64dc995-60af-306c-bcb6-9c509f870b7b | -7.2222 | -43.0447 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 203.8 |
| 2fdc61e5-a5a3-3751-b84e-6a8c5b8fda1e | -6.9607 | -42.858 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 860e0185-5c3f-3a6e-a64c-cf6a82e820c1 | -6.9793 | -42.8798 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 25aee655-8ef1-3ecc-aeed-e61fdcb2fb1c | -14.6481 | -53.8994 | 2025-07-03 00:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 961e6f26-08f8-3f03-992c-de8393d472ae | -14.6291 | -53.8809 | 2025-07-03 00:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| eacc9478-20d3-3f82-b4d6-9f44be3c7f9e | -18.2 | -51.3481 | 2025-07-03 00:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 1a3734d0-4824-3617-b7d0-0df118b019f2 | -9.1671 | -48.7577 | 2025-07-03 00:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 45065771-d3d1-3e8e-b302-0926ac3c3d79 | -9.6417 | -61.4615 | 2025-07-03 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5d81cc30-ac57-3123-956e-233dc2f97aaf | -6.9416 | -42.8834 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 163.9 |
| 3b35cda1-9a69-398b-8a4d-89f75b503995 | -18.2195 | -51.3666 | 2025-07-03 00:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6a3975a4-7eeb-3dcf-ac1b-ae7cba3cde93 | -14.6484 | -53.8785 | 2025-07-03 00:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d54482d6-a8fc-3813-9d42-4d7ec4db392e | -7.2408 | -43.0664 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 820646f0-9e7d-329d-ab53-7f86133bf2cd | -11.6383 | -48.0644 | 2025-07-03 00:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e1c8ab61-e5c0-371f-821a-bff6c001a139 | -6.2943 | -43.6891 | 2025-07-03 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0e978d43-9f39-3025-a665-b67bf7973d34 | -7.2028 | -43.0936 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| f31bf872-363a-34c1-ba93-b2b98175fcb5 | -11.64 | -44.577 | 2025-07-03 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| d7e19f8f-9565-3433-9593-acd2d3d11c12 | -6.1606 | -48.0507 | 2025-07-03 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1e915e90-e8f8-372e-b4aa-b9719165987c | -7.2219 | -43.0682 | 2025-07-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 365.3 |
| c576b03b-b5e7-3fc6-a2a1-7f57fd85e27b | -7.2222 | -43.0447 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.0 |
| a57ce778-fb43-3a2e-ad95-d235ff92faab | -18.2 | -51.3481 | 2025-07-03 00:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a7899ca1-1de2-3741-862f-4a21200a1270 | -11.6592 | -44.5741 | 2025-07-03 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| cfc0a5af-12ba-39cf-8bcf-7793d3f241d3 | -6.1606 | -48.0507 | 2025-07-03 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 76788885-0ceb-3a56-8d3a-600cc25d9a13 | -9.1668 | -48.7794 | 2025-07-03 00:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 612a164c-d82a-33ee-b0b0-70ad5555a701 | -11.6588 | -44.5974 | 2025-07-03 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 3a4c9282-9d7a-38a6-abf6-03fa01621806 | -6.1792 | -48.0494 | 2025-07-03 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 12b388cf-0b68-3d1c-b905-bf55cc8edae8 | -18.2195 | -51.3666 | 2025-07-03 00:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3515adab-5010-3de7-a381-bc2207b5102e | -6.6112 | -43.8941 | 2025-07-03 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 19faccb5-305f-3041-a86b-ff840662b46b | -6.9607 | -42.858 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| a9be19ac-0c76-34e2-8a2e-c4a8cd09318b | -11.64 | -44.577 | 2025-07-03 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a7669ae1-f425-3205-8f02-a8947868addb | -17.9371 | -50.6685 | 2025-07-03 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 12d1a7e6-ff97-3097-91f4-f46798595c23 | -6.9793 | -42.8798 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 3f1c9fd3-e66e-339c-9675-6bb8aae1b470 | -6.9605 | -42.8816 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 481.5 |
| b49736d4-104a-38f8-b2b6-ae7cb1964cfc | -7.2408 | -43.0664 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 780a4486-c7e1-3ace-869d-5a55be5a4930 | -17.957 | -50.665 | 2025-07-03 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 661060ef-abe8-3511-a538-4fb89dc9eea7 | -6.1791 | -48.0712 | 2025-07-03 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 358b849a-6d12-3d93-8320-4fdc7109a132 | -11.6396 | -44.6003 | 2025-07-03 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2b036df5-9ef3-33f4-be32-bbf4a43af32e | -9.1857 | -48.7776 | 2025-07-03 00:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 5fedee80-68fc-3751-b1d1-ebbc2c6666ee | -14.6291 | -53.8809 | 2025-07-03 00:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 879b9450-7257-344f-aa93-da3d407c54d0 | -14.6484 | -53.8785 | 2025-07-03 00:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 84a60100-42ea-3d31-b666-1488907536bb | -6.9416 | -42.8834 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 194.8 |
| 6121f502-175b-303f-8c45-5cfe0195fb1b | -6.9602 | -42.9052 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| ae134c7d-f12c-3980-b6b1-d63074ba8e64 | -14.6481 | -53.8994 | 2025-07-03 00:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| cc8d941a-9ea7-368c-a7d5-5e46092dc6bb | -17.9565 | -50.6872 | 2025-07-03 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 7e045951-045a-30d3-9160-908ee693f19a | -18.22 | -51.3446 | 2025-07-03 00:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 6a786993-438a-3daf-9a2d-4afb74e987d1 | -11.6383 | -48.0644 | 2025-07-03 00:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 8ddfbaa4-22b1-364e-aa5d-e84179dc87e8 | -14.6287 | -53.9018 | 2025-07-03 00:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ed674723-fbd5-39e8-b3d0-9fc37561651d | -7.2028 | -43.0936 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 733be7b8-7d42-3fc7-855e-7d57115e7a4b | -6.0206 | -49.2234 | 2025-07-03 00:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b9db1e7e-2d77-3aea-84a5-1c91debf190a | -7.2031 | -43.0701 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| b8724bcd-3456-3217-981c-31faa916e631 | -7.2219 | -43.0682 | 2025-07-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 332.8 |
| 0d2131dc-2cdf-360d-a685-60098150cde8 | -9.1671 | -48.7577 | 2025-07-03 00:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7e13ba8c-2711-3f8e-86ce-f040458d9e01 | -11.6379 | -48.0866 | 2025-07-03 00:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 24dbf2c5-6970-3666-8854-a6c139e1349e | -18.22 | -51.3446 | 2025-07-03 00:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 193.1 |
| d9062600-5d53-3c13-a7ac-c8065b4e9570 | -7.2219 | -43.0682 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 228.7 |
| 4ed7c3f1-5e80-3560-9abe-6bec477db9b2 | -11.6592 | -44.5741 | 2025-07-03 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| b5719b7b-231a-35d7-b598-c3d460e169a4 | -11.6588 | -44.5974 | 2025-07-03 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 4978b821-523c-3cbd-a732-60f2f2fa05fb | -7.2222 | -43.0447 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| 483e347e-5741-382d-9145-ffb4271f5217 | -6.9793 | -42.8798 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 2b3f10af-6516-3485-9b45-667f451580b5 | -6.9605 | -42.8816 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 478.3 |
| 07255ba3-34dd-3e67-8ebd-fd9aaeca0866 | -18.2195 | -51.3666 | 2025-07-03 00:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d42cc4f6-3967-3642-a73c-bf7c4636f6e1 | -9.1668 | -48.7794 | 2025-07-03 00:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 4a9b3607-3101-3424-b868-03346e9c7c27 | -17.9565 | -50.6872 | 2025-07-03 00:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 49348ebc-5f9b-3364-ae79-2b9b7725a006 | -7.2411 | -43.0428 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 57ea8e5c-8f19-32c9-b910-c9199c1547c7 | -6.1791 | -48.0712 | 2025-07-03 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| aaf67d0a-abd1-3074-97a0-3289315a8b2f | -9.1671 | -48.7577 | 2025-07-03 00:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8138c558-1b5a-3d36-ad0c-5ee766f390e3 | -6.9416 | -42.8834 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 235.5 |
| 359bc1a1-0e1e-32eb-9dee-e880a74b628d | -14.6287 | -53.9018 | 2025-07-03 00:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 78eda2da-3ab7-31ed-bf48-e8c460391fad | -17.9371 | -50.6685 | 2025-07-03 00:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 091d9655-a8de-3925-922e-7ab564dc1b04 | -14.6481 | -53.8994 | 2025-07-03 00:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8882efd5-9e32-3f1d-a574-28a2eb6ab4c6 | -6.9607 | -42.858 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 244c16b2-c481-3931-8026-43b61e2917a8 | -6.9602 | -42.9052 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| a5691d8d-e5a5-306b-854e-7f23809ca64a | -7.2408 | -43.0664 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.2 |
| 18a71884-109f-3f62-b6fa-bfe83732efba | -14.6291 | -53.8809 | 2025-07-03 00:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 184.8 |
| cc5372ad-aa00-3f3c-aea4-694618714045 | -17.9575 | -50.6429 | 2025-07-03 00:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 232f3afb-7fa2-306c-a0d9-35ed96faa4f1 | -7.2031 | -43.0701 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |


[Clique aqui para ver as próximas entradas](README3.md)
