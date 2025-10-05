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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 009ed825-fc89-3da8-9c21-a533162518e7 | -14.62152 | -52.51192 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 701786ad-f33b-352d-b404-988ad940a4e8 | -13.74817 | -51.30755 | 2025-10-05 12:59:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| f4a7c6b4-c0e5-345d-91a7-a671784e4faf | -12.16188 | -50.92641 | 2025-10-05 12:59:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| c7cc6ac3-5333-3adc-bdb1-52939d128398 | -18.25621 | -53.33623 | 2025-10-05 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 007976a7-843c-3050-8d6c-20877db5d0b1 | -19.79124 | -51.97698 | 2025-10-05 12:59:00 | TERRA_M-T | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 1f10ef2d-0854-3bdb-92da-f18af61f447d | -17.96036 | -57.5973 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.1 |
| a8ce3317-f07e-3f6b-b51a-fd496d16ad23 | -19.79872 | -51.95734 | 2025-10-05 12:59:00 | TERRA_M-T | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4dfe895f-a05a-3ed8-9186-0b9be705e809 | -14.9802 | -54.83037 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 32ece6e0-2fdd-3991-bf50-064b21e604ec | -15.99419 | -59.52792 | 2025-10-05 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7f6e6541-6ca1-3ea8-9326-53824efe553d | -15.24015 | -56.76642 | 2025-10-05 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 982ccbc5-f6c2-3864-9496-cdd0dbef5531 | -19.78711 | -51.93021 | 2025-10-05 12:59:00 | TERRA_M-T | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 23.7 |
| ea0f2d7c-a40e-337e-af9b-a6323ddb4b36 | -19.00938 | -50.60754 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 185.0 |
| fbff69e0-a320-350f-96d1-45e1bfc6af8c | -21.46797 | -51.51175 | 2025-10-05 12:59:00 | TERRA_M-T | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.6 |
| 50f84020-c2cc-3d02-8588-9cc682de44f2 | -12.53599 | -54.74969 | 2025-10-05 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 57686dfa-600a-35ce-a59d-a8817a53cbb1 | -14.56367 | -52.46569 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| b0eabffa-3fda-3898-a914-9a9b6708bb8b | -15.58603 | -52.51774 | 2025-10-05 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 3b62bdf1-b5b4-372c-9671-57b683e62a26 | -16.38194 | -52.15656 | 2025-10-05 12:59:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 35162c56-1f34-388c-968e-02c31a247f49 | -12.75679 | -58.58537 | 2025-10-05 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7cb1f42e-a653-3c4f-82c3-c662e748c519 | -12.59533 | -54.76967 | 2025-10-05 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 7a6794b7-7420-3850-8f49-f1c80a112881 | -17.8788 | -57.59001 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| eaa85224-c6d4-3368-9b0c-253e1571a24c | -15.18724 | -52.81103 | 2025-10-05 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 05251cf6-1ab0-358b-aa7f-a796da323fb8 | -16.35567 | -51.4479 | 2025-10-05 12:59:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 23e21a40-252d-3a97-8492-7e2ac46063f0 | -16.09296 | -51.09208 | 2025-10-05 12:59:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 04735c98-a01b-3efc-9999-68b1899e9636 | -16.07866 | -51.09075 | 2025-10-05 12:59:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 065e2d78-7197-3c1c-aef6-075508701b4b | -11.32963 | -57.92361 | 2025-10-05 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6029fa2b-12e7-3a5f-9f2b-cd4c418effb9 | -11.87404 | -56.88298 | 2025-10-05 12:59:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 7de2d150-cee7-35e1-8ff8-2f23d82b0fa7 | -12.56487 | -54.76587 | 2025-10-05 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9aa338ca-63b5-30f5-88f4-63872db32093 | -12.58517 | -54.76844 | 2025-10-05 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 8ce2997b-0e60-31d6-bd9f-1cb8e997ce93 | -17.96304 | -57.57724 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4727cb71-4dae-3fcf-9993-779298d1af6b | -17.94992 | -57.53439 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 9e6650b5-ec1f-318d-b773-0ca85b194ffe | -19.00602 | -50.61301 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| 99750157-b2d9-379a-bc95-d3fac4b50f5b | -15.20278 | -56.83337 | 2025-10-05 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a0585ae5-4e4f-3578-accb-2b7fcc69e6ce | -17.89052 | -57.64232 | 2025-10-05 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 51893ebd-491d-3fb0-91c7-4224c98327e1 | -14.15668 | -53.03148 | 2025-10-05 12:59:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ead56dde-67c1-3ef1-ab59-a49359c6096e | -17.97347 | -51.151 | 2025-10-05 12:59:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 63f3f72b-d3f0-321f-82a0-5c57f328499e | -19.77983 | -51.94989 | 2025-10-05 12:59:00 | TERRA_M-T | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 194d18e1-1e0d-3542-b150-819be1e61af4 | -20.53361 | -52.2865 | 2025-10-05 12:59:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 6b6cb348-c8e4-383c-9fbe-08d1c6c0d620 | -15.64857 | -53.83523 | 2025-10-05 12:59:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a091eb54-6b17-3d65-ad8a-9681010fb77b | -15.58825 | -52.49836 | 2025-10-05 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 8a834ceb-1bae-31a8-ae50-a69bd7a34c83 | -15.21616 | -56.80399 | 2025-10-05 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 55e835a3-9563-33ae-850c-affdf8cd01a0 | -16.04093 | -51.03563 | 2025-10-05 12:59:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e55b1fc7-1b00-316f-8fd9-9e0804dde01f | -13.74481 | -51.29077 | 2025-10-05 12:59:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c31d0425-5ed8-39ae-97d9-9afa97542ddf | -19.78464 | -51.956 | 2025-10-05 12:59:00 | TERRA_M-T | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4c4ed6f7-ec4e-39e6-8b5e-a34563f307b3 | -18.25358 | -53.32864 | 2025-10-05 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f2944922-12e4-35f8-b3b2-109bd25d42d1 | -12.46552 | -58.56093 | 2025-10-05 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 576e8980-db5a-35e0-8622-8fc859515102 | -12.51535 | -57.3007 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 01f1abea-58a4-38aa-92b3-ad60428ded69 | -11.48377 | -59.08811 | 2025-10-05 12:59:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f11d9ea3-050b-353d-9c8b-4cde8fd43425 | -19.02431 | -50.58332 | 2025-10-05 12:59:00 | TERRA_M-T | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 6320ca81-fa30-3ef9-bfd2-f1d3bbaa7463 | -15.59865 | -52.51944 | 2025-10-05 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 81bea8db-3cfc-35b2-aeda-4765619975ea | -14.74183 | -54.62061 | 2025-10-05 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e9c487b2-e59a-3987-bdeb-646c737e7cff | -18.19822 | -53.37746 | 2025-10-05 12:59:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 85446e94-66e6-3934-b503-2cf0cce5a5f3 | -11.84428 | -57.75131 | 2025-10-05 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8d7e5b41-d83a-3287-b643-dfaad00c06ee | -13.7284 | -51.2908 | 2025-10-05 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 055317c5-7277-338d-92e8-b3271fb1b938 | -8.468 | -45.9332 | 2025-10-05 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cba9976b-15e4-3405-acd4-421432bd8adf | -10.9303 | -47.0882 | 2025-10-05 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 8ac9632c-df90-3413-8b1a-6d7ffb1233a3 | -11.8033 | -45.0856 | 2025-10-05 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 51a32e4e-af8e-34e1-b3dd-480250264a7f | -10.9497 | -47.0634 | 2025-10-05 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 2a31eec5-dd85-3368-9598-5ea821191a6e | -11.8418 | -45.0799 | 2025-10-05 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ba9e587e-88f7-3b6a-a585-9c205b51be06 | -8.5596 | -47.6813 | 2025-10-05 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| cc018f32-6091-3b94-8763-9516138bf34d | -13.7476 | -51.2883 | 2025-10-05 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 449ce8ce-ae8e-3f1b-82da-84b4d689b58f | -17.9605 | -57.5904 | 2025-10-05 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 72d11fc5-0580-39d9-83e1-5555729f4196 | -11.8225 | -45.0827 | 2025-10-05 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 890960d7-ee9c-3caf-a709-c6450588ecf9 | -10.6378 | -46.3396 | 2025-10-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 1a5dc955-25f9-3a91-ac73-5ed31dd9016b | -10.0504 | -50.4113 | 2025-10-05 13:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| d37351e8-2ec9-3836-bf29-f21132603d90 | -12.5672 | -54.7698 | 2025-10-05 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| cceca30b-ee89-35db-86e8-4305030b7ec4 | -11.4298 | -43.4833 | 2025-10-05 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 4e17822d-5b00-30e0-8cb7-fa0bd7e57c3f | -9.9556 | -43.7632 | 2025-10-05 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 7303673a-f6a6-366b-bc54-a9b6299291ba | -13.7473 | -51.3097 | 2025-10-05 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 309.9 |
| 756daed9-bc71-37a4-8fd6-3fbe9e7ab8b5 | -10.6568 | -46.3372 | 2025-10-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 5a5e732a-469a-303f-955f-ba9cf469c23d | -10.6382 | -46.317 | 2025-10-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4554fed6-2a74-3fc2-a508-b85cabd3c227 | -13.7469 | -51.3312 | 2025-10-05 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 2919093d-a735-3793-bb5b-0198b06460f9 | -11.8038 | -45.0624 | 2025-10-05 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 31ab359b-57f3-3d5a-b651-b821051d2613 | -15.6015 | -52.5102 | 2025-10-05 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 7d37da3a-7625-3af6-82c7-d1a41ef5e7af | -12.573 | -48.1615 | 2025-10-05 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| dc45afa2-a0dd-3299-b708-c793af0cc8c5 | -12.5863 | -54.7679 | 2025-10-05 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 263.3 |
| 55a15eba-4dfe-317c-b9d1-60287486d3f3 | -12.5733 | -48.1393 | 2025-10-05 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 82b5c73b-e4f4-3148-9392-4f127e1d3f2f | -10.8093 | -48.8229 | 2025-10-05 13:00:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 2e3e2e67-793d-32aa-a69d-53a99c915b16 | -12.6053 | -54.766 | 2025-10-05 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| a3046ba4-2e61-325c-8dbf-36cca3723c35 | -7.7746 | -42.5865 | 2025-10-05 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| d2c09666-2b82-3fc8-994b-22b06a4bf6e2 | -7.8127 | -42.5587 | 2025-10-05 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| c864cce0-33da-30fc-bee5-d4fb3bdd492c | -18.1769 | -53.3669 | 2025-10-05 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1902f29e-80b8-3ed8-8e91-0aaeef33b2e9 | -8.2316 | -46.8066 | 2025-10-05 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 178d6ade-29b2-3504-8739-2f03ac5a2353 | -12.7106 | -45.8452 | 2025-10-05 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| babe4ec0-e6ff-34b4-85f4-146150f2623b | -10.93 | -47.1106 | 2025-10-05 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 15df9bae-7a80-3ad6-9175-c97c1e1d0ab0 | -13.728 | -51.3122 | 2025-10-05 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 225.5 |
| f29f3923-4ed4-3deb-87e4-94fed7b81c5b | -17.9408 | -57.5928 | 2025-10-05 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 9d96722b-0ae7-3a0f-b85e-4c132429eea0 | -18.1968 | -53.3638 | 2025-10-05 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 743f370c-eb51-357f-9939-60e5f953fbc5 | -16.0966 | -51.0829 | 2025-10-05 13:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4921d7c2-e8a8-335c-9571-62a5961e0899 | -11.0313 | -46.7171 | 2025-10-05 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5a76195e-3577-3137-9e67-25684f4e5abb | -11.823 | -45.0596 | 2025-10-05 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |
| 6f257add-8bc3-3241-8cc0-b33c5e068272 | -7.774 | -42.634 | 2025-10-05 13:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 01d03515-f302-3b8c-98ff-b4ca2d2abe0b | -9.2973 | -46.0026 | 2025-10-05 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 15b2682b-2b20-38bc-81bd-73bb7e01f871 | -12.2876 | -49.2101 | 2025-10-05 13:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 92099a36-ec1a-340f-be6d-6b28cae65249 | -11.0978 | -49.8513 | 2025-10-05 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 69854a2e-ee2e-35c0-807f-9e63a96c495b | -7.7743 | -42.6103 | 2025-10-05 13:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 241.7 |
| f8086b3e-11fc-3cca-89cf-5fca13d96aee | -7.7938 | -42.5607 | 2025-10-05 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 52876d02-eb3c-3541-a90a-f9d4f28f11bd | -12.6913 | -45.8482 | 2025-10-05 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| c16c13c5-69da-3d05-a735-ed2c0c2d681c | -7.7554 | -42.6123 | 2025-10-05 13:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| b7bdc536-a2cd-3bba-9fcb-fa2e6b96528b | -20.7174 | -49.6306 | 2025-10-05 13:00:00 | GOES-19 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a91a912a-40ee-3c5b-8da2-db6f62d20690 | -9.9207 | -50.2323 | 2025-10-05 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |


[Clique aqui para ver as próximas entradas](README156.md)
