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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f66b648b-3c1d-3461-9bdf-3a3c25fba81f | -17.712 | -46.7798 | 2026-07-02 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 159.7 |
| b5c61713-3a8a-31c6-9152-bcb612b727a0 | -6.9323 | -43.7264 | 2026-07-02 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 514aaefd-40a0-3e07-9363-297ae0d4a29c | -12.5135 | -48.2802 | 2026-07-02 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 30499333-3440-30e4-94a0-7f059ab8e0b7 | -12.5138 | -48.2581 | 2026-07-02 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 516a5a57-07e9-3c04-a4aa-3138d0f9d8d8 | -10.3663 | -46.7102 | 2026-07-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 4f325977-3b3c-333a-98f7-fb2d6e4320f0 | -12.5135 | -48.2802 | 2026-07-02 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 6529615f-5bcb-35a6-8f03-827b886708a9 | -12.8746 | -44.3357 | 2026-07-02 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 856aed8d-f48b-3588-9893-9f8cba79cc76 | -6.9326 | -43.7032 | 2026-07-02 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c44edc47-a68b-3eb9-b30c-02971e5110e6 | -10.3853 | -46.7079 | 2026-07-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 9cc6555a-efb3-37a3-a2b6-101137e51949 | -10.7843 | -53.5434 | 2026-07-02 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 87350e6d-d8fc-3d9d-b26a-6a666a7787e4 | -6.9135 | -43.7281 | 2026-07-02 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ad6a3efd-3591-3750-867b-77085655fd07 | -17.712 | -46.7798 | 2026-07-02 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 203.7 |
| ea516051-1869-31e0-acd9-363d0b48c861 | -17.732 | -46.7756 | 2026-07-02 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| fdff9365-f487-3e4b-a080-74e90bb2aa7a | -5.3787 | -43.388 | 2026-07-02 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 46f47c46-855c-3494-a92a-d85a1a0a0f75 | -6.9323 | -43.7264 | 2026-07-02 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 997893e5-f433-3c37-a65d-3faa6b880add | -10.3857 | -46.6855 | 2026-07-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 7cb5c628-a0c8-3da1-8e0f-e389935d0af6 | -17.7114 | -46.8031 | 2026-07-02 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 50de6c99-341d-3966-a24a-3454bca576aa | -12.5138 | -48.2581 | 2026-07-02 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 87955a32-cb0c-3ada-8bd6-0fbf81538d56 | -12.5135 | -48.2802 | 2026-07-02 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 65aef401-468a-3530-93df-3655cee490e4 | -6.9326 | -43.7032 | 2026-07-02 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 4ec9f65d-6b28-3fb3-8736-85a4b64425ac | -11.4149 | -56.0525 | 2026-07-02 13:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c278fbc3-46c5-3801-b9db-609f7e647df0 | -6.9323 | -43.7264 | 2026-07-02 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5390aa12-c228-3e34-8cf2-1ca4c556e38d | -12.5138 | -48.2581 | 2026-07-02 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 273923cc-2928-384e-aa5d-6e5cda97f30f | -10.7843 | -53.5434 | 2026-07-02 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| e1ac0f17-7848-3ff5-9e67-fba7521eb423 | -11.4147 | -56.0726 | 2026-07-02 13:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 2a4c9658-327d-3f9b-a92c-dbe94baae4ca | -3.8671 | -42.9685 | 2026-07-02 13:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 54b3a047-6cfb-3328-a459-6b13b6d94953 | -17.712 | -46.7798 | 2026-07-02 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 9c063931-9f12-38e6-9c37-dae519183a78 | -10.8032 | -53.5417 | 2026-07-02 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 12a1a085-7195-3c55-aa79-4a6785c5dfa8 | -17.732 | -46.7756 | 2026-07-02 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 42e94ad6-9878-3954-9ae8-8797c21412c1 | -5.3787 | -43.388 | 2026-07-02 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c8fe8689-fe4a-3f19-9f03-84991b778f68 | -6.9135 | -43.7281 | 2026-07-02 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f7410a16-5de9-3417-89f2-765a3c30388e | -17.732 | -46.7756 | 2026-07-02 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 90dc0b41-ea94-3b60-86ab-92cb5d1fdc77 | -6.9138 | -43.7049 | 2026-07-02 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4bf8ce3c-912b-3704-8461-d027236b662d | -10.8032 | -53.5417 | 2026-07-02 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b2bed8bb-0962-3770-9e83-42d988614f80 | -6.9326 | -43.7032 | 2026-07-02 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3e7d96ed-affc-31fd-85c9-4c613958490a | -10.7843 | -53.5434 | 2026-07-02 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| af3a9c50-b04f-3f20-9199-817bf3ebda98 | -6.9323 | -43.7264 | 2026-07-02 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e3fe85c0-412d-3da5-aca8-c218c874126d | -5.3787 | -43.388 | 2026-07-02 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0264e558-2d6a-30f2-82e7-54d2164c7dfb | -11.4147 | -56.0726 | 2026-07-02 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| edef25df-2b38-3d82-baf5-6081df4c384e | -17.712 | -46.7798 | 2026-07-02 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 5b8db227-82d7-3861-bb75-272489cd17a6 | -12.5138 | -48.2581 | 2026-07-02 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| dadd74d8-93b1-3839-97ec-e5e1fa7ccfd3 | -11.4149 | -56.0525 | 2026-07-02 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7e518d04-82c5-30aa-86b2-986cb1fb3ee4 | -6.9135 | -43.7281 | 2026-07-02 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 6c971344-e891-3d3a-a9f5-95dec35806b2 | -12.5135 | -48.2802 | 2026-07-02 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 9b597c1d-61a4-317c-8954-2b4f5436e8eb | -3.8671 | -42.9685 | 2026-07-02 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| edfb64cc-3dfe-3b84-9867-3459dd88157b | -10.7843 | -53.5434 | 2026-07-02 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| f3fb5073-b158-3e21-84cc-3250df2c848f | -17.712 | -46.7798 | 2026-07-02 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| a7623c84-6625-3a30-8379-f92ecb48b3c4 | -6.9326 | -43.7032 | 2026-07-02 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c1bbbb7d-5bc3-337a-8d2b-e18f751ec9c1 | -10.3853 | -46.7079 | 2026-07-02 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 6a29eb2f-54df-3443-97b4-cc53537ff125 | -12.5135 | -48.2802 | 2026-07-02 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| cf6903c7-28e4-3607-9093-fdf1b8515586 | -17.732 | -46.7756 | 2026-07-02 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 00fcb39a-874f-3dcc-ba0a-4e72d91b4d3c | -11.4147 | -56.0726 | 2026-07-02 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 1f8770af-5779-3fcf-879c-2d57875664f7 | -5.3787 | -43.388 | 2026-07-02 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| afc7052a-3a96-30b2-a8dd-6b2e1d743193 | -6.9135 | -43.7281 | 2026-07-02 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3cfec2ea-0aea-389c-a638-7f94458cce92 | -12.5138 | -48.2581 | 2026-07-02 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| fe6c5b16-47d5-3f29-af57-5082f19c8ae2 | -10.3857 | -46.6855 | 2026-07-02 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2db0d72f-3c46-3074-b1cd-94f7bb358b81 | -6.9138 | -43.7049 | 2026-07-02 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b9ae40d5-6722-3997-bfa4-61cb2a53cd8b | -11.4149 | -56.0525 | 2026-07-02 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 5f4784bf-5b27-39a0-add4-7cfedb7f8768 | -6.9323 | -43.7264 | 2026-07-02 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3510c83a-e182-3a22-bae5-3cabeead7d56 | -17.732 | -46.7756 | 2026-07-02 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3850b484-df79-3813-9ece-12c887551d35 | -12.5135 | -48.2802 | 2026-07-02 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 4e55ca05-19c5-3a3f-9c88-880f63ffd6f9 | -6.9323 | -43.7264 | 2026-07-02 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 3383a246-94b7-3721-9405-c3bb81fe3171 | -12.5138 | -48.2581 | 2026-07-02 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 738e47f1-1380-3a27-ab44-a14a21e884ae | -6.9326 | -43.7032 | 2026-07-02 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 45f8a694-3333-392c-a3cf-29ce89669c2a | -11.4147 | -56.0726 | 2026-07-02 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 189.5 |
| ffa1a473-3c06-3547-9bce-76ae8e01c60f | -17.712 | -46.7798 | 2026-07-02 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 117.8 |
| c0cdc614-9505-3c54-b4d4-88fd6520857f | -11.3655 | -55.431 | 2026-07-02 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 615f33fd-19d6-3f32-8299-8d28b2978a79 | -6.9138 | -43.7049 | 2026-07-02 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7d39e070-2d52-3584-9a5e-333a855dd513 | -11.4338 | -56.0509 | 2026-07-02 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 413b5648-27ea-3ace-878d-4ec3f18d8225 | -6.9135 | -43.7281 | 2026-07-02 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9c23380f-ae8f-33a9-b338-1914bd88a871 | -10.3663 | -46.7102 | 2026-07-02 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| be49c978-d0c3-37a4-ab33-5ba77d1cbca0 | -11.4149 | -56.0525 | 2026-07-02 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 224.2 |
| 9abcb541-5870-30ef-8247-ffa8d1500651 | -3.8671 | -42.9685 | 2026-07-02 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7afef6d4-e015-3089-bb97-7efceb8fa017 | -10.7843 | -53.5434 | 2026-07-02 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 4d3c8313-ca87-3417-ae82-2de02a8a19e9 | -10.3857 | -46.6855 | 2026-07-02 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| bd9c63d4-0402-3c1e-9b5b-3c7bdb8a091d | -11.4336 | -56.0711 | 2026-07-02 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f70243d4-6397-3de8-b5ad-a88dc5a283ab | -6.9326 | -43.7032 | 2026-07-02 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 97a0a648-dcdd-3a7e-b31e-5e0ca72d3be9 | -11.3655 | -55.431 | 2026-07-02 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7cbf92b2-2f5c-30f2-9927-8da19b42e985 | -3.8671 | -42.9685 | 2026-07-02 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 51b59abd-ab05-3a78-be6a-85e194ee32b2 | -11.4149 | -56.0525 | 2026-07-02 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 270.3 |
| 9f5546b9-ef93-3fa7-851b-cdc3e4a82d3e | -6.9323 | -43.7264 | 2026-07-02 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 70c855bf-c02b-322f-a958-f05e7ffea6b4 | -10.3663 | -46.7102 | 2026-07-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 53198715-abe4-302e-8f21-a295d2593185 | -10.3857 | -46.6855 | 2026-07-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0568ccbf-dc57-3b99-8a46-22cd20601d2d | -6.9135 | -43.7281 | 2026-07-02 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 36feaa13-f053-3386-98b7-dd28f8d6ff77 | -17.732 | -46.7756 | 2026-07-02 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8316dc4a-b87a-347b-ab1c-0f40544c3550 | -6.9138 | -43.7049 | 2026-07-02 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c6019b0b-0a04-3ada-8e2c-b7ccae9288c6 | -5.4738 | -45.4201 | 2026-07-02 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 701210cf-8252-3565-bdd2-6f01d83327aa | -11.4336 | -56.0711 | 2026-07-02 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 2815dc15-1812-3425-9327-560cda2ec2d6 | -12.5138 | -48.2581 | 2026-07-02 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 4c5177be-1dad-3b8a-bf1a-d2f297f76708 | -11.4338 | -56.0509 | 2026-07-02 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 245d92f1-7223-34ee-8b0b-dfaba612a81d | -11.4147 | -56.0726 | 2026-07-02 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 241.7 |
| 3bda9179-da02-336f-b272-f9a6ced472ad | -10.7843 | -53.5434 | 2026-07-02 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f8db034d-a510-3325-9879-af323c81a816 | -17.712 | -46.7798 | 2026-07-02 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 46423624-84e5-39c5-a1d8-0967f716ac8b | -17.732 | -46.7756 | 2026-07-02 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9a18a399-1d15-3de1-909d-f6a0d171d6b3 | -6.9138 | -43.7049 | 2026-07-02 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| cc157152-2782-3460-9656-a0cbef0ee6f3 | -6.9323 | -43.7264 | 2026-07-02 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 352e6608-6e93-3927-b11e-45dd60beb4f6 | -17.712 | -46.7798 | 2026-07-02 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 0228c29c-8715-368e-959f-63cf4df7bcbe | -12.5138 | -48.2581 | 2026-07-02 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 87a988a9-4034-3b80-b54d-31879c48ff7e | -5.4738 | -45.4201 | 2026-07-02 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| eac82152-2bab-3bf4-8a83-fd2f571a84cd | -6.9326 | -43.7032 | 2026-07-02 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |


[Clique aqui para ver as próximas entradas](README28.md)
