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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0862e372-e816-37f7-8330-ec2f468dc6f6 | -11.89516 | -50.50361 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a830f9db-212d-32b3-b448-f8b3cab73fd9 | -10.81944 | -57.19316 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0325c8c8-a686-38c6-b5ad-3393b99e67c5 | -11.96985 | -50.57986 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bebd87ab-e3da-31f3-aa87-e3349336c199 | -11.27384 | -54.43732 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b9adca2-31fc-30ec-b87c-df76106498cb | -12.0233 | -50.59472 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 1d75351b-eb33-3044-ab66-b77a9004ac99 | -6.90474 | -59.84577 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 958f80b7-a3a2-3b06-b9bd-eb218f2b68a4 | -10.60967 | -53.99796 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38cda066-84d1-3269-96fe-0c98da2fb994 | -12.13958 | -50.32693 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 442e329a-c689-3ce1-b18f-5f4dbd54ffc8 | -11.05526 | -54.19173 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c760c041-a14f-3daf-9be4-330bffaa3dce | -10.40752 | -53.81322 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7fa3cc01-ed8c-3bcd-9bac-54e094cee155 | -11.96199 | -50.50866 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a47716b5-9702-3ba6-b230-1edd6f03ffb4 | -10.4173 | -53.80615 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc80cec5-5b4a-30fa-b7fe-fed2b6325ea5 | -14.11802 | -46.32556 | 2026-09-27 05:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7523ae95-beec-305d-a764-40b5b931a13c | -11.8769 | -50.5171 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d71e49d5-bf6e-3195-b571-21202fb15c74 | -10.81096 | -60.72425 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ffb5e9d-b9c6-3116-9f1e-8e4d698e357b | -11.9823 | -50.56349 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b15bf60b-c95f-3321-b057-cda4e4d8eeb4 | -11.03834 | -51.32853 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f545afa4-4c99-3b0d-8850-13de63cb4691 | -9.31208 | -47.62698 | 2026-09-27 05:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d91ebda-1959-3c31-9fcf-023e45ed271c | -12.66349 | -47.31195 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4adb6f30-acbd-349c-b247-9ac63cda1214 | -14.11723 | -46.33332 | 2026-09-27 05:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9000cc50-e939-3a5d-a8f6-15e8d48e93e2 | -11.88795 | -50.51852 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd2a1d57-8480-3882-9f62-1fa77892a858 | -9.98513 | -57.78136 | 2026-09-27 05:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3d04543-bc7f-3390-9487-99128a13ab86 | -12.67027 | -47.31308 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb84a9c2-6d34-30c3-9dec-ca7b5de387d6 | -11.04993 | -51.32063 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 281c3ce7-4371-3912-93e7-24dfab7efee3 | -10.41991 | -53.81923 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 310b2ccc-4a65-3f1e-8b60-706ba3117b07 | -11.23711 | -49.85223 | 2026-09-27 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bcfda08-40a6-3a56-80a2-46d58fd1e291 | -10.72615 | -53.99218 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a187e82c-7860-3f09-b9c5-9445367f5296 | -7.49636 | -55.02286 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 175107cd-6ae2-36f6-9fd7-e141e802701d | -11.2824 | -54.43739 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05d90ff6-b2d0-39c7-a231-c4ad4a520330 | -6.86747 | -59.89415 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e63c700-2aef-37c7-8ef0-7cd5574b8db2 | -12.65879 | -47.29226 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 311ee0f0-61b6-38b4-a48e-354ccce345d9 | -11.8102 | -50.51199 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f44182e3-3029-347c-bda8-77776d3af9f3 | -8.59295 | -54.64713 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7de67f55-2876-301a-a205-af705756b882 | -6.88003 | -55.55576 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e0f6cde-71c6-3f2e-a912-f0989ed44164 | -11.81661 | -50.50546 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bce208dc-ce6f-3c80-b3c7-2e94ec063dbc | -12.28343 | -50.29346 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b6451ef9-75c3-3443-a742-c0b09699d9dc | -10.25241 | -59.12706 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f95cdea9-ddcb-315b-8002-87fad636083d | -13.38202 | -51.31989 | 2026-09-27 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5cac2a4-d432-3f01-95d6-899958d6d6ea | -12.02926 | -50.59182 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| e48dfe28-af61-3c81-820f-acc1e9509bf1 | -12.25685 | -50.6926 | 2026-09-27 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a140f29-960f-39d2-b7fa-aa8092ecf865 | -11.27767 | -54.44068 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2a8995d2-1b72-3ab7-bea2-e7a8f2d9a7a6 | -10.22508 | -49.98241 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f8a62c7-8e69-3b61-9843-7942fd04c3a3 | -12.14004 | -50.32314 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a963299-2345-38b1-b52e-3eb567fcb845 | -11.28293 | -54.43348 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ff7b10c-0bdb-321e-b38c-557346cdb2e6 | -12.26233 | -50.69332 | 2026-09-27 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a79d9eee-63f0-3021-b36d-65be8c023d09 | -11.89347 | -50.51924 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cbf13e1-741d-30a6-bb0e-59cc20675e63 | -12.0297 | -50.58821 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c9ab388d-c2fb-3729-83c1-49cbddff4d39 | -9.39786 | -60.34145 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 890660ab-379c-361c-85cb-8f6963d76a84 | -9.31142 | -47.63231 | 2026-09-27 05:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1834228e-35b5-3d8a-8c25-a5535182c1c8 | -13.09871 | -47.41079 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a27c1f0-9741-358a-9fb1-49df1aa655c0 | -8.60225 | -63.92998 | 2026-09-27 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 23f27a9a-6827-3fe6-8e0b-ee1b99118cfa | -11.16328 | -62.86761 | 2026-09-27 05:29:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| af25790c-4319-31fe-9d9a-bc46e54ad315 | -12.2717 | -50.29581 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ca65400f-4ea9-3b3a-b47a-a6d3353a43a9 | -12.65809 | -47.29851 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ca71f2d-616c-3643-a679-b20094152d2d | -10.41183 | -53.81391 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e527ce16-eb03-3494-b130-6167198f1e3c | -12.24008 | -50.36889 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae81b620-958b-3f7a-960a-090fed19dd2e | -11.98317 | -50.56323 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9c744d49-f48d-3921-b8d9-6f98c2e9023d | -6.85404 | -59.9137 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c77c0827-fb55-3b66-8473-dfe27aafa206 | -11.94166 | -50.49114 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5c34e4f3-858b-3dde-ad3e-1764fbe196bc | -11.8934 | -50.5182 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f2dd319-aff8-3322-81e5-26fc7c16727e | -11.89946 | -50.51634 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72cde5cf-74e8-31f9-8b14-f9a1f7444143 | -10.81316 | -60.73192 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc45f0aa-055f-331a-806f-f853aa1c4f17 | -6.63953 | -59.9444 | 2026-09-27 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3738dbfe-a74a-3b19-8867-83fe6c8b0da9 | -11.01917 | -54.04301 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce1b0ef9-cfdc-31c2-a759-cd13d77bdb1b | -11.98899 | -57.59918 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb862516-9f41-3a85-b27b-29a4cf9c1cf9 | -11.94277 | -50.57263 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6ac9b99-be49-3767-ad6f-d2c1912acdb1 | -6.87236 | -55.58132 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5290778-f839-3997-9c03-9f21113eeb33 | -11.2744 | -54.43341 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0300f08-f117-3d22-9bb5-cf7d4eb3b156 | -11.77032 | -51.01057 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74ab2df0-c3cb-386e-99cb-2404e4000ddb | -12.23962 | -50.37267 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c81aa445-fe49-31ac-a926-366bcc8807c0 | -9.08101 | -66.10092 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8158295-54e1-33b6-b502-6a6d017a0f04 | -11.89472 | -50.50726 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cfd20e42-9d5f-373e-a317-c7d00efcbfd3 | -8.59618 | -54.65291 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5a388fdd-4ece-3809-8e15-319907f681ee | -11.98274 | -50.55986 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1bbfc5b1-4003-30d8-bde4-03f4e92d4fc9 | -6.86356 | -59.89714 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3368d5c1-a577-3aee-8c9b-ea846c5e89f6 | -12.13577 | -50.32764 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 519d5ed4-cfab-326a-84c6-df85de08e6e3 | -12.05083 | -50.59833 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c40506e-7c9a-3a04-b809-8a081b40602a | -11.88788 | -50.51747 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63aa9807-a0f4-3f0c-9d4d-6e028e37cc92 | -11.88748 | -50.52216 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9cf239f-7d5c-31f0-90e1-d239df27011f | -11.23817 | -49.85059 | 2026-09-27 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 045cd630-3365-317f-ae5a-29794a3426cf | -11.77354 | -51.02804 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f9506e4-0e54-376e-8f7c-4fddf7aa5743 | -11.89993 | -50.51271 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbf68e45-1f60-31b0-826c-8c27b0e9042e | -11.89007 | -50.49923 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fbd87898-24b4-306c-9ebd-844abcff8796 | -9.04299 | -66.10772 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 962ab66d-93fd-31f9-9a9f-2e1f7db04b8a | -12.67184 | -47.31308 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 468c8ff0-ca8d-3b55-ac7d-220c4e066ce0 | -9.03821 | -66.05662 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99199255-0765-3c8d-bece-7bfdf4247ed8 | -11.03482 | -51.31545 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e27acdf6-93bf-31a3-a5df-0d0f32033a54 | -12.29658 | -50.2796 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a180a57-462e-32fc-96db-c107e9721236 | -11.04472 | -51.32638 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d95caee-bcd0-3895-b9e6-22362aed47ff | -13.09746 | -47.42191 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4453289b-49ee-3e7f-ac96-fe2508508e95 | -11.04719 | -51.75051 | 2026-09-27 05:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2b108319-c398-3cda-bbfa-8746f0c8ab86 | -13.09986 | -47.41634 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd15e573-f0a2-3171-9884-522120ca7a3f | -12.59348 | -51.95282 | 2026-09-27 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abbf5527-21b3-3be7-beee-2db24afb61a0 | -11.89892 | -50.51894 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2736c10e-29d5-382a-aa3a-47bea1d44a6c | -10.02043 | -50.1376 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08f57ad7-90c6-3032-8c09-8ebf623d3445 | -6.69326 | -59.96381 | 2026-09-27 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b88507ad-cd14-3fc9-add2-a82012ef2d57 | -10.41616 | -53.81448 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1d7c3f6-ed0f-3439-8c64-40ae20b6eb4a | -11.03523 | -51.31236 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21715db2-6768-372d-9575-0e814d581c6b | -11.27507 | -54.42834 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| facdb145-c6c8-3459-9301-2ceea61d88e5 | -11.99132 | -57.60773 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README45.md)
