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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de2ea8cc-a204-33ba-ae9d-a1931cde1ea5 | -5.66179 | -60.23333 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b47538f1-dd79-38ff-9a70-9dc200c389b1 | -6.1097 | -57.69187 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5699a1bd-8c52-3184-977e-ae9b04e6290f | -6.47072 | -57.88268 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85d631b5-3d36-39ef-aa1c-49959478a9be | -9.9852 | -59.86899 | 2026-09-15 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7c1eb64-9117-380d-8e78-374ae2f09b96 | -9.36065 | -50.09516 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30ff3f0f-8df1-3976-9ea9-d624763875d3 | -8.96915 | -57.43143 | 2026-09-15 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5397711f-0529-307b-813a-5006915c260d | -8.5415 | -54.69617 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6225666f-8d20-3228-ba3a-e55cf302b063 | -8.54401 | -54.70732 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 659428ee-77dc-389d-b05a-bdd44b0f22f2 | -5.45652 | -60.21959 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b42a84c-2d53-3e22-b113-0e7d2ef087c8 | -6.08325 | -57.863 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc612e45-be4d-326f-874e-ae42737f3a07 | -6.85797 | -55.56161 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eee769a1-09db-35f5-be53-ec7955e662d5 | -9.35838 | -50.11345 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1064a5ec-8dc4-3962-af1c-cb7775c596bd | -6.56426 | -58.97052 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c58318c2-02e5-3db4-acbb-5f71cf85ec45 | -10.88802 | -51.56334 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9142e7b3-cd0d-3c6e-8648-68faf6aa3421 | -6.6957 | -58.69399 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2581c77-b529-31d2-b7f4-cd8c4f47c55b | -10.66485 | -54.13663 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38ee6f0c-9979-3f22-a1a6-8e1bf211144e | -9.01575 | -61.01022 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a070bf3b-340f-3d31-8d85-dc4ee48b0e16 | -6.66141 | -54.98094 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a25d603f-f55e-3671-a082-3288b05b119b | -8.26597 | -55.02593 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f50240f-95a5-3043-bf3a-d5f2c5e4fe78 | -8.50433 | -50.14516 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f03b1267-679a-3ab3-b992-cc63bec0fedc | -6.10412 | -57.7057 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c0d8df5-d1a7-397c-b299-e924706a38f2 | -6.10297 | -57.69086 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0955ea67-90ce-36ee-9c16-6f5b5ef8e1f4 | -9.46066 | -56.70576 | 2026-09-15 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01067e24-fcf9-31af-bb63-9cee918824d0 | -6.83772 | -55.54493 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 84f4b89c-c884-32c2-bce4-da11d5187e1f | -6.11191 | -57.67754 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e2719c7-d89e-36b1-ab64-b85114629064 | -6.00573 | -52.19183 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74e77916-ceb9-32c9-88ba-2da1f806ec53 | -10.67659 | -54.14648 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 834fc1f1-1c73-3390-b769-c6de08033d7d | -10.58234 | -47.74155 | 2026-09-15 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc7d0a8f-d66a-3a51-9927-7a8c586fff8c | -6.69516 | -58.69746 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 641be94a-e945-3ad2-a4f3-f3385e97e2eb | -9.1995 | -60.38985 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba971924-e275-348d-bd76-740571d9f450 | -6.31073 | -59.9817 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac245c0-851b-3a78-a3c0-7b52816db7ed | -8.81845 | -62.49374 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90bc8df7-e0f1-3f61-a3b6-f41ce6f28ebc | -6.13524 | -59.88599 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8cc1cd-fe79-3b3e-9264-3dda3467acc8 | -6.10855 | -57.67702 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1f62aaf-4bf6-3e2d-8054-b92fcddaa721 | -10.6734 | -54.13778 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 731df855-aed3-313c-a74e-aab365887cb0 | -6.36079 | -55.83303 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10b61c41-e8db-3790-b823-666002a4cd48 | -5.88159 | -52.07544 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 092427e5-8b1f-36ab-a33e-05c277783ac0 | -6.69847 | -58.69797 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 43f16ffb-82eb-3192-bed3-88f50465b4d2 | -7.22965 | -46.16175 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bb86d7ab-728a-382d-9414-7bb2f1eeb9eb | -6.84751 | -55.55552 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| ec585181-e41a-3835-8ee5-12f593e6a18d | -9.16296 | -60.2979 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37f34f27-f549-3f67-b7de-5d0272efe07a | -6.6974 | -58.7049 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 893f4c7f-e434-3f06-a38a-310816feae8c | -6.11532 | -57.70005 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f8de603-497d-3cbc-906f-1e15bc6c209c | -6.01572 | -59.93127 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db9047ca-c3e0-313e-a506-6d50ad45c09a | -10.69517 | -54.1699 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ad2b5eb-a8fa-38e8-a89c-20272bfcf08e | -10.66912 | -54.13721 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0643ead-44a2-3392-a823-125948fa7c77 | -5.45988 | -60.22011 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bcf00ed-630e-3bdc-8d74-9035c014eff3 | -5.35695 | -55.88881 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9897b6a8-9ea4-3115-ab6d-c6ccb8cb815d | -8.80964 | -50.49026 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e73774a-ba34-36de-9913-343da66e70c7 | -11.27005 | -54.13077 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d86bf1f-3ec1-3cb6-9f12-28a513784eb2 | -10.93933 | -54.08861 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6dd993a-859d-3089-80a4-2e2405b0b974 | -6.69293 | -58.69001 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d7718049-32db-3473-8318-234db57b17a3 | -10.97769 | -48.32713 | 2026-09-15 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 33cb9941-8bb5-3c5a-81ae-c444d65cbb0d | -8.5445 | -54.70383 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e9b5a78-0768-34bb-91d8-b30cd694e27e | -6.58479 | -58.86045 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb6fef5-97ac-3f7b-8ea2-a2a2ff8c3d42 | -6.02991 | -57.76374 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba821caf-48ed-35f2-8df7-8a003ce1191e | -9.71937 | -64.9122 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833829c9-ca3b-3259-9d77-8341c0f87e95 | -6.1626 | -55.70719 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0b83f51-acc5-381f-b38e-7fa999c96972 | -8.53555 | -54.70956 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92a3e920-2913-3814-97ac-57a53522dfe2 | -6.3289 | -59.99531 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb96ec48-da3e-3f22-8a92-3fa9d527a096 | -9.25642 | -60.43842 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84cc222a-dc02-3baf-a36f-a7ac1f7cf62e | -10.03379 | -52.0919 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a31eb795-27cf-380d-95ea-91cd0b15d50d | -9.13077 | -65.83922 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4eedf005-ef02-34d6-ba4d-9a125d66704d | -9.41035 | -50.10212 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df7c4bf8-e6e4-3d75-82f5-4672b0623189 | -7.30572 | -55.60959 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9caae614-afc7-343f-b27f-48e49627898b | -10.6696 | -54.1662 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bc3649d-a56a-3bf4-b32a-e83ac209f95f | -10.65404 | -58.76667 | 2026-09-15 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7e6da5-22e5-3d15-a46e-e5bd613ac0a8 | -6.10914 | -57.69545 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6bf78e0-af83-31a4-a1c5-fa95c5ce4bbf | -6.45271 | -58.15539 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c7499cc-f56f-375f-bbf9-f5d98c7223a5 | -9.40988 | -50.10577 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 392c7b75-317a-36a8-8e4b-24941f52b6ce | -8.80202 | -46.90806 | 2026-09-15 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1abbf119-f9cd-3eaf-ba94-f3b5dc726242 | -7.31249 | -55.61528 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0432a4e-07b5-37a6-b7cb-56e47eba9f76 | -5.13551 | -55.94153 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f08b4edd-021b-32bc-a8f5-cdfe90c7f188 | -10.67866 | -54.1634 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a10eb1a6-f23b-3ff1-b3be-8b479d8fa646 | -6.85559 | -55.55217 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8b62d09-0e03-36eb-a81d-516cb3b9b931 | -9.71416 | -64.91862 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cedc228-aa00-3104-b13b-2677595d0156 | -6.108 | -57.6806 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5469495d-17e5-3cbf-9547-8723120acf42 | -6.67977 | -58.70927 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49b34543-ee24-33bb-9b34-8840a7f52e4f | -6.68469 | -58.69939 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e4b5ee-d282-3801-85f9-d645e53f0a19 | -6.28295 | -59.91999 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99dbfd63-39a3-392f-83db-6307d8f7aa87 | -5.81126 | -53.80447 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09b246a7-c76c-37b1-8a81-92f96f473b85 | -10.23167 | -56.26423 | 2026-09-15 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95736d57-fb33-3ed1-bc14-db9104900bb3 | -10.67394 | -54.13373 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b19e72c-d458-38d7-a07b-bf33a598df02 | -9.35917 | -50.19243 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6563cdf-44c4-3c7f-8211-bdc527b23d59 | -6.72693 | -48.12262 | 2026-09-15 05:18:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abb6e3a7-a90b-3e8b-8eea-a6027146e114 | -6.11086 | -59.88936 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4fd8170-1553-3289-9ba4-b90cbd785c72 | -9.01902 | -61.03283 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f9abb80-8d1f-3b35-b85e-3547ec5cac87 | -6.10511 | -57.63227 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25e8ac8b-8cbe-361e-a067-92d1e8a987a2 | -6.58809 | -58.86097 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3661528-0890-353a-ac44-97ba7781c1ba | -8.79895 | -50.48888 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4f21126-a65b-30f9-a970-5a60235e9de3 | -9.07057 | -61.01163 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a2b7124-5c85-39cd-9070-19f063ee9052 | -8.50559 | -50.14761 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c36fbba8-2304-363c-9355-9d3bba836b47 | -6.11346 | -57.86086 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e52f704-e462-31d8-9bbb-ba2d2ec0d8fa | -6.10076 | -57.70519 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ed83555-f770-37dd-9ffd-6c192cb9f94e | -10.98449 | -48.32371 | 2026-09-15 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4c2e11e3-dbb4-3f82-a889-b4ea36f03511 | -6.05793 | -52.1849 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e596d1eb-4421-3940-ae25-fd3d179bbddf | -10.60412 | -57.31711 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfc15d4c-cba9-3c86-b580-3b32a872e9c3 | -6.87863 | -59.63685 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbab9fd7-727b-37c0-9a4a-8a6b6a5f7c10 | -6.05724 | -52.18962 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4abf7dbb-8b9a-3ea5-93a6-94f3c4d90f67 | -9.28815 | -50.30983 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README58.md)
