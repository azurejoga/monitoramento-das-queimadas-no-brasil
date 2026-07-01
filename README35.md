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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8be05866-0c91-3fcc-8858-d7f9a1d2bd39 | -10.6598 | -54.5169 | 2026-07-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 254.5 |
| 6d5ac0f5-b922-3515-a1c2-b2607d5185c6 | -17.712 | -46.7798 | 2026-07-01 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 1793625c-7f1e-350f-83a5-bad90fe37905 | -10.6784 | -54.5356 | 2026-07-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 200.1 |
| 62bd3acc-6079-37af-bc13-a39f339b0a10 | -11.4336 | -56.0711 | 2026-07-01 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| d49b8d0c-6e9d-355f-8f2c-ff1408843fe6 | -8.7841 | -44.8315 | 2026-07-01 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c97ff445-20b8-3a66-8da3-5ebd3e61077d | -10.1237 | -52.0905 | 2026-07-01 14:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2a873b39-390c-3ec1-8eb3-e1fd01b2551f | -11.4338 | -56.0509 | 2026-07-01 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| a5f02edf-62a7-3107-b5cd-6fafacf80d34 | -11.4149 | -56.0525 | 2026-07-01 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ff4a4206-e6bf-354e-8b5f-fefacdfad44e | -10.6596 | -54.5372 | 2026-07-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 224.1 |
| d1390821-41ae-3758-8f64-28a1e3125a65 | -12.5135 | -48.2802 | 2026-07-01 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 93470445-aebd-371c-8193-a39d409fc3c8 | -8.9989 | -45.7191 | 2026-07-01 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1962b434-b42a-3502-bdcb-92de0d1525ad | -9.1833 | -58.0584 | 2026-07-01 14:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 687643bc-ba18-3ab5-bf9a-923898e998e9 | -10.6787 | -54.5153 | 2026-07-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 129dc350-9b3d-3dc4-8ae5-b68f06d6305e | -10.7654 | -53.5451 | 2026-07-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 5754fb8c-afd7-3b01-a44e-5078abd5b60f | -11.9113 | -43.3843 | 2026-07-01 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| ee696a7d-5ef6-3d24-962a-c6aadf5cb2c2 | -11.4147 | -56.0726 | 2026-07-01 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d7dc3532-e8dc-37b1-9369-020f37ab39b8 | -10.6596 | -54.5372 | 2026-07-01 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 279.6 |
| 0ea46365-7ce3-36bd-a9a2-d8d6dfc14986 | -11.4147 | -56.0726 | 2026-07-01 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d62a5088-f0f9-369f-8beb-a8c896111a8a | -11.4149 | -56.0525 | 2026-07-01 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 2810610e-3f35-3fef-8cfc-b80028048600 | -10.6787 | -54.5153 | 2026-07-01 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.8 |
| e760a95d-f891-3151-8e42-b61e5c3a9936 | -11.4338 | -56.0509 | 2026-07-01 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 30285bcd-229f-363a-876c-e4177e0dd634 | -10.439 | -49.5789 | 2026-07-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a604e8b6-01b0-3a17-889a-ea58e4348dcd | -12.5138 | -48.2581 | 2026-07-01 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6631978f-b3d5-3dfd-8ae3-a3d8b297b778 | -12.5135 | -48.2802 | 2026-07-01 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 74e7712b-6e17-32ea-8b87-52d49d4bef87 | -10.7654 | -53.5451 | 2026-07-01 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c85c7823-b776-3a45-94fe-6df3e9b85da1 | -10.1237 | -52.0905 | 2026-07-01 15:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 98dcb298-6373-3e3f-99a4-8169b22bf48d | -9.1833 | -58.0584 | 2026-07-01 15:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 3b32047e-1fc2-3882-b049-b266b48133b0 | -10.6598 | -54.5169 | 2026-07-01 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 231.0 |
| 6089db6f-23b4-3352-bdbd-7e2f70f727af | -11.4336 | -56.0711 | 2026-07-01 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| c4c524b0-7160-3c11-8a02-f660895f596f | -8.7841 | -44.8315 | 2026-07-01 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 648b43c2-c173-321b-bdea-40f14b440f69 | -9.202 | -58.0573 | 2026-07-01 15:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f8309d79-19fe-3122-a84c-9f08abd3cf22 | -11.9113 | -43.3843 | 2026-07-01 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| ccf4dc8b-45fe-3885-a017-ee09a54defd2 | -10.6598 | -54.5169 | 2026-07-01 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 264.7 |
| 0d8f7605-0d22-37ac-9e0e-08c1ee0a0f12 | -10.6787 | -54.5153 | 2026-07-01 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 221.4 |
| de943a36-5969-3747-aa1a-afe73c6390e3 | -10.7654 | -53.5451 | 2026-07-01 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2238babc-ec3a-3f9d-b075-b19b087064b0 | -11.4147 | -56.0726 | 2026-07-01 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| d441a6b5-d38f-3aca-b669-62af1bccc2c5 | -10.439 | -49.5789 | 2026-07-01 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 870a4fad-ba8f-3d86-814f-0c6bab30cbda | -12.5135 | -48.2802 | 2026-07-01 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| c2c668cd-eaf1-3e68-88cb-2ccde27e1c59 | -10.6596 | -54.5372 | 2026-07-01 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 249.1 |
| 04d71940-92aa-3819-9160-f3a047be7d07 | -9.1833 | -58.0584 | 2026-07-01 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 8dd704de-9ea4-38b2-945c-348de21e27ea | -9.202 | -58.0573 | 2026-07-01 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ba14f28f-8e7e-352c-a156-83260df84bf4 | -10.7843 | -53.5434 | 2026-07-01 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f911a41f-2141-36b1-8e34-b6ea8b6276a4 | -11.4338 | -56.0509 | 2026-07-01 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| a38b9cb7-41fa-3744-8291-5a8b2e84a038 | -10.1237 | -52.0905 | 2026-07-01 15:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e1550ef8-d22e-3ca8-bc38-4df983e788f6 | -11.4336 | -56.0711 | 2026-07-01 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| bdf0a1d1-fee3-3029-b969-fecb7a15a797 | -11.4149 | -56.0525 | 2026-07-01 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 0d304e6c-8782-3536-a371-6f6b1a297e65 | -11.9113 | -43.3843 | 2026-07-01 15:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 4bfda97e-5f87-3949-892f-64cb1444f0eb | -10.6784 | -54.5356 | 2026-07-01 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 227.4 |
| 2759796b-ba7f-3643-9b43-3502b8c90c6e | -10.6598 | -54.5169 | 2026-07-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 230.3 |
| 515a6d5c-f4ac-3d0c-8315-4d72e513a739 | -10.439 | -49.5789 | 2026-07-01 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 91bffb1f-df28-313e-87bc-252c10ebd3b5 | -12.5135 | -48.2802 | 2026-07-01 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 19828ae1-ec7b-36fc-b3a3-ffcc8e60701a | -10.6596 | -54.5372 | 2026-07-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 289.7 |
| 312b3bde-290b-3254-a8b7-015afd1f92f0 | -10.7843 | -53.5434 | 2026-07-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c37641ea-b058-303d-bd81-3b227fd10e11 | -11.4147 | -56.0726 | 2026-07-01 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 82a39624-2322-3ab6-8775-e2057cd98be5 | -10.6784 | -54.5356 | 2026-07-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 230.2 |
| 3148374c-4b96-3542-9769-49ba4e72fdf7 | -11.4336 | -56.0711 | 2026-07-01 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 344aa366-95a8-37b5-9fa3-4f5813801b5c | -9.1833 | -58.0584 | 2026-07-01 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| b831d3fb-14eb-3ae5-893e-fe7d5a5c8745 | -9.202 | -58.0573 | 2026-07-01 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| cdfc3dff-7a78-314d-a450-7a5f61d99aef | -10.7654 | -53.5451 | 2026-07-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 56a4791d-70a0-36a7-bfd0-2f577ec9ed2e | -10.1237 | -52.0905 | 2026-07-01 15:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f8bcfbba-33de-3360-ad0a-bc587d8ad636 | -11.9113 | -43.3843 | 2026-07-01 15:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 06c72732-7d59-3abc-81a4-867d98fb86b5 | -17.712 | -46.7798 | 2026-07-01 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 2c83cf4b-0a67-3f23-8cd5-6c70d11a1c96 | -11.4338 | -56.0509 | 2026-07-01 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| f5b88468-acb0-3494-a392-c327eea98280 | -10.6787 | -54.5153 | 2026-07-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 68d03bb0-2743-3c30-8d16-f2e318988e95 | -10.8485 | -45.0595 | 2026-07-01 15:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 95580089-4065-3a36-9e0c-ffac731c6cca | -11.4147 | -56.0726 | 2026-07-01 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 176.3 |
| da2856bd-66c7-3585-90a6-46ba4ffcbd20 | -10.439 | -49.5789 | 2026-07-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a8f8d99a-ab7c-3669-b7df-8f8a55ba7c2e | -10.1237 | -52.0905 | 2026-07-01 15:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 894a133a-075c-3e1d-9751-64ad90d6e117 | -10.6598 | -54.5169 | 2026-07-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 372d728a-43e2-3bbd-9b72-5b7eadd18acc | -10.7843 | -53.5434 | 2026-07-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 373e24a6-b613-3679-9dfa-0c5742519ac6 | -10.6596 | -54.5372 | 2026-07-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 191.5 |
| 630dc9b2-fcb7-37d5-84da-142ffa59e743 | -10.4387 | -49.6005 | 2026-07-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 79615939-6824-3db7-add1-a9c9b293cc22 | -9.1833 | -58.0584 | 2026-07-01 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| dfc7d228-f3fc-35b5-9423-8fc42df26da1 | -11.4336 | -56.0711 | 2026-07-01 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 7aad8e0f-4742-3039-b322-ef21492e09a7 | -9.202 | -58.0573 | 2026-07-01 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 2cdf752f-e03f-3322-a3ea-99efe84b694a | -17.712 | -46.7798 | 2026-07-01 15:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 624c8b7e-29aa-34ff-b4cb-7b1e359a499a | -12.5138 | -48.2581 | 2026-07-01 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 81dd7f55-a25f-3350-a5c8-fec2a8318867 | -11.9113 | -43.3843 | 2026-07-01 15:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| b33999e9-9122-3f3e-8e38-e507b73dd8ce | -11.4338 | -56.0509 | 2026-07-01 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 4e2523c1-79de-3543-befb-a2c5f0cc9cfa | -11.4149 | -56.0525 | 2026-07-01 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 176.9 |
| ab86fffe-00cd-3d76-b1d4-eae93f92b9b4 | -11.9108 | -43.4081 | 2026-07-01 15:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| afff933a-8bd0-3b55-9c2b-96eda8428962 | -12.5135 | -48.2802 | 2026-07-01 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 1d58371a-cbd7-383b-8b19-919db03f7ef8 | -10.6787 | -54.5153 | 2026-07-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 188.4 |
| 208e4ddf-99cb-3a9b-bda0-93c6d1029411 | -10.7654 | -53.5451 | 2026-07-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e53655fe-18f7-3536-b2a7-c3a36ddcf48a | -10.439 | -49.5789 | 2026-07-01 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 0466d666-2c01-31ab-87bf-73a6ee2b4a04 | -17.712 | -46.7798 | 2026-07-01 15:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 120626a4-a166-371d-b86a-49bd8e67c724 | -6.3142 | -47.5386 | 2026-07-01 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 55e6e738-a3ef-3809-bbd7-b84397dc6e17 | -11.4338 | -56.0509 | 2026-07-01 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 00bbd622-7daa-30e2-9539-1d490b1a103e | -10.6598 | -54.5169 | 2026-07-01 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 7bb6ae7d-62c9-31d0-b70f-651d68a95b4e | -9.1833 | -58.0584 | 2026-07-01 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b22c900f-3555-3807-8ff0-5a4ebb058bd4 | -11.4149 | -56.0525 | 2026-07-01 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 9ab42b5a-f22f-35ac-a82f-b3b29435ee7d | -10.6596 | -54.5372 | 2026-07-01 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 3adce1a7-074c-3e54-b183-caba8082f78f | -10.4387 | -49.6005 | 2026-07-01 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| bf66e679-6b1d-340a-8f90-a4bc56c17b10 | -10.7843 | -53.5434 | 2026-07-01 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 9ad9c5eb-cd83-39ce-85a4-c127471d26bb | -10.1237 | -52.0905 | 2026-07-01 15:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d07d9a8e-4800-3006-af89-6703a856e765 | -10.8485 | -45.0595 | 2026-07-01 15:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 117e527d-8bba-3934-b295-5108313963af | -11.4336 | -56.0711 | 2026-07-01 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 133.3 |
| b4bbd153-38eb-3a92-b304-355b7e19bdf8 | -10.6787 | -54.5153 | 2026-07-01 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 199.2 |
| b890262c-591a-3ff9-9c26-9d9630a0c52a | -11.4147 | -56.0726 | 2026-07-01 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 198.7 |
| d0b3e581-5b12-34cd-b624-a43b108e4b91 | -10.7654 | -53.5451 | 2026-07-01 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |


[Clique aqui para ver as próximas entradas](README36.md)
