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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 395de17a-5646-31bf-9a12-80f73447a015 | -6.1359 | -59.9446 | 2026-09-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4be76193-1f9f-3dc6-923d-70ff57454c42 | -11.3419 | -51.3606 | 2026-09-21 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 7e3ad5f2-4e12-3799-a1b7-565c8bd87d1c | -9.2756 | -46.2077 | 2026-09-21 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ec0bd428-c54f-3f35-bb21-acd4c09eea85 | -7.4092 | -44.7885 | 2026-09-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 3675b525-e346-3205-bc81-e102cbbf4fbf | -15.4471 | -48.4566 | 2026-09-21 13:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c306b1cd-b028-3a8f-9b81-939435bf004f | -3.177 | -42.8376 | 2026-09-21 13:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| a35f1dfa-e81c-3122-b71e-6db852e9ddd9 | -12.8899 | -50.9695 | 2026-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 179.9 |
| b45dafc2-9161-3e46-8f8a-d6c4a3751531 | -6.5569 | -45.566 | 2026-09-21 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 9fd4c886-47bb-349e-93e3-9eebd6bdce06 | -8.4922 | -47.0257 | 2026-09-21 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 512d3d6b-a51d-3be4-9cf6-87c15c377599 | -6.185 | -43.3491 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a5cf3cda-a3d9-3dab-b2dc-455d8f0bce97 | -10.09 | -50.2581 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| ed5e610f-2693-3e6c-98cc-f3a8e00cb298 | -14.1819 | -51.7866 | 2026-09-21 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| f6743e26-e247-3e86-acd0-0dddc84edef9 | -12.4012 | -47.0255 | 2026-09-21 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| d523bab8-9001-35a7-bd9c-9835c76e0dc9 | -10.9112 | -53.9635 | 2026-09-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 47e23f49-0743-3cf4-aec1-9919206869f3 | -6.4486 | -59.9717 | 2026-09-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 9be9cfae-aee3-3de9-a947-7804e903355f | -8.1876 | -54.7219 | 2026-09-21 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 88e3e3a3-b4b7-347d-b321-2287b903ef11 | -9.257 | -46.1873 | 2026-09-21 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1740c500-cdc6-34e4-a1f9-24a2f2144977 | -9.977 | -50.248 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f95b5505-17f8-371f-abbe-393e4aee64b8 | -8.1872 | -54.7622 | 2026-09-21 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3320c132-993c-3485-af36-51abafaebe49 | -3.3267 | -42.7606 | 2026-09-21 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 35a617ca-f2d2-3cb8-90d9-5d772fd9b2bf | -13.4331 | -51.7334 | 2026-09-21 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 45c7ac10-1d2c-3f89-82d2-23e81bb9e5b4 | -8.727 | -44.8607 | 2026-09-21 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a5f32d6a-9516-30a8-b330-50173eff4e33 | -12.8711 | -50.9505 | 2026-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 4e257d3b-d4f2-327a-8285-757ee57e712a | -13.3443 | -51.2973 | 2026-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 18412749-cac0-3b75-bbcc-7d8394076ef2 | -10.3728 | -48.8936 | 2026-09-21 13:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6e8761d4-a245-3ae7-97e6-ce83e509b869 | -14.1815 | -51.808 | 2026-09-21 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1918fe6e-eeba-3aef-82fc-14a8e9eb3aa1 | -13.2791 | -51.7737 | 2026-09-21 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 294ee3af-91e8-3137-bb3a-c5aaa32fce13 | -10.6889 | -50.6658 | 2026-09-21 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 75897a0d-afdc-3513-81bf-8ea625f794c4 | -11.8014 | -49.8129 | 2026-09-21 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 0b35a3b8-6e79-322d-8610-cde7866fb5d3 | -9.3986 | -48.3213 | 2026-09-21 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6e39908c-950b-325a-98e6-17e23c45424a | -11.4541 | -45.3662 | 2026-09-21 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 986393b4-b967-374c-9d11-b29ca3454f4d | -3.6946 | -60.6025 | 2026-09-21 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 65fd8879-d956-3ea6-861e-6569dea72592 | -10.3917 | -48.8915 | 2026-09-21 13:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 48c871bd-afa9-30e9-8005-605167cf5bde | -9.457 | -45.395 | 2026-09-21 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 270ada2c-11bd-32ac-9165-52d38490a3b5 | -5.7504 | -43.7091 | 2026-09-21 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| e3276667-68c4-31ed-b62d-02990da41d17 | -10.4675 | -50.2624 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 989b685c-89c0-3c8e-bd33-e137e5b0191d | -10.3924 | -50.2275 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 53a953a5-3f16-3968-9f24-22b1c0f1af1b | -9.8307 | -48.451 | 2026-09-21 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 216.6 |
| baa55194-b95c-30b7-803f-22237c32ce00 | -11.041 | -54.1567 | 2026-09-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 5dc3d488-a3dc-3d7c-8db7-9c4ac433f33f | -6.728 | -59.423 | 2026-09-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 585e1103-ae16-33eb-9db9-99c89d0e0246 | -10.8662 | -50.156 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c4064563-c9e2-393f-9abc-dbd7e90c2083 | -10.7652 | -50.6153 | 2026-09-21 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b826acbd-4b51-3cad-bd9a-2e6345485f91 | -8.7267 | -44.8836 | 2026-09-21 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| dc87567d-de7b-372b-bce4-fbb6b070feb7 | -4.9533 | -45.16 | 2026-09-21 13:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f123f07c-123f-341b-be4e-f705fe720363 | -6.1841 | -57.7786 | 2026-09-21 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 95415669-2c36-3ffd-969c-697e1a6e2476 | -9.4567 | -45.4178 | 2026-09-21 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| bb30b832-961b-3828-ac84-0446a7c6c077 | -9.7504 | -46.0637 | 2026-09-21 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 634760dd-d876-3d79-bc61-7389e1037c87 | -8.7723 | -44.3031 | 2026-09-21 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 3c5d96b2-566e-377a-90d8-4ac20bf11fef | -13.2602 | -51.7548 | 2026-09-21 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1e3603f6-71c1-327c-93c3-f2a0df355c75 | -11.4545 | -45.3432 | 2026-09-21 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 50a66b1b-fab1-3faa-93bb-b150e3ef40eb | -10.4486 | -50.2644 | 2026-09-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f9cf2709-15be-3819-8bc0-2d648af0906d | -6.7464 | -59.4223 | 2026-09-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.5 |
| fd3a3def-b773-33b7-bf0d-f3f2d5b04812 | -14.541 | -53.3686 | 2026-09-21 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4abf44a8-68cd-39fc-8460-576d33ea150a | -10.8096 | -50.1407 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4306fae3-8ec1-32ef-90f7-31fbe517e0be | -10.8011 | -50.7604 | 2026-09-21 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 5896d288-6906-367d-94ec-540658ffb178 | -10.955 | -50.5738 | 2026-09-21 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a7a9b9e3-470e-3c3e-a50b-f26517513181 | -9.4567 | -45.4178 | 2026-09-21 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 04175c0a-dd9b-3760-ac6f-a367eecca37d | -3.6632 | -58.8643 | 2026-09-21 13:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 353ef6d9-61e4-35e7-be7d-7188e996a375 | -13.2787 | -51.795 | 2026-09-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0f365d30-3f66-390f-9cd4-272215310057 | -7.4092 | -44.7885 | 2026-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| b61cd615-4692-3f02-8071-6e330ac092de | -13.2602 | -51.7548 | 2026-09-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| aad7d63a-75ee-3fe1-9e61-f84ce6d3ff1b | -10.4486 | -50.2644 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0979c586-be73-3df1-a3b3-7e1dbbc3fce4 | -3.7129 | -60.6022 | 2026-09-21 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 72b40249-7b31-3887-882d-d84fec8d1dc7 | -11.6798 | -43.4446 | 2026-09-21 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 0e07484f-3a22-312d-adbd-c150fea9aa46 | -12.9091 | -50.9672 | 2026-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 7bfa3dbb-b9aa-3305-b243-be7e7f7bec81 | -10.4297 | -50.2663 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 857b9809-4fa5-3957-8934-668608db3199 | -11.1183 | -54.0062 | 2026-09-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ec5252d7-4fc1-38dd-b28a-f505f7622629 | -3.7129 | -60.5832 | 2026-09-21 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 67a2bf24-b8ed-3f05-be1a-7aa7b2cc3ddd | -4.9533 | -45.16 | 2026-09-21 13:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 0d6964d1-b6ee-3123-94cf-c7e907f8b655 | -9.247 | -57.1488 | 2026-09-21 13:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| dc2d4e6a-8db6-39ab-8473-366a674a3405 | -6.4671 | -59.9711 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 39d12ce6-2f73-3269-abdb-9a4b65cbdaa2 | -11.4353 | -45.3459 | 2026-09-21 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 9aedd5e8-b9c6-35a3-b83a-17d2d3e27466 | -10.2979 | -50.2372 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ccc64524-0aa5-3f7a-b1a5-c5794170d554 | -4.0142 | -53.4946 | 2026-09-21 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 2ef49aaf-d9de-3e80-bdde-a5bd5c637f65 | -6.1359 | -59.9446 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 43bb24bd-2349-3318-b38d-0c21d5c58142 | -10.279 | -50.2391 | 2026-09-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 39ca042b-0336-38de-b99a-f030fb061f84 | -6.5571 | -45.5434 | 2026-09-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a717f474-0800-3f39-9842-31bd35b051e6 | -5.757 | -47.2915 | 2026-09-21 13:50:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 28130c2a-baca-3481-8e27-901b9a37fa21 | -8.3764 | -47.2802 | 2026-09-21 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 21300c54-1e29-30b7-9e20-7ebb3531cdf6 | -10.7262 | -50.7044 | 2026-09-21 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 514a00a7-e91d-31ae-9b30-517dad028219 | -3.3267 | -42.7606 | 2026-09-21 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 46a42c1d-505a-381e-a2e5-2de92b2f5707 | -13.2596 | -51.7973 | 2026-09-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 933d4df2-fd09-3c51-b002-3857ca6b0d7b | -14.1819 | -51.7866 | 2026-09-21 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 948a9ace-6acb-36f6-ab6e-5eca2a5f1055 | -5.841 | -53.5205 | 2026-09-21 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| c71e2548-df62-30fb-a85c-8d5691a22b6e | -10.3917 | -48.8915 | 2026-09-21 13:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 173.9 |
| a727042a-39ea-3303-a7ae-1aa18d750ab6 | -3.6946 | -60.5835 | 2026-09-21 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 2a086bf8-ad17-3f8a-bd33-4d0dcc07bf2b | -10.9544 | -50.6165 | 2026-09-21 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| b94a8c5d-ca6f-3ff9-a0fe-175d74d19a88 | -4.9535 | -45.1374 | 2026-09-21 13:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| f9910a8f-2e18-3002-9ebf-66944e7bffc0 | -3.0947 | -59.3173 | 2026-09-21 13:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c1366e87-6c58-3055-b66a-aaaac4dae429 | -12.4016 | -47.003 | 2026-09-21 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 10d80419-dbda-3e4c-8c22-4222fa8a7b0a | -5.9151 | -59.9522 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c14c55b1-393d-3be8-b0a3-c100167128dd | -9.2759 | -46.1852 | 2026-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 70cb0d9f-e653-3b35-aab9-ee36247e288e | -13.2794 | -51.7524 | 2026-09-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 2be1ea06-3f7d-3c4a-94b6-3fc781a98063 | -11.4545 | -45.3432 | 2026-09-21 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| baabc9ef-2787-3f8d-a744-4c6209f66b74 | -14.0989 | -52.1376 | 2026-09-21 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 9d71b3eb-21d6-38e9-8448-ea9bdf328efe | -7.3289 | -55.2155 | 2026-09-21 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 030e4782-a8b2-352b-884f-951e1eed54b6 | -9.8307 | -48.451 | 2026-09-21 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 796fd0df-66e2-3a96-8c7d-243f18236d36 | -10.3687 | -46.5529 | 2026-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f1dfd208-4787-3441-8e48-fc8696c9f831 | -10.3725 | -48.9153 | 2026-09-21 13:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b20dc1e0-d4a6-316e-a93a-23fa5b98f68e | -6.4485 | -59.9909 | 2026-09-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |


[Clique aqui para ver as próximas entradas](README122.md)
