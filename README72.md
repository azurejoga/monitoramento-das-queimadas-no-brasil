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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7da7a003-820a-37d5-9448-bd03cf516415 | -13.28258 | -43.77438 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80884748-e349-3258-8e3a-90e30d736f91 | -15.12414 | -47.03105 | 2025-09-11 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b971e3f0-32fb-3c3b-9f44-4cb54c73bfe7 | -14.79476 | -48.17729 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c8c17fe-6bda-37e7-af8e-aa702a9603dd | -12.00034 | -47.59631 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13e4ac72-33d2-3ab4-ae86-2f4736172a67 | -15.09259 | -48.04487 | 2025-09-11 04:23:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 384cfd0c-cb6e-311d-b2b4-0a0145f8b14a | -12.06167 | -50.94257 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e393043c-247b-34e1-8455-abe78f1f4023 | -11.99693 | -47.59574 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e86276f-6c47-3990-87e4-f49cf0941f92 | -12.92139 | -54.76719 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bda7724-b00d-3044-87c8-f146f26ad817 | -8.56798 | -51.34692 | 2025-09-11 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca2adbbd-ff91-3b72-bc58-6fe9ca697773 | -10.54445 | -49.88967 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aac79e5-38c9-3fda-aace-3e3a5690e13c | -11.47503 | -43.68174 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70374570-8cf9-32f2-af30-4f6b22c47804 | -14.36654 | -47.30646 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bce91b49-3505-31ed-8648-aadbc5f1c376 | -13.15647 | -40.68253 | 2025-09-11 04:23:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7bab7359-2546-373c-be1e-211653e22b67 | -12.00898 | -47.58634 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6277ea70-c4c2-3db9-938b-124c4387fe53 | -14.77928 | -48.22839 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9033f860-d9ff-396c-975c-58afcd3f11ef | -9.99117 | -51.70549 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af48c265-9676-30ef-859b-d0d0167d206f | -11.59778 | -52.21957 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5af4d479-6789-34f9-bf1f-6f2534198b25 | -11.39126 | -43.52376 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ef8ab76-1912-3049-bcd3-029ca6093b04 | -12.60619 | -56.96492 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e2d27d8-87fa-34f2-b39d-fa8081c904b3 | -10.34449 | -46.38945 | 2025-09-11 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9210936-f265-3eb9-bb80-3b4215d16b08 | -11.30883 | -50.74691 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c76e8621-69bd-3a64-a346-7ce4ee875c0f | -8.87619 | -49.56204 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea205f0d-db20-3875-856b-f70e4a97ea8e | -14.56519 | -48.74458 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c78d513-051b-3a09-870d-6abb4429eb18 | -13.29079 | -43.76752 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed84dc0b-1c53-39a5-bd0c-286701cc3eba | -12.85295 | -47.96031 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6d03085-abd8-3e5f-9c78-678ae0608cb8 | -13.21854 | -51.766 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35871b88-b453-37f5-8d38-1e4017a148eb | -10.66086 | -48.6442 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a281b263-4e65-3cb7-a531-18355215aeb3 | -11.34357 | -46.47207 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23af6ae2-4408-38c7-abe2-e7c7f3509781 | -11.39833 | -45.59398 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29406fa7-6d0b-3765-99d3-832399cbb673 | -11.48436 | -43.63118 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82f65f52-167f-3894-bbf4-5dd924d714ed | -9.89583 | -50.17169 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c0e70ff-e2c2-36d1-b8b3-acd121bfbfe8 | -8.79856 | -48.09697 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93f09743-428f-3992-ad32-1113fdb0afe3 | -11.4785 | -43.68227 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f93b8921-a8e5-34be-aaba-8224eb28a0aa | -9.99552 | -51.70634 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a79786ba-d08d-32a3-ba19-177f6f3f184f | -9.80305 | -47.7852 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18a880a0-7549-385e-8af2-847d965ae379 | -9.97888 | -51.69873 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447c7f07-f199-3538-8407-312948c9c891 | -11.16146 | -52.03966 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79a0bcbf-8860-3705-bd32-18f5a96d244a | -12.13358 | -44.84286 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c3a8a46-2673-30cd-8029-6478298e7cb1 | -11.11053 | -51.94708 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 881d34f5-6292-3bfa-8543-a025fbc521ad | -11.47157 | -43.68121 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b026aac-ca78-3cee-b92f-bf86185cd1db | -15.24759 | -44.02714 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d95cea6b-8e34-3d6d-a450-f442ef77d664 | -13.13154 | -54.91776 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4974492e-00a8-315f-8fc2-9dadcde3b1e8 | -12.91346 | -47.99305 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0991845c-1d33-387e-931b-ffc3b61701a7 | -11.8277 | -46.74178 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f327f7f-558d-3c38-93a0-b808e8c20532 | -13.9809 | -47.94115 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff67424f-7ff5-3d8b-b083-c147da6d28d5 | -9.10334 | -49.85152 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33fc06e0-17c6-352a-beea-4ddf66adf87a | -10.13819 | -47.4422 | 2025-09-11 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a575b9c-c038-374b-a928-d8c84f9db613 | -12.92634 | -54.79671 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc6965b-cde1-396b-b61a-285c62d9b476 | -11.16071 | -52.04393 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e617218-095a-3b01-a29e-92063ef64649 | -9.05994 | -50.49153 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35ec1686-4b2a-3689-9e3f-5c5a1502f72e | -11.07366 | -51.33227 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c22e14d9-2fa2-33ef-9044-65a41150d313 | -10.5684 | -51.49837 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 097f6473-5440-3004-8eb9-b3cf0ff2f4d6 | -9.84685 | -47.78065 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0e479bb-c80c-3d58-84f9-27bf848b26ca | -8.87538 | -49.5669 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e5109e1b-4454-34b1-aa56-324bc17f6e82 | -14.59638 | -43.93331 | 2025-09-11 04:23:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54ee7f9b-5239-3d19-971e-b88113623cfa | -11.08685 | -51.33072 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 131f0d5f-983e-3602-8f60-21c93bd2b889 | -13.65599 | -45.72042 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7ed8fe8-ae13-3bdd-bdda-23948ca821cb | -9.2104 | -51.81555 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 912640b7-f5ef-3546-933b-648f6514fbaa | -11.19309 | -48.39417 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a55b3b-6999-3b82-8acf-692f4145b700 | -12.87329 | -47.95912 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d15fa14e-39b7-3dba-904e-19bfe51979d6 | -13.26445 | -43.77564 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8836aa29-1b64-3107-a8df-ab6b54a72065 | -12.84176 | -52.9449 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ac4673e-7364-3419-b564-ae764b716e55 | -10.64783 | -48.63366 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d61a6dc2-e8c7-3e1c-9a84-4d89218f12f8 | -10.93966 | -46.81338 | 2025-09-11 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a249898b-95b6-3ae6-b9ba-42fbccda873c | -9.0907 | -49.85449 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7047d9f9-e7ae-3ba4-9ced-e82e597b99f9 | -12.56471 | -44.67084 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7ff53fb-218a-32e0-b827-07df5c485662 | -9.61446 | -48.07117 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bd143a9-6ff4-3b65-9c83-0ddd7b9e639f | -12.97806 | -48.02426 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6c07b67-551d-3b37-b814-e6d53a5331a6 | -11.47733 | -43.68994 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd3d6472-625b-33a0-b068-880b27191870 | -12.47993 | -53.82444 | 2025-09-11 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dce4f0b9-44ec-3c28-ba81-17dd28acccf0 | -11.49077 | -43.65974 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfa8a19d-afbc-34b8-8927-9838f91a5a29 | -12.03661 | -47.61021 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07da20ee-c58b-30a9-b0dd-5cbaeddf7af6 | -12.92692 | -54.79361 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfe317c0-fc05-380e-a452-293785cf39a0 | -10.15913 | -46.17348 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e217ee1-fcd8-31f7-8d2a-de250d4d77ec | -10.311 | -48.79588 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ded1a40-8b26-3192-802d-385e7e8dc568 | -12.90228 | -47.97543 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cd0cf11-af13-3493-a372-cb60dda56070 | -10.20021 | -46.67805 | 2025-09-11 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95af67db-ba19-324b-ac45-9942d1cfa88f | -12.2404 | -47.32563 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6733e7d2-19b7-3a2e-9a76-6d9fcbe17aba | -15.19927 | -44.04197 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a8388a8-9ac5-32f7-b202-806704effdb5 | -12.08178 | -43.33182 | 2025-09-11 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 277e29af-f749-3ced-beea-099e379737a0 | -12.2551 | -47.32065 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 75660eb0-cfbb-3c41-bc3a-b7e4e69ad399 | -9.89187 | -50.17098 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1751190f-8b8b-33bf-adf0-d525fcb9b6a5 | -15.19987 | -44.03791 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3f01248-a795-32e8-8888-9cc23572cec7 | -12.40489 | -49.31516 | 2025-09-11 04:23:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e790e2ad-a265-3a22-8a5a-61f86baac612 | -11.47328 | -43.69323 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| af25f3d0-3d17-3685-81c9-27a6dad71501 | -8.80214 | -48.09756 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58f6cf05-03b0-39fe-a77c-3c5c5adb561e | -12.84764 | -52.96669 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ccba8fd-2c16-394a-a7f9-522558fe85dc | -9.08486 | -47.07233 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ffc1e14-0f09-3780-9b2f-3093088e5408 | -11.49424 | -43.66029 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d7ef323-9e39-3941-afb2-511eeb6db2f5 | -15.22401 | -44.04013 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e6544b4-1ed2-3241-b804-a034b52a4ba0 | -11.48147 | -43.63951 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e283a1f6-0b8f-3e59-9718-56fb47f352a1 | -9.43966 | -46.69192 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07e2dc21-746b-3cbe-b3ad-52a6186f3b61 | -11.36905 | -46.53801 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2b89ac3-2758-30fc-b11d-01a578d850f6 | -21.9171 | -47.90885 | 2025-09-11 04:25:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 258507d0-d526-3c13-97b2-4082ee07b9eb | -20.33518 | -46.60703 | 2025-09-11 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7c85cfa-2c5f-38ee-93f8-ba8681f903e0 | -16.49212 | -51.9745 | 2025-09-11 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9ca9cd2-f55d-38af-bfb5-f36abd5a5fcb | -14.28333 | -54.744 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7ce283f-1b81-3bb1-8dfe-e9a133e233e1 | -16.61678 | -49.41607 | 2025-09-11 04:25:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 316713dd-ce06-3b4a-a8c2-d7074c6a7e5a | -15.13697 | -48.60679 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83a87498-75df-3334-8189-1c26dcb998c9 | -20.15468 | -43.6717 | 2025-09-11 04:25:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README73.md)
