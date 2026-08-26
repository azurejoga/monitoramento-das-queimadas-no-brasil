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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fe0e19b-6404-3701-8efc-ff1d85db9ece | -13.28882 | -51.50615 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7334aa9-28a9-3960-89c3-fad5bea806f7 | -10.9866 | -60.79002 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40536d5c-8524-33e2-becb-91fbe2763cd9 | -10.77078 | -54.03012 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 535e52f0-5781-370b-8fe3-538871cddea8 | -10.76469 | -53.98249 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a28044c-1821-3fb6-aded-33732b651cbf | -10.98652 | -60.78748 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4657b8d2-b271-32a2-9874-4a0a95488670 | -9.09301 | -59.40233 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03a2d4fd-d0bb-345c-96a1-0011a0f3d450 | -15.67893 | -53.8938 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d9829b7-eeeb-3758-ad9f-7331f99d299f | -12.35206 | -51.21216 | 2026-08-26 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4a9ebd4-04f5-3588-97ad-5ba3301b45e1 | -13.86345 | -54.07991 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8339838a-c604-3e70-a6a9-52b7288db860 | -13.29169 | -51.46058 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c6b2f8a1-995e-3a46-871e-8ef363ba85fe | -10.31204 | -50.40193 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca4cfd66-9c67-39ac-acf0-15fdc063eb44 | -12.02804 | -46.0104 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 525f3c57-c652-31b8-bc53-d223911eaef1 | -10.94151 | -49.59312 | 2026-08-26 04:53:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 382e6e19-4d1a-3689-9e0b-24a4b1165371 | -12.00493 | -45.99583 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93c6ebaa-8479-3b5e-b07e-46716f271c5b | -13.65915 | -51.84744 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 43324878-0b5a-35ff-8ece-6336f49b0041 | -8.26067 | -63.9921 | 2026-08-26 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6bb3502-ab48-34c7-acd8-f3c3c29c1335 | -9.66999 | -55.09777 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e59e81c-b69b-3547-9b37-58c38568665f | -11.19363 | -54.00137 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 151c3ef0-2c20-335c-bb91-1d2d9ca8dd30 | -12.17253 | -50.60786 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 906a9a09-e646-3751-a47c-f31dd1be85be | -12.67653 | -48.42146 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 083b08aa-f72c-3bb5-b4e1-37e3a2000545 | -13.38485 | -48.21797 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f9b470a-2764-3d24-85fe-39da0cb5f531 | -13.16451 | -51.3435 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca3eda76-8b73-395b-aebc-2ea53d3fbbd7 | -11.80198 | -47.24267 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b9b9c09-cb40-3f28-9dd1-c1b34f7ffd4d | -13.20079 | -51.36419 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8c248d8-f49d-3acb-84d7-1cf707357d20 | -12.76606 | -46.45424 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e37ea434-c5eb-369d-ae08-1cbb1ddd9270 | -13.19366 | -51.3631 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acd48fa0-b6cb-3e37-9f53-50e9157115ee | -12.688 | -48.39984 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae643c25-cb5e-3ebd-9b7f-d0884cb97f7b | -9.16941 | -58.33503 | 2026-08-26 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ced6a9b-5e31-378a-9d41-30e1df3dc02e | -9.48403 | -56.92319 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 088d2414-a751-38e2-9eae-3588d73b89cf | -11.80709 | -47.67178 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 979c53b9-f4a3-3c8d-a288-26a6863da0f7 | -12.69954 | -48.40971 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a5cf1257-0dc5-360a-8dad-6903e471ead2 | -13.19601 | -51.34657 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94f2a511-7338-3328-8085-41203a1feada | -13.28231 | -51.50099 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fe0b746-7a5e-30bf-9def-3fbd17fea49d | -14.36594 | -51.75429 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db709c0d-63cd-3b45-90c4-10e817226b56 | -13.36867 | -48.20781 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebfff4a3-e29c-3956-a38b-04bdcb78044c | -12.75945 | -44.26443 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 803b71a5-a6d0-37a3-b66b-bc7ab1df0996 | -13.65622 | -51.8429 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3b53a2a0-01cd-3019-8ef2-f591a46c292d | -13.61435 | -49.00829 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a22640e-1ac9-3111-94a8-8cb1afbe13e0 | -9.65657 | -55.07304 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b6282cd-bb12-3967-bceb-2c196b5834ef | -11.72147 | -47.76992 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5caa63a1-7148-34f6-bc56-8e054bf6f61f | -13.26653 | -51.46245 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a95d19b-99ee-3a78-a776-ad038fc4417c | -9.27735 | -60.9204 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f0479e4-9b93-3e12-b69a-7e1ec4e7321d | -13.30648 | -51.45865 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d17cddc0-297a-3496-a7cf-43d140f0614c | -13.19957 | -51.34711 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01309638-7a08-3b7e-bb62-fc74499f7083 | -11.0161 | -45.07403 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 87c770af-89ce-3df4-8777-e6fb616d409b | -13.43032 | -51.84835 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2352aa09-36b3-3937-bfb6-56d453296fe6 | -9.29244 | -60.91799 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce8dc6df-d14b-3a7e-aac8-4b8ca62d5c42 | -10.76745 | -53.98652 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f0a6984-baab-3aea-b941-b993e4d62a7e | -13.6505 | -51.85102 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 37349026-f119-3aa4-92cd-a56a952315da | -8.81926 | -62.31598 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2ea6019-45d6-3252-8ba4-74012d6fe7a6 | -14.53642 | -52.00151 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0eb6baae-65f5-3648-b152-81c70dae5713 | -12.22172 | -54.23273 | 2026-08-26 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9b105c7-5c2c-3892-9dd6-ca218ab108be | -11.76667 | -54.53067 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc51403a-220a-3669-afa6-ce5026a866a6 | -14.32576 | -51.73137 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b91f91a5-5844-3f80-a72f-b1de2cc7e347 | -13.35213 | -48.23347 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08d96f16-aa59-319f-93be-691c6b461f27 | -14.32222 | -51.73082 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a332c851-44f0-32e0-997f-b40d6bce1e37 | -13.24294 | -51.37481 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| b82624a2-1cb7-3dbc-bb40-fc496771fbbb | -11.15835 | -54.01007 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0add3463-86a4-3b64-ae56-0396ec564269 | -14.41503 | -52.90502 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 409da6b8-c329-3d23-8606-3b0b8da0d2e5 | -15.68227 | -53.89435 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 177634c8-2832-35ca-8bce-e499f80a4f1b | -12.68327 | -48.40314 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 402dd752-db8b-357d-a0c2-015b1bfd724c | -9.92749 | -53.63989 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d9f92a4-6042-33c0-87e3-20b90a5c7f31 | -13.26131 | -51.39868 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc6a7146-b6ed-3e3e-abf1-0dde171396b0 | -10.06893 | -60.50334 | 2026-08-26 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| faa51eaf-16be-3265-b4e5-e3694640d33c | -11.97149 | -45.88794 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04011fd3-6d18-3aec-a729-766837c1b028 | -8.81459 | -62.31186 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5eaa178a-aeaa-37b9-b6e8-619499d3935c | -11.42459 | -44.54623 | 2026-08-26 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a1b59233-4530-3116-a891-5a193c670033 | -13.25755 | -51.5237 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58f06cbc-2383-3d3a-948b-bd1ba4940a97 | -12.66438 | -48.41621 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77403eea-1339-3ced-af6c-1d7a00ea992d | -14.78988 | -48.79945 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe51a7a2-18ce-3f37-8d64-a66a3f00e8de | -15.87934 | -48.34093 | 2026-08-26 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bff20cc9-b062-3c4d-a740-33341430e8be | -13.33555 | -48.22636 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bddaaaa7-5977-38a8-baca-21ca10db5a28 | -14.44357 | -53.08475 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0ab8837-db9d-3911-8eb2-ef3c9c842408 | -13.18649 | -51.34261 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fd200f1f-1c86-3b6a-bf9a-f8315f1b1d87 | -13.29524 | -51.46112 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 86fc03da-66df-3f00-a4fb-d1e6dc5c1696 | -14.79361 | -48.80378 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b03fa14-7685-3c1c-926a-e6097f25ba8b | -11.18646 | -54.00381 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cff4672b-082a-3c5b-a136-b3abcb667280 | -14.81668 | -48.79195 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01d733b7-281b-37b3-ae2b-a406f0323a80 | -13.86343 | -54.05812 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9554dce3-f006-310c-a8ae-334720cc0711 | -11.97246 | -45.89375 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e0fab92-efe8-336a-9537-4161905a2900 | -10.43213 | -61.21881 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfc61d16-5861-35f2-8738-5f38ee9e3149 | -14.84017 | -45.52501 | 2026-08-26 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01bea504-d3e1-3210-b038-287346a3deea | -15.36048 | -53.7984 | 2026-08-26 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e67c0693-b75e-3d57-916b-db6a9caaa994 | -12.13023 | -43.38184 | 2026-08-26 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d86387e4-9cec-39f2-96af-da23c45f21ab | -12.67855 | -48.40638 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 12bc7502-348b-3776-9441-bd1d4789b0d8 | -10.26542 | -50.38323 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd9ec7d4-b3ae-3669-b764-159d59da423d | -9.60769 | -55.11781 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17588a75-2fb0-3368-ad05-8839c35539c4 | -9.97501 | -53.94427 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57fc8a43-1a4e-372e-9f94-aefa37ea5e41 | -11.76723 | -54.52714 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e76da4c5-c985-3bc6-8f97-fb4dd51f88c0 | -12.73514 | -48.37115 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 869815de-486f-374f-a83e-539c734582d9 | -10.35838 | -53.88425 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e10c007-5653-3f9a-ac40-3f678bae7832 | -10.76635 | -53.99352 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3001f15-71cf-3632-b9db-f242aa58db3d | -10.41985 | -57.23584 | 2026-08-26 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad973a7c-722e-3856-a72a-0a65ff5aeb51 | -14.3195 | -51.72692 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b8bd921d-93bb-37c5-8317-0eefd3ca70fd | -13.60669 | -49.00322 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8214bff3-8ae5-3d85-a61b-811c082da753 | -10.75533 | -54.02047 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4e697bbd-400c-3eae-a184-68975448a53f | -12.43397 | -51.17414 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0abbb56e-acd2-3a26-800d-66119e50a1b0 | -13.24222 | -51.52968 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab317532-1b36-3dac-b776-fc9fd5c4e22d | -15.76454 | -43.37539 | 2026-08-26 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5aab65d5-1cb0-3924-bd6b-42cf5735e189 | -10.75312 | -54.01294 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README46.md)
