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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3a957d6-9eb3-3e25-9cc4-266ca46baa18 | -14.87824 | -50.30089 | 2026-10-09 05:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 131b3ad9-0720-36e5-a8cf-b178bc83ac88 | -13.16582 | -54.35846 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7639734-33e5-3f01-a294-c04a67f86661 | -12.22599 | -57.1362 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 965fcb86-b201-3e8e-92c6-2330614dd1f5 | -13.1819 | -54.36478 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10a67b4b-1357-3a16-aeb8-e95a75b7f3b8 | -12.20633 | -57.09759 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73fa3d9b-b097-3492-9350-3a95a5848924 | -14.01528 | -48.76608 | 2026-10-09 05:06:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8a29627-eee8-3b5f-8815-9988554211af | -13.26246 | -44.0018 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 840e0909-e08c-311f-8c1e-ebcea7071294 | -11.97352 | -57.62073 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95a67d61-cf6c-3ae4-9b3d-d459aa0779d1 | -10.85594 | -59.11385 | 2026-10-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 505bcce3-b7bf-3fef-a9a9-99efe5529c58 | -13.16143 | -54.34314 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2c8f9dc-cfec-32e9-bcc1-45b47ccaf1ae | -12.10282 | -57.15598 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79b0bf2a-7ae3-32eb-a4c4-b4bc1c0c49d8 | -14.73505 | -48.22022 | 2026-10-09 05:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cadbd776-2f26-363d-b1b3-1dbd64a436ff | -13.17248 | -54.35957 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 70e6a64a-27e0-3c74-bc17-25ef3500eac2 | -12.23033 | -57.11052 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b70c0bbf-77ee-3bff-bdcc-4d03c83ae5ce | -11.75635 | -61.05902 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b53258a7-7548-32ec-ad5d-f2b3992ccb97 | -15.11918 | -48.52237 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd1b6ae0-c23c-3287-ae62-de811233fbde | -13.20246 | -54.36455 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 239bb4d4-1288-3b3a-82b6-1c6446ae19c9 | -13.20579 | -54.3651 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd898129-7332-3500-925d-41c367f085a1 | -13.20465 | -54.37222 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa5f3e57-3bd2-3146-a06a-a58e67e559fe | -13.65097 | -49.40327 | 2026-10-09 05:06:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d87be95-e3c6-3350-97d8-f016107613ef | -13.12012 | -46.32781 | 2026-10-09 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e56b2f4-70d3-3da5-8d78-a3e8b856a1e8 | -11.90623 | -46.56572 | 2026-10-09 05:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| affefd6a-2afb-39c3-92e0-9f1e880f769f | -13.1958 | -54.36345 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fa87195-d63e-3963-bba8-bd28229a3bcf | -16.59017 | -46.75723 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e94ec732-7071-3fd6-9f78-69f851ea4100 | -18.08908 | -42.26516 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 71ab801c-ba61-3e74-a277-fbdc4b2bcf01 | -11.53199 | -49.93869 | 2026-10-09 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8af1997b-3a28-345a-8805-9bb798ab2e5e | -13.17199 | -54.34125 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e96d9893-a1a0-3416-93d4-0a2b275a34be | -15.11488 | -48.52189 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b3337d8e-128b-32f3-a224-8ba67798d7a9 | -13.15591 | -54.33493 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8f43e16-e897-3409-874c-0c6acb383b4f | -13.13047 | -46.32377 | 2026-10-09 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1019e11c-cba4-38bf-aaaf-61877adb8175 | -16.12501 | -43.7414 | 2026-10-09 05:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0edeec1d-c252-3d42-a780-4c72bae45b60 | -13.11466 | -46.33217 | 2026-10-09 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c8ff412a-69a6-35b0-b408-70ad5c948d9c | -14.92584 | -48.08874 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efc9365d-34ee-38f4-9d61-dd35744bdad6 | -18.32899 | -42.36574 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| c6536bd2-27e7-351e-866f-a1697ac8da41 | -13.45964 | -61.11556 | 2026-10-09 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cb87e21-30b4-3b74-9839-8d190a1a92b9 | -13.25722 | -42.24911 | 2026-10-09 05:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 54ff76bb-f3ca-3044-9c78-9edd729b3379 | -12.20924 | -57.10249 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b729ffcf-e126-321b-9fa6-c524ad42af41 | -14.40518 | -55.44322 | 2026-10-09 05:06:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b13d12e-3629-3362-a691-0aea3f8e0a76 | -13.11628 | -46.32977 | 2026-10-09 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb5cf9c1-6f52-380f-84af-52253e998269 | -13.15981 | -54.33194 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4a1ee45-16a6-32c2-be99-819475323d82 | -13.17524 | -54.36367 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 611754e2-d704-39a9-b536-dd8dddff0546 | -18.08185 | -42.2705 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0202fd5f-ab8f-3424-beef-3de529e6a612 | -12.20997 | -57.09821 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 93f37fb2-23b1-30da-866a-3501183f1426 | -17.36504 | -48.1786 | 2026-10-09 05:06:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e9aaabc-dfb1-35bc-9358-677d04cc0c0e | -16.5846 | -46.76213 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ca8055a-e3c8-3b10-802e-f61936926c82 | -12.20708 | -57.13721 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac6cfae8-3e53-33fc-930d-8dc2bd81304e | -12.20925 | -57.12445 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab169028-2978-3933-abfb-8d1187a45f7c | -11.99006 | -57.61428 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f47f19e-bd58-3750-bc65-476739aa6920 | -11.96763 | -57.61026 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9094f38-a323-3a1b-b53b-fef789fa6ef7 | -13.349 | -43.9667 | 2026-10-09 05:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac5bdf4f-5008-3d29-a4c5-054eaf3db3e8 | -15.08456 | -43.1147 | 2026-10-09 05:06:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 32e2f5bc-c44e-32b2-9730-306ccabc3398 | -9.25777 | -62.30892 | 2026-10-09 05:06:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ab8fbff-95ec-3511-87e1-3f79ed61ac84 | -13.17857 | -54.36423 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1569eb29-44bb-3dc9-85ba-06c931e14e56 | -13.37024 | -43.8853 | 2026-10-09 05:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f8051b8-a92b-3cab-87a2-9f0ffe1bda6b | -12.23029 | -57.08859 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7f3ce4bb-e67f-395a-ba27-bd5662095f22 | -13.15803 | -43.28191 | 2026-10-09 05:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7b732362-b009-3855-8370-e0a804ad0d0a | -13.1603 | -54.35024 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 89409f70-62da-3cad-a57a-374cd22f8e48 | -16.63901 | -47.20855 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecf97169-e625-3249-8c50-d1ed572d5479 | -16.12459 | -43.74531 | 2026-10-09 05:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95427038-1790-343c-9f06-c7143c51c0f5 | -13.21302 | -54.36266 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 478a1b98-f773-3092-b52b-8baf1200707c | -14.05192 | -43.83152 | 2026-10-09 05:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b50d09b1-f411-3ef2-924d-f115467b2557 | -13.49528 | -44.37395 | 2026-10-09 05:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c145644e-6a63-37a0-b1fe-b64c9eeaaf6c | -13.19856 | -54.36755 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51c4f0e5-39ba-314f-b112-8b5e2484fda4 | -13.17362 | -54.35246 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5de8711b-6692-3a71-9d44-768b067ab123 | -15.25287 | -42.36055 | 2026-10-09 05:06:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9e19a5b2-ca07-367d-ab7c-09e183310b56 | -10.85082 | -54.02602 | 2026-10-09 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ee25070-e16f-32f3-b38c-2fe4c33b7aaf | -13.49569 | -44.37049 | 2026-10-09 05:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52cb59c4-e5e5-3799-af0a-d2bb85c98a77 | -12.21433 | -57.09455 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 21759ebd-66a6-3313-a0e8-94b434c921b0 | -13.25678 | -42.25293 | 2026-10-09 05:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 78267fa7-52d9-3d1b-b2d7-a31504d9b716 | -9.25249 | -62.30781 | 2026-10-09 05:06:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59b9ef64-4072-3e33-a294-1cd010981f3b | -12.21436 | -57.13851 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a89059bd-854d-3580-be21-09459a336eb3 | -16.96059 | -46.35522 | 2026-10-09 05:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e58ac5b7-12b5-3c76-a923-a43c32c0b5fa | -13.19133 | -54.37 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 653823bd-f33d-375d-84c0-5fcdb38f18f5 | -15.79335 | -50.13126 | 2026-10-09 05:06:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5fee48c-a761-35a9-9fd9-b3f217fad42a | -12.2158 | -57.13002 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf72bc55-c5a9-3c45-be53-4996e25c7a21 | -11.57466 | -49.77893 | 2026-10-09 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b4adf3c-0769-3f5c-a984-a9bcbf28e2a2 | -13.38461 | -46.68714 | 2026-10-09 05:06:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d147d6c-b6d7-3642-b14e-f42d1d2249bb | -10.67786 | -58.73116 | 2026-10-09 05:06:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a81cf4ef-376e-37ab-888f-8d2d8ca31f7e | -14.97651 | -47.54271 | 2026-10-09 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c93a01e-4c21-3fe6-be04-cae16ae8cc82 | -13.15852 | -43.27758 | 2026-10-09 05:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| de078510-5f91-39ac-9051-579a35360f43 | -13.62935 | -44.4243 | 2026-10-09 05:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6a7d8f8-7863-3288-a519-f623f3ec20dd | -12.22669 | -57.10989 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 42f13cba-1270-3180-9dcb-a8599bd1da1c | -13.16915 | -54.35901 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d8e6ca63-24a5-337c-a57a-54f8189ce05d | -13.17589 | -54.33825 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8925a5c6-17f3-3b01-bb73-757921b4a392 | -11.78431 | -46.79383 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a25c186f-6def-3aa1-831e-cd7708c90102 | -12.21288 | -57.10312 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb856c1d-2b27-362e-82e0-35d496d61708 | -12.22523 | -57.09644 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87e8806b-522a-3e69-88be-ba2db021719d | -12.20853 | -57.1287 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0bd0037-3690-3a99-ae56-c2aa1cdc664d | -12.21142 | -57.08964 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 233b4dca-6926-39a3-9703-4d4b2e37c0c4 | -12.78172 | -60.60674 | 2026-10-09 05:06:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63b8393-3e07-3a3a-8463-54956b9068cd | -13.162 | -54.33959 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 992eb180-667b-3d58-877b-16e244a1bf35 | -18.05241 | -44.56027 | 2026-10-09 05:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56e86c54-32dd-3850-9dee-4bcf4fb2ad68 | -18.33233 | -42.36618 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| f695594a-2050-38bd-9c83-f816e9516c8a | -12.2332 | -57.09348 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 406aa2b8-0b2a-3b09-9cd9-1f835f33e56c | -13.46051 | -61.11086 | 2026-10-09 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db7dc8ae-f682-3027-a655-6b5fc3338f77 | -15.78741 | -44.68492 | 2026-10-09 05:06:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9d6f13c-05c0-3de1-9b52-fc177af3fa0d | -13.38478 | -46.6884 | 2026-10-09 05:06:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b7538c9-f273-3805-92e9-b9cc0ba3e586 | -18.07886 | -42.26312 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 30c0fc17-e1eb-3614-82a3-b3201e180ed1 | -12.23249 | -57.09773 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f5af6f-4ae7-3435-b863-87dcafe9b912 | -18.08549 | -42.26436 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |


[Clique aqui para ver as próximas entradas](README175.md)
