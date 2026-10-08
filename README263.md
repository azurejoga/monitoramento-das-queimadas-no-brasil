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

## Dados Diários - Página 263

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c890a11-8fd5-3fd8-a477-f9e15a28269c | -12.18638 | -44.80905 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 30ea4913-e4dc-3d0b-91f9-63a7629d549c | -9.90777 | -44.82275 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 37f82a22-2cd8-3ffc-8d38-02fba1abf06c | -12.23373 | -44.74316 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 209548bb-c316-3eff-ad4b-4b615334fdc9 | -11.84068 | -43.57029 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bf7365ad-cdf2-3831-9ed1-78cc59cdf1e2 | -10.53052 | -47.26441 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b701ffb0-1e98-33f2-82c3-71e5812edb2a | -12.08832 | -38.75853 | 2026-10-08 16:18:00 | NPP-375 | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 904392b4-2f8a-3e9e-ba43-934292f423b5 | -10.35038 | -36.50614 | 2026-10-08 16:18:00 | NPP-375 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7b377ee0-cb12-35e1-bf45-9c32ecafb560 | -11.30504 | -44.826 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 212037df-1ec5-3a73-84d5-2a7c49d244c0 | -14.04685 | -43.82591 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9f94feb7-7c39-37b2-b2b9-499ac2ca28d1 | -11.79977 | -43.51856 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 80d4dc6e-5098-3a51-969e-0e8a03d8ac89 | -9.13956 | -45.85062 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 7943f75f-239d-3d22-9366-3ad44c171488 | -10.25117 | -37.86018 | 2026-10-08 16:18:00 | NPP-375 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 5d552636-2d11-31b2-b422-812bfbdc26b3 | -11.39782 | -47.55629 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94963608-f4e6-3761-8025-5440057511fb | -10.17489 | -48.04963 | 2026-10-08 16:18:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d3bcdbde-3d9a-3f29-85d4-2e016bf57359 | -9.39383 | -45.88932 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f0cca0e6-8610-3e9c-9d30-4d209c2176d2 | -11.86308 | -47.33444 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c159f193-50a7-352a-bd1e-ddf8f201ef47 | -9.26714 | -45.63132 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e38fe4b-c05b-3bb7-9b8b-e1642f6613a3 | -8.2932 | -45.72775 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ef3eac77-245e-3776-af3d-c893d508d84b | -13.81536 | -47.84952 | 2026-10-08 16:18:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 749133e7-b96e-3019-afd7-2f903350cc78 | -9.54544 | -46.85475 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e00a2c3f-4636-334f-b3d2-9988a10e019e | -9.22888 | -45.66144 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| efface32-027b-3b6c-bd33-7197df14dc75 | -11.30972 | -46.68674 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 74be979e-a65f-3655-8669-faeca1c1b91a | -13.70074 | -49.10466 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d3c0c954-094d-3f79-9d51-eb0e35bc9a4f | -8.97547 | -47.54824 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a510e79d-642d-3b4c-9387-9c9052c04f15 | -8.95675 | -45.15297 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 5337583e-3931-33fd-9dce-83d8c029ae69 | -13.11831 | -46.34941 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9c51efb7-1912-34d7-b1ec-250dc0c68d6e | -11.31087 | -46.69603 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 75156df0-5cac-3808-b4fd-fa529bfc7d82 | -10.87474 | -45.55317 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c53c83c4-64a4-37cd-9936-ef9bbacff73b | -11.25856 | -45.18337 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b07f18fc-d80a-34e8-9069-72e8502f4c8f | -7.37232 | -37.99213 | 2026-10-08 16:18:00 | NPP-375 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e301784f-4f43-3534-ac24-e672a0279f7f | -9.5207 | -45.61119 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 50d496cd-da28-3410-8682-5f1efad1d193 | -10.47842 | -47.23343 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8cced78d-528c-390f-be11-cd3d921a066f | -12.71333 | -45.81812 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 36071758-864f-385e-b450-5b528c713260 | -12.77024 | -44.86637 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ebe1e182-95f5-37f5-8a0b-fc0e6e584295 | -14.58596 | -47.53614 | 2026-10-08 16:18:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0fb9905d-9e00-3aea-b98f-0df7d18aa027 | -11.34495 | -46.71928 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fc3e8cba-aa01-3a2c-8801-4cccd823d124 | -11.72791 | -43.42163 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6a80d826-7bab-312e-b86b-4be8434b7d2b | -8.07151 | -39.56826 | 2026-10-08 16:18:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 85adfc72-683f-3284-b9e0-60619508b317 | -11.77199 | -44.94776 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b8ce3416-6599-37a3-ad0a-0c3d1a21834a | -11.5856 | -43.67867 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.0 |
| 15f487e3-1f9e-38a9-a265-65ebff1bc7b2 | -13.67518 | -48.64205 | 2026-10-08 16:18:00 | NPP-375 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d40b9e5e-0cc9-391f-9ae2-417ec4871c41 | -12.90682 | -43.2896 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7f1388ed-79b8-3ca5-8dc6-53d506a9a8d8 | -10.68386 | -47.82739 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 193aa184-b8ee-33b9-819c-36d5fea5d8ca | -7.08161 | -35.0379 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d8556075-b737-3d7e-8338-9485a308ed77 | -10.48168 | -47.21754 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f5dbfa08-e571-36d8-b636-5100027f8e1d | -8.30689 | -45.45656 | 2026-10-08 16:18:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 883f7b06-d822-3e37-9eb0-a49ef9317938 | -10.42001 | -47.27693 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9ae68bd1-d8ed-3170-aeb5-67b4f2d3ae2d | -12.77484 | -44.86578 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c45aa144-22fe-3786-abf5-c6a0d01ddd35 | -9.21291 | -46.68071 | 2026-10-08 16:18:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e8179630-e16e-3809-a0a9-4e4a4c65d383 | -12.16278 | -44.76962 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 5ddfe8db-6b6d-3f73-82f7-b965bc22e612 | -9.97327 | -43.57538 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0e84f390-8b2b-3253-b1e5-e535cd1ac4df | -11.91738 | -46.7926 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f98c1575-c03f-3110-a110-8c5e6ef6f8d6 | -8.32227 | -45.01783 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f2829a23-4076-3d13-a7d1-1c5de2bb0e27 | -12.15678 | -44.72347 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9040aef0-9b5a-3951-ba6d-d81cb872ea03 | -8.29435 | -45.73388 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 36615830-9846-30e6-bbcf-767426efea89 | -9.3585 | -46.58471 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| cc0149cd-2a53-3a7a-9009-fd8ffeca4d69 | -11.78108 | -43.53645 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 588ee7b7-8598-3616-bb44-112b04cad315 | -11.67016 | -46.76963 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6ff2336-4241-3486-8e2e-a2a805a132f4 | -10.76228 | -46.60961 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 07f1fb10-62a3-3a86-9b35-e7009a09d045 | -14.66823 | -51.45412 | 2026-10-08 16:18:00 | NPP-375 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f3608fb7-c5b4-3d78-8491-8873bf304b57 | -8.28164 | -45.71099 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 853b00fc-9a12-362b-a21b-3b20fa9401d2 | -11.87028 | -47.39265 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f2d1e1a0-6b20-3252-9c44-53659a8ad37b | -9.80354 | -44.77579 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 29c461da-2b9e-3507-aa1f-beea25dace3a | -10.82182 | -47.33432 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 64d8a508-f5b8-3029-992c-6fefe1295ba9 | -9.18541 | -46.70148 | 2026-10-08 16:18:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7169c16a-ebf0-3042-aa31-fae8503c384f | -9.97549 | -43.50275 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| da104f3f-1814-3ea6-a9cf-f9caf3a8724e | -8.2886 | -45.72819 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 151406ac-b62b-3341-8071-26ee54a477d0 | -11.83081 | -43.5294 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| f415f15d-055b-3fc2-aa92-e4f593056547 | -11.58772 | -43.66289 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5b744746-c67b-3ff5-975b-2fd6d53a9e97 | -10.16225 | -45.9693 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c01c2900-d72d-3ecd-9bf7-26319e7ed518 | -8.7866 | -47.37051 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1d449c77-e913-357b-b56f-eebae9cecb17 | -10.46912 | -47.24394 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 55fa6ba5-2333-3b10-b326-4b78437bedf8 | -11.8561 | -47.36646 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 93d8c6d4-64ff-3a38-b597-ee9f16b7bf5c | -11.00945 | -47.97529 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7c8fa14-152a-3c6e-9a27-10643f730f1d | -9.13415 | -45.84585 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 2267a146-ba18-31e8-991e-8adcb08a6536 | -11.58837 | -47.1805 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 864d951b-ab17-3f36-aeaa-735e5f548436 | -9.63945 | -45.73441 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6d14a3e3-b7b1-3124-bb8d-95405aa4137b | -12.15586 | -44.75179 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 812e1412-1dc0-335c-a2e0-8b0646c6a938 | -8.18186 | -45.76303 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 518c5937-3fe3-3033-9fe1-99920d7e325a | -10.81695 | -47.33828 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0b1ccad2-04a6-35ee-a71b-1a13ebc0028d | -9.65613 | -45.58014 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c444ea41-4f98-3a8e-8eec-71f24cee9bf7 | -11.24759 | -45.243 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 525040b0-cf47-33dd-aee8-1dd1867db3b2 | -11.62622 | -43.69586 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 46c87e1e-27a4-3d01-ade4-49a53290b3aa | -9.88711 | -44.86967 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 250.9 |
| 57262b16-3736-3910-8124-176a687261eb | -11.2074 | -45.21304 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 47abe27e-38b0-3d04-af94-0c707223acd8 | -11.62405 | -43.68001 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| bfa52890-0789-3667-b9ee-3532e852c9f3 | -12.21957 | -44.74033 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e3f34035-c312-3940-819a-3d610eeb9001 | -13.70388 | -49.12685 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| cbfab56a-c110-3cbc-a2e4-2a395ef6eec3 | -12.18883 | -44.82774 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| a2ff9723-cf12-35c5-a086-4a5587e74bdb | -10.80954 | -47.32245 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4b87831-ac4f-3bcc-b764-4286ba6691d4 | -11.76245 | -45.54863 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 3ef6e2ee-63c2-37f0-ae93-5fafb20fe844 | -9.02371 | -44.37817 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 3a0d988d-1d80-3dfb-afe4-8c100c3e1108 | -10.8969 | -45.54019 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a4c532f5-cbca-3153-93f3-2a0393ccc054 | -8.29103 | -45.74335 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 21d02504-8388-3c78-acd0-b9e02c918412 | -9.8824 | -44.86083 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| d5e8277c-a02c-30f8-99a8-947940569dac | -11.21313 | -44.87341 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a4745ded-f0f1-3583-a5cb-146c2ef5776d | -9.03579 | -44.3725 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d89fb40a-918c-32b8-afc4-1bc618bc57a5 | -11.8707 | -47.39609 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4bcfa9db-0243-3574-90dc-7be34b2575df | -8.53696 | -46.91304 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2746ef76-86e2-3ec5-94b7-c2523c9de5ad | -13.93333 | -42.35727 | 2026-10-08 16:18:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README264.md)
