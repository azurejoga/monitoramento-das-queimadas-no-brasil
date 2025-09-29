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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82bd00ef-e44c-3d47-bfd8-1b41ae0c6d5d | -10.26801 | -48.07189 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9501127c-67c6-3ce8-a7a7-328861208f8a | -8.85497 | -47.85916 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f6b72b4-6b3d-3faa-b2bf-146bd9ffdffd | -8.27955 | -45.48785 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c016529b-c5c1-308d-a020-a800d603f401 | -11.42762 | -44.91362 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5777f031-b0df-3664-9485-86fd12eb5c78 | -9.79868 | -46.94427 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbd19b03-af59-3db6-8129-6f9e7c26340b | -6.89148 | -44.5341 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67aae004-2b79-3208-bfe1-5964bf7b95aa | -7.89579 | -44.59971 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b4e0fd7-c47a-361d-be6a-f83adc6acbd5 | -7.23003 | -44.78245 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0a07044f-5d03-3b4d-9e0c-4ca9dcba4c9d | -5.84752 | -45.94928 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a6bc252-6ddf-3a98-8989-64655f627f96 | -7.75508 | -47.00313 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8c94190-d587-3e54-9b79-6288feaadee0 | -3.4868 | -51.60358 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0b84e87-ba76-3975-baa2-68790fa217d6 | -6.76217 | -45.61911 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5cc641a-439d-3bed-ad0e-3458855bae57 | -7.24787 | -43.0061 | 2025-09-29 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f9495ae3-3349-3f82-91e1-a61fe502f3b4 | -11.36177 | -45.06308 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6c582f0-ea85-35b4-826f-e02c1320f8e0 | -7.58719 | -44.80534 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 824fddb4-c974-358a-acc0-0e6c8ae0c0ff | -9.86936 | -47.7358 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1142bc9a-6979-3cc2-a97b-2931c65c6913 | -10.39735 | -48.15283 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d961b3b-1b74-3089-85a8-c8e79ad49923 | -5.34937 | -43.68677 | 2025-09-29 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1580913c-e3a8-36a8-b0d2-9c5205d88151 | -9.31748 | -45.69096 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f6a122b-98ff-38d5-bd6d-3116cc2fd0f3 | -11.42119 | -44.91327 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 68b867bc-5170-3a2f-bd31-127265919b2a | -9.05813 | -46.71026 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d015a36-b928-34cd-b7ae-f81f3c7a23f6 | -9.30825 | -45.72058 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c458bfb-30c2-35f7-b449-7263d5c9188b | -7.90662 | -49.19948 | 2025-09-29 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa927c5a-06cf-37fc-9f17-fd5b5c3e4543 | -9.46068 | -45.49324 | 2025-09-29 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c9c4137-062f-3e99-a361-95785d092607 | -4.58003 | -50.16439 | 2025-09-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f8532b6-604e-3cbb-9a90-a5316e25252e | -10.82383 | -47.9427 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c6a0519-8632-3a73-92b9-46a3d58c99a7 | -7.54895 | -46.10776 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 630118e3-27db-36b3-b06a-53830cbf2736 | -3.33546 | -50.24767 | 2025-09-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4f0fadd-dab9-3a18-9616-9812ce4b6226 | -9.75901 | -47.78951 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 076e0d33-3c85-3668-bc3a-0761b0db8bad | -6.68882 | -42.78093 | 2025-09-29 04:57:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 351a3027-eaeb-30ff-a5f3-d8587998787c | -3.84322 | -48.96023 | 2025-09-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dc483d8-131b-3d0d-9a24-b5e5152d54ca | -9.3149 | -45.71111 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af396da2-46ba-3ab5-bf95-4bc6f0d06a91 | -8.91418 | -46.08429 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1de79fb-9acd-39f1-b1eb-da07ac473fba | -8.86568 | -46.61898 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a6f7f4b7-73e0-35be-ba12-95fae08fb74f | -5.82463 | -42.79442 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0965abba-f0ee-32ab-8cd3-f8db86d85838 | -8.85896 | -46.58928 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37b1281d-b1d4-39ca-b5ce-17deb67caf8f | -7.7503 | -47.00241 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00f44d3a-ff81-3867-95f9-de09035302c8 | -9.92411 | -48.80157 | 2025-09-29 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 902cd213-ffa1-3d9b-963f-c6e723cb1d0c | -4.40305 | -44.0836 | 2025-09-29 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5500b5cf-416a-3ff1-903d-cd6a03a8bdbd | -11.36691 | -45.06869 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4979cb67-5ea5-3107-9963-7f7022e42e00 | -9.4096 | -54.7019 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6a80369-1da0-397e-9946-b1ebc28ded60 | -8.30332 | -45.51394 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 4f034acf-023a-3da7-9477-fc52484cc7c9 | -9.91295 | -54.87862 | 2025-09-29 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9bf2267-3c88-32d0-ac27-ec52e713531e | -5.81987 | -42.827 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e9748915-9f34-371b-9133-bc5cc7f4616e | -3.36591 | -49.75327 | 2025-09-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d044fc17-1832-3f91-8190-1ad6a1170737 | -7.54935 | -46.10482 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12290f8d-6506-30ff-bd15-f3e73f1f521c | -6.6164 | -44.93684 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edd055c1-9574-302d-b777-3b1af4e1e49a | -10.79646 | -46.68578 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69b1b7f6-bb45-39a7-9013-41107fac5802 | -8.8844 | -45.03235 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5948590f-e621-3db4-931a-ce82e73ef180 | -7.81205 | -46.90942 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 482a8ab8-61c7-3f6d-b77f-8db83db59fc3 | -9.36095 | -51.48492 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b94e2c5-d985-3bc3-907f-4c7cade88e64 | -8.28386 | -45.49656 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5505b3d9-d078-3d8e-92c7-b13dea10d420 | -10.28514 | -45.19548 | 2025-09-29 04:57:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93226794-b238-3a15-a31d-d422fcdc1831 | -9.41922 | -54.71044 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0596ed5a-6fb1-35e3-822b-d0d958bc8775 | -11.27334 | -47.19139 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 78a5203e-88b0-328e-b7a3-1afd0ae87b95 | -9.77199 | -46.1969 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae7350cd-51f4-339f-b9ca-a9c01211ac47 | -9.28149 | -45.7312 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e8943a8a-1a42-3a08-8fa1-ab6a82d7f4fd | -9.30783 | -45.72387 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51a85162-c336-3001-af0d-25b8965c572b | -9.47019 | -45.50526 | 2025-09-29 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5229ce0b-90ab-347e-a6ee-79bcce21f061 | -11.48818 | -43.21578 | 2025-09-29 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2f2aa202-24c2-34a7-a569-4d55f5eec31a | -11.5118 | -44.85117 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f57c036-1813-3852-b376-c85e69c8306f | -9.40685 | -54.69791 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e893833d-0df9-392e-9f8d-0b81d0c331ec | -8.81317 | -46.19913 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a761b6f-3624-3c27-a38a-b83690193ebe | -7.93767 | -45.68567 | 2025-09-29 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 632e7bfd-26ae-33fb-a605-ff425ddf64de | -6.30695 | -43.4462 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ce6923e-d6e8-3bc8-bea7-72eb853bac38 | -9.41646 | -54.70645 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6613fae-241c-3ea3-ab2c-032930ca231d | -6.61237 | -44.94055 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 465bc5b8-eceb-3811-b14b-6b83f825edc4 | -10.40702 | -48.11515 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e51b223e-f499-3e6b-a54b-3ee6986bd78a | -3.33182 | -50.24712 | 2025-09-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f25239dd-99b7-3df4-bdd1-a763f175ad5d | -7.21802 | -44.78801 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e19166f-e136-36a3-ba01-47bafe3031df | -6.83493 | -44.82728 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a31d327-927e-3b26-9c4e-d83ecd497eeb | -8.66034 | -50.09027 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 810f4771-912d-3305-b530-6fb1637744b2 | -7.81941 | -46.99685 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c3f5db9-89b0-3758-96c4-0bf64b9e4117 | -9.54355 | -51.36185 | 2025-09-29 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06401457-629a-3ce4-974d-8d6a4e1e24ab | -9.41809 | -54.69603 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba963291-bbda-3b5f-84f6-5c8887ff8c3d | -10.48407 | -49.37033 | 2025-09-29 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8e5e232-56ab-3e77-8dae-049cf456a0a8 | -10.39679 | -48.15701 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1f64c21e-c399-32fa-93b2-9bdd31c360fb | -5.02626 | -42.53882 | 2025-09-29 04:57:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce5bdf93-6e9d-3a02-9f8e-aacf60d5135d | -10.32945 | -48.20408 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09501345-a613-3b44-8c9f-e7127cec3d5d | -10.80744 | -46.68124 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c13c2680-dfe9-37f8-9dce-4d0aaa0e5324 | -5.48895 | -46.97111 | 2025-09-29 04:57:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d453cf94-acc6-3c0f-8bff-2ec20e416ec0 | -10.40135 | -48.1579 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f9319cdd-10f7-347e-a707-4f039c7bf7a5 | -7.47602 | -47.39947 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fddc0071-eaf8-37ce-a723-c9fa968b4b2b | -10.62164 | -48.533 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38dbdc6c-2e41-3670-ac7a-ed59ecba65b7 | -6.74978 | -44.75454 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6d7e74f-e9b9-3332-8997-efc3ebc6b3c5 | -6.28027 | -42.48374 | 2025-09-29 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3b2fe605-f1d7-3824-91d1-0df7acc57aef | -9.40301 | -54.70086 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2125b56d-6d59-362b-a5a0-df6532e1c004 | -8.1539 | -46.3983 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 71a12b7d-301b-3f20-982f-5da35fcecd71 | -9.749 | -47.79313 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2133174-3e90-3890-b5c2-5630686cf2b5 | -8.71887 | -50.04335 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04ab1477-7520-3db1-b615-d9d95ea92de7 | -9.41862 | -54.69255 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4325d62-2351-3196-bfc0-bda3eb538478 | -4.3471 | -48.3541 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dff5c23-1a27-3442-9510-afa2b18fb8b0 | -8.29889 | -45.50639 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8394d5fa-2278-3da4-9f7a-3b7e651d1639 | -7.90208 | -44.59561 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35dcd437-bee9-37c4-8159-74451e58fec1 | -9.31532 | -45.70778 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d93b885-a2a6-3109-aac8-442e631c36d9 | -6.89259 | -44.53603 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 530fa40e-3129-3b6d-b9d4-11749621268a | -5.15216 | -46.07721 | 2025-09-29 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf1927f2-00b0-34fd-8560-d03c29631477 | -7.31693 | -44.72079 | 2025-09-29 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b31ca0fe-238c-3794-b8f7-41487036502d | -9.9999 | -45.40702 | 2025-09-29 04:57:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13c8f19a-5f50-3e63-b513-47dd269ce5de | -9.41236 | -54.70589 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README57.md)
