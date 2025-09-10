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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7327505-b5fe-3030-9967-7c89b1571409 | -15.10795 | -50.08084 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bf157bd-ed82-35f2-bd8e-f18292cfbcbf | -11.77643 | -64.93403 | 2025-09-10 05:06:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da6f13b1-cec8-3a49-a310-e61a3119051c | -12.60487 | -56.96719 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c7c4be5-027c-3e05-b6c7-33f235d70427 | -18.01117 | -47.13026 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f09cc92-53db-3d22-bc4a-37745b100584 | -15.83241 | -48.96812 | 2025-09-10 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 576b7ea4-31b3-3575-9f03-f5250d81b41f | -18.12992 | -51.72389 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79a9a02e-b6f3-3f49-bcb9-b6d81eb7d5c4 | -17.75234 | -44.47458 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dfc7f3db-c022-3873-9056-f486bbf9f148 | -16.45672 | -51.97546 | 2025-09-10 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 331a3001-a902-353c-b28a-a4482ddfe3c6 | -11.77542 | -64.9395 | 2025-09-10 05:06:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ac9eb76-67fd-3549-8a34-313c8d32d78c | -14.38949 | -47.31853 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4c1c836-7aae-32e5-b9ee-67b433d1169d | -15.09076 | -50.06219 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b19596bd-47fd-39d9-a9d2-ed333979594b | -17.73474 | -44.49016 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| edd90dc2-4542-38e5-b92d-5a08e5786e19 | -14.88953 | -55.86049 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc75719e-2b5f-3122-ac8c-2ab89b14722a | -19.7281 | -47.90737 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a538482-b6ce-34bb-aa7a-6c16ec6a5803 | -14.43897 | -52.95565 | 2025-09-10 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5bb5e868-0def-3847-89c7-32b40e11cb2f | -15.02372 | -50.09317 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1d850375-479a-3ad7-9d4f-a4200e8513bb | -12.61923 | -56.96228 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb3b7521-a3e7-397e-9fdb-22fbf6fb9457 | -15.76245 | -53.50658 | 2025-09-10 05:06:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3900db1e-be2d-3b56-9a8b-dca509c3efa1 | -15.27813 | -53.78304 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dcbfa03-60c0-37ad-a563-6460a864657d | -18.00314 | -47.10936 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db5d4793-e197-38c3-9d7b-815052669547 | -13.94387 | -48.26017 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| afc4c3de-6a25-3c63-b5eb-aacb41e8ef2c | -15.06154 | -50.14093 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| affaaf3f-3c3a-3bfb-8482-d5103dae22ea | -14.92483 | -50.10783 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43a0187e-b55f-31a8-ae87-80379f1bb7bc | -18.02388 | -47.14695 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 127cc767-0cb3-3268-9f1b-a110bdef65db | -15.80764 | -52.26623 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6931236a-1359-372b-aa8b-90a8e0df7ce4 | -18.01845 | -47.14024 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1b511053-2e5f-3abb-9369-07e112ff4a31 | -15.81644 | -52.23241 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55f8c300-1768-3d15-9c6e-fc5d2e4b8be2 | -15.05138 | -50.14472 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 56bc1e95-8f58-3fb8-8d1f-77d44e6da6ec | -12.86943 | -62.1039 | 2025-09-10 05:06:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c11602a-d4c4-3431-b9ce-0d457112bff3 | -15.1641 | -47.95786 | 2025-09-10 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7770b725-c20f-39fc-b112-2839a789d29e | -14.90774 | -55.85571 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f916f17-0c6f-37bc-a986-f45acaa1d6f4 | -14.89922 | -55.86599 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b28e6137-1b1a-3d96-b337-d2d5e1b884c1 | -14.39044 | -47.33035 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e370a55c-9996-331a-bbc5-220236c5a9bf | -14.89636 | -55.86163 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a0a6715-efd8-3d15-aaed-77821c92c22e | -18.13827 | -51.72976 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd38b89e-3eba-341f-8b58-7e467da6fdd6 | -14.32662 | -53.19305 | 2025-09-10 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6de38fc9-094c-374a-bd7d-4ded29b4637f | -16.32369 | -52.92402 | 2025-09-10 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c69dcdb-e0a9-3ce9-b59b-4821964c4f0d | -13.12255 | -54.93135 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09a7c83-d910-34f6-9b24-768b0658ede6 | -15.81072 | -52.24329 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 240a88a5-3d1d-3483-929b-a25418bae2e0 | -17.25157 | -46.083 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4559ac84-cd8d-38b1-85c4-138a7431e1c4 | -16.61679 | -49.77718 | 2025-09-10 05:06:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89f84975-3ad7-31ca-b2e1-d91e886135d8 | -13.13475 | -54.92121 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c299f71-f3c4-3123-b0c1-f4078eec3a70 | -12.35141 | -63.64515 | 2025-09-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66f19e6c-e587-33a2-ad30-0040906e9004 | -15.01624 | -48.02765 | 2025-09-10 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93df97d6-6d32-37df-a2a2-739f29b4122a | -15.83315 | -48.96165 | 2025-09-10 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d24dab5c-9a52-3cc5-a7a0-f08b1e182990 | -19.73309 | -47.90602 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0cb158e-3faf-345c-95f3-113030698860 | -13.12139 | -54.91512 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 781ebbed-38c3-3d98-98bb-bd63b8e2c419 | -14.55244 | -48.75314 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91b594e1-cf2e-39f3-b203-742c6b7d7f84 | -15.1397 | -52.39615 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d65a5b2e-02ae-3aeb-b41a-9ff472d7d872 | -14.89407 | -55.85348 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8300bb6-926b-3a2a-89e7-549cf589384c | -12.61868 | -56.96582 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad28e982-27ac-3446-b5c9-f029b1ef90df | -13.94529 | -48.26342 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f7d4ace-b13a-334e-a97f-b0cd0e3bd4f4 | -13.9641 | -48.22571 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 115a9f38-bbc9-3052-b0c6-19c6f9f67aa2 | -19.63722 | -45.04078 | 2025-09-10 05:06:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| fc8d5187-dfd3-3b9f-bda3-cea74a54e318 | -14.92546 | -50.10265 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf82756c-83dd-300b-a746-260ec46acee9 | -16.58082 | -49.21952 | 2025-09-10 05:06:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7780bd85-ea59-3f21-9533-50ad33f7e93e | -18.01792 | -47.14571 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 07a346ae-d18a-3580-80a9-a6369e17fc80 | -14.90718 | -55.85951 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 08b63d8f-0482-3d74-946f-71c66d859662 | -16.54567 | -55.14051 | 2025-09-10 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6e23c513-afc2-3f44-bb9d-252d55894419 | -15.95988 | -50.23103 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99086aa7-5104-3c5d-8f48-d58b67142bd7 | -15.84229 | -52.26979 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a597be6-7230-3aa0-b786-c82ee4f81acd | -14.92943 | -55.92129 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c38468b-ee4f-393a-bd1b-2002c6e46bfc | -15.16412 | -47.95771 | 2025-09-10 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c70cd4e4-1c94-301b-9e11-3bf01d46496b | -15.11852 | -47.02852 | 2025-09-10 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7f718dc-48b4-3bea-ad68-a27c8259bd31 | -15.81188 | -52.24146 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03115900-2b91-39de-aa88-8d506fcbf4b2 | -14.89749 | -55.85404 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 163e64fa-d797-3c06-aabf-f57708a65f91 | -15.13454 | -52.40335 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 34284ff4-2f84-318f-9816-0dd1d6106eab | -14.61371 | -46.36334 | 2025-09-10 05:06:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ce607f7-eed0-3f53-95de-f4ffcff50852 | -13.94606 | -48.2572 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61b4dabb-7a52-3d7b-8a32-c7b6d8f79ad5 | -12.42048 | -63.89034 | 2025-09-10 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f63b49aa-1090-36ba-9829-7286bb024364 | -15.80491 | -52.25482 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 388a4af2-7592-3588-b9e0-f114f0310732 | -14.92774 | -55.9326 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d65227c6-e3f8-31d9-9b00-2fcdf46008bc | -15.47886 | -49.38862 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 065bb643-746b-393a-8473-b7e460dcca1b | -13.12081 | -54.91906 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ac794237-e9ff-3551-a68a-5d383cf84e91 | -13.1301 | -54.92851 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d16cd31-4565-3a11-af4f-e8a50266d218 | -13.11965 | -54.92688 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19537b72-c1c6-3479-8c42-8841ce1e5043 | -14.32758 | -47.30406 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 970d08c9-e955-354f-9776-bd3cf5223f23 | -15.13051 | -52.40226 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5206c9db-e9c3-3c87-8e79-a044236c0c30 | -13.12894 | -54.9123 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce9cbe50-ddc6-3416-9f0b-a47a8289abfd | -15.60495 | -52.75257 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ada2d7f-cb81-367f-b307-05936ce2dd85 | -14.90355 | -50.1184 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| caf7a696-2215-3f42-bda4-1639527a1748 | -12.64717 | -55.95004 | 2025-09-10 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6cb6828-c4c0-3ad2-b8a4-5749b02cdaa4 | -13.94567 | -48.26034 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ab47820-c81d-32de-878d-712d2bcca178 | -19.80935 | -47.79151 | 2025-09-10 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00b9008f-1f15-3a88-9c5b-8cd5ec54cfad | -15.11108 | -50.09417 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2231384f-fb63-3644-a9d9-86d75c73e207 | -15.09761 | -50.12395 | 2025-09-10 05:06:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c4bb253b-c97d-3147-b64e-1e1256b0dfc3 | -13.92464 | -48.25533 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 127d7d07-85b0-3d6c-8c84-30405e8dce6d | -14.92602 | -55.92073 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d5e5ea0-7b76-36d3-9ab1-7303cafc2ff9 | -13.29425 | -51.72182 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 20bba639-de3f-3b2e-9ee6-a931be9b674b | -16.57531 | -49.22177 | 2025-09-10 05:06:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 144a596d-725d-32fb-bfba-db9a843b5a07 | -14.9009 | -55.8546 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97b6e93c-e27c-3117-8f17-56161a4923fa | -16.67173 | -48.52124 | 2025-09-10 05:06:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48ca89f1-698a-3cf7-8f75-fd021c59b344 | -17.24899 | -46.08471 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98cd8b96-f0e4-37a4-9471-1cc8be0c3ee5 | -14.56007 | -54.52674 | 2025-09-10 05:06:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d8dbf57-4c78-35d4-a5a8-ac1df6838b7a | -17.74403 | -44.48795 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 70aa2e05-c51c-3aa5-a342-77eeb46dac79 | -15.8052 | -52.26049 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7e92395-e1c0-3feb-8ef2-6638b587abc7 | -14.46234 | -53.2753 | 2025-09-10 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90b43ed1-c5c9-302c-9855-ee19170fb7f4 | -13.96446 | -48.22263 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 500b05d3-6d92-3a6b-a6ab-7dc09a75ebd8 | -15.80393 | -52.26214 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cfe7218-1e3e-37a3-be11-1b861daee43b | -15.81265 | -52.26877 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README100.md)
