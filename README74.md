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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b63ef228-0b8d-348b-b0bc-60ed0604c1c3 | -11.2493 | -45.0501 | 2026-08-28 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 62f122fb-e974-36e5-9baf-517c62c84b67 | -10.899 | -50.5159 | 2026-08-28 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 01f16071-49d2-3688-8644-ad717e448b71 | -2.7303 | -47.0644 | 2026-08-28 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f98e420a-407f-3a44-9538-d4ea8fa695c7 | -12.2281 | -50.5578 | 2026-08-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 8e8bebb5-08e3-3b09-b363-cb6cf8724aab | -12.3041 | -50.5701 | 2026-08-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 10a12611-9a46-3877-92ee-ae94b5f925a7 | -14.9985 | -52.5925 | 2026-08-28 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 32d48e57-73d9-3853-8185-0b435e6080c9 | -12.209 | -50.5601 | 2026-08-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1cc66108-9ef1-355c-9c4b-f69827944d3e | -14.9209 | -52.6029 | 2026-08-28 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d40cf3ef-0b18-3ceb-b02b-0dae13b862ae | -10.8996 | -46.6216 | 2026-08-28 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 292.4 |
| 0a430a32-3cd4-3e86-ac07-13c54161e425 | -11.8239 | -47.2178 | 2026-08-28 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6939a218-3cc7-3073-ad09-8ceb9058ff72 | -10.8802 | -46.6466 | 2026-08-28 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7e49f16d-534e-383f-889d-3c22f2e14acc | -8.093 | -45.8128 | 2026-08-28 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 5eb32330-7d29-3e7d-bda0-b596ec9e0078 | -12.0733 | -47.1614 | 2026-08-28 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 0a626d91-79d8-3c13-a3ae-5a965168f91e | -14.6024 | -53.1508 | 2026-08-28 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d110773b-3a06-3684-b2df-01fdf54cc2ce | -6.1656 | -57.7988 | 2026-08-28 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| adbc01db-6598-312f-b40a-614b8d6c632a | -12.285 | -50.5724 | 2026-08-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| fd4a2984-6e82-39f4-8edc-fce62e8977ce | -2.7304 | -47.0424 | 2026-08-28 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 334.7 |
| e6a507b5-fab9-3c29-861d-6fd9b43cae40 | -10.8992 | -46.6442 | 2026-08-28 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 603.2 |
| 378970bc-454a-32e7-9d1f-593f88274410 | -10.9183 | -46.6417 | 2026-08-28 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| bb7dbf99-f327-3de0-972d-16f0b13cca3a | -6.1472 | -57.7995 | 2026-08-28 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 48a71053-a907-38ac-aad4-213a9d50ec08 | -8.5969 | -54.7755 | 2026-08-28 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| b3cc1b3f-08c0-3d1a-914e-316888328b79 | -8.0928 | -45.8354 | 2026-08-28 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| eb298571-53c8-3dde-b506-9fb7b1a20a12 | -8.0742 | -45.8147 | 2026-08-28 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 81e63376-396c-3d16-9479-c232facddeae | -9.9708 | -53.9419 | 2026-08-28 13:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 315ad76c-ca90-3105-a252-d638368ea5a2 | -6.1657 | -57.7793 | 2026-08-28 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 38097949-7c08-3bff-8db6-1d42ab800c4d | -11.2693 | -54.0129 | 2026-08-28 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 434787c8-60c2-30fc-bfd8-830e5242c309 | -10.8801 | -50.5179 | 2026-08-28 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ba2801f1-ad89-348a-8a59-9da0a5f2c639 | -12.2854 | -50.5509 | 2026-08-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| b86564d8-cf32-30b2-9496-c0b03352f0f2 | -14.9791 | -52.5951 | 2026-08-28 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 8d563a95-6ebe-3561-84f7-cfd8fca8dfc5 | -10.9187 | -46.6192 | 2026-08-28 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7516453f-2bcc-3a42-a50f-cf6c6daebd2a | -8.0548 | -45.8616 | 2026-08-28 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 681ea2d6-cd2d-38ea-ac66-c7ff3034efc0 | -10.498 | -64.5193 | 2026-08-28 13:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d95f0fe7-ce72-374f-b19b-8536f89418ba | -11.2879 | -54.0317 | 2026-08-28 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 02bb20ac-49ab-32d1-9b6c-068f34a94544 | -10.937 | -50.5118 | 2026-08-28 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a2edac03-832f-38b8-b4e3-09d42af19917 | -10.7839 | -50.6346 | 2026-08-28 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 93c302ad-6506-37ad-8670-24d3c31e6adc | -12.3038 | -50.5915 | 2026-08-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ac4c2c3d-1415-3741-b5e0-3416595d23e3 | -13.4191 | -51.4159 | 2026-08-28 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4964c3ec-4709-3a5d-8cf5-aa2421ba97e5 | -11.3476 | -48.3872 | 2026-08-28 13:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 130fdb11-b313-36fe-bf18-a914b2b17cab | -14.9791 | -52.5951 | 2026-08-28 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| aea23d56-ce2a-30d7-a6e3-53481f745390 | -11.269 | -54.0334 | 2026-08-28 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 12db906d-cb54-34bd-8862-a08532996b30 | -11.3285 | -48.3895 | 2026-08-28 13:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 492a4440-1799-3b4e-95e1-2733e6a9082e | -6.1656 | -57.7988 | 2026-08-28 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 873d1647-d901-3522-96df-198d0308ef90 | -12.2854 | -50.5509 | 2026-08-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 7fc3a476-48d4-304e-bbb7-2d3aa910c335 | -10.7596 | -54.0384 | 2026-08-28 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a27d08e9-12bd-3702-9c78-4f3902b87f8e | -8.036 | -45.8634 | 2026-08-28 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 346f0134-d07a-38e8-a43b-1a2cbc510026 | -11.2693 | -54.0129 | 2026-08-28 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| a853026c-f0ee-3067-8fa7-3fdf7344e2bb | -12.3041 | -50.5701 | 2026-08-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 4e3b4ddb-9722-338e-a314-db4eac93f330 | -11.2302 | -45.0528 | 2026-08-28 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b1a58fbe-fa77-3186-8899-a2c84bb7bb53 | -12.2281 | -50.5578 | 2026-08-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 0c66350d-7107-385e-98e1-59bb87933500 | -12.209 | -50.5601 | 2026-08-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 1cacc3fe-f393-3c17-898b-81d7afd05c76 | -11.8239 | -47.2178 | 2026-08-28 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a3753e9c-bbb9-34be-841b-d2e9ae166d7e | -10.937 | -50.5118 | 2026-08-28 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 30b925b9-b838-3b9a-b44d-252ade8f09a6 | -10.9183 | -46.6417 | 2026-08-28 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 59644345-1a88-36ac-93ca-201730975c6a | -10.8801 | -50.5179 | 2026-08-28 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 48178172-888d-3118-b11c-73191f41c191 | -10.8028 | -50.6326 | 2026-08-28 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f4a0fdec-97e1-3f8b-9ea4-dd4b5bba7d77 | -11.2493 | -45.0501 | 2026-08-28 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| a6d6e621-9ea3-3b0a-be63-9c8bfed8214b | -6.1472 | -57.7995 | 2026-08-28 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f5f323d2-5b71-3d14-99ae-101f9f4592d9 | -12.285 | -50.5724 | 2026-08-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 253df9ab-bb39-3444-9d34-dd8d54be85f7 | -11.8051 | -47.198 | 2026-08-28 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3275afef-f2ba-37f0-b68e-ae2813b436b4 | -12.0733 | -47.1614 | 2026-08-28 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6242bbb0-c184-3170-823c-63798ef05f32 | -10.8805 | -46.6241 | 2026-08-28 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8c3c8429-f0f6-301f-a3d6-1a60a5582a73 | -13.4191 | -51.4159 | 2026-08-28 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| f7bac5f1-8156-315a-acd3-825a6e1afef6 | -21.0372 | -57.8494 | 2026-08-28 13:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 967b86d7-88a6-346a-aaec-f8b1d89ff9eb | -11.2497 | -45.027 | 2026-08-28 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 37a0cc87-1e42-32de-9323-8c8cf524a293 | -12.3038 | -50.5915 | 2026-08-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 659c4921-6838-373d-99a4-15dc3256647a | -9.9708 | -53.9419 | 2026-08-28 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ca9ddc09-d838-3b43-b5c8-675b0387fa89 | -10.8996 | -46.6216 | 2026-08-28 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| ed70b871-ff42-38e5-8ebc-d81ab107a755 | -8.093 | -45.8128 | 2026-08-28 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 059d73b5-5890-314c-b009-6ee77c611de9 | -8.5969 | -54.7755 | 2026-08-28 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 9cbf65ac-f9fb-3607-9189-c11748527a65 | -11.2879 | -54.0317 | 2026-08-28 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 139e09e5-cc0c-3d84-8257-22c649237dd4 | -6.1657 | -57.7793 | 2026-08-28 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 5c142aa7-0bc3-339e-a08c-23c680d8ebd7 | -10.8992 | -46.6442 | 2026-08-28 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 474c5b39-d0df-304d-87be-caad399216a8 | -10.7839 | -50.6346 | 2026-08-28 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 491d4b75-973a-320c-b2ea-7e0a9780c489 | -2.7303 | -47.0644 | 2026-08-28 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 6e597c55-3e32-36d4-9a36-06b4ba523614 | -8.5969 | -54.7755 | 2026-08-28 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 031d807d-98e8-3ebd-87ca-b6bf98aeaece | -6.1656 | -57.7988 | 2026-08-28 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 23bbe5d5-3dba-3d1b-b3d0-9bc329a86391 | -8.093 | -45.8128 | 2026-08-28 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f2bb6119-1802-3802-a5d9-0157535d17e8 | -14.3182 | -51.7046 | 2026-08-28 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5d82cff3-90b8-3422-8067-159394449409 | -11.2882 | -54.0111 | 2026-08-28 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 01f2569b-4d08-394d-bb0d-a4187451dd10 | -10.918 | -50.5138 | 2026-08-28 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 63db6b15-dbe9-351d-8670-144febaf3443 | -8.0742 | -45.8147 | 2026-08-28 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f49db909-f8f6-316e-8105-390efccdbcc2 | -10.7596 | -54.0384 | 2026-08-28 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 46e009de-1bd3-3f21-ac41-0916d6bba603 | -10.899 | -50.5159 | 2026-08-28 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 622ed102-f14f-32a7-98d3-33577827af94 | -6.1472 | -57.7995 | 2026-08-28 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 3777ee3d-dc2f-33fc-a827-9f55d2e70245 | -12.209 | -50.5601 | 2026-08-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| dc45ea6c-2c13-302d-a1d2-e569b33ba898 | -9.9708 | -53.9419 | 2026-08-28 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 820966d2-0fe1-317d-a6d3-c9c6f1c54104 | -21.0575 | -57.8465 | 2026-08-28 13:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 111.3 |
| b00802fc-8ae9-352e-8629-99a7d830cf17 | -21.0376 | -57.8284 | 2026-08-28 13:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| a7e463fe-fc54-3efc-bfac-5b558bd4c6e6 | -10.8992 | -46.6442 | 2026-08-28 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| fbcb8bbd-d6ce-37c0-8aed-f919786686f2 | -14.6024 | -53.1508 | 2026-08-28 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ca72f3ee-d81e-3824-940b-7f16405b340c | -11.3476 | -48.3872 | 2026-08-28 13:20:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f8df196f-a3b4-33d5-ab43-d8ab74753ee7 | -10.8996 | -46.6216 | 2026-08-28 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| b6bc0e14-4004-3a22-b896-6d8a2d5238b4 | -12.2281 | -50.5578 | 2026-08-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 233.6 |
| b859aa1e-cdf6-31dd-bfbd-2d747e1d1965 | -11.8239 | -47.2178 | 2026-08-28 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8063d604-65fc-376a-a85d-29d6cfe82457 | -11.2317 | -53.9958 | 2026-08-28 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 4c2dc96e-42f9-3e7e-810a-fd7d133d3d44 | -21.0372 | -57.8494 | 2026-08-28 13:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 150.1 |
| cf1aa97c-4779-39d8-85c6-86fe1c7c791a | -10.937 | -50.5118 | 2026-08-28 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 4989e631-8c86-3abd-8507-3a3fa59b12ef | -6.1657 | -57.7793 | 2026-08-28 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 56155331-e157-3eb7-aa2a-bcff60d25137 | -10.9183 | -46.6417 | 2026-08-28 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 4f791890-0d46-398f-bf99-ad8aead4554d | -13.4194 | -51.3945 | 2026-08-28 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |


[Clique aqui para ver as próximas entradas](README75.md)
