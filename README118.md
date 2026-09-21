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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 265ce3b0-b5be-3dc1-85e4-2d295c66f93e | -12.9091 | -50.9672 | 2026-09-21 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e6622ef7-d400-344d-9e18-e3993aacf1fe | -8.7729 | -44.2568 | 2026-09-21 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 25de3a8b-3b2b-3ce5-9c4b-eaa28c32edc9 | -7.5704 | -57.6766 | 2026-09-21 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2e41f72a-b699-3924-8481-f14d228d7ebe | -12.8437 | -54.0422 | 2026-09-21 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 365.1 |
| de468d17-0dec-34a0-ae7d-b6d78fdb70f3 | -5.9334 | -59.9707 | 2026-09-21 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 23db371d-2858-3ff8-85c3-50a9035c2200 | -10.3725 | -48.9153 | 2026-09-21 13:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5ac2ce39-4180-355b-b860-a594a64d9031 | -11.9967 | -58.0821 | 2026-09-21 13:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| bd271aab-09dc-3245-95b3-864367c990a3 | -12.8899 | -50.9695 | 2026-09-21 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| c686055e-b0f9-3395-9dde-8575c3d2a745 | -12.2914 | -50.1633 | 2026-09-21 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 6b3d4911-1474-3fa8-9bd2-049ba59934c4 | -6.5759 | -45.5419 | 2026-09-21 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 50771f2c-b67b-334a-8801-72cceb294ed8 | -9.89 | -48.41 | 2026-09-21 13:15:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aefcc296-faeb-36cd-b49b-c17c09b950eb | -16.04 | -52.52 | 2026-09-21 13:15:00 | MSG-03 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6abe73f-6574-33a2-93f7-114f4c551ad1 | -6.4554 | -48.4423 | 2026-09-21 13:20:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 78e813dc-429e-3cd6-82a4-46439fe636d3 | -10.0714 | -50.2387 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 0dce0e80-10c0-3d7c-9301-ed41608aad16 | -8.7726 | -44.28 | 2026-09-21 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| a198ad44-62e7-38e3-b574-84b8d612d510 | -11.8491 | -46.8556 | 2026-09-21 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6ec26f0e-2dbb-35dc-a605-a60fbe019ae2 | -8.7537 | -44.2821 | 2026-09-21 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| ffc1f51b-ddf9-30b9-b5e7-f02e75062c02 | -7.5889 | -57.6757 | 2026-09-21 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e5ae4dc1-c277-36d8-b591-43596ce923f7 | -11.9967 | -58.0821 | 2026-09-21 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 173.2 |
| ab83afbd-a315-340b-9fa3-849f14eced47 | -13.3443 | -51.2973 | 2026-09-21 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 90af7d0b-6705-3fc7-bcf6-988c97e85b0d | -10.1749 | -45.5591 | 2026-09-21 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 84a679ec-a204-3309-9f71-8b988d6db5ff | -13.2787 | -51.795 | 2026-09-21 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 818e8d63-ffc6-3203-aae9-9b4056b7f11f | -10.744 | -50.7876 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 1a707347-f144-31a8-abe4-220727e40025 | -12.2914 | -50.1633 | 2026-09-21 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 93307c68-2df1-35e0-8d21-346ec9332349 | -9.7504 | -46.0637 | 2026-09-21 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3f19a2ff-8cea-3ad8-8fa9-8bfb63a127de | -7.3291 | -55.1955 | 2026-09-21 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 66c446aa-7190-3e92-a24a-c71dc96643e9 | -3.753 | -59.419 | 2026-09-21 13:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a2e63c62-8538-309a-bc93-7ea2f930a6da | -5.841 | -53.5205 | 2026-09-21 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 73d3ca2a-a8db-3ede-9b63-8e1dec2d1177 | -11.8682 | -46.8529 | 2026-09-21 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8330e9a7-55b6-3c29-9bf2-2e0cf6764dc6 | -10.3725 | -48.9153 | 2026-09-21 13:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 3b4bc7a5-40bf-3f1e-8575-5708fc6af04b | -6.9037 | -42.9105 | 2026-09-21 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.5 |
| b735d673-7b3a-3688-a9de-f3c0e2ced4a5 | -9.8121 | -48.4312 | 2026-09-21 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 263e6dfb-95cf-322a-9a53-1789d184db62 | -10.7253 | -50.7683 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 3865f0be-2dea-3383-8942-2c335a398eeb | -15.4677 | -48.4084 | 2026-09-21 13:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7c3e89d6-5ee1-34de-93c7-659d4351a0cb | -9.2756 | -46.2077 | 2026-09-21 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| b03ce987-3ec4-3a43-9445-dac6d272418f | -8.7723 | -44.3031 | 2026-09-21 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 204a2a41-5b13-3032-b7eb-7c34843e263e | -10.8014 | -50.7391 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 44e57a04-7914-3f10-9cf2-d7ba4eb5b0ee | -7.4092 | -44.7885 | 2026-09-21 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 0164f5e5-ed3b-3bf1-9c47-e55baa5164fd | -9.457 | -45.395 | 2026-09-21 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 88d6be71-8af7-3264-9fae-fb57a1dd3b43 | -9.831 | -48.4292 | 2026-09-21 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 5bfacbc6-8782-3e32-a055-bb6fed4f0259 | -14.0993 | -52.1163 | 2026-09-21 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d80652e6-5020-31de-98f9-56cb4dacd7ce | -7.5704 | -57.6766 | 2026-09-21 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a806ff38-5eb2-3135-8fbd-152c18e5f0ce | -10.8472 | -50.1581 | 2026-09-21 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ae8ad24e-2795-39c3-84a4-74d565a20bb7 | -10.4672 | -50.2838 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e067f3c7-3639-3344-bab8-2788aaff0834 | -11.36 | -51.4221 | 2026-09-21 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 45eabba8-f1f3-3478-ac43-56ac31e0ae7f | -11.0991 | -54.0285 | 2026-09-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e4d01d12-c704-3501-bbe6-363f543937d6 | -10.3924 | -50.2275 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 82356025-7981-3519-bda5-b1c363de9471 | -10.336 | -50.2119 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| feb3daf0-e1c1-3b7f-9694-00abf3fe6640 | -10.8096 | -50.1407 | 2026-09-21 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 0269deb2-9c8f-3e0f-963e-a064c18ce843 | -10.8002 | -50.8243 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 709fcf13-ed2d-3ee0-b69c-71c1fb93234d | -4.9533 | -45.16 | 2026-09-21 13:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2c76c2f0-de62-3bf6-9ad9-30f2b80ea7ee | -12.9091 | -50.9672 | 2026-09-21 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 3088fe34-95c3-32fb-818d-7a8e6e9f0fd5 | -12.8711 | -50.9505 | 2026-09-21 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 477fb838-a744-3185-83c0-57cf7d7304e8 | -6.1841 | -57.7786 | 2026-09-21 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6da43693-12dd-3dcc-bb39-c59f0ffab89e | -10.4675 | -50.2624 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 35b1d5e5-bfb6-38d0-b15f-8884933ea648 | -4.2239 | -48.6127 | 2026-09-21 13:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c63b10f4-015a-35fa-a266-fd1e6c7c4ada | -6.5571 | -45.5434 | 2026-09-21 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 75936b36-9db3-38fb-b667-da71b107dbc9 | -6.4485 | -59.9909 | 2026-09-21 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ff9be6b3-67e8-3ba9-aa23-7b29ab473ae1 | -10.4486 | -50.2644 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| d6f89c73-fc12-3750-a182-358435ccf1bf | -9.257 | -46.1873 | 2026-09-21 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3ac0d6a4-1dac-3206-974b-31ec65087560 | -10.7999 | -50.8455 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| fbe4f954-c2c6-3570-8039-6fb0c3bb3dc0 | -11.8014 | -49.8129 | 2026-09-21 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| aeb26b96-6434-3256-8663-05e48222fd5c | -9.9768 | -50.2694 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fc54380d-5403-37c7-b764-96de79035914 | -9.0227 | -49.8262 | 2026-09-21 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ad0097b8-ee92-3521-aa30-1f8ec3ee750e | -3.3454 | -42.7597 | 2026-09-21 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7af0b396-92e8-3abd-a952-d41dc4f67ad9 | -3.9127 | -44.6505 | 2026-09-21 13:20:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 52278253-2140-3046-93cc-aa8abd4962cf | -10.3917 | -48.8915 | 2026-09-21 13:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 2e0c707c-b311-34a2-b40b-b3f34ca78ba8 | -6.7464 | -59.4223 | 2026-09-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 168.2 |
| cf36b8bb-2562-3a3d-999f-888a6731de6f | -10.3549 | -50.2099 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 29d2b9ac-68ab-305c-90fd-904945f2104d | -6.9223 | -42.9323 | 2026-09-21 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 70933cd6-36cc-3985-aa07-1db96479c4c0 | -6.4741 | -48.441 | 2026-09-21 13:20:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 99.0 |
| d6d61fee-ca04-387e-b15b-32768f9ba5b5 | -10.7064 | -50.7703 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 18be7313-92d7-325d-a048-11d5c351b59a | -9.8307 | -48.451 | 2026-09-21 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| f5e652b5-75ec-3cee-b95a-74fe35e5113c | -10.3914 | -48.9133 | 2026-09-21 13:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8b30c9dc-d9a3-3d72-94a5-f8db8f29818d | -10.8662 | -50.156 | 2026-09-21 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 31b70fcd-9f3a-3bc1-9cee-9b2531125074 | -10.5558 | -46.732 | 2026-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 98cf1721-350c-37a4-82de-0e5bd8bce5fa | -10.7521 | -46.3252 | 2026-09-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 14033466-375c-39d4-bbb3-0d00e316dd6d | -12.4204 | -47.0228 | 2026-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 241.0 |
| 8ab2ad38-64f3-378b-b0a6-454dc5c1b6d1 | -10.6889 | -50.6658 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ff53600f-c665-3808-b293-b35307af8f6d | -6.4486 | -59.9717 | 2026-09-21 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 61cfe5ce-d268-3f72-83e2-be7e455c4269 | -10.0526 | -50.2406 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| cafbc94b-7702-3d5e-b798-ed9d8f8c1322 | -14.1815 | -51.808 | 2026-09-21 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7777787e-4a69-30e3-a485-dd55113102b1 | -10.279 | -50.2391 | 2026-09-21 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| cdb9df80-0859-3f20-baaf-43b186805c3e | -12.8899 | -50.9695 | 2026-09-21 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 218aa248-3682-3dcd-9e98-c765d99fc1ab | -12.8708 | -50.9719 | 2026-09-21 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 1c402e77-05fd-334b-a806-149754f592e5 | -11.1183 | -54.0062 | 2026-09-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| cd49d8e4-8a43-3c59-8dca-38cf2bdfb018 | -10.7437 | -50.8089 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 91e17299-b3ad-3387-87be-489cdeef2b1e | -9.2759 | -46.1852 | 2026-09-21 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2608abf1-1519-30e8-b546-726740ec79ad | -11.5026 | -50.7272 | 2026-09-21 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d8e492ee-dcbe-3c80-91c9-caeaec67d5f7 | -11.3419 | -51.3606 | 2026-09-21 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 23f26233-f3cf-301c-9c02-8b999b7da32c | -5.9335 | -59.9515 | 2026-09-21 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 156.0 |
| a67f86a7-8e99-38b8-b53c-3b22de068505 | -12.4012 | -47.0255 | 2026-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| d53140ce-b644-30be-b6c8-1cfe0f1400a9 | -5.9334 | -59.9707 | 2026-09-21 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 0d43866e-27a5-3056-8800-50211bc17e7f | -10.8011 | -50.7604 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| ae72c61b-da93-3766-95c7-4d034834ec3a | -10.7626 | -50.8069 | 2026-09-21 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 66403f97-b5d4-332d-a424-56bc07e737d8 | -6.8263 | -55.5421 | 2026-09-21 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 26b3f42b-3d96-3970-8905-c271686dd82a | -6.5759 | -45.5419 | 2026-09-21 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 76479882-b859-3bad-b699-372e275357ff | -6.8448 | -55.5411 | 2026-09-21 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a3f17cb1-3893-35aa-a982-959aee233f97 | -10.8282 | -50.1601 | 2026-09-21 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| c63a4b53-c038-36af-9fc1-263d19861c3b | -3.7713 | -59.4185 | 2026-09-21 13:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |


[Clique aqui para ver as próximas entradas](README119.md)
