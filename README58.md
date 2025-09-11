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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0ec6060-b107-36b8-9892-2606e65a739d | -10.10717 | -48.17392 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9978f7b2-3b27-3376-be42-67756138b88a | -9.72604 | -48.09712 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f74ce5e1-a627-3fe7-b9bd-f40d03b8e972 | -9.4552 | -46.4246 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| cc7b2c8f-38c7-3586-97b7-6bf9c68f7944 | -13.34567 | -44.00028 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9698862a-d9ba-3480-810e-1d531c37b55a | -12.13414 | -44.83924 | 2025-09-11 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f15d53a-fe6b-3ea5-aca6-f2e7da895a32 | -9.2936 | -48.42468 | 2025-09-11 04:23:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a43efd5e-e6d5-31c0-849e-11a622a9c45d | -9.20152 | -51.81386 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5b46104-4127-3a61-8135-9cafae533875 | -10.41085 | -50.5241 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c24c1d7-d9da-3c2f-92fc-4a8e8f479f44 | -11.48435 | -43.64387 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| abc32da4-3237-3c30-b1ac-1139539ffb16 | -12.8777 | -47.97502 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db98a84a-6dc8-305e-988f-6b64ee5974e7 | -9.81398 | -46.81964 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37ce8e18-585b-33de-a665-26c8015e9659 | -9.12053 | -46.97834 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64cebd43-1295-3d93-b81a-be8e6b1fed88 | -12.96862 | -46.73503 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19afbfa7-762b-3be2-b760-9a1d6ebb0c6e | -10.37927 | -48.8325 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 831864d1-5d00-35cf-b805-6d12ddbcc262 | -9.02861 | -49.77509 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de051912-3a1a-3f9d-8697-7325640460c2 | -9.5153 | -54.64227 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df0678e9-276d-3adf-8622-1e0db4b89632 | -11.73729 | -50.62575 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a556ece-aaee-37d2-8a1f-19498a4893c8 | -12.96887 | -54.75251 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba6965ce-6278-3de0-97db-f3a3669b16ad | -9.51995 | -54.647 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b6f4fbc-18ed-3164-95b4-817982482b03 | -11.68741 | -46.89911 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 808e91d6-0157-3ca1-b477-07a2b15143ee | -11.65092 | -46.91144 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dcd0cf09-fb64-337f-869d-12c99717c81d | -12.47216 | -47.48846 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 120e1902-1883-33c4-b9e7-eb3321230cd4 | -9.98682 | -51.70464 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53f83a66-cf61-33a8-b7cc-ba77f20b2d2b | -10.54223 | -51.52185 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9f51a39-9325-3355-8698-3e079d227743 | -9.05556 | -46.9716 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85804a83-94d4-35c8-9ccc-f1ea5e15c038 | -9.07718 | -50.48346 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 747b4f2f-2e41-3fab-b02f-288b8f3d72f9 | -9.51837 | -54.64356 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26320ffe-a1f0-32f7-8085-9e915eac1df2 | -9.78174 | -51.1011 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a630c22-d1d0-37b4-a8aa-ab2a19f9b9f7 | -11.71702 | -50.64857 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1313cfa3-7916-3fad-a1ce-bc0482373598 | -12.04744 | -47.60822 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f344dab2-4fdf-3df6-99f7-54b56115a84f | -9.06716 | -47.07304 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20f31ad4-885e-35c7-bbc2-4ca7bfc24f85 | -9.78522 | -51.10595 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c5835c7-073e-35de-a6f9-1eec412017f2 | -11.14675 | -48.45814 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 585098b0-add5-311a-a12c-318606c79c3c | -11.78152 | -50.57214 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1adc12a4-5765-30e7-b164-e9f993db1a80 | -9.3624 | -46.80232 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d8149bb-502d-3a44-b7bf-a9021bb2251f | -9.86057 | -43.12868 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e9dce3c-6dd9-36a0-816a-ad24f38a43a5 | -14.40688 | -47.32401 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee1e45bd-bdb0-30d9-a79e-0d9247c0a12c | -9.30669 | -46.75945 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fbf1e56-3216-3197-8204-ffe5a3ad9499 | -9.70183 | -43.53414 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 626da19b-7379-3bb2-86fe-7aaa9f81b80f | -11.47445 | -43.68557 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad70ea00-d4da-370c-89a7-c9494a3b4220 | -13.25507 | -43.79041 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 993cae77-c96d-3491-ab19-76aabeef3b8c | -11.10818 | -48.4051 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 253b98a2-f2c5-3d61-aa3c-ef64333a3eda | -12.94494 | -54.81001 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0439ef6c-4125-3691-8ed7-8223a3b44a39 | -12.60706 | -56.96067 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb0e9396-203f-3f38-b260-1e395c83fc79 | -12.98472 | -46.74137 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd77e96f-e210-3282-ab5b-0d42ad012930 | -11.48612 | -43.64325 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a0b91215-9dfc-3482-aaaf-113dc2e10f69 | -11.06948 | -51.3315 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc410c90-55c9-3d14-8ea3-ef463d59d8a7 | -9.07249 | -50.4862 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4dd9fa4-e08d-389a-8e48-cec4f941bbbb | -11.9673 | -46.6549 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd57f2a2-ea94-341a-a817-ecbd6e2f008f | -10.14356 | -46.16375 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 355581db-d55e-38f1-a357-96159a915e67 | -12.56863 | -44.64514 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d73bc41b-8ffa-3efd-a18a-9ee767a03562 | -11.47221 | -43.63025 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 537cb111-5a47-356c-9c6e-d896c5fb2026 | -9.91891 | -49.86681 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 707e7911-e2be-344d-b2cb-faf9af33e0c3 | -13.04875 | -47.16436 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20890c62-d9b1-3927-8146-11ca710dd62a | -11.3911 | -43.53052 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76c50a6b-4d79-3f32-9493-3f9b8c63cd11 | -12.12631 | -44.86763 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6edfc3fb-50ad-342c-8c1f-eb5981ca8c3c | -9.70239 | -46.88369 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4624d658-0e67-3e2d-8b74-dbb3bccbc0c2 | -15.20047 | -44.03386 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4c47f9b-8fe7-30a9-bd16-06063506e9bd | -14.91675 | -43.09368 | 2025-09-11 04:23:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa85aeb9-af9c-3f76-9c98-9d951f820e10 | -9.05516 | -50.49492 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3f27975-26ee-3be6-a095-be320b088ac4 | -13.94045 | -48.27074 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7befa7b0-6ee5-35d0-acae-998b3ac7acfb | -11.40794 | -43.53712 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94e7dc06-f43d-3c35-9e22-6c7225627ee1 | -12.47276 | -47.48478 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6299bcc3-7966-31a2-963f-d6ab91e4413f | -13.45059 | -43.48409 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6aa3bfe-ffe6-3718-adb0-3a873888340c | -14.36101 | -47.29816 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 292f8c47-4d16-33cb-adb3-5e13fc2cb7ab | -9.15351 | -46.05497 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8909dca-5642-3d23-a59a-ee6ea4a6e777 | -11.47386 | -43.6894 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9af2568e-4b88-3c1d-9a69-f58057a3646d | -12.21885 | -53.88068 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a20da062-4452-3983-bc9f-9db18c4db2c6 | -14.36932 | -47.31057 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7dda05f-9f39-37b7-96b1-4936f767c4ab | -11.35458 | -46.51041 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bf377bb-22c0-3647-8b76-388fa50ea949 | -9.02315 | -49.52774 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3457f461-f523-3fc9-86b0-ebde16b4f96d | -11.39008 | -43.53151 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9b859e4-0b6d-3705-aae7-6640a43db126 | -9.07218 | -47.0855 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89aea8ca-caec-3481-9ff8-59bf63c3d66d | -12.13023 | -44.86455 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ff95191-990a-3ac8-bdf9-ff6a80fdc039 | -9.09092 | -49.81153 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c563ce3c-6fdd-3813-8366-96d0b78f7107 | -10.55779 | -47.23056 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47d23077-3bdc-3c6e-a529-ece18e5a4a3d | -11.37229 | -46.56049 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38c1cae1-df71-33e0-9274-2e0d35bf5cac | -9.72316 | -48.09256 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccf7c6d9-3584-3579-8beb-aafba9e31989 | -11.4265 | -43.57975 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ccbba3-a616-3525-bcf4-65018ab54cfd | -9.08764 | -49.84882 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8d6e935-e0da-319b-8214-bd5cf5a4e7b5 | -9.83861 | -47.78719 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55cf5889-ad17-393d-89cf-f3d0896d3b49 | -9.45183 | -46.42406 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 97a3d48d-271d-3535-b005-82843bc6188b | -13.27497 | -51.73752 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc3865db-7ff6-3f84-bbf2-84302c28ee3e | -11.41028 | -43.56927 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aef9e69-9792-341b-940b-67585d4c82e4 | -10.73506 | -48.28395 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bdc82c6-0e8a-331e-8e4f-27892ace7f1c | -11.40584 | -45.60647 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b71b7fd6-205b-3d1b-a33b-a8c7ec68649f | -12.85445 | -52.95208 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5299f581-4e12-3b68-93db-7183760825f7 | -10.26818 | -48.82795 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09b60615-cbaf-3519-9cd1-6385f8b23e5f | -9.68373 | -46.77976 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e723ba3-a53d-3bc7-b0b3-6e1b3a75a210 | -12.1628 | -48.49092 | 2025-09-11 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31a810ee-f3d1-3cc5-b321-71bff7d17cfe | -9.69179 | -46.75114 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b079478-2e1b-3db4-bd40-c71cba8fe9b0 | -12.92314 | -54.75798 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dd66815-da06-3b91-85b0-72b01ea89790 | -10.143 | -46.16727 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c67517d-277c-3acd-b3dd-8be179410dff | -11.65545 | -46.90476 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f31b511a-2474-32ec-8593-504865247020 | -11.41665 | -43.55041 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7fb179ff-3b6a-3f19-91f1-a74b294e4f0e | -12.10205 | -51.01965 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02ef852d-89ad-3489-aca9-1b5486018c72 | -11.74664 | -46.53063 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2942246b-b583-3901-bad1-64727fd45094 | -9.07903 | -47.08664 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cb136f3-f3b0-37c2-a698-e36d2a84b752 | -9.05649 | -50.48705 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73f2f775-87e7-37fc-8c1d-87abe0499aa2 | -12.58789 | -44.79079 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README59.md)
