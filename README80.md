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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d18076f-5497-31d5-90fa-9c73f69dbebb | -9.91182 | -48.12799 | 2026-10-10 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6337e417-b2dc-3089-a9d1-72449101c24f | -6.77402 | -48.67036 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04778995-d21a-3b2d-a384-2add6218dd38 | -10.99452 | -45.39185 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ee7bd25-97bc-33f8-a2fc-0a0693df586b | -14.45179 | -43.93106 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b6d11c9-5323-3a18-8bbb-b4f25a14fa2a | -6.02225 | -55.33208 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f0a4f0f-9d48-30ed-b218-7a62673ac2fa | -8.21102 | -49.70192 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4660a5d0-ede3-3405-9078-18cc659596ed | -6.9341 | -59.25759 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5697402-b4e9-392c-b883-7589c2193c4a | -5.98375 | -55.36243 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 597522ce-cc8e-32e3-a9d2-f3fa78b58925 | -11.69941 | -47.28968 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5bea528-7838-30ef-b937-715141f3ef68 | -7.52127 | -45.30945 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b27686e-0c41-3734-8097-388199761e7e | -6.77067 | -48.66982 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9dfb64e3-4338-3ed2-9157-842503b7555b | -10.54302 | -47.30474 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 793b07b7-f69a-3b07-bb96-ed4a96c9f7f9 | -12.01839 | -43.43752 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d273250c-8be8-3e30-878d-7d1ed41997dc | -13.38134 | -43.88968 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40b9a64a-8c2c-3084-9ede-21cc4d325ff6 | -9.27847 | -47.40441 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f6f0fe1-34c1-36c7-9057-e2365b28192a | -11.02997 | -45.43184 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 789f5aa7-55c8-362d-bc37-c83ea9856c80 | -11.90856 | -46.56518 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06c5eab9-484e-35f7-98d9-fec31024fef7 | -6.4914 | -55.28453 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eb67172-85d6-3c1d-9161-c32ed5fca71b | -9.30526 | -47.37542 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7facdd47-1fc6-3e1c-8f49-8ff2f7751238 | -10.04691 | -48.21111 | 2026-10-10 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29dd3f5b-3f68-3bb7-9b34-c056d5e540e7 | -7.19031 | -52.63695 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2b2fe5f5-5946-3f8a-b465-98087d62127f | -6.37374 | -55.17218 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10d0df3a-fab6-3d70-b658-58690e0678da | -7.21881 | -55.07463 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97c4b215-c6f6-3ecc-b5cd-f27f825a1368 | -10.57655 | -46.37941 | 2026-10-10 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83c161c8-bb7d-314b-87c6-d15f081fb355 | -8.36179 | -44.20675 | 2026-10-10 04:46:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca6bc39e-8b70-3ff4-81a1-870d5a9f1269 | -6.25069 | -52.85712 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ccd797f-a4c0-300f-a754-8ddf638005fa | -7.28313 | -46.15045 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 107fc35b-8033-34cd-8b25-27e7178804e5 | -8.24757 | -46.4329 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d07059af-4dd2-3c25-ad1e-0e89a6b0fd88 | -10.97944 | -45.19774 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29535f14-585d-37db-a687-ebed262fb427 | -7.49878 | -54.99714 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 66a42ce6-018a-301f-934d-0d7dc9e822a0 | -13.72227 | -49.1338 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c880e10c-ffe4-32a8-baee-9ba69236dc17 | -8.18335 | -54.71351 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be17f05a-6877-3c18-8a25-951b4aed2649 | -15.38424 | -41.90129 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 78a1cdb8-ffa5-389d-b082-bb5bf78cb430 | -11.02014 | -45.42213 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f70e85a-7e0c-3abd-9580-c32576ca4be8 | -13.8415 | -49.68256 | 2026-10-10 04:46:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75c0106b-37e9-3906-b756-10c4ab7490ac | -12.02601 | -43.48092 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 443f1301-4456-3bf8-ba66-218119f902f8 | -6.37437 | -55.16975 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ba6d9c6-5d07-326b-9fa5-0f205ff98f9c | -11.58465 | -43.69403 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 580b99c3-1f33-3170-a93c-45debd374574 | -10.28042 | -43.94616 | 2026-10-10 04:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ca61ba2-a9d5-33db-95a4-f62b70a2d60d | -11.67464 | -46.78289 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 019b953e-7a5b-3eea-9ccd-bb8f6ed0f790 | -8.94796 | -47.37819 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2445991c-8ea8-3caa-900b-5bf8087d96a5 | -8.89839 | -51.71479 | 2026-10-10 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 737bead9-79e6-3577-b2be-3af2220ec089 | -6.11974 | -55.70407 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 990b37a6-1f4f-35c8-93ad-9c385c59eb41 | -7.0228 | -47.65804 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0d69443-a325-3b3f-b72f-bcffa7f4caeb | -13.26004 | -43.99659 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c783d72-65de-3659-afad-dcb7914d37dd | -6.08883 | -53.50178 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bd80d1a-983b-37ce-be33-7e9be9b2657c | -7.52298 | -45.32197 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a5330d8-c73c-3eed-8034-2d6be0230024 | -7.03889 | -47.66414 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 056d5f0a-7523-3164-9a7f-c50016a6fdef | -10.86253 | -49.14281 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18ee6114-2b87-37a8-a3cb-f2c53236f014 | -9.90169 | -44.77866 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a7c8e36-e683-341f-8341-af0c49ed385b | -11.59336 | -43.72163 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bbf481f-2989-3317-acf1-98515da7ce0f | -13.91838 | -47.84343 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eb61302-d73a-3b1a-a7ec-f812558fb144 | -11.50032 | -47.60977 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e8fcbc0-67ac-34e8-8c06-f940401d615a | -10.74208 | -48.53847 | 2026-10-10 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be33ea43-48c5-3ffa-820c-5383eb85fa82 | -5.07409 | -60.22392 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f06065a0-6568-3af5-b390-09fec48366d1 | -9.30304 | -47.38969 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01b69f6a-688a-39e0-96c2-86b7feb74f1d | -10.99819 | -45.3924 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad93633f-6259-3a0e-b95b-e1863b3012c0 | -6.48571 | -55.28886 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1812720f-b73e-392b-a64e-f1788eb324ac | -13.20111 | -48.13596 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cecc345-12cc-3a24-9308-50d49b62ddd6 | -8.23788 | -46.42766 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd85aa7e-f5d2-3dfd-9889-0ba482c2f0a8 | -7.01837 | -47.66447 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 37321212-4891-32c6-aaa2-2731bc10ec83 | -11.51385 | -47.61188 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4ad80b8-3fdf-3c28-b07b-94252adb00ca | -7.19513 | -52.63255 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3868e3d1-521f-3bd9-aa1b-5b1616f885f0 | -9.63257 | -48.88138 | 2026-10-10 04:46:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dbe82a84-6296-3f67-abfc-7f87be3381d2 | -9.93611 | -44.88768 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b56a9fa0-457e-3697-bf0e-a4325b3aeb3b | -6.80495 | -52.77639 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aa95470-518a-3814-b68e-d0cf56aaaab2 | -13.52126 | -48.43265 | 2026-10-10 04:46:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50bfe795-4dba-3a21-9ba7-072b2c34aec6 | -7.19117 | -52.63189 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fc0b9f5a-daa3-3650-9bc7-1e363cb7c423 | -12.45232 | -51.39853 | 2026-10-10 04:46:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74ce4b85-53eb-3c88-85a8-778bb6393257 | -10.8317 | -47.35696 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d51c35e7-5b72-3a5e-b0ae-f4bb8509c951 | -13.17389 | -48.12848 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 765b8712-7d0f-3ea9-9de8-9d36070a6f90 | -12.38102 | -46.58063 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 686687ac-e24f-3d75-b797-65c1283fa478 | -11.85733 | -43.54921 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3759150a-0aa1-38bc-984d-585ca1f74344 | -6.49803 | -55.38781 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4306da7a-b393-36a9-9486-03238daf7dda | -10.44149 | -50.54592 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc1fa23-c4f0-31a2-aa0d-47fba5e8685c | -11.0834 | -44.11993 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa53f17c-7fb4-33e6-8c17-1861e1f1546b | -11.75509 | -46.79158 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 486c4d08-616b-36cd-adec-267035c0b854 | -8.25268 | -46.41786 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a614c3f-d858-3c35-b9f4-3775b7925624 | -14.46178 | -43.95255 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec713b51-73ee-3acb-a82c-f4b2622fa16a | -7.71391 | -43.96343 | 2026-10-10 04:46:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a008c65-b01e-306f-98ef-19df15400801 | -13.41141 | -43.72924 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71c28d3d-7a23-3a0d-8632-9f77771a7549 | -13.77798 | -48.12532 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5c9012a-de88-3bee-9528-b087516220e9 | -6.46232 | -55.50659 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5051ee0-cb3a-3681-abb6-bb4b7c1a3354 | -9.74609 | -47.65285 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 316621a3-1e44-31ed-ae79-ccdd91545c61 | -12.03439 | -43.45049 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52a63a72-5b4e-38f5-b104-7a20c7be6fa4 | -8.4992 | -54.61378 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 1c61e7c0-ee8d-30ba-8130-779780ea7c53 | -7.92708 | -54.72412 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7f45dd9-d103-3f79-9cc2-cf40339ac0d9 | -10.99554 | -45.39402 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a17bb21-4206-342c-b649-412d46f58947 | -6.49447 | -55.96354 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5c42a47-ecbe-3201-9be9-433a0d572ef7 | -10.45254 | -47.8438 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7757d06-b2f7-3326-be9d-ef643f30a973 | -8.2601 | -46.41521 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c842f9a-70e4-38ce-a597-6b97bdcdb867 | -10.76644 | -46.64464 | 2026-10-10 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78a6acc4-1636-389e-8362-e333724e1607 | -14.52977 | -48.04096 | 2026-10-10 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61a1f52b-f6ba-361e-be56-6b1f64d8d9cd | -11.86135 | -48.02562 | 2026-10-10 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c051df34-e83c-3543-baa7-cbe6b0253933 | -12.45297 | -51.39466 | 2026-10-10 04:46:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a40b5a48-f0f5-3c3c-9d2f-a9eb1e1b117f | -5.0808 | -60.22513 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a0ee6f6a-d4a5-3750-85ea-08adf7f44fdf | -11.69257 | -47.28862 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 088ab14d-53b8-3c27-a0b1-06dbf621bdfe | -11.75961 | -46.79536 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56ff6779-80d5-3c6f-8a6c-8f7afa17f9b5 | -11.98631 | -43.4529 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 28fbfe8f-9c85-3c88-be02-19b0a7137318 | -7.52544 | -45.30599 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README81.md)
