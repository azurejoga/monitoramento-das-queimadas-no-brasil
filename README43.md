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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef3d8f93-b11e-36cf-b0cd-1bfb4f47425e | -3.09307 | -53.71582 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c01ff904-e493-3cf7-a837-3aab5c9f5bfe | -3.22894 | -53.88057 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a42a91d-ac45-309f-9887-a9b8c79c091e | -2.7803 | -54.09626 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62cab4bd-5e07-318b-a21a-a84be8617f68 | -2.99012 | -54.10617 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 132443e0-e8aa-38ab-9f1e-7dcb5853157b | -3.16104 | -50.44793 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01456bd2-0d9a-3259-9cd6-3c366e13970f | -3.06236 | -54.15443 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6a83b56e-927d-3eeb-af6f-76b090b12758 | -2.9918 | -54.0998 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ba96f12-c06c-3430-a871-5d0a1cd50a58 | -3.09678 | -53.7209 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4424eff8-affc-38d9-b8ab-0f2e6d531f2f | -3.08072 | -54.24409 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dbadc2be-87e4-3634-bd82-b0878afcc0b4 | -4.14629 | -54.02942 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 487904d5-1482-3ff3-af44-5931247e927e | -3.08134 | -54.15305 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f167fa0-b883-3fda-b77d-726c157720c5 | -4.96972 | -47.97419 | 2026-10-06 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a522c89a-ce5d-356a-812b-8d1fb8652ceb | -2.87505 | -54.1496 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 800b7937-42f2-3a20-909a-c47c8496f098 | -3.16751 | -50.43965 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8c97e7f6-762f-372a-98dc-074675d151a8 | -2.80073 | -54.14455 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51c10de2-b41c-3f26-9e4b-66c698492895 | 2.47523 | -50.83079 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b3b396a-7e3c-3faa-a05c-03a50d1aea5c | -3.33211 | -53.39397 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d344cca4-9cb1-3622-8bae-15a5b9155c7d | 2.45615 | -50.83902 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9cf7a236-1735-3498-aad4-0a108d9703d0 | -3.49529 | -54.63254 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9603d9bf-6762-3231-9130-2e0741191b65 | -2.70453 | -49.03646 | 2026-10-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1413961e-99cb-3c2e-9e13-0603814462dc | -3.60186 | -54.35998 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37853867-0429-3aff-94bc-eba1e11d3ba0 | -3.62747 | -55.28364 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d96ff26c-deef-36d9-b80c-573465029fc9 | -3.1012 | -53.72165 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4325dc6-bfcd-3cf2-bc31-88a143af3b11 | -3.08143 | -54.18145 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcaaf81a-7de0-3add-bf41-0d4bff94b302 | -3.05471 | -54.23003 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d890b3b3-0b40-31c7-ac1f-c692769b21ac | -3.41678 | -48.33672 | 2026-10-06 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e20a02eb-4018-39a4-ad7d-c73c1aa9750f | -3.46753 | -50.09018 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 387d372e-704c-32a2-bf14-fb9ce3dd4f1f | -3.4911 | -49.90049 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e42825f-bf8f-32d4-9c55-52157ffc797f | -3.10731 | -53.76751 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5af4f496-4090-386b-bd94-299837dcd250 | -3.51327 | -54.6403 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dec8898-5a3b-3ce5-bc1c-f6813dcfb9dc | -5.12676 | -43.99615 | 2026-10-06 04:38:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4194bd49-daa4-3103-aaf2-8367ca4cdc08 | -3.31877 | -53.85313 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2cea820-2318-37a5-90f8-182c8a0e94ff | -3.5149 | -54.63044 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c96c510-1ac0-325a-8255-8f631bc21c70 | -3.4981 | -49.90163 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae1ee231-860e-3475-b8e7-bf002a51008f | -4.19511 | -44.26668 | 2026-10-06 04:38:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dbdb5df-e1e6-3ce7-b3ad-b85ac70e08e4 | -2.80609 | -54.14062 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 558e69c2-f06b-38c7-900a-1c14a7600396 | 1.15412 | -50.74445 | 2026-10-06 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f98aba2-6461-3014-afb7-e587920f3041 | -2.95209 | -54.16714 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a499e9d-0ca6-342f-aef7-1110f0c6286f | -1.61589 | -55.1177 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c319ce6d-40bb-3390-b114-a95a0ad90490 | -2.8719 | -54.16824 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e466678f-3ebb-311c-a469-5b3a6174e70e | -3.09987 | -53.75729 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f98e1a7a-1beb-3141-a7bb-28ae416b7bc3 | -3.27948 | -54.17755 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d59fd85-5fd9-3619-b13c-f838d41e174b | -3.39982 | -50.32648 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f33b5394-7842-33d1-a186-99f263748292 | -2.99245 | -54.12371 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56cd7c0a-3708-358b-afe6-363560ea56bf | -3.73253 | -48.87703 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 79fc5a49-4c11-3b58-ad8d-07dca738e467 | -3.39448 | -44.48494 | 2026-10-06 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d3fee0d-f4b1-379f-a67b-776f12211999 | -2.83256 | -50.47047 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f14dcba-7e93-3876-8de1-75af5d29770a | -3.5841 | -53.475 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f79099e7-4f62-3771-80a4-21c8f2bed31b | -3.09687 | -53.74783 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3c3282b-0374-3776-8ff6-c9133f025e0c | 2.15069 | -55.95455 | 2026-10-06 04:38:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04f2a482-7884-37d2-a01a-2192524bccc5 | -2.17789 | -48.13768 | 2026-10-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c31639c-995f-3546-8aa0-efa5bba30a83 | -3.0616 | -54.15907 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 183eba4d-ab84-3b88-abab-cd1002da2631 | -3.08449 | -54.24686 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e8ae6e88-a8dc-3aff-acd3-0b81287fc34a | -2.77573 | -54.09549 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 29aeeb91-a705-32be-ad55-944d5cbbfc60 | -2.99625 | -54.12629 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f9ba96a-3055-3ee5-9bf8-be9a6b7df80b | -3.16325 | -50.44311 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cf5eb251-fae2-3281-b8a3-9be91e827f4b | -3.02565 | -53.89958 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 9f652765-39e4-3851-a5e6-b670734f572e | -3.00081 | -54.12702 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 757d60ea-01db-340d-ad8d-a56e1a9f9a0f | -3.09462 | -53.73394 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 90797835-536d-32a7-aa0f-57c95cc7421d | -3.08792 | -53.71945 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 982da74a-d22e-3f16-b7d5-0c08540ac1bc | -4.06676 | -54.04908 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f907172-50e5-3081-b9be-06553d5f9aec | -3.46207 | -50.10148 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97e8cdbe-a84f-3dd4-aa3c-0ad33b2e079f | -3.67195 | -55.94852 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3fc5797c-1a60-3eab-8e04-c4b88af1ee07 | -2.1345 | -56.70403 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb1a8cd5-f464-3aac-8650-4dbfe0da8ac5 | -3.46096 | -54.59435 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40352a8b-0ed4-350a-b2e7-5dba7f223c72 | -5.95114 | -41.37586 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b728ecb8-4738-3a8b-b5fd-db377c9f8a5e | -3.02394 | -53.89629 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 2cdd3e83-6d24-3002-b758-bd6e507a3784 | -3.06536 | -54.25159 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 270ba567-38ff-3130-8476-4fbfeab4f161 | -3.87879 | -55.81118 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3facc170-b89c-3979-b54d-6a32a8185b1a | -3.51409 | -54.63535 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd7fe710-39b7-3a7f-adaa-7463035c3ed2 | -3.09235 | -53.72017 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 80c3998b-1e69-37d8-a940-a67aaaafd27c | -3.79922 | -50.60986 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f16719e7-cca7-32b2-842f-eb0ad71cc35b | -2.77797 | -54.11193 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad8c3d67-b984-3a5d-b6b3-10ec32c7e693 | -3.13805 | -53.71881 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83c90b8a-b283-3749-8bfc-92b23941c552 | -3.27811 | -50.40507 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9035fb0b-931b-3b1d-867e-910b755a527d | -3.16031 | -50.43847 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 827c2ba6-b046-3881-aa3d-8a0c16b7ab84 | -2.77804 | -54.11031 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cff35771-75de-393f-a934-24e47462f672 | -2.7788 | -54.10563 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb9b4c68-ec7a-3a75-83a5-1a2b0489dbe4 | 1.03832 | -50.02456 | 2026-10-06 04:38:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ef4b48d-2399-3375-85ff-21f82a07bf02 | -4.33673 | -50.40667 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30b9b63e-cee1-303c-b32d-30952f6269d0 | -5.60572 | -44.03124 | 2026-10-06 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfbb9540-4b2b-3f27-9a4d-57380bb1f490 | -3.37584 | -58.19208 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 453a37fa-3693-34fd-bcbb-c95c53934fe6 | -3.08823 | -54.1684 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab7775dd-df34-3442-9415-eb253499ae35 | -3.22 | -53.8791 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69a777f8-dae9-3f79-9f21-dfde69818983 | -3.05474 | -54.17233 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b5cdcd8-d572-38db-b188-91bfd9102aa8 | -3.2752 | -50.40038 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50da0a9d-3493-3b97-bc42-51a64ec81bf6 | -2.80152 | -54.13982 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c4fafa3-4e1b-3a7f-8f38-dfa5ae4e815c | -5.41206 | -44.35266 | 2026-10-06 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c018c4b3-ca3d-39df-b21d-052735e2dae9 | -3.1262 | -53.70791 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d72a747e-820a-3e25-b14e-99f27f5352af | -2.90433 | -54.08717 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d39d17a-46d3-3ecf-af9b-6fb6b8257258 | -3.04784 | -54.21443 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8f11295-6d05-3504-a6ff-632e7cf0aec0 | -3.07303 | -54.17533 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33c92192-e2b7-3394-ae4a-d234a0c71cda | -3.7331 | -48.87345 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| adb983be-85e9-34be-88d2-2893d94f1901 | -2.78333 | -54.108 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8c16c1f-1c01-37ee-bc4c-9f139f0b287a | -2.77649 | -54.09079 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 493dd129-f941-36fc-aa15-9ff4d7224be2 | -4.4204 | -50.44805 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cf2dc20-5c4c-374e-9d6b-a4a47acef0b8 | -2.85197 | -51.29753 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab1cc37e-25f2-3df0-ba75-a070b0629fba | -3.14726 | -50.44149 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64f11890-4a6c-3143-86c7-d18da54511c1 | -3.84103 | -50.99294 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c85e0bb3-f0f0-3e2b-b1ff-0ffd437c6260 | -5.67426 | -42.58931 | 2026-10-06 04:38:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README44.md)
