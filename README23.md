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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 092c5ead-8c07-3c39-afa8-af896effac34 | -11.6785 | -44.5712 | 2026-07-07 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e800a1c9-5842-3909-a1fc-36eff3a3e0fb | -6.9138 | -43.7049 | 2026-07-07 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fc40d4d7-26e4-377c-b454-d9a591d35112 | -11.6789 | -44.5479 | 2026-07-07 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| eefa7a83-1ce8-31db-a659-e5b8ea6f1987 | -15.5135 | -42.1948 | 2026-07-07 12:20:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 7e636265-5f0b-3e09-b037-b60dab158b9b | -6.9326 | -43.7032 | 2026-07-07 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 696a3f69-4ad5-37b5-88b4-175d5f08ec24 | -6.9138 | -43.7049 | 2026-07-07 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 27495097-fcbd-338c-b342-853acc3497c1 | -11.6785 | -44.5712 | 2026-07-07 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 2547e624-cbcc-38be-883f-7ad3a4788807 | -9.3713 | -48.82132 | 2026-07-07 12:25:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ab6f9f9a-6186-3921-9d54-4939dd19252a | -8.12093 | -47.103 | 2026-07-07 12:25:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 53e85a9d-919d-3430-8326-fb0c201f1ea2 | -7.39893 | -49.76336 | 2026-07-07 12:25:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 7e77ee36-81ec-3515-9281-6ca0fb891964 | -9.37406 | -48.79813 | 2026-07-07 12:25:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 6673eae3-39d7-3de9-a25b-f3ef96e92392 | -8.11759 | -47.10897 | 2026-07-07 12:25:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 20d75a14-dbd9-3310-84a9-48dd3046ae48 | -7.90412 | -48.25056 | 2026-07-07 12:25:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 19f78c00-bf67-3750-9a8d-9269f3aa83f0 | -10.42047 | -46.86985 | 2026-07-07 12:25:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 5e2b97a9-317d-3a70-beac-03d4a0bf6c0d | -9.3671 | -48.7905 | 2026-07-07 12:25:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3f6214f1-aeb3-35be-a442-a56a31dd40cb | -7.39657 | -49.78125 | 2026-07-07 12:25:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 29ec1aa6-ba7e-355d-aead-6016a564c935 | -9.3642 | -48.81347 | 2026-07-07 12:25:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 6265d4d7-7c17-3384-b5c2-0dd7c33599cf | -7.40248 | -49.77034 | 2026-07-07 12:25:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 769bae4c-f6ac-3373-96ab-a9d70d41a02a | -10.77834 | -54.1073 | 2026-07-07 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 108ee57e-6ce8-39ba-af38-0f30b2caa6bc | -17.38484 | -52.12814 | 2026-07-07 12:27:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d277834c-4446-3f58-80bd-1f306006a1cc | -13.32029 | -54.37159 | 2026-07-07 12:27:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 023848f7-9bc3-32f7-bb47-43fbd90fff34 | -13.53598 | -52.95069 | 2026-07-07 12:27:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| ada7f876-0d26-34f5-8b30-16837863b282 | -13.54084 | -52.91165 | 2026-07-07 12:27:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 29fdee9b-320f-3ac8-b7f5-bd650964f3d9 | -17.3868 | -52.11052 | 2026-07-07 12:27:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c9e3a387-d077-3537-94ca-1ea4404ba63a | -12.51217 | -48.26632 | 2026-07-07 12:27:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 5a062515-0f96-392c-8148-fba064d83c06 | -12.51118 | -48.27282 | 2026-07-07 12:27:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| fbb7688c-5080-3c72-9fad-7e4c4722a591 | -11.55821 | -52.79141 | 2026-07-07 12:27:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 42369df7-aaef-387c-802e-74ba255dee69 | -12.49722 | -48.26451 | 2026-07-07 12:27:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5d176b38-59dd-3fd7-8d57-847bdbad8158 | -13.5376 | -52.93769 | 2026-07-07 12:27:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 2c6cf314-931b-36e6-9e94-a7833466ff07 | -17.38363 | -53.03912 | 2026-07-07 12:27:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 72b2d7fa-d6c8-3595-8e02-9c09499faae3 | -12.34426 | -50.0231 | 2026-07-07 12:27:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fa25e095-61bb-3713-8d1b-b857edc1fae6 | -13.3217 | -54.36108 | 2026-07-07 12:27:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b303c714-8328-3680-9e6e-0edc3617c7e2 | -22.01879 | -48.22976 | 2026-07-07 12:29:00 | TERRA_M-T | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 297edd40-a7fa-37ad-8cdd-4b1e1093072f | -22.02297 | -48.23508 | 2026-07-07 12:29:00 | TERRA_M-T | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 3cdb2377-382b-3b9a-b24b-708597cc972c | -15.5135 | -42.1948 | 2026-07-07 12:30:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 2965b88a-b823-3656-b7d7-29fb9c4dad1c | -11.6789 | -44.5479 | 2026-07-07 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 158e11b3-1600-3b5d-88a2-f3a706ee3b7d | -11.6785 | -44.5712 | 2026-07-07 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 1221d39a-3b37-3b64-965a-6e10506d3758 | -11.6592 | -44.5741 | 2026-07-07 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 66de49df-a227-3cc1-a89f-d1eabc6b1441 | -6.9326 | -43.7032 | 2026-07-07 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a4b43ef4-d0ef-3bf0-966b-5b97c64aaf6d | -6.9138 | -43.7049 | 2026-07-07 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c9def9aa-cb03-365a-84d4-16ba32a2a438 | -6.9326 | -43.7032 | 2026-07-07 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 14a7ebcb-5538-3f85-94e6-caff1ed44e21 | -11.6785 | -44.5712 | 2026-07-07 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 5ee2899e-821d-3994-bf8a-e15b40ad1b3d | -11.6592 | -44.5741 | 2026-07-07 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1c7bf2cd-8e23-3b72-b0d9-453c9ece4c11 | -6.9138 | -43.7049 | 2026-07-07 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 02304eea-061b-3d6f-8245-9dec37fd8424 | -15.5135 | -42.1948 | 2026-07-07 12:40:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 0719ca69-6268-3b71-ae0b-b3cb6569188d | -11.6785 | -44.5712 | 2026-07-07 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 661151de-0c46-3c44-9cdc-205ca5d43017 | -6.9326 | -43.7032 | 2026-07-07 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 153.4 |
| c8890e3c-409b-3413-98b5-5d87b6603f95 | -11.6789 | -44.5479 | 2026-07-07 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 377ec201-dd3d-3d0c-8166-3962c8a13f17 | -15.5135 | -42.1948 | 2026-07-07 12:50:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 178.3 |
| c6fddfb7-4151-3409-8302-231e2219071d | -6.9138 | -43.7049 | 2026-07-07 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 70fe5547-97d5-3bfd-af60-4a8ebe2d9244 | -11.6592 | -44.5741 | 2026-07-07 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| e3e263c8-5fb9-3714-bf50-d7806f61dad4 | -11.6785 | -44.5712 | 2026-07-07 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 772f726b-6b75-3360-8f3f-a63ac7e98dd5 | -6.9326 | -43.7032 | 2026-07-07 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 181a659c-98a9-3503-ac6d-fcd7f41fcb5e | -6.9138 | -43.7049 | 2026-07-07 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 5c28b65f-004f-3ef6-9f28-6aab53d85ff2 | -11.6789 | -44.5479 | 2026-07-07 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| dc68761c-82c7-3cb6-bd13-328757dcb0ee | -11.6592 | -44.5741 | 2026-07-07 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 48553af1-eb81-341d-ba1b-035930ca17be | -12.5138 | -48.2581 | 2026-07-07 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b65814fa-8fbc-3821-af29-3a1f7ee25bc0 | -6.9323 | -43.7264 | 2026-07-07 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 673ea9b5-bf36-3753-b222-16865a7b5fe0 | -6.9138 | -43.7049 | 2026-07-07 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 143.7 |
| b6f3d9da-fa7e-36a1-bd2b-4e7351a7422c | -6.9326 | -43.7032 | 2026-07-07 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| a5864d63-c7cd-3207-b086-10d071c6714a | -11.6789 | -44.5479 | 2026-07-07 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 34305ee3-09f3-3ce1-aa18-1e87188decf5 | -11.6785 | -44.5712 | 2026-07-07 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 24a02d03-b3c5-37b6-85c7-9fa98f4487b6 | -13.5292 | -52.9249 | 2026-07-07 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 95096c19-8923-3577-8bbb-88f14687ac43 | -11.6592 | -44.5741 | 2026-07-07 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 0c6dbf1b-7ccb-350a-95c1-abf96ede8148 | -11.6592 | -44.5741 | 2026-07-07 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 283a8f33-c8ef-32a7-8999-f63cb655cc66 | -6.9138 | -43.7049 | 2026-07-07 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| eaecdce4-8be8-3684-9c32-9aeb91703ab7 | -6.9326 | -43.7032 | 2026-07-07 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 192.6 |
| d380a6bb-8ad7-3ce7-9b98-ead7b45d0181 | -13.5292 | -52.9249 | 2026-07-07 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 10dd2436-e515-382e-b674-0d2c7f267e76 | -11.6789 | -44.5479 | 2026-07-07 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 89b431fc-a32b-397b-be3a-78cca8833d03 | -6.9323 | -43.7264 | 2026-07-07 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2e337034-9838-347c-be50-88802244e5e9 | -11.6785 | -44.5712 | 2026-07-07 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| f9ef452a-b1a4-3eee-9f7c-3d746235aec1 | -12.5138 | -48.2581 | 2026-07-07 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4abcaa69-8f4a-3073-9b31-214bfc41eb8b | -6.9326 | -43.7032 | 2026-07-07 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 764dd6ea-19d7-31b2-b154-fd9b72c3692d | -6.9135 | -43.7281 | 2026-07-07 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 097d7612-ab95-3534-959c-456b2bdbfc07 | -12.5138 | -48.2581 | 2026-07-07 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 89d8099e-563f-348c-a574-93769b205e0d | -10.4397 | -46.8804 | 2026-07-07 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7ef3f104-9c59-3c0c-8e42-22126a8cfe0f | -11.6785 | -44.5712 | 2026-07-07 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 782501dc-2247-3bca-836e-16dbb07e1346 | -9.3736 | -48.8025 | 2026-07-07 13:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 54781d82-d4f3-3db9-9715-cf59bd1117c1 | -11.6592 | -44.5741 | 2026-07-07 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8bedf246-af99-31bd-baea-54eb84b3c701 | -11.6789 | -44.5479 | 2026-07-07 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 6ec312a2-5331-387d-853a-1241d8ca7ea7 | -6.9138 | -43.7049 | 2026-07-07 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 237.5 |
| d2ab20a8-201e-389b-83ff-c9ad0dfbdc01 | -6.9323 | -43.7264 | 2026-07-07 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 85edba68-fb88-3f30-9cb4-e4fd7e9ae932 | -15.5129 | -42.2195 | 2026-07-07 13:30:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4c10f789-7cd7-385a-af3d-327f463dbcee | -7.3945 | -49.7692 | 2026-07-07 13:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 728ad4ec-055b-34e3-a17e-ce3b997f3072 | -13.5292 | -52.9249 | 2026-07-07 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 99bb4ef2-9903-3858-9488-a1ece0896e96 | -11.6789 | -44.5479 | 2026-07-07 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4f7ac9df-5a5e-3ce0-b812-310eb93b3357 | -6.9135 | -43.7281 | 2026-07-07 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| d9fb5467-b04c-3f91-82d3-c1638b769c8a | -6.9326 | -43.7032 | 2026-07-07 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 230.3 |
| d012645f-22af-30f0-881e-6583a7b1b1ab | -6.9323 | -43.7264 | 2026-07-07 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| ca7de850-0f63-3b75-ad46-03f5aeddeeaa | -10.4397 | -46.8804 | 2026-07-07 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b0885d81-7de3-38b5-915b-10b6daabefe6 | -7.3945 | -49.7692 | 2026-07-07 13:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 45dac598-8e52-3165-8bd5-20f27b29eec8 | -13.5292 | -52.9249 | 2026-07-07 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5e31c503-daf4-3b1a-ac50-8d4460581b8c | -11.6785 | -44.5712 | 2026-07-07 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 64f30eba-48e0-3d8b-81db-21bfe1f9c873 | -12.5138 | -48.2581 | 2026-07-07 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| dc0e2c79-8610-34d5-b58a-f363491491d7 | -6.9138 | -43.7049 | 2026-07-07 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 291.5 |
| 2b486ab4-ff81-30fd-b1e3-6bcac719507c | -9.3736 | -48.8025 | 2026-07-07 13:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 191d7f4c-8d02-3d8d-b93a-9472500fbdb0 | -10.8463 | -46.3808 | 2026-07-07 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 914a2e7b-1897-34a4-8c62-291166bc38ab | -6.9323 | -43.7264 | 2026-07-07 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 635ea65d-9026-3172-b114-d820a22e2a92 | -10.8463 | -46.3808 | 2026-07-07 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| d746ed24-a28c-3328-981e-4390d378354b | -6.9326 | -43.7032 | 2026-07-07 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 284.4 |


[Clique aqui para ver as próximas entradas](README24.md)
