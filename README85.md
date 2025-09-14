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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8031d65-3c99-3a46-94ea-20a0eafb642a | -9.7389 | -46.8728 | 2025-09-14 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 9adc2d7d-b77f-338f-872b-bbe9e55abfea | -6.9798 | -44.5529 | 2025-09-14 13:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d7a11130-9d3b-3be0-83c6-bd0ba8399560 | -14.2917 | -45.0964 | 2025-09-14 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| bf93c2d9-d5c4-3d61-989a-870d31334245 | -10.929 | -47.1776 | 2025-09-14 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 7043ba21-e56d-3f17-a275-4b9647696434 | -12.9101 | -54.7558 | 2025-09-14 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 5ee54494-9368-36c8-8ceb-368311ed9e62 | -10.9262 | -47.3561 | 2025-09-14 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 741c2617-9370-3462-b381-661f3ce84712 | -9.7579 | -46.8706 | 2025-09-14 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 7e4c7230-27e1-3477-94ca-70b20896a9bc | -15.7516 | -49.7821 | 2025-09-14 13:30:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1802b86a-7a1a-36c1-821a-d78feeeffa56 | -10.5459 | -51.4844 | 2025-09-14 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| aefc2a42-c5a7-31eb-bc88-a3b3fa5f54d9 | -8.1386 | -43.653 | 2025-09-14 13:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 1e6ce71b-80c3-3b97-9275-838462516297 | -15.7786 | -53.482 | 2025-09-14 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 236.7 |
| bc0563ee-d82f-3d5b-9c5e-ec5697de4807 | -14.4779 | -47.3368 | 2025-09-14 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 94c62cfb-7b3d-3a76-8f3b-dee4a50d40de | -12.9294 | -54.7333 | 2025-09-14 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 296.4 |
| 9ba685cb-1ada-3b24-8a1a-ee21d8dcc2be | -8.4143 | -47.2545 | 2025-09-14 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 6eb4ed18-7b84-3dd3-911d-7386f4f2cd5d | -8.1383 | -43.6764 | 2025-09-14 13:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 7e38c072-b1c3-3c59-a190-27416c1586cf | -10.3885 | -50.5264 | 2025-09-14 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d3cad779-ca4a-3b0e-8d16-3618b3e05a81 | -12.7671 | -48.0236 | 2025-09-14 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 5c70114b-2cef-3f7f-81ec-be3f38d5b4cf | -14.3747 | -52.927 | 2025-09-14 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 98b49e5e-7132-3a1c-8c0f-127118479316 | -13.9473 | -44.8541 | 2025-09-14 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| bd456e43-85aa-3da5-b16b-ea4948c8f0d2 | -10.3512 | -50.4876 | 2025-09-14 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9203bbe9-3a56-3d20-9da5-f83bf8965b3f | -14.4783 | -47.3141 | 2025-09-14 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| da2f22f1-7afd-355a-9cab-fd17be647a8f | -20.6168 | -50.3545 | 2025-09-14 13:40:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.9 |
| 3b074ee6-2a9b-31a7-953a-81c722c70d9a | -12.8019 | -47.1474 | 2025-09-14 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| f8afd845-2cf3-3537-a6d6-17926ceb7179 | -15.0477 | -47.9856 | 2025-09-14 13:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 58f66319-a904-3a54-824e-f427c12457cc | -8.1386 | -43.653 | 2025-09-14 13:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 86087462-0729-3cd2-84be-fcf11e80882a | -11.0427 | -49.7283 | 2025-09-14 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 019c8fa8-2b34-383f-9aa0-8dc42bad8f4f | -14.3747 | -52.927 | 2025-09-14 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7e29bce0-ec3f-3ec2-be15-35e03e3377a2 | -14.2917 | -45.0964 | 2025-09-14 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| a238e32a-3fa4-3ae9-b4b5-b5fd55095825 | -11.293 | -50.793 | 2025-09-14 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| f5410843-a45d-3d25-93dd-1c993b307b41 | -10.7579 | -44.7721 | 2025-09-14 13:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 6167ed7f-0ee7-31fa-a8cd-9c6019157055 | -16.0061 | -47.9329 | 2025-09-14 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 050eb7b8-85b3-36a3-84a2-bb4aa54ed91e | -14.2912 | -45.1198 | 2025-09-14 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| b7971c06-b315-3aa4-9c6b-dc1670734ec8 | -3.6924 | -47.4886 | 2025-09-14 13:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e9415fd2-c1e2-3e2a-b73d-d3ac47d22965 | -14.4779 | -47.3368 | 2025-09-14 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 40ae9ddd-163b-30c4-abdf-7ece4a85e128 | -6.6883 | -45.5328 | 2025-09-14 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 841cd604-e57e-384a-8f9f-d1f1fb8fa996 | -10.3699 | -50.507 | 2025-09-14 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f1e36294-ad4d-31c1-8ee5-635df9673906 | -13.5876 | -51.6715 | 2025-09-14 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b76348ad-276f-3c53-b817-2076008ef400 | -3.7333 | -40.4406 | 2025-09-14 13:40:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 91.2 |
| bc56cbb5-f9c5-3df2-8a20-10e5026f9ebe | -18.62 | -47.1901 | 2025-09-14 13:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 81f9edad-ba24-3a1a-9621-e2835fd63e19 | -8.4143 | -47.2545 | 2025-09-14 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 291e1481-16c3-38c7-a4e4-6feb24d2ec01 | -14.4973 | -47.3336 | 2025-09-14 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 3fcf7d11-aa14-3ff3-aece-35d7bd036857 | -13.9478 | -44.8306 | 2025-09-14 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| eee629a6-d5aa-3062-902e-0d33096aee44 | -10.5459 | -51.4844 | 2025-09-14 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 37bcc785-a20a-33ad-b0b3-812b0cc6113f | -14.4312 | -43.1986 | 2025-09-14 13:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 406.8 |
| 3464c620-9447-3465-8fbe-8acf21bdfa66 | -16.4128 | -49.0732 | 2025-09-14 13:40:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 4f90ae57-74b8-3a51-a348-b2feae6f1779 | -10.9477 | -47.1976 | 2025-09-14 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| af846962-9f43-3980-a372-bd82dc3f9ac7 | -14.4307 | -43.2228 | 2025-09-14 13:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 3234e7e0-6f7f-3b9b-988d-c9e659bfd9a8 | -15.7786 | -53.482 | 2025-09-14 13:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 88886218-4a84-3b8f-95dd-0acc98d8f57d | -8.9371 | -46.1094 | 2025-09-14 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 6a17c0ef-1209-3dff-97ce-4a2bebbe5630 | -10.4065 | -50.5884 | 2025-09-14 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4a0da0bf-6841-390e-b82a-b36c97f49075 | -11.0617 | -49.7261 | 2025-09-14 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| fd9bb166-606a-3d2b-b2b5-a783cebffca8 | -8.956 | -46.1074 | 2025-09-14 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 1799bf49-6439-3c8e-882a-13e7d998f4f9 | -8.9976 | -45.8098 | 2025-09-14 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 033aee29-f7d0-3158-b6d7-0fe78173a98b | -15.7516 | -49.7821 | 2025-09-14 13:40:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a6934dad-30aa-35fe-a797-c4d92ba35458 | -13.9283 | -44.8341 | 2025-09-14 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 701b6eb4-997a-3b8c-971d-f486487d8670 | -10.9096 | -47.2023 | 2025-09-14 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 5d27b495-c87b-3f9f-9a16-e45608cb37f9 | -12.7671 | -48.0236 | 2025-09-14 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 2cd8179c-e942-35f7-a04a-c7eadf845e5f | -10.929 | -47.1776 | 2025-09-14 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| c741acd0-fed7-33f1-9f7a-6c90bd48463c | -12.1048 | -47.5592 | 2025-09-14 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 31c3efa6-f107-3249-ac5f-26dedb6dc848 | -16.0056 | -47.9555 | 2025-09-14 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 909c56a7-e803-3b96-814c-1e48d545b8d9 | -13.5096 | -51.7451 | 2025-09-14 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f7a4b26d-bb5a-3f11-a46e-f930ca9bca18 | -8.6436 | -44.0396 | 2025-09-14 13:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 805bd74e-378f-3713-a61e-27ec08e217c8 | -15.7591 | -53.4846 | 2025-09-14 13:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7e59d6bd-192e-3981-a19e-844f29f9689d | -6.1065 | -47.8368 | 2025-09-14 13:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| eea48045-6017-35ad-b7e1-2d61f6bca535 | -16.6532 | -49.7649 | 2025-09-14 13:40:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 4ba7125d-0669-3720-8d53-13cf9b108ec0 | -12.8208 | -47.1671 | 2025-09-14 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 208.5 |
| f8293b2e-2848-390a-bf74-b148854f098f | -10.9286 | -47.2 | 2025-09-14 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 90355f86-a0c2-3d6a-a02d-7a113ee163de | -11.2927 | -50.8143 | 2025-09-14 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 05efdc7b-4c3c-3ff5-9028-a47831c7dd8e | -12.8212 | -47.1445 | 2025-09-14 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| ae2b9564-46eb-3c23-8979-9334af90757a | -9.0193 | -47.0394 | 2025-09-14 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| d5fea689-44b4-3f49-900d-0a392297297e | -14.329 | -46.0857 | 2025-09-14 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 433.6 |
| b3c956f5-a0a8-3692-b956-9716fa4e0534 | -8.4145 | -47.2324 | 2025-09-14 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b67505a3-217b-3485-b03a-1809e333ed0d | -8.9979 | -45.7871 | 2025-09-14 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 45345f94-b0a5-327a-8a4a-101fec4940df | -8.979 | -45.7892 | 2025-09-14 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| cdb84d6b-2729-3f97-a4a3-59561f0eb01e | -13.9278 | -44.8576 | 2025-09-14 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d753959d-c23a-3c16-a121-dd3168d3ffbf | -6.4177 | -42.6246 | 2025-09-14 13:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| d9b113e1-face-3242-9064-baca2199bb51 | -14.31 | -46.066 | 2025-09-14 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b1333f67-7899-39fe-8290-ae0b23bfefe6 | -11.4097 | -43.5336 | 2025-09-14 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ddc1c9e3-18b3-33b0-8169-59ccbcd52efa | -8.4331 | -47.2527 | 2025-09-14 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 80a91426-8fba-3c0c-a64a-0bc1b43c2d06 | -7.5281 | -47.642 | 2025-09-14 13:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c177865d-d0d8-3095-bbc5-0373e58c99d3 | -10.9452 | -47.3538 | 2025-09-14 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| ac44d84d-a82d-3650-96bf-40fac5588538 | -12.0856 | -47.5618 | 2025-09-14 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 414946ab-c550-3562-a596-7383672645f0 | -9.019 | -47.0616 | 2025-09-14 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a95550a8-c28a-3d7a-96a2-a1f4c2183322 | -8.9079 | -45.457 | 2025-09-14 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 64a978ea-de34-305a-801a-21e2cff599d6 | -11.3831 | -47.3429 | 2025-09-14 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 31571689-0b5c-369c-8249-40a71f4fc278 | -8.4334 | -47.2306 | 2025-09-14 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 871cc668-27b5-3006-b722-ebc02811a3ad | -10.3885 | -50.5264 | 2025-09-14 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c3cb3236-d9ba-30ac-9009-898fc13558f7 | -9.7389 | -46.8728 | 2025-09-14 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a9a14019-4b42-383c-8230-a39ec3dfd913 | -8.7683 | -46.0373 | 2025-09-14 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| e7d1ec02-24c5-3396-8ac6-83e825ec3d77 | -14.4779 | -47.3368 | 2025-09-14 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| da592677-4182-3956-b75c-6fda4f9028e0 | -12.1048 | -47.5592 | 2025-09-14 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 95616d54-dca7-31fe-8ae3-3b4b2d57250a | -10.8994 | -45.4426 | 2025-09-14 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 0c99c02c-92b9-37ef-9aea-3a0da6d65d0c | -8.9176 | -46.1565 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 9442c909-5c02-39d8-8686-4ea3e7d5df7d | -12.1427 | -47.5763 | 2025-09-14 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 5e76c933-c129-3bb7-b15f-b0f27e533d85 | -11.0617 | -49.7261 | 2025-09-14 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a88edbe6-e3dd-3c0b-834a-fe87bf71c65a | -8.979 | -45.7892 | 2025-09-14 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 10dd5098-eaad-32db-969f-6429233306f1 | -12.4541 | -57.7872 | 2025-09-14 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7c90a4ba-ef3b-355c-9923-aaee6e9933c3 | -15.0477 | -47.9856 | 2025-09-14 13:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 235a61a6-9845-3682-80c6-233e0b5b0f91 | -10.9096 | -47.2023 | 2025-09-14 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| c59777b1-657a-3891-a101-2b0fdaeec50a | -8.8984 | -46.181 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |


[Clique aqui para ver as próximas entradas](README86.md)
