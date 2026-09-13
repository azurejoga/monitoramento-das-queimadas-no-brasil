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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12fe640e-6cbb-3607-94c1-bba90407a49f | -2.6658 | -57.505798 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb7c5683-15f5-3a74-a2d3-39b30d321765 | -6.96 | -59.742599 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07f3e66b-c08b-39f4-8089-72d1e2bd2137 | -10.9381 | -57.176201 | 2026-09-13 00:43:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab34a086-4a55-32f3-8126-e2815f210f04 | -9.704 | -54.352001 | 2026-09-13 00:43:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1640244-c187-321e-acc7-a3345954b29d | -10.6855 | -54.1357 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 889a81fe-6fe2-314f-bb44-4659fd889d6a | -3.7323 | -61.7383 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2b50a8c-e1ed-3e2f-a7a3-e32645e6597f | -6.5616 | -51.0737 | 2026-09-13 00:43:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1054eae8-e03b-30ea-8aaa-f26bf729531d | -8.0349 | -54.848598 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c98443e-b8d0-3f68-9255-e020663c96cd | -3.5941 | -59.055401 | 2026-09-13 00:43:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 422c885c-fb53-3ad2-88c5-5e112eac90e5 | -10.5314 | -51.3764 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf46a7de-b975-3def-8932-b1dc13af3da1 | -6.1264 | -57.676701 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2b497c1-8a2f-356a-a478-19b17aeba58d | -6.2899 | -59.920601 | 2026-09-13 00:43:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be6a6a32-67f8-3d8f-8b56-fa72bdd7e602 | -10.5148 | -57.447498 | 2026-09-13 00:43:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 994a1889-5dcc-37c4-9fa2-a69d6514c9f3 | -6.074 | -57.855 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2ce325-3b2c-3c7e-b2a8-f85ac3b5e2a5 | -8.1134 | -54.7873 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 592e28d4-13a5-3438-aaff-27a5df39a152 | -3.6405 | -58.622101 | 2026-09-13 00:43:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 828f91c5-77a1-3438-b5a7-8dd238a04d6a | -6.8289 | -58.645699 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19e0f8ce-3afc-3fd5-956e-d2d3405510cd | -12.6686 | -54.717499 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de7714a0-d14e-368d-975f-0328a7be46b9 | -9.3964 | -50.076401 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78275812-8bc9-3955-8151-47eae15e8759 | -3.9589 | -59.348499 | 2026-09-13 00:43:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09377174-9f1c-3185-94ec-e715fa815fc6 | -6.104 | -57.623699 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec4717f0-7440-39d3-927f-0ffb3c023ff1 | -8.5757 | -54.557499 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfcf219a-0dc5-3b80-af44-4ff4f96b4ce7 | -6.128 | -57.683601 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3c1697-4772-333f-abc0-1e70d55b2c5d | -6.8635 | -55.579498 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09cf7ab0-5cee-3c10-b23e-a0cc818c7049 | -6.7445 | -59.420601 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 136ba9cf-743b-3ff0-a3e1-39987d79d6fe | -6.8273 | -58.638699 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1c5bd71-4d23-352f-b65d-627730b533fc | -12.6501 | -54.6819 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09cd5871-a492-36f7-b29b-ea4a6bfddb3f | -2.6723 | -57.534302 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0b5a181-7760-3257-8fa0-bf036f9f2c1b | -9.377 | -50.081299 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f0e331-68c7-3b5f-b7ac-5907fc6331e1 | -6.1087 | -57.644402 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29355e47-fe2c-3f84-91d7-f7ea09aeb3bc | -6.1988 | -57.7691 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7255e29-e3e2-3e3b-8d5c-6afcc9bd4f0b | -6.673 | -58.869301 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0be7c4e9-9644-3887-9c07-e47e0a056b5c | -7.8618 | -54.6814 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f43cba-a612-3b8a-8822-48f651e95b87 | -11.521 | -54.619701 | 2026-09-13 00:43:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f744c964-cf7d-33f9-8077-04d05e2fdb16 | -5.8099 | -53.7994 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f940ffd-e7f4-3832-b746-7792e8fce473 | -1.458 | -52.955601 | 2026-09-13 00:43:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86274cd6-e4ad-35b0-af6c-13dcb04f5c3c | -6.0875 | -57.641998 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff80a56-fbcc-3ff3-8356-15ac9413498c | -6.1848 | -57.7071 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d0a3ae-fd60-3fd8-a52c-e4940bf14799 | -3.8654 | -51.183899 | 2026-09-13 00:43:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af8dbbe-9e8d-35bf-bf0c-6b70ec854ff9 | -5.8002 | -53.801701 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e278eb79-2fcf-3c80-8e85-e70105b19075 | -9.7021 | -54.3438 | 2026-09-13 00:43:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 886dfc9a-d7d9-3670-942b-87dfbf4f7bfb | -8.5281 | -54.707298 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3047083-9e7e-3448-bf82-a23b1c523099 | -13.5394 | -49.469601 | 2026-09-13 00:43:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 94852d10-73bb-3cd6-9cb6-0aed66b5e2b9 | -9.7158 | -54.358002 | 2026-09-13 00:43:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e861e19a-e632-3c32-b380-c02582fc85b9 | -3.7305 | -61.730202 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee687783-15a4-364e-9b27-e0a68a3f51d5 | -7.854 | -54.692001 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ea34c9-7537-3169-b0a3-01a6a0f9afec | -8.1115 | -54.779099 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef55407-12a4-307c-a4e1-c5ce7d3adbbb | -2.6707 | -57.527199 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d65e4523-5279-3a30-be67-da959071b7c6 | -3.4498 | -59.512001 | 2026-09-13 00:43:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beaa525b-f75e-3bd6-9930-e4b8e1996779 | -9.3904 | -50.093899 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b0c6a3-d4c7-352d-9f11-e8f1c4a382ad | -3.5642 | -53.001598 | 2026-09-13 00:43:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6920915-ae4a-3908-bdc2-89423274a708 | -10.968 | -58.943199 | 2026-09-13 00:43:00 | METOP-B | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75b2d39c-1b5d-35b5-ae9c-0ec242d4efe5 | -5.7806 | -53.806301 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94273fb4-1610-3a2a-acb0-9794e288d211 | -5.9624 | -57.771599 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44448090-1d78-30e4-ac31-bccacbd1cf02 | -12.1461 | -48.9492 | 2026-09-13 00:43:00 | METOP-B | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 579bb223-f173-3fdf-b92f-094cf294917f | -5.7904 | -53.804001 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c74f9e7c-ff18-37ce-9707-845cee978da6 | -2.9357 | -50.3745 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc7812b-bdac-3319-8180-ca743806f1c0 | -3.895 | -60.577499 | 2026-09-13 00:43:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 751c1dd4-87b4-3107-819d-8adcc90080fc | -6.2235 | -51.677799 | 2026-09-13 00:43:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21d50d3d-7422-3725-9237-c38f5341ddcc | -9.7119 | -54.341499 | 2026-09-13 00:43:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d98e342c-2255-3937-9390-824bd50717d3 | -6.086 | -57.635101 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe55e675-ab6b-3bd2-9120-9d659050b4ad | -16.2836 | -53.831902 | 2026-09-13 00:43:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34760127-2632-3a0f-aa3e-98e962ffdd5f | -2.9303 | -50.395 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e39782-f5aa-38ef-a528-f63c04bd02c9 | -2.9443 | -50.4109 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d168cb6-260a-3444-8513-612760bdc37c | -7.8598 | -54.716801 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba314ac-e93c-367b-a267-9191e97e0479 | -12.6819 | -54.730301 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dffe0c1b-37b8-33ab-bcb0-71a89753d2bd | -3.1706 | -58.640701 | 2026-09-13 00:43:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d6f926b-956d-34b2-a678-421095c4aeff | -6.1378 | -57.6814 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8a18d85-80d4-350a-a3a0-f12610906bdb | -10.2496 | -57.6898 | 2026-09-13 00:43:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bddd044-59ea-3fe6-a779-ce99bbdff95a | -13.3368 | -51.7798 | 2026-09-13 00:43:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85c7135e-8c6f-38c0-a1a5-1a5063548d89 | -1.728 | -57.1427 | 2026-09-13 00:43:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a241c8dc-a826-30f2-8be7-7bf5a51e92c0 | -6.102 | -57.6605 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7429f29e-a558-3cc3-9b9b-13a9e6c60bee | -6.8363 | -55.819698 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9698c928-fd3a-393b-b7e8-b6f44897b287 | -6.9584 | -59.735298 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8d2fe0b-d1ac-35b3-9e2a-750b3fde97b0 | -10.5742 | -51.3405 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae7fedd1-efa4-35c2-b707-8461b1cea286 | -13.4059 | -57.0243 | 2026-09-13 00:43:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59d822eb-af4c-38a8-8f7c-e93923418080 | -8.5398 | -54.7132 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97e410c5-46cd-3ae4-9c57-d46a5ef9d985 | -8.0544 | -54.844002 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad16508-f715-3da9-b8d2-045054eed831 | -2.6095 | -54.7397 | 2026-09-13 00:43:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55ab6b0f-4fd3-3e52-8dee-6e80b5f3bb58 | -3.7421 | -61.736099 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3ed3132-3e42-35bc-b7cf-5c4ae786698e | -6.162 | -57.697701 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfe39f00-0604-32eb-b353-177f41d66cdd | -3.8617 | -51.1684 | 2026-09-13 00:43:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caf9e084-3758-3371-b698-598002c12862 | -3.1802 | -61.108002 | 2026-09-13 00:43:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d39cd5e2-c0c3-3a8a-965f-907efc840a8f | -3.3937 | -48.8666 | 2026-09-13 00:43:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8517ba6-eb95-338c-ae28-a586778c7bfa | -6.1476 | -57.679199 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a04e8ac5-b8ab-3a32-847c-56b5c51a4749 | -12.6703 | -54.725101 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3e61564-e97b-3784-b1f6-419006779324 | -12.1364 | -48.951801 | 2026-09-13 00:43:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db8160d1-687d-3d26-99b4-fefae09a2ddb | -6.6033 | -58.8339 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 095dee00-c605-3539-9891-4a9701e68be3 | -6.7317 | -55.6343 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f60e5e1-a2df-31d9-972b-7c33eae8a182 | -6.7762 | -48.638199 | 2026-09-13 00:43:00 | METOP-B | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1f3392-b691-3fe0-b3ee-027317237f43 | -3.1115 | -61.1231 | 2026-09-13 00:43:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bebef235-be05-3bb6-9da0-55e68f7a3f98 | -6.1295 | -57.690498 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 731bfa00-560d-39f8-a569-2e566ed83019 | -13.5491 | -49.466999 | 2026-09-13 00:43:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e82aae95-c5d0-38a5-a26b-5fbc0644cd0e | -9.4075 | -50.121399 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be3f2df5-6d70-37e7-b76c-a88f249ea1bf | -3.4483 | -59.5051 | 2026-09-13 00:43:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0fdaa62-3c90-3983-a27a-271afbaa67d1 | -8.1172 | -54.8036 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad61c0fc-6f77-345e-a2d5-16a0fee25725 | -2.9681 | -57.2038 | 2026-09-13 00:43:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66c04468-c96b-309f-8aa6-4a6afa2e6fa0 | -2.6675 | -57.512901 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 514f2260-4323-3621-ab4e-9ee17c725424 | -9.4588 | -59.183998 | 2026-09-13 00:43:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98cdd17a-d5a0-3ba7-9f1a-293d42e2a69d | -15.5691 | -53.778999 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
