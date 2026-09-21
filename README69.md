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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cebda3eb-335e-3b6e-81bf-fd0042925ed3 | -10.90748 | -53.96518 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9db960cf-a648-382f-a9b3-d9b0ed6b27e5 | -9.75127 | -54.30579 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f211579a-d3d6-304f-a364-edc5d295279c | -7.57506 | -57.69077 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9fbdca6-c615-3864-a89b-f3244159d5b4 | -8.78445 | -48.7445 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7eba60c0-1c50-3c30-bdc4-cc97e8b2d0ff | -10.76794 | -50.81911 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 425cded2-85c8-3478-b0fb-bc82a1fd9331 | -7.24816 | -55.58683 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aa4ce50-9c65-3358-93d5-a50bf57ebfef | -10.67564 | -48.71606 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e996e937-df86-3885-8262-cdc5dcaf4850 | -7.88061 | -54.72309 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1921d599-8f60-31cd-8086-62652d4a59ce | -8.61635 | -54.58891 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9e9485-67b7-37c2-bcd0-76207da162b7 | -9.45735 | -45.38807 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84509425-01c8-3f29-bd93-45d2c435bf83 | -11.85871 | -46.88406 | 2026-09-21 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3edbbf85-4376-3b7c-b5ad-c012a0869f22 | -7.5814 | -57.68479 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f85418a4-7bfc-39d4-a786-3f871cb793fb | -12.76786 | -52.85331 | 2026-09-21 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ae75cfc-4eda-3008-a25b-50e9d293ecaa | -11.09818 | -48.31005 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9c056e1-16bc-35a4-a53f-0751cce5bc06 | -11.464 | -58.16178 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6614337-578f-367f-80e9-d4ea9f93f9e4 | -9.82849 | -48.31831 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e612e649-9940-343b-b932-e74092384a36 | -11.99569 | -44.89138 | 2026-09-21 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58bebda9-a66c-382c-8333-bc7e8a166137 | -9.27133 | -46.18546 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64091d26-a63c-3718-844d-828d00d57fab | -7.32683 | -55.60679 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bf8c07f-32b9-3afe-b2ef-cb4507b66eb0 | -9.71106 | -47.10349 | 2026-09-21 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21957298-b89f-36bb-99ca-9988d97d3ce6 | -10.37884 | -48.90699 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 44567bac-1acf-3e86-8363-a87251dffb6e | -6.65304 | -59.96489 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e311b9db-ced6-3456-ab20-6a8a414d3919 | -8.85758 | -62.36062 | 2026-09-21 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82ca053c-ef23-35cb-a746-705d152e77f9 | -9.44947 | -45.40588 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| bfb52406-a0b7-37f5-99e9-625c3a6fa218 | -9.53844 | -45.39431 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecd15b5d-a858-3c7a-b08e-e34e49643557 | -7.33743 | -55.20721 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34351c0e-71e8-3e82-b6e3-a9f07ba07198 | -10.88112 | -56.23671 | 2026-09-21 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3e52efc-954c-32ba-9f70-f1c0548a44a0 | -10.41716 | -50.23895 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 817505d5-8d2a-3bbd-bfb2-1aa3e07cfb48 | -9.12375 | -58.91845 | 2026-09-21 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d0f492-f1ef-31cb-b29e-7fe347b3443e | -12.76839 | -52.8551 | 2026-09-21 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8456521-e164-38f3-8ab3-0d7d7fbbdb84 | -9.97825 | -50.26226 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bc95ff3a-1027-3563-b1c4-b3b3851c1c15 | -11.27801 | -54.12501 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c50f78c7-e8ce-3bd6-acd5-cf5b5d270ee2 | -9.58284 | -55.10416 | 2026-09-21 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e865404-475d-3f91-9a40-b4c53b55788b | -14.22796 | -44.63918 | 2026-09-21 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad529b0a-e0dc-3659-a926-ed50ab4807ed | -7.81372 | -61.80326 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e1a3feb-fa9f-3a1e-8c19-235f89470401 | -7.81786 | -61.80394 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de6e8878-8239-3409-8954-6773536499a2 | -12.30591 | -49.18209 | 2026-09-21 05:06:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7467a710-43fe-392f-a45e-46747b09f555 | -7.24769 | -55.61171 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b96b621-e820-3471-9222-0a3a2aee5dfd | -9.65794 | -54.32354 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ddcb94b-603e-35a0-a51d-d1e892e3b6d1 | -6.44893 | -59.98021 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf5aa816-8cdc-37f4-aecd-5a824c087118 | -12.77617 | -52.85633 | 2026-09-21 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cff9dfdc-2acf-3b15-aab4-928388a8bbe4 | -7.32576 | -55.61371 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 774197f2-b7ae-3ba1-8e88-f0f351816a83 | -12.77685 | -52.85132 | 2026-09-21 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1e03b0c-bade-3fb0-88bb-3f27f51808bb | -6.92011 | -62.90699 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f011b81b-1649-322a-9965-d6d3a3ef8d28 | -9.28275 | -56.89438 | 2026-09-21 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c59677b0-ea4d-32c0-b943-bc9e34644b46 | -13.27156 | -51.75659 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb980dbb-fdd2-3346-a850-a1db16bc480d | -10.80214 | -50.84285 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 562d48da-0204-3ddd-b70d-802885292749 | -6.44598 | -59.97231 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d07a74aa-099f-350e-b886-9251caff10c3 | -10.70694 | -54.17525 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d62f76d1-b682-36bb-b11c-b1f897e333d6 | -8.79006 | -48.73962 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3a75ac8f-befc-3daa-86fb-a9e25ffd9461 | -11.04319 | -54.90403 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a7af3b0-58e8-3ffa-8ac6-8ba5e6f08e14 | -9.37218 | -65.48025 | 2026-09-21 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cad51964-c06f-39cc-b487-d19baae9876d | -10.88483 | -53.97017 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ad7ba25-3e78-3810-b979-f3c4edb2c3da | -10.704 | -54.17068 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a84f4cc9-fb28-3fb4-b01c-d7f85cb2837d | -9.82144 | -48.41349 | 2026-09-21 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 208e2ab1-1c2a-32ee-a972-dbb2144cc170 | -9.27083 | -46.18943 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46028794-51ef-3ef1-8216-de787993740e | -9.03442 | -48.14866 | 2026-09-21 05:06:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c5ff3fe3-e664-33d1-8de5-a892ecfdf937 | -10.42242 | -51.8659 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| da0d74e9-1d18-3362-ad41-e2aeb637da4a | -11.02373 | -49.63375 | 2026-09-21 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cea4e1f8-8f89-3f96-9d7f-f53d934ba6c2 | -11.25721 | -54.14861 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ddbc06c-94ca-3c51-901f-dbc9159148d0 | -10.14356 | -45.55475 | 2026-09-21 05:06:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ad58744-8b0a-3a6f-8e9b-c54a14edeea4 | -10.81544 | -50.77649 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8f2556d5-b503-3988-8c45-5b7a3bb3cf0a | -11.13317 | -54.00523 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f6c1d70-a4ac-3959-bfae-6fccf2408891 | -10.37712 | -48.90144 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33a44696-3289-371f-bf31-1936759b6987 | -8.60508 | -54.61763 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d72ac87f-9467-3064-b1b8-a4fae2ac53ee | -13.34034 | -51.29715 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 012dc5cc-c2f6-37e4-84ca-bc9cc832fd7e | -10.37873 | -50.21971 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2ca18c3e-59ee-30f9-8ffb-152de8872f67 | -11.4756 | -47.76953 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 018f5b05-80e6-3fe6-b3e7-3fbd2214b860 | -7.58127 | -57.67327 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c42c1fa1-f8b3-32d8-b34c-2a83186072bc | -10.41269 | -50.23831 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e9ce7926-4c80-3d03-a15a-ee44fc654e76 | -8.18118 | -54.73118 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9ff9fe6-7526-3e91-823f-4d9cfc593ad8 | -9.55855 | -66.02745 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7713b438-ef09-35e3-adcb-61fdf6c2797d | -8.60564 | -54.61393 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 735262b2-4daa-3d81-b7b6-6e15984aebf2 | -11.33359 | -51.34556 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d43c93e1-eff9-3f5c-9881-2f7999bf9eb2 | -10.16734 | -46.54629 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30fb5243-2d23-36b6-8815-aedb687f0339 | -7.54909 | -61.31808 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5423d209-6588-39a4-9efd-a45893a4cd2a | -8.16945 | -54.76298 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a165752b-4cae-3cae-801b-8beeb2f97166 | -11.79905 | -51.13108 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5cf644f-4fab-3af4-9e8e-7ac816108dd1 | -10.85642 | -54.11693 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0886fc9-46fa-3691-b817-319eaff7f67b | -6.98815 | -59.67598 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29eca262-5c9d-3995-8c0d-c7226cdf0809 | -9.26974 | -46.19813 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72f51e4e-f733-3d5c-8f95-9943ab95478a | -9.92835 | -58.31448 | 2026-09-21 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12bd7c80-4500-3aad-ab65-9622cf8b66d1 | -9.11397 | -60.95029 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0c02408-554e-3571-aa74-bca2bf90ad1f | -7.24985 | -55.59779 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e631d53-bc59-3e45-9089-caea149ad3ce | -8.07838 | -55.33981 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26d6d565-c883-3f21-b716-8f004b468b64 | -6.92463 | -62.90776 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8841c3bf-08f0-3d71-a39a-7318e7419a89 | -10.48328 | -50.27753 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3cae58ed-9990-330a-8a7f-559d4fdeb6cd | -11.03208 | -54.15432 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faa39d33-3329-3aa2-8ff6-dd6b4a3f005c | -9.55537 | -66.04452 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3a8cc9-18d7-3ae5-803e-ddd1d4546c70 | -11.03389 | -54.14207 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1a575e3-4585-358a-8ef2-8ac214550522 | -6.93016 | -62.91132 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9d86d88-ec1c-30aa-97af-dd069c7649a4 | -10.44941 | -51.24774 | 2026-09-21 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32c9bca2-8ded-39a6-b59c-714802026406 | -10.90985 | -53.97404 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a441b24-6c9f-35a9-8f53-f7605a125960 | -7.57734 | -57.67634 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 55b669be-97c8-3bdc-a366-d6dc13ca6241 | -11.17454 | -54.12095 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 996dd2c7-4da5-3bf8-9a82-37c4d17f83e9 | -10.80005 | -50.82555 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aa2a204-abd8-3fcb-8b33-3c634b5b896d | -10.58861 | -57.48158 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8709cfe-1d1f-34cc-8b6e-1718415aa72a | -9.44952 | -45.40073 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d6858a87-16f1-3fe6-8ad9-fcb2aee9e384 | -11.67506 | -43.42081 | 2026-09-21 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02930844-030d-3a38-9f5a-6c6c4f077642 | -8.36548 | -47.20808 | 2026-09-21 05:06:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README70.md)
