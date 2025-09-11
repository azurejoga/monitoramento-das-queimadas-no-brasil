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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b18f37e4-80e8-37f7-80ee-cff8f5b05242 | -12.8873 | -47.96798 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6978d9c1-67cf-302a-866d-f803fb78f31d | -15.67868 | -47.02354 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 121500d9-8bc5-3e5b-9890-77fc632238d6 | -9.76316 | -47.85424 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34af29a1-e294-34b9-a454-b6e8072b6b5c | -11.19544 | -48.39389 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a5212fd-60b3-330b-b959-10e6db11d363 | -8.57624 | -51.29869 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 085fd853-f2bd-319b-a785-39e578f6d983 | -16.05251 | -49.99631 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1bf1cbf-5f98-38c3-b443-c3dc6aa96812 | -11.36662 | -46.54678 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 00badaaa-99fd-3e34-8456-dd7283bcc66b | -15.55174 | -54.74565 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e81a40d-be09-3b0c-92be-59baba0e7c39 | -12.47867 | -47.4944 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3a4ed0ee-36fd-3068-b404-26c8bf0652e2 | -10.0112 | -51.71708 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f9be160-c785-30c7-b685-226e9cac4450 | -15.1335 | -52.41171 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edd2abb2-f489-3ef0-9afd-b468b61d4459 | -13.25266 | -43.79042 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bc52bec-e10d-38f1-b466-82e04c145b0b | -11.16938 | -45.28059 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f0071bb-5bef-3695-8ab4-92f3cc472f16 | -14.13976 | -45.3946 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ab664f5-aa81-3bc3-be5d-b1fc17acbfbb | -14.91623 | -47.30396 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1702ed4e-4db2-3659-b176-81a404376e22 | -12.60048 | -56.96605 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e4dfd0c-fbd2-3a42-ad65-d23ae8bb6287 | -11.97458 | -51.1136 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8287418c-c6f0-34c8-83c1-1c699cefe349 | -12.11405 | -51.04655 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ad55c9d-3e95-3357-8a7a-f2352d817043 | -9.8395 | -47.78067 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce3a3e3d-260f-3f18-8226-e25798796161 | -8.87333 | -49.68796 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7812180f-9ea3-3c13-8a54-e9405ed8711f | -10.56252 | -51.49305 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8c8b172-e89a-37dc-ad0c-f9ad0c17df56 | -12.98145 | -46.73918 | 2025-09-11 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5e64e66-0d06-37c9-bb08-80c214588270 | -8.51821 | -51.38599 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1c4d32a-89b2-3ed3-b758-f979e5a921cf | -9.90615 | -49.91479 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a6ac628-110c-3335-932a-1ff9c44cde59 | -11.26509 | -51.12135 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8ad75bd-21e0-3e88-b654-9e5ba5474c71 | -12.88796 | -47.96321 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59991fd6-fa5c-369a-9dcc-44ea73ce9e9e | -16.42983 | -45.68759 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af0ecf30-1bf0-305d-ad2d-5f54db4f2565 | -10.15559 | -46.17282 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 321b3f6a-795b-3dc1-9f56-75627f683c7c | -12.47339 | -53.82852 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9d048a9-4b89-311f-b8b9-9c5d8ef902e6 | -12.40679 | -63.81786 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fe6e7a5-f825-3afd-b5b4-f819135b7e63 | -12.07132 | -50.99886 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d35b7204-ef01-3bf4-8e9b-8f418edcbcb0 | -9.00741 | -49.51945 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cec5a350-1f31-3ef8-a75e-e6392380a288 | -11.10314 | -48.41494 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56d28ee6-c4a0-39a4-accb-8646f937fcdf | -12.0554 | -47.59761 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c6c69fb-71b7-3052-81f9-25833e0b259a | -11.82494 | -46.74754 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9f6ef2e-3c5b-3900-adac-4f7c6e763eff | -12.84271 | -52.94707 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2837c376-08a5-3740-8dd3-07cf75d87e53 | -12.94709 | -54.81173 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbfa55db-8375-311f-90f8-206bf6f489de | -14.38639 | -47.33941 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16e38517-0824-338c-9a73-1cc4837bab79 | -12.42824 | -47.79184 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e12e5f5c-dda1-34d6-aa3b-4cdce45830e5 | -11.63018 | -46.76675 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc67906e-0848-374b-8544-e662bdf9ca90 | -11.15616 | -52.03757 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0947d513-07ba-3baa-a754-fa27049077ba | -11.47544 | -43.64819 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5adcf75-ca43-3791-87fe-a0e7ca90809f | -11.43764 | -43.5785 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0a8c544-bee6-3e09-b74f-5365e915fcfd | -9.75122 | -47.85706 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a97ff517-9bab-301f-8994-978dfc96429e | -11.40758 | -43.54768 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c289d06-69a4-344e-8a7b-03fda14fad3a | -12.9499 | -54.81623 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b07a80ae-3435-3d12-9423-fe3a43c2aefa | -12.8522 | -47.96319 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 360b0f61-a42a-30b6-80fa-9ce777b3689d | -15.16783 | -52.43219 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32d5aed4-0317-34d3-a31a-49e671d612a3 | -9.01659 | -49.52861 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 210e5695-04e9-3960-a4c1-2da2ceb6e8ad | -9.5966 | -50.91838 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a1eeaef-1c26-3369-b870-2a1eafc915f2 | -11.72642 | -50.62714 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 723bb67b-98df-389a-b656-40f8e6f5567b | -11.48724 | -43.63737 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4324c7a9-23f1-3cc6-94c0-dc06ff4803f4 | -11.12911 | -52.01524 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eec4d5d-b6f3-32cd-82c9-06f35800d104 | -12.47469 | -47.4938 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 97386080-462c-3109-903f-1e7d9b1d39b3 | -9.01603 | -49.50915 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1192bc3-2f4c-3745-b174-c4f478bb5ea0 | -12.91832 | -54.77081 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 785ffae1-5c81-3909-9e13-db99294caa32 | -11.71908 | -50.62977 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| ce05342f-6aad-3c4b-94bd-3b0bc45a7993 | -10.00236 | -51.70851 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c2f6ecf-36ee-3cca-b8ee-11295ddd1109 | -15.13849 | -52.44564 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 693cfcb2-f374-3ca7-a20b-d4609df6a9a8 | -12.46823 | -53.83897 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38caf916-a6aa-31bc-b1e8-93891462034e | -11.21979 | -54.99512 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7d47d11-10d3-3552-a9c9-c60621d73e11 | -13.97491 | -46.64943 | 2025-09-11 04:46:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1dbc713d-fb15-3f6d-8dc9-190bf54dce67 | -10.89323 | -47.25525 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 689fcb86-6465-3e1f-b08e-6da424f312bf | -12.85103 | -52.93755 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b01ef03-1add-3845-afb9-9de54c711fc0 | -14.39488 | -47.30744 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f260d5a-858e-3d4e-be5f-0b9f9df504ee | -12.85199 | -47.96097 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bad41d83-bbb1-3662-9fdd-e1dc112f28de | -14.88308 | -55.85622 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29a0c0fe-85a8-3fd4-b8c2-39ffacf19d7b | -9.98912 | -51.70639 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09b225a0-5160-3676-b186-a0c40495ec3e | -10.53899 | -49.89316 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39149074-d155-3b29-8302-2c8dc0afe28f | -11.4805 | -43.68863 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 799658db-cc43-359c-b1a2-b9378db4527c | -9.30712 | -46.76799 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dd6aed6-9eaa-317e-a72f-b54d2251203f | -14.51197 | -53.95664 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3822773-21f9-3617-a950-cf869d71d6f6 | -11.12856 | -52.0403 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9639d1d2-7218-3db2-826c-74ecffd94f3a | -10.56719 | -52.025 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d9b0521-f051-3521-a000-bb800d468bb2 | -9.20824 | -51.8134 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78ec88dc-cc3c-31de-8fd9-5f5cd901c0e5 | -9.05694 | -50.49953 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 722e937e-9b36-334e-b2f8-95cf4cba54e0 | -10.01174 | -51.71359 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0177642-cfaf-3ab3-becf-eb1ddef0d12a | -9.58362 | -48.52171 | 2025-09-11 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfcd48e8-aeed-3bdc-afde-7e69df0dc7bd | -12.03754 | -47.61057 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc405b38-e364-30f6-93db-4889357c3c5f | -11.64371 | -46.91297 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 301c717c-20ab-3089-9e19-ef785cf4735c | -9.43995 | -49.4343 | 2025-09-11 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b5d377f-896c-3141-8743-807fe5cf9a72 | -9.77835 | -51.10208 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31831aa3-550f-3525-b616-77fff3887450 | -12.93129 | -54.75706 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 574e801b-f383-35db-b3df-0534d0350a1b | -15.61468 | -52.76564 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a3a3eee-4f03-357c-aba7-240bb99905d9 | -9.07254 | -50.48738 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0a24c32-69a7-3d1d-8986-5e3e6d1ee55c | -13.84929 | -47.36017 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc95226d-6e67-3240-a0de-6b8b69bc494b | -15.22639 | -44.05184 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b61f0d3-7e0d-39f2-94f1-3ddc5b6a62ae | -13.8574 | -43.8206 | 2025-09-11 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78c526d1-bca3-3190-ac05-ac26a6d751ed | -11.15561 | -52.04108 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2ec8552-4898-31c0-a694-3a2e622e67ed | -11.38479 | -43.5225 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd5dcfbb-6c5e-3b66-a65a-777171b65994 | -11.63238 | -52.24739 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0c0c88-4d29-33ff-b249-dbcee4473f22 | -9.01538 | -49.76637 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 67a81140-4240-3b69-aa30-91d3af188236 | -11.22688 | -54.9964 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f22a5927-b1f3-3c1f-b0fc-6cbb04213a3d | -12.85041 | -52.96286 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b43064a-b389-32b5-89a8-fbfa48e5e9d3 | -11.47583 | -43.64518 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f578357f-48aa-3c4c-9ed5-94c692b26e3f | -15.28233 | -53.79301 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42ad58ea-ba88-36d5-9e16-ad71f70b797c | -11.11254 | -51.94787 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1007059-df3d-3ea9-8d32-51a164509ac6 | -12.07861 | -50.99628 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b15a920-c3a9-390b-b107-59bf7a0cf18e | -14.3088 | -54.7484 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b5d5e62-4468-3fdf-814c-a34901088783 | -12.21961 | -53.881 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README116.md)
