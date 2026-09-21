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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edeb83e4-6405-30ec-84f0-d0d07583a3cd | -9.247 | -57.1488 | 2026-09-21 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 33e3faf0-b95e-340d-b374-aee93727af9f | 1.0212 | -51.1654 | 2026-09-21 15:10:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 06d5d474-c7a5-31d9-919f-997d05654cf4 | -12.8918 | -52.0742 | 2026-09-21 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 781f4168-93b2-3ae7-8a43-1cb1b0f50aa5 | -6.306 | -55.9253 | 2026-09-21 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 33acdaf7-0f4c-3912-b6f6-97fa19aa9cb0 | 1.0397 | -51.1445 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ce3ad778-9206-38f5-8be9-a724838a64e3 | -9.1708 | -50.0049 | 2026-09-21 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 215.2 |
| c44c6824-dd91-3ea9-9653-4c390c63855c | -10.6875 | -50.7722 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 837b884c-669f-37cc-9226-6d8312cf32f0 | -9.5594 | -66.0359 | 2026-09-21 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 6bfaf001-f17b-3b05-ab59-d94ac8e89c55 | -3.4369 | -50.6142 | 2026-09-21 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 04121c92-719f-3dd7-bd69-b37ef9c3a072 | -9.8689 | -48.4252 | 2026-09-21 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |
| c1e41cd2-f46f-3ec2-8fe4-e31bcea42a62 | -4.3542 | -55.6455 | 2026-09-21 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b0296a12-6699-3695-aca6-c2bf9831c73f | -7.5477 | -61.3247 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c5daacb2-a0c3-3746-8552-d8299feb33f1 | -7.3103 | -55.2166 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| dd805a66-289c-3032-96a4-fdd2a800c6ea | -12.0451 | -50.064 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 7daed799-ca50-3fee-97a0-3a647a19b03d | -6.9223 | -42.9323 | 2026-09-21 15:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 157.9 |
| c8e2b53c-1141-3c8e-a9ed-86c9727f742f | -7.326 | -55.5953 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1ab91213-2ff5-3424-8ffc-6e0f549c67aa | -7.3444 | -55.6142 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 81d0eaa4-40f9-3347-bb38-bbb34f036121 | -10.7061 | -50.7915 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 454.6 |
| 521152d9-9088-3018-b422-46aaaba7aa83 | -11.8715 | -48.9792 | 2026-09-21 15:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d135d1da-80d1-353a-ac02-87933536fa75 | -10.3738 | -50.208 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 072ca560-cdb9-3407-93ff-c3c5e0c37f22 | -12.1662 | -50.8646 | 2026-09-21 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 02840aab-881c-34e7-b2fd-c7442d720433 | -1.4487 | -48.9526 | 2026-09-21 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 598d558f-060e-356a-a446-26790da235e2 | -8.0094 | -61.3633 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| facb99a9-d86d-359d-b717-e92736d6540b | -3.4461 | -58.0199 | 2026-09-21 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| abf5e4a7-3c1e-3d3e-97eb-779ef114fe17 | -12.5039 | -50.0075 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3b57a8bf-54cd-303a-8319-7fd260b3af01 | -3.4599 | -59.54 | 2026-09-21 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 369895ab-5dca-381e-8fa0-24468b83f681 | -14.6487 | -45.6833 | 2026-09-21 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| fa47bc0c-3260-3ec2-b0aa-f28fd4fa1798 | -8.6169 | -54.6328 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cf37e141-348d-3c83-8ef8-9b5552c4e04e | -9.578 | -66.0353 | 2026-09-21 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| a388d914-9c1e-3f4f-95ed-91d18c34063f | -3.8096 | -58.8994 | 2026-09-21 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ceaac9a2-77c0-396c-81fc-81314e159cc2 | -5.7692 | -43.7077 | 2026-09-21 15:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 403ee570-b341-3570-be6c-8ab83c40361f | -1.4302 | -48.9529 | 2026-09-21 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c259f1df-ee60-380e-86f5-e5e733899e7f | -12.5227 | -50.0267 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 23dbae25-1399-3cdc-a1c1-3c830dce4a9d | 1.2608 | -50.976 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e79a0d23-4302-39de-a67c-eaa9a25f0e0a | -8.6171 | -54.6126 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 95fbe175-f8b9-3179-bd06-68eb5ae4e5a2 | -11.3419 | -51.3606 | 2026-09-21 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 5bd1d372-b745-39d8-a50b-e3d3b3a127af | -6.3198 | -59.9572 | 2026-09-21 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 81027807-8cc6-3e17-b0ae-36c8f5e26008 | -3.0507 | -50.2702 | 2026-09-21 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d4c4c7c2-ab45-3060-ac65-062cae2f6ed9 | -9.2567 | -46.2098 | 2026-09-21 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0f2a4ff8-ea92-3dd2-aab3-03e0c696c966 | -12.5415 | -50.046 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9bc58e09-7f34-3292-b602-f051f4b2594a | -13.5075 | -51.8728 | 2026-09-21 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f8072c96-1f1b-313d-bf2c-4ca8e72d7aa1 | -9.2472 | -57.129 | 2026-09-21 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 49459e04-efbd-32a0-8be7-491b31dce90f | -11.8559 | -49.979 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c47b9ba3-14a9-3c34-b107-2cdda703feb8 | -3.3358 | -58.1384 | 2026-09-21 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 5060ab07-3ab3-3259-9726-77665757faae | -11.041 | -54.1567 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 261.7 |
| fba3617e-b3bb-3834-bf62-bcec12ac8188 | -8.1688 | -54.7432 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c2d400ca-66ef-3a2a-946e-0ecb1a2c19cc | -6.8058 | -55.8217 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 56e2cfa6-09c8-3726-bd77-9059e0daac0c | -11.0221 | -54.1584 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1aabc2a9-ac78-3ce5-a208-378804261136 | -12.4844 | -50.0315 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6b9e348a-7d67-3f27-902e-fe46cd136721 | -1.4671 | -48.995 | 2026-09-21 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3ff337db-2b43-3bd8-a74d-41700ac82c52 | 1.2424 | -50.997 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d9fd7680-5c70-3737-b7b6-d859eec33254 | -8.3764 | -47.2802 | 2026-09-21 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1682c362-66d0-34ce-9343-ab0a2fdb3d74 | -6.1653 | -47.5052 | 2026-09-21 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 6b917ba1-796b-3bbe-b8a0-4441100ecb7e | -8.0465 | -61.3427 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 939a601f-1538-3d62-a0bf-4987707b7d03 | -10.43 | -50.2449 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7da6098c-c20f-39ae-a735-3f45820567c4 | -10.336 | -50.2119 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| c5995edc-abb3-30f4-956a-f08aa423ab21 | -8.7729 | -44.2568 | 2026-09-21 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 064e54cc-3ac0-39e5-b9b7-bf8d6afcc337 | -8.1871 | -54.7824 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 36d0a03c-61e3-3052-903d-9d9b64192aec | -10.2979 | -50.2372 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 3fe63070-1502-3965-8071-c2560f4911e2 | -6.392 | -45.1948 | 2026-09-21 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 276.6 |
| 11917d62-59e3-3ca3-a89a-10cc206f477c | -7.2519 | -55.5994 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 18a65002-22b6-32b1-bd86-b1a5b8f787c6 | -10.3916 | -50.2916 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d3bce56c-1b59-3fb2-a647-03b005b56be1 | -6.5759 | -45.5419 | 2026-09-21 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2ad288c7-371c-3618-8255-5958a8dc9ee9 | -12.3397 | -50.7371 | 2026-09-21 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5827d90b-5d8a-3234-b316-1e45f36edca6 | -10.7466 | -50.5959 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0c3f21f3-f555-3fd5-899d-4d4013c238d8 | -10.4728 | -51.302 | 2026-09-21 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 345.5 |
| 8cab8be8-3be8-3709-9ce4-daddaef3b80f | -10.7652 | -50.6153 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| d7f81686-a496-31aa-a381-2feb7877f46e | 1.0581 | -51.1443 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 00fc4a51-8753-3ca4-935b-00a151b5f168 | -9.1711 | -49.9835 | 2026-09-21 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 008d8c27-8325-34f3-b918-6b2bdbdbae17 | -7.5703 | -57.6962 | 2026-09-21 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 261cab77-9477-357b-8b02-9c82e48661f5 | -10.8197 | -50.7797 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c5af4399-333c-3a5a-8012-f31f6f8113b7 | -3.3823 | -50.4486 | 2026-09-21 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9757cafb-f35d-391f-afca-092f023b18b6 | -10.9358 | -50.5972 | 2026-09-21 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f03f5fd8-a873-331f-9181-b2ed5a2d48a8 | -8.7911 | -48.7502 | 2026-09-21 15:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 140.3 |
| a605b9af-a525-38df-8b2a-81459d4fd04f | -3.2086 | -57.8119 | 2026-09-21 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f5cdee21-898d-3982-b509-430265aa06ed | -7.3289 | -55.2155 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 534e963e-34d4-3981-9e34-0c46db691914 | -11.801 | -49.8345 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| dfd0aca7-0b26-35da-9344-a1661844d0a2 | -6.8985 | -41.6976 | 2026-09-21 15:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 152.3 |
| f54104e9-00cb-3296-9356-269a1f689281 | -8.7914 | -48.7285 | 2026-09-21 15:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 102.4 |
| bdd84ccc-5bfa-3970-9cb8-dd901932f993 | -12.2723 | -50.1657 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 92970353-f92e-3d57-9e6e-87c601ba1b33 | -6.7369 | -55.0874 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 494418b2-129d-3253-94e8-359653899da2 | -5.9335 | -59.9515 | 2026-09-21 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 89f8393d-8d8d-30c8-ad51-9e1be9d6edce | -10.8735 | -53.9668 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5ed0d177-e4ce-3e03-997f-7fe853474cc4 | -6.5571 | -45.5434 | 2026-09-21 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| b1f8cbb5-a88e-3585-b401-3ea1219e2d84 | -13.2407 | -51.7784 | 2026-09-21 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9dd46f88-f2b8-3719-af3e-e11b6339485c | -11.8359 | -50.046 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9cd31804-b261-3cce-90b5-93794a4fafe4 | -3.4186 | -61.2895 | 2026-09-21 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 2e792ee3-94ea-3d22-be89-04491f8f6c3e | -2.4451 | -49.2306 | 2026-09-21 15:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0d020d59-fffe-3863-9653-d66a397e8e60 | -11.1017 | -48.3072 | 2026-09-21 15:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f6928573-4231-327e-875d-934e941c89c1 | -8.7706 | -45.8567 | 2026-09-21 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 457f3521-a48c-3b8b-b61e-2f8528403dc8 | -7.566 | -61.343 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0157ccb9-b8cd-3766-bea7-93e8909733c7 | -4.0925 | -62.0874 | 2026-09-21 15:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d369dba0-e969-3f44-962e-84d8d2c72e55 | -4.4303 | -55.0867 | 2026-09-21 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c744fc4d-be18-3a76-bd0a-841c9fd6a820 | 1.2608 | -50.9552 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6550ee3b-76a4-33c5-b17e-e4821442eb95 | -10.9355 | -50.6186 | 2026-09-21 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7e8a725f-4baf-3e61-90fe-59372c16e989 | -7.5661 | -61.3239 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9fb8c171-5f83-3f3c-bce5-a9597ce4097b | -8.1686 | -54.7634 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| b62e3950-31a7-3d50-9d23-2900e8cd9d2a | -8.0466 | -61.3237 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b74da6e9-7c16-3806-a3b3-3260022fc2cb | -11.8555 | -47.615 | 2026-09-21 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8a256dc8-69f1-3c44-8a5b-916c5b53eed5 | -9.5779 | -66.0539 | 2026-09-21 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |


[Clique aqui para ver as próximas entradas](README138.md)
