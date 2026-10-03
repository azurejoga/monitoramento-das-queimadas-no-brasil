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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6186e7d3-4441-3422-bf14-6bf8afb8b5d2 | -4.43266 | -55.7509 | 2026-10-03 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0407ceb9-0036-39bb-bf91-5aed1e298526 | -3.51395 | -54.61026 | 2026-10-03 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 1bdefad2-a742-318a-8b76-4902e857603b | -3.12281 | -53.73019 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9999a160-bc2a-3cfd-8939-b06f85b6f496 | -1.0861 | -54.10157 | 2026-10-03 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5d63aa9-b786-30bc-851d-f628a4f27367 | 1.91296 | -55.77927 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 38758261-bf12-3b86-b59a-f3c1d7ba4212 | 1.92433 | -55.73251 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cfb97b53-0d06-3c5d-a4cb-800f502878e3 | -0.36533 | -52.02488 | 2026-10-03 12:19:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 033dbb17-6c39-3a5e-baa4-972906f8cbd5 | -1.26984 | -54.56546 | 2026-10-03 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ca0951b1-b66d-337a-af0e-9d86d60a4558 | -2.93318 | -54.14997 | 2026-10-03 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 297defe2-29cd-39b2-b2aa-f270cb3a8514 | -3.13079 | -53.74155 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 3dd3710d-3957-3cb9-b15f-329b870924c1 | 1.84371 | -55.54564 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d2ad473-1b6c-38eb-92d3-a666a68f8722 | -3.13696 | -53.73844 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4101db59-1c3f-3e57-8897-02785ecc3181 | -3.85186 | -55.79813 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e7438960-78fb-30df-8e0f-dbf23b41f7f6 | -3.06105 | -54.16381 | 2026-10-03 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b11c7bc2-05fd-3ab8-a8b7-3d316e69cdf9 | -3.14754 | -59.01907 | 2026-10-03 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 97bebc29-eaad-38aa-ad36-20141dcff332 | -3.25029 | -54.51762 | 2026-10-03 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1536f2e4-e3e7-3f0e-925a-15bd5bcf1536 | -4.79611 | -55.72651 | 2026-10-03 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ec43162-424d-37e0-bd20-0286df4b2e0f | -4.42382 | -55.74971 | 2026-10-03 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 541e8488-2a59-39ac-9306-7c7540455668 | -3.79233 | -59.37091 | 2026-10-03 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 33b0e7f9-c5b7-3b66-be82-fde40517f430 | -4.53681 | -50.78477 | 2026-10-03 12:19:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| fc832417-78f9-31ad-be5d-c7b13bc50fd2 | 1.93317 | -55.73129 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 231d2d99-669b-373f-9a21-a954e4ce4a91 | -3.01823 | -53.88309 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 867c9494-95e3-3924-859b-2629d1015e28 | -2.28597 | -47.86696 | 2026-10-03 12:19:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| ffe0ca93-937c-34fe-a614-aa28d45582d6 | -3.22052 | -53.93879 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f369d615-383d-3b16-9af7-34958a80fac4 | -3.16147 | -48.73906 | 2026-10-03 12:19:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 023ddace-e0ec-3844-a99e-467350c7b69d | -4.12151 | -55.00976 | 2026-10-03 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dd5e5143-0ad4-30b7-8be9-19a5e31fc788 | -2.46959 | -54.75528 | 2026-10-03 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e134cbec-5c07-3781-9a5b-011f41631217 | -4.29973 | -54.79296 | 2026-10-03 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1fa6576-73f2-3957-8450-68e4e0e406a5 | -3.21912 | -53.94884 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b5a4c685-a18a-3067-98be-2604b2067f4a | 1.78543 | -55.59568 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f8b0bb7f-d98b-31fb-93a5-99a66714ce17 | -3.84741 | -55.97346 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 584d9a96-06d6-3a3a-9814-4e14856b703b | -3.7165 | -50.65505 | 2026-10-03 12:19:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 80eb2195-11c5-307d-b9f5-2cc990268e6f | -0.36699 | -52.01308 | 2026-10-03 12:19:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b9940df5-36db-3401-adb0-c6d93609daba | -4.78725 | -55.71035 | 2026-10-03 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bab85d00-5ed9-3997-8738-45f5e8c02e23 | -2.28121 | -47.88716 | 2026-10-03 12:19:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| df98546a-909d-336e-85f8-9a02136d522b | -2.21599 | -48.03845 | 2026-10-03 12:19:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5f7f516d-da64-3227-bd45-d3033788d08b | -1.35532 | -49.06874 | 2026-10-03 12:19:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f008c254-7e32-373b-b524-d9c8da6f7e1b | -3.13223 | -53.73146 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 0269d63a-e4c5-3222-b832-6337d7fb5034 | -3.76978 | -55.53777 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cc5da81b-b0c4-3a4f-abd3-d260dfce7242 | -5.25691 | -55.92067 | 2026-10-03 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d7639999-68e9-35e5-9592-561f2f77c5ef | 1.78037 | -55.6233 | 2026-10-03 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 56170d49-69a6-3fe7-a7c2-6d378ac606f4 | -2.97527 | -53.26342 | 2026-10-03 12:19:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 0e5bb650-4572-3f93-8943-23126166cd9f | -3.7622 | -55.52763 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03d23411-e697-32e2-a88d-d7dc16958bc9 | -4.30714 | -50.54279 | 2026-10-03 12:19:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 770923fa-d028-38c8-9118-676605448ae4 | -3.13836 | -53.72833 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 891dbc75-2673-375a-af79-26f96d58c29f | -3.12138 | -53.74029 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 369b5cae-d12f-3fd5-88b6-fbf30a0ce4b9 | -3.11235 | -50.28692 | 2026-10-03 12:19:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 42e1ee4c-90df-3171-b5ed-5999e457b452 | -3.51527 | -54.6009 | 2026-10-03 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| a71c47b3-626c-3571-b07a-95bcb6e89bdf | -2.98495 | -53.26464 | 2026-10-03 12:19:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f29e3ba6-4af5-34f5-8e1a-f6bf2698598c | -3.29197 | -53.83735 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2dd0f232-1f56-3498-b4df-f417198b0704 | -1.02764 | -53.73072 | 2026-10-03 12:19:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f79acb6-117d-37f6-bd4f-b43cbe55aa1a | -3.8562 | -55.97468 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 30fbf522-c610-3476-a227-2fed4816e332 | 2.5615 | -50.9577 | 2026-10-03 12:19:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f0feb988-fba9-35e6-b3b2-513ccd79a433 | -3.64721 | -55.49681 | 2026-10-03 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a5b83bc6-824c-31ab-a0da-13941b28c167 | -3.13557 | -53.74855 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 35aa48a0-a1ec-3192-89e5-43158001af39 | -2.28241 | -47.89383 | 2026-10-03 12:19:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| fad9f28a-a98b-368a-a906-25b45160bddc | -2.21952 | -48.01258 | 2026-10-03 12:19:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 847fd3c6-73de-3a7d-83d8-47716ac0dde2 | -3.13368 | -53.72136 | 2026-10-03 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3e900946-f1f4-336c-91a9-87f4b04a6f87 | -6.12773 | -57.8241 | 2026-10-03 12:21:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4355eddc-d3e9-3cb4-b675-60b389a5de23 | -10.99508 | -59.13564 | 2026-10-03 12:21:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| be70bc42-f9d2-34c9-8800-e05dc6fb5df8 | -9.83997 | -49.5197 | 2026-10-03 12:21:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f7d3e431-b924-3d4a-92d7-5c2e404c50e1 | -10.87271 | -57.11219 | 2026-10-03 12:21:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ee48130a-beec-3ccc-bad7-dc5b2de26746 | -6.21719 | -60.0255 | 2026-10-03 12:21:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| af2f61cc-3a3c-326e-ba75-b76a05fa5b5f | -10.87146 | -57.12116 | 2026-10-03 12:21:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1c3a6c4c-90ef-339a-acbf-2ce699395294 | -5.96522 | -55.34584 | 2026-10-03 12:21:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 30b4f3a5-2a0c-3745-81f3-ab470e94d642 | -10.99646 | -59.12627 | 2026-10-03 12:21:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 31aefb44-82b9-3419-9cda-8f52f9aed578 | -9.16624 | -61.39925 | 2026-10-03 12:21:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1dee23de-f0e9-3292-abe1-ce1bf2950ac7 | -6.0686 | -53.46309 | 2026-10-03 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| afc96f36-0037-3bce-8211-432f12b5b97f | -16.25053 | -59.29906 | 2026-10-03 12:23:00 | TERRA_M-T | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cdaee045-827e-3b29-94ad-fde3c221747d | -22.93402 | -50.60212 | 2026-10-03 12:25:00 | TERRA_M-T | SANTA MARIANA | PARANÁ | Brasil | 4123907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| a2ba8611-3595-35fc-ad2c-46198ee87ad4 | 1.9315 | -55.8205 | 2026-10-03 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 72f60efa-914b-3498-9d71-8132c2a61e80 | 1.9132 | -55.8011 | 2026-10-03 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| b0077aa9-3ca0-3669-8f7d-34c4ffadaebc | 1.9132 | -55.8208 | 2026-10-03 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 68840dd0-a06c-3591-b530-0588d272805a | 1.9316 | -55.8008 | 2026-10-03 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f8c60451-8755-3e47-b2d4-be3f1db5a1ca | 1.9132 | -55.8011 | 2026-10-03 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 82877333-4d3a-3239-afa1-0f1384a529a3 | 1.9315 | -55.8205 | 2026-10-03 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 32a66582-f04c-32ee-a972-41781f0da685 | 1.9132 | -55.8208 | 2026-10-03 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 4fade135-8a02-303f-88bd-5669441fe21f | 1.9132 | -55.8011 | 2026-10-03 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3a375554-8023-3a51-9953-36bc2195fa52 | 1.7854 | -55.6054 | 2026-10-03 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c8fb2d78-d0fe-33e7-8701-4ec32bf4c730 | 1.9132 | -55.8208 | 2026-10-03 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f4ee470e-1e69-3c4a-8db8-9e41dc3ca066 | 1.9316 | -55.8008 | 2026-10-03 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e3c28364-6044-3665-8b20-8535e91637e0 | 1.9132 | -55.8011 | 2026-10-03 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 5bbba7f4-0663-36b2-9697-befd64d620b0 | 1.7854 | -55.6054 | 2026-10-03 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 2d75023a-31dd-3b35-9c3e-05beead1a187 | 1.7853 | -55.6251 | 2026-10-03 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 0b73d437-ed4d-337d-99f4-e542363f1b02 | 1.9133 | -55.7813 | 2026-10-03 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0280fcff-2acf-372e-9121-59da5624f97b | 1.9132 | -55.8208 | 2026-10-03 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 4c2f1d17-f1a4-32e2-a866-5bfc1e7dce23 | 1.9315 | -55.8205 | 2026-10-03 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c14f9e13-26c8-3ac9-96b6-cece8ab11f04 | 1.9132 | -55.8011 | 2026-10-03 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7dd32dd4-2ebd-3c37-8aeb-516cbf0804a3 | 1.7854 | -55.6054 | 2026-10-03 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 98ad670f-5433-3028-b199-88bd9e14716a | 1.9133 | -55.7813 | 2026-10-03 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ec4cb906-99ed-375a-8f76-bc93af0febf7 | 1.7853 | -55.6251 | 2026-10-03 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2d02ce03-2910-3ee8-9bc9-e47811143814 | -11.1183 | -54.0062 | 2026-10-03 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 1d7d8182-c131-373d-ad8d-508eb7ce3b07 | -13.0584 | -51.205 | 2026-10-03 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b2d28fa2-848b-39d3-b867-b4072767ccb7 | -10.9879 | -59.1393 | 2026-10-03 14:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b8abe605-6de0-3e62-907d-3b7f456297d1 | 1.7854 | -55.6054 | 2026-10-03 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 15c347c0-5ac1-3c53-8287-6620bacbdf69 | -11.1183 | -54.0062 | 2026-10-03 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3dd9eb5d-b69e-3390-a371-db56e02389c7 | -13.1153 | -51.2407 | 2026-10-03 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 55e144c0-4b36-34c8-966e-a8e646b62a15 | 1.7854 | -55.5856 | 2026-10-03 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d4e47b43-1373-3067-b321-21b3c77a9511 | -8.8705 | -66.7822 | 2026-10-03 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| b857ae51-5c78-35d2-b32c-2fc86f9c7216 | -13.0009 | -51.2122 | 2026-10-03 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |


[Clique aqui para ver as próximas entradas](README48.md)
