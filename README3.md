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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 093c5042-6506-3112-8e38-9ebb7fca7108 | -11.20492 | -55.92462 | 2025-07-01 01:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1b449320-915c-3d7b-b847-654b7af43668 | -11.03184 | -56.2692 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 25fac5aa-31ad-3de7-808e-83fceaa28d96 | -12.01545 | -47.76896 | 2025-07-01 01:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| cf21a259-c774-3c05-9a43-1ff891bc2f68 | -10.02455 | -54.32331 | 2025-07-01 01:22:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c3518a5d-7d89-3034-9138-caa9d2fa6aca | -9.69785 | -56.17768 | 2025-07-01 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0a50c8a9-3312-3cb5-bbbc-44fc73458589 | -12.62608 | -54.2174 | 2025-07-01 01:22:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 44d8a85a-89cd-3c3a-aec4-6db7ab8c04ad | -9.25095 | -58.76656 | 2025-07-01 01:22:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| af8ffda8-7a83-34a2-afb8-0866d2d4be2b | -9.11553 | -59.0526 | 2025-07-01 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6a11158b-7039-35ca-b867-b47482e0bb4e | -11.20721 | -55.91798 | 2025-07-01 01:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 82ea25ae-9bf3-3824-b819-36356a543f7a | -9.40057 | -63.26474 | 2025-07-01 01:22:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9779b5ba-bbe4-3738-97cd-9ae56a33d033 | -9.66113 | -50.73857 | 2025-07-01 01:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 3092b646-dcc5-303b-960e-50709da13d73 | -10.08461 | -52.74016 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 63c23f6b-3bac-3219-a925-e82ffbbc6692 | -10.2832 | -52.82885 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 9b03c4ee-2b10-36dd-8be9-451519331f27 | -9.2497 | -58.75764 | 2025-07-01 01:22:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 326922eb-1011-3d3a-8edf-99cefb060ab2 | -10.07212 | -52.74216 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 24db1607-20f3-3fb5-af6f-0466708a3146 | -9.08138 | -59.4721 | 2025-07-01 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ac83e60d-f9a6-302c-b8c2-2e1e42a4d81e | -12.10808 | -54.58066 | 2025-07-01 01:22:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 74e5b970-4f80-31df-9b91-2408caa24b73 | -10.88218 | -53.75674 | 2025-07-01 01:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 17b11621-2cde-3417-8b5c-c6a07469e091 | -13.00705 | -53.42621 | 2025-07-01 01:22:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e6d51250-0422-3bf7-ba36-6b7b80871dce | -9.70757 | -56.17623 | 2025-07-01 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 520f19fa-2881-340f-b713-f16ee83855ff | -11.20332 | -55.91367 | 2025-07-01 01:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d22e4b5d-c921-3597-8c72-8244461a7553 | -9.98086 | -48.26028 | 2025-07-01 01:22:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e4f8b2d2-4cb3-33fa-a9cd-7536acfcd576 | -12.63875 | -54.22883 | 2025-07-01 01:22:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fbffe5e7-c038-387b-8173-755f08d7e932 | -10.87297 | -56.4435 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4a3074d4-367c-36c4-bacf-c9b161f44abb | -9.24846 | -58.74872 | 2025-07-01 01:22:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 9de520ae-755d-3387-9e9c-ce518da1f148 | -10.12495 | -57.77651 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0cbd2f6b-9537-3cdb-9ba0-79d3d53a4624 | -10.89332 | -56.4509 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 306bd6ef-d294-32be-ac9f-eed793b04826 | -9.6613 | -50.74492 | 2025-07-01 01:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 9032cd8f-696d-31b5-af81-15a88a179667 | -11.12418 | -55.44286 | 2025-07-01 01:22:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8a1db2f9-ae3d-32b5-bfeb-8a30c7ac75e5 | -10.07517 | -52.7609 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2151c1ce-1503-33d3-992f-c079ed5aa12d | -10.1288 | -52.36468 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| c658f013-2264-3ca1-b827-e1fa03033941 | -9.69948 | -56.1886 | 2025-07-01 01:22:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 010a64a2-70f1-3ad1-bea5-3cee467b8b3d | -9.98077 | -48.25418 | 2025-07-01 01:22:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a59708ac-8241-3d18-8dfa-51183efaf53b | -12.97523 | -54.6801 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 06903d8f-de73-360a-bb77-2464bab8c9fc | -10.08036 | -52.72718 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b48e8b3a-1988-38a9-b604-1aa9caad437d | -11.0303 | -56.25874 | 2025-07-01 01:22:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 47ebbd8e-c4b7-3978-89b0-1f5333575fbc | -9.08261 | -59.48102 | 2025-07-01 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1de5ac62-3a2e-3b7b-9109-c3a0af936baa | -9.09023 | -59.47083 | 2025-07-01 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 423d200d-820c-3628-9746-7be9a1e9305f | -10.08326 | -52.74592 | 2025-07-01 01:22:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2b673a98-5c92-3d99-876c-768d1e05b05b | -6.2943 | -43.6891 | 2025-07-01 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| cb73d41b-4fc1-361f-a3de-9abc57747f75 | -7.6239 | -45.7447 | 2025-07-01 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2d8a2a44-79d2-3d29-98fe-09392245dce4 | -10.0784 | -52.7393 | 2025-07-01 01:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 85acf5f8-b359-3ba8-b150-6c5edaeab39f | -6.4814 | -43.743 | 2025-07-01 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ecead299-0e0e-3711-99a7-bdc065866cd4 | -6.2945 | -43.6659 | 2025-07-01 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| b2e544c4-e7a7-34c5-b82a-63e8417cdb60 | -9.9847 | -48.2378 | 2025-07-01 01:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 94543915-46ac-310c-a754-031c5bf458fa | -10.883 | -56.4567 | 2025-07-01 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| cc97ac7a-cc93-3a07-8317-7964e429f91f | -10.8832 | -56.4367 | 2025-07-01 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 0df023aa-1553-3bdd-8a40-9e2f14da8448 | -10.1207 | -52.3409 | 2025-07-01 01:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 5d094e04-7bc1-30c8-88c9-c8df1fc6f14c | -10.1207 | -52.3409 | 2025-07-01 01:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 4b167360-9d4b-3381-8523-f4ee53293c51 | -9.9847 | -48.2378 | 2025-07-01 01:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| dc5193ab-9fb7-3b3f-9299-8cbc38cf14f6 | -6.2943 | -43.6891 | 2025-07-01 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 8fd4e3c9-c860-300a-a75b-b4e7682bbfb8 | -10.883 | -56.4567 | 2025-07-01 01:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 97b82f58-054b-3301-88dc-ebc3d7c45fcd | -6.2755 | -43.6907 | 2025-07-01 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5d82c427-0b56-36ea-9e84-02fe56fb0b28 | -6.2945 | -43.6659 | 2025-07-01 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2be824fa-d339-3800-8b91-7c3f1af15297 | -10.8832 | -56.4367 | 2025-07-01 01:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| df805cb5-4017-3483-b6a3-e3b7e0ba6737 | -10.0784 | -52.7393 | 2025-07-01 01:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f9287711-2367-3086-8ad2-f4e74a96ee66 | -6.4814 | -43.743 | 2025-07-01 01:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 32e9ab41-364c-3c22-8983-da2b0bd63af7 | -7.6239 | -45.7447 | 2025-07-01 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| dc0a6635-50ea-3ca0-8efe-856e6f8cfd82 | -10.1207 | -52.3409 | 2025-07-01 01:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3c463bdc-07fe-3fca-a61c-5dcea7677136 | -10.883 | -56.4567 | 2025-07-01 01:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 208d0661-fc8a-3809-88d6-09916dd2735e | -9.9847 | -48.2378 | 2025-07-01 01:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 7ef3c755-fbbb-3825-baee-63fad2291098 | -10.0784 | -52.7393 | 2025-07-01 01:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d3a9f105-4583-3cff-98c8-45266b8ef6d4 | -6.4814 | -43.743 | 2025-07-01 01:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| d663be84-4ee8-3e7e-9ca8-6e4a7a41d91d | -10.8832 | -56.4367 | 2025-07-01 01:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f0011452-7cb3-382c-b55a-f0459fb80d76 | -10.1207 | -52.3409 | 2025-07-01 02:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6206d5ed-7f6d-3eb8-834d-dff43224caad | -6.4814 | -43.743 | 2025-07-01 02:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 862c1532-09d3-3335-abbd-51a89bd27ef5 | -10.0784 | -52.7393 | 2025-07-01 02:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1e1f1516-d01b-33bc-9d1d-bff8a6ac7afb | -6.2943 | -43.6891 | 2025-07-01 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e97ada3b-9649-3d18-8e76-cfc86c53e7e5 | -9.9847 | -48.2378 | 2025-07-01 02:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 34ddf3bb-1f0b-3d96-8f3e-7904644bbe9e | -10.883 | -56.4567 | 2025-07-01 02:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7bd2fcb5-a9b3-36fc-a46e-9e7d6847246c | -6.2945 | -43.6659 | 2025-07-01 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 7f3b5785-6154-3d1d-9202-332183d4a45b | -10.8832 | -56.4367 | 2025-07-01 02:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 3fd564af-ec34-32b8-8f24-4f6f470a7cd4 | -10.1207 | -52.3409 | 2025-07-01 02:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 428acaa2-e8e4-3710-9d40-93ca354d452b | -10.883 | -56.4567 | 2025-07-01 02:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3fddcfa8-c51b-3b00-87e8-a050d1909f4e | -10.0784 | -52.7393 | 2025-07-01 02:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 13fbc652-a7dc-3c48-9354-fd32895a5e05 | -6.4814 | -43.743 | 2025-07-01 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 73529bb8-0d14-3443-ae30-51df8d4e6b68 | -10.8832 | -56.4367 | 2025-07-01 02:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| aa89417e-4625-3aa0-ae0f-53b0dfd39d05 | -9.9847 | -48.2378 | 2025-07-01 02:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 55d6ac17-d8a6-302b-a3de-58ab67f9a360 | -9.9847 | -48.2378 | 2025-07-01 02:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| fc051bde-0ad7-3955-9e96-8e70efb5d109 | -10.883 | -56.4567 | 2025-07-01 02:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 181168e3-242c-341d-80c5-cfd82f21cdc0 | -10.0784 | -52.7393 | 2025-07-01 02:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 428fc14d-42a1-3106-8376-a900e24386ca | -10.8832 | -56.4367 | 2025-07-01 02:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c160c516-77d5-362f-a410-40915bfeb580 | -6.4814 | -43.743 | 2025-07-01 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 31da343c-99e5-341e-8453-a282a6ba5d55 | -10.8832 | -56.4367 | 2025-07-01 02:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| a5ca2453-9bcb-323c-a17e-77985354ac75 | -10.0784 | -52.7393 | 2025-07-01 02:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5be5ccb1-4a1a-3e47-9a25-7d492b6c42a8 | -10.883 | -56.4567 | 2025-07-01 02:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e378eb0d-7959-3bcd-bba6-ca23fe680f36 | -10.0784 | -52.7393 | 2025-07-01 02:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c45b663e-d54b-384e-8e14-848dd60ea650 | -10.883 | -56.4567 | 2025-07-01 02:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 40940311-220c-366b-8745-f986fbdcddc2 | -10.8832 | -56.4367 | 2025-07-01 02:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 654d867a-b96d-32d4-87bd-f4bdd9e44567 | -10.8832 | -56.4367 | 2025-07-01 02:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fbab7639-0170-3810-8a93-eaaf1ab129e5 | -10.883 | -56.4567 | 2025-07-01 02:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 30dd7541-b1a7-368e-bb06-3bbf816a7694 | -10.883 | -56.4567 | 2025-07-01 03:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1c53eca5-f4a1-3659-978f-09e3f11fd31d | -10.0784 | -52.7393 | 2025-07-01 03:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 181c3d17-2e0d-316e-8bb6-d0336b4170b0 | -10.8832 | -56.4367 | 2025-07-01 03:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4798464b-693a-352c-b968-e31b94a0f976 | -9.9847 | -48.2378 | 2025-07-01 03:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| cfe1f881-9763-37e5-8c4f-4575a71edb92 | -20.22415 | -41.01009 | 2025-07-01 03:08:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5421005a-a999-3597-9bb0-c9d0a2be07af | -19.38528 | -40.20968 | 2025-07-01 03:08:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7f2c2893-b3ab-3760-8d8f-097d18f58a4c | -6.2943 | -43.6891 | 2025-07-01 03:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e85755c7-ce42-3818-a8be-fa12316f87fb | -10.883 | -56.4567 | 2025-07-01 03:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1fd498fe-3562-3d73-934d-74bd3d5b3384 | -6.2945 | -43.6659 | 2025-07-01 03:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |


[Clique aqui para ver as próximas entradas](README4.md)
