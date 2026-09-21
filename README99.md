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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8128e9f2-b0bc-3d54-b4e9-0c35fa936874 | -6.35749 | -58.28485 | 2026-09-21 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e6b5fc0-4af2-34ac-af57-f4671feb38de | -6.22629 | -55.61774 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53fbbed9-9401-39b9-ab0b-2e3e8af9edd4 | -11.13432 | -54.01184 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 936c4fc6-b599-3e07-a254-248b8907696a | -6.83396 | -58.98566 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e739feb-936a-3838-aff1-a199f3d0189d | -6.87459 | -63.11326 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30dc23d3-46ed-34a8-9048-3d49f311c2f0 | -5.83666 | -53.55051 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40c42ed-ada2-3d49-a423-3ab78b4c2490 | -8.18383 | -54.76757 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cabba4d2-2906-3c91-b2aa-5e59bbfa2a28 | -10.48734 | -50.99815 | 2026-09-21 05:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bfd6ed8-aad4-393e-8d37-d4b5a6b5a589 | -6.76704 | -59.73582 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b738c0a-27f8-3e25-8cd9-e1c8a29642f3 | -9.02453 | -49.82629 | 2026-09-21 05:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49d44b79-4bde-3e59-a351-44102b3f9e16 | -6.19941 | -55.4444 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4ba2aa6-5fd3-30ac-9432-322150f862ec | -6.46125 | -59.97024 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41523439-af65-34ea-be44-afbc40054994 | -8.85868 | -62.36198 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7a98ade-89ec-305b-8f83-a0ea1bde2242 | -10.79142 | -50.76767 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ead4b890-3b8e-3374-b2e5-b7bc682a73dd | -8.15561 | -54.82911 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 801dfa3a-3b88-3f84-a2cd-f392a1f0b736 | -6.77583 | -55.49115 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67613b90-f209-31fc-a50a-8f6ef0eb9b87 | -7.56664 | -57.68076 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b58e6071-cad9-3b16-949d-130d6dff90e6 | -6.26247 | -55.42823 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a34a193-be76-3bee-8e42-1ede37f29fa2 | -10.88221 | -54.06429 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a73ed2b-7c48-39e9-bb6c-6e540081b501 | -10.90132 | -54.08381 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e62a8ecc-16ba-31ba-9591-61b336041c56 | -6.96485 | -71.75879 | 2026-09-21 05:42:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bcab366-7ea9-35e4-bed2-c8095fdf85a9 | -7.11832 | -48.437 | 2026-09-21 05:42:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f46bc6d-553c-3a51-8b19-d476d5583599 | -8.17922 | -54.72824 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cacbe0f9-d32d-303f-93c6-c819cef9f798 | -10.87788 | -54.0977 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8408cb7f-b5dd-36c3-9b3f-c5f4a419a866 | -9.07494 | -61.3624 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e167970-96d5-3076-afaf-f2caaff49b1d | -7.5793 | -57.67746 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 50a14275-c776-3310-b208-205394e62c8b | -5.76949 | -57.5876 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9deabafe-cace-3ab3-92ee-9eb2a7854046 | -6.73999 | -55.10124 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e201cf5-5b1b-36ce-bcbf-8003df7a8048 | -5.20808 | -56.10139 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2a0af49-107d-385b-815c-eb2831ffd883 | -6.73535 | -55.10044 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ba08d17-c00a-330e-92ad-fddc11a4dadc | -8.17261 | -54.77692 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7febe0dd-2bc8-3831-8152-94ed75dcfbcb | -11.79903 | -49.80757 | 2026-09-21 05:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f32e3a95-8dce-396b-bb25-3e126acb663b | -6.28267 | -56.03865 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8424ac-8f11-36f4-b36f-2da93e363737 | -10.43517 | -50.24473 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a333d7b0-6796-3faa-8d27-36a3d5cfde33 | -9.36067 | -60.31892 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d506918-f6c0-3d2a-9c6f-21cb2745a65f | -9.07776 | -61.36655 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 509126a0-82d5-38bc-8e25-07ef7a1d98a1 | -9.56862 | -66.05421 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03217e99-dd34-36da-8254-e32e61fffae8 | -10.69298 | -50.75513 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a12f751-818d-3b66-af95-1bb2e87255e1 | -10.79816 | -50.75742 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7289e1e4-4a39-3718-aacf-56ed8420cf34 | -6.14497 | -59.94352 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0395825f-191e-391c-a279-83dc37af3d68 | -5.77265 | -57.59305 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2bc7df0-6801-3b82-adb1-48911487319d | -7.24721 | -55.58286 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afdb9974-5bc9-3116-86e5-36a5756d6ccd | -9.55367 | -66.00998 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0cc8d19-ad1a-3c6c-b83d-028cbe7e4ada | -6.4618 | -59.98985 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1a92ee1-2878-3ee8-8987-2eb362a2d9e5 | -9.03307 | -61.65472 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 334f3faf-9ed6-3b30-8d39-b2582138c7e4 | -10.3189 | -50.55856 | 2026-09-21 05:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5564cd02-3c5a-3c12-9a9d-ad00c1638f48 | -11.0163 | -54.1386 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a20c5eb-9c94-3cdc-829d-aa2e851d0ce6 | -6.64991 | -59.96314 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 351c6861-84f0-3771-8740-e5fd3017b319 | -7.40086 | -55.22155 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57cd985a-fe36-3d4b-9a8f-ecf11c5bc816 | -10.70567 | -50.7767 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d23b9702-8aaf-3f58-a719-69c3579c73f0 | -5.37493 | -56.05243 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ca8abc1-dd82-3c25-86d2-46464944613c | -5.8299 | -53.52473 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c003d826-1ab6-32b6-86e8-26c3e95ebb89 | -10.92334 | -53.95727 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6548b4a4-4d59-3a86-a5d5-79c188a9e902 | -6.15943 | -59.94178 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2efc5cb6-0f70-3df6-b70a-35c7b58abcf9 | -10.69363 | -50.74955 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a58cf5e-195e-35ab-8544-4ce73a40c62f | -6.73871 | -59.42286 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| daaa6644-6227-3486-bafd-ba7e8e864ebb | -5.86405 | -60.16231 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e3347ca-213e-38a6-88df-384194bc9c35 | -9.67521 | -54.33408 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6882cf0-b059-32b4-bd30-7bcdf89c2f94 | -10.80935 | -50.7759 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e83f6735-0efa-31d0-a7ba-2c167c785fbb | -11.03769 | -57.23938 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73bffc2d-321f-3ca8-abc0-a34f1f0bd54c | -5.89728 | -52.09618 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c6192a5-556f-306a-b065-fcc9f1d8f7f6 | -6.45891 | -59.98549 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3a268a79-78ab-3cae-ab2e-d98329b9d05a | -6.71315 | -59.45741 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa0a8a6f-5991-39c7-a845-84b70bf1fb8f | -9.54946 | -66.03529 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ea97efa-a3bc-3ade-a425-4db42fe25035 | -5.82183 | -53.50791 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91c36d5b-1704-3e48-8567-5e00a9a67cc4 | -10.90176 | -54.08046 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61ab0606-7c2c-3dc7-8869-e95e8389dbfe | -10.77088 | -50.82716 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31987e3d-b8f5-3f80-b41c-f85e1ab72c12 | -7.58252 | -57.68316 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e8dc5c1-901b-3576-bce5-ca0eb7139fe4 | -6.25666 | -55.43657 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89f79023-2efe-3855-bb44-f50dbe79f961 | -6.31692 | -59.96509 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a480c034-1667-32d3-8392-f71ef61f62e0 | -5.84074 | -53.48578 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e0e0c55-08aa-3f72-8efe-919295b88077 | -10.90504 | -53.97208 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa9c08fe-cb0e-3890-badf-eee1d400335f | -7.59197 | -57.67414 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0b0ce4ad-a461-39d4-8c5b-f7bb566c6582 | -11.0403 | -57.23829 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9c08b6c-311a-3b6d-a942-90cf86037428 | -10.39012 | -50.22078 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 345a3fb8-a20b-36e9-a49e-80f39a66b37d | -8.23357 | -71.05261 | 2026-09-21 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df35c2aa-a3cc-392a-a670-6e3abef537c3 | -6.71311 | -58.99925 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d557d8f-51e3-3327-b4ad-0d7a32c8d55b | -5.83123 | -53.5155 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8074f8c6-ee3c-33cf-be86-e19aebb6b6c1 | -6.2556 | -55.43922 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3520d5e7-179c-3d87-934c-d323677201cf | -9.55297 | -66.01416 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05df6ba-bd57-38ee-ba18-703fa053168c | -7.86339 | -62.53598 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f279509e-4fd0-3611-9b29-33bc5725acd7 | -10.70217 | -54.17415 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce3497c4-21fd-3e6f-a092-89dbc4b00b87 | -6.13746 | -59.94621 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fea39a8-6fed-390a-accf-303ddeab2e42 | -6.44736 | -59.96811 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b6faece-4803-3a3b-8f0f-d2d59d2a507f | -5.84778 | -53.54595 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 345cf6b3-7849-37e9-8d8c-a7730a5e060c | -6.11292 | -57.74519 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c731406-f414-34b7-9580-6f201f62564d | -10.79799 | -50.76849 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 844023cc-3a1c-3abe-949c-9d98533f9022 | -10.8669 | -57.1625 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6955d30d-36cd-386b-a78b-0d5b49c017d3 | -6.42153 | -55.01297 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fb019ee-779e-36d1-914a-c654732ea5d6 | -11.16641 | -54.12111 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9c281f1-df93-3356-8db7-68054db398b5 | -6.45314 | -59.97678 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62eb1565-a0ac-3b04-925c-e5d1cc9bc97b | -9.55659 | -66.0148 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 846fcc6b-7641-3d67-8aa2-6b15657d4ef9 | -9.74361 | -65.0181 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6c7f33e-557d-3ba1-aec2-e8e1d83f3a43 | -8.18235 | -54.77834 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 332514a2-7760-36c4-81b7-c0f68953fa82 | -5.82696 | -53.50866 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f53c706-bcfd-38c6-ab21-b2fc5a48c7e9 | -10.71151 | -54.01395 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 844fc3a4-d2c2-3712-bde9-ec63598268a8 | -6.07024 | -55.6228 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69be75b6-4194-3cbb-9988-bace065a6396 | -5.82008 | -53.52014 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d7f4b41-9c9f-3b7d-9e58-8af2fd2ed5ed | -10.70415 | -50.77357 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a75ae893-2225-308a-bd3d-6cab327d401d | -6.83096 | -58.98085 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README100.md)
