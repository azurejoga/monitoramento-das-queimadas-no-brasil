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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8ff2fb1-0985-3486-b886-f57be9abf9a9 | -13.68244 | -48.58844 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e1e8100-9b52-3768-bf69-424eadedcfe0 | -12.58493 | -49.10462 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 891e1f9f-e9aa-3f37-b399-d424c2f0124b | -12.98319 | -46.97818 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a170e3be-0108-3b28-8d38-27b628d0008a | -12.59511 | -50.88007 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1310a89e-c96f-3c74-bbfa-1def0ec13db5 | -12.69096 | -45.97038 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 055e16c4-193f-314d-af11-c91579517ce8 | -10.86253 | -54.10618 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8e4ff30-0f8c-3da6-83c4-fcd2c7a111ee | -13.38033 | -48.03391 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35aebd72-dd88-32b1-9004-b837160f7b12 | -13.23421 | -46.91467 | 2026-09-19 04:59:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49b5501e-8334-3c07-87e4-c4faa111cbc2 | -12.59738 | -50.91562 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d16ae31a-2ed7-3c8c-968c-f1b33e40610e | -12.57462 | -49.11394 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73a0e4e0-039a-3917-b17b-e15570b688ef | -10.87032 | -56.20111 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58a35578-c563-39b8-90a2-09c7f4ea9bd5 | -13.74425 | -48.80283 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceb8b8b4-b8cd-31e0-bc6f-bfc612d4b68a | -14.93964 | -49.94287 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1351329-10fa-3875-938c-6b92111e66ee | -10.70799 | -60.73104 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ffda1f33-c3f1-3c61-a920-35e5734f5e35 | -11.67553 | -54.4406 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85bc5287-4b8c-3934-91a7-93074209a29f | -15.77546 | -56.46707 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69aeff3f-d625-3224-b9a2-ef1aa88e5c12 | -12.74149 | -47.02248 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90fde1eb-a98c-3bbc-a324-db194f5a4a66 | -11.49547 | -47.72595 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cdca91d-73bd-35de-8187-bdb74f2875b7 | -13.74054 | -48.79862 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ce0f954-44b8-323a-a691-ed0d62d6ee71 | -12.28479 | -49.17409 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b77b0b2-83e2-32fa-a238-268dd5b38163 | -11.42389 | -51.4563 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6a3d5c4-a276-3e05-8666-6424d1bd4a02 | -12.01986 | -55.3385 | 2026-09-19 04:59:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ab1a3a-0336-3932-9d98-416f3e386feb | -12.74216 | -47.01742 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b58658c-2f06-3fcc-aa44-58664ae5ac2e | -11.77159 | -47.43607 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09f5012d-167c-3efb-9a6b-e27bbfa706f1 | -15.60755 | -56.57243 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c19c8a3-ae5f-35c9-bcb6-1190abdd582c | -15.66975 | -52.73357 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c67eb77-4d14-3738-9e78-51ed99e150df | -12.28224 | -49.16293 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fd22a92f-32ee-3937-bd4c-0b3d990844c8 | -16.30502 | -53.86 | 2026-09-19 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa5b0967-5b71-37ba-b87b-55bf3ad85360 | -10.90178 | -53.98686 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2b6d698-e6fb-361c-b2d9-cec76335e4ba | -10.85991 | -53.99439 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d9bfddf-7a7c-33d2-98de-410c412f3d1f | -14.15192 | -45.21344 | 2026-09-19 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56b4c6a6-04f3-3170-882c-17f398fbb3ea | -10.89302 | -50.87533 | 2026-09-19 04:59:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24a4466c-3bda-3086-8e19-21546f46932c | -13.02054 | -48.64426 | 2026-09-19 04:59:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3021edef-e3cc-3305-842e-3e7e0c2f4e0c | -14.79653 | -48.56216 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14796b85-43eb-36e2-a43e-97c91c9da62d | -12.28674 | -49.15997 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ac36be-e3a1-3595-98fe-8a3dd752f06b | -16.88075 | -50.58075 | 2026-09-19 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aa3d7d9-1616-3311-8107-0bacb33448c0 | -13.52265 | -48.94387 | 2026-09-19 04:59:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb88e8eb-3e94-3f01-9ea7-80cccbbedcf9 | -14.81984 | -48.56741 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92d644f7-9ea5-3fa5-ae4f-cb00f644f878 | -14.67272 | -46.6553 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e5e4fc0-c867-3fd5-aba4-c5604ee32189 | -12.97846 | -46.97786 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3e1cbe3-e1dd-387b-82b9-9eddf094fa7e | -16.04595 | -49.9878 | 2026-09-19 04:59:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fba378a4-96b8-3124-b558-b2606785a336 | -12.5453 | -47.08733 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a5b66f9-ad1f-3bdb-9f39-4cdf56a8c171 | -13.6143 | -48.32756 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f23b46e1-a7a2-3fc6-abcd-ef7bcd20da23 | -9.58883 | -60.52533 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a3e6cdd-333a-35f1-a6c3-940a4ea2ba3a | -10.9051 | -53.9874 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75104b2e-1d65-3779-a2eb-18daa0a3782a | -11.67109 | -54.44709 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6d931eb-6c63-337a-b590-9f9520136ed6 | -11.28093 | -54.12388 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7146f27-a69e-36b0-a6c8-b6dafb558480 | -15.62547 | -52.73162 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f67dc73-678e-3f83-a688-29ce20499118 | -10.85556 | -56.18264 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0791639-b5b9-39fa-a561-c3bac8782d3a | -11.8173 | -48.8369 | 2026-09-19 04:59:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02c73fea-2602-3b77-95f4-7cf63a51a66f | -10.86882 | -56.18875 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21a321f2-8dd2-32c3-8ca3-5c7614298f13 | -11.30684 | -51.72642 | 2026-09-19 04:59:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5aede24b-76a6-3a58-bc8e-0bc1b219b434 | -10.86798 | -54.09264 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbca3d9e-a31b-3e3b-b3ff-bec1e7a06c15 | -12.99613 | -46.98886 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8c768463-16bf-3870-9215-98c9b2cb20ce | -12.6034 | -50.92531 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 853aeac6-9d3c-33d2-a5ec-feefbeabe7e3 | -15.02518 | -48.55937 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 885a014b-f647-3eec-bc98-3d99d840f742 | -11.10225 | -49.45275 | 2026-09-19 04:59:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 078bf7d5-3fdc-3d10-8396-c896fa1900b5 | -10.70238 | -60.73187 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0aff3acd-6f52-3543-a62a-b830117629e9 | -10.70712 | -60.7357 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c99e7d7f-c5b4-3f0d-8d1e-78fd0a13366f | -10.69247 | -60.73487 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3591bf24-a718-35e3-92a0-29ea3be5e516 | -14.95693 | -49.93481 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b6961f0-7f99-3645-8434-b7f2a09fd14a | -11.55305 | -46.90246 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 57d16130-56be-3152-8896-258d46a4e001 | -12.97779 | -46.98316 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83e9bd18-a7f5-3667-b96b-8e95aaf8e317 | -11.47401 | -51.4802 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffe7272d-6437-3566-ae2f-2d80ad777e5f | -14.95536 | -49.93624 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94ccf57b-da30-3111-9f4d-ca4d2abc1f71 | -10.91614 | -53.98201 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c8ac6f6-32b0-3aee-ab21-604d83cc3fe6 | -10.92499 | -53.96909 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78a477ca-cbb0-3e4d-902c-9405d43f4360 | -12.55576 | -50.68929 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5893a282-1ec1-3a96-afd9-349de841c1b0 | -16.30558 | -53.85632 | 2026-09-19 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 642b49a1-ab03-3956-9489-6634960f03c6 | -10.71599 | -60.73445 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20b1dd58-64b7-307b-9b15-5fd9287ac537 | -14.66782 | -46.65464 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f06d6ae-0a42-34e7-962f-9b63e046bd02 | -16.80402 | -46.99226 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3b50b3a-b6b3-322e-ad6a-0a67c9787655 | -11.11143 | -49.44402 | 2026-09-19 04:59:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33fa5936-0c70-374b-8270-656e3772fb67 | -9.37576 | -60.3222 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ef6750a-b2f8-3520-a7ab-44a959d9e930 | -13.68297 | -48.58446 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f80d5ed5-7032-3500-a1d5-2b437cc88412 | -16.09545 | -49.64268 | 2026-09-19 04:59:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85741a39-c491-317b-83fa-21c131ab943d | -11.41397 | -51.45076 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26b36997-3fff-36e7-b635-46a17317b053 | -12.16471 | -46.96834 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63125e6e-d17e-34bf-834e-1592c365922a | -11.05898 | -49.75078 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79de65ac-0e79-343b-8874-0ed9d38069d5 | -14.67977 | -46.679 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 548c7107-80af-3f7c-800c-6b2ed279f383 | -10.89474 | -50.88823 | 2026-09-19 04:59:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47d288d1-c843-37e0-bcfa-e82482d87a78 | -13.02155 | -46.97658 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d06a1bf4-87a1-366b-8bbc-61f00d5e09ac | -15.66514 | -52.74089 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cdf77f8-17b1-37de-81b2-932b933c7170 | -14.68745 | -46.65725 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c06d595a-8873-34bf-8a9f-95bb13722321 | -14.93175 | -49.94157 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23ffaf6c-8190-36b7-aeb7-92934af0d1e2 | -12.99063 | -44.83395 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 970e57d4-8f5c-32ea-88b2-a0f215d7032b | -15.6295 | -52.72831 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b63c341a-d07d-3618-b6a8-e4cd12bcb26f | -12.57866 | -49.11454 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bafa3025-16df-398c-810c-e5ad05b226aa | -13.39786 | -48.03657 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9514ee88-b576-3dea-b184-de76e7657901 | -12.10458 | -52.55846 | 2026-09-19 04:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8634af48-8de2-33ce-8b02-9a518d3a8086 | -12.12385 | -45.15779 | 2026-09-19 04:59:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dab5f7b4-4303-3225-8f37-a59994ad4ddc | -11.90822 | -50.12378 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9b6b8d0-7840-367b-af4e-bf40264d860d | -16.09088 | -49.64571 | 2026-09-19 04:59:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9469734a-dabc-32e8-9707-9a66455915aa | -11.30202 | -54.88104 | 2026-09-19 04:59:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45890807-f42e-364b-9457-e2e5fa0ee327 | -11.20279 | -55.03334 | 2026-09-19 04:59:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50fdb62d-0061-3b60-9d25-fe97c9e6da47 | -13.59077 | -46.94222 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73b20802-0842-3261-8603-499061b953ac | -15.02725 | -48.57686 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f83f13ad-1c24-315f-bedc-d08ba6c808c7 | -15.59124 | -56.56572 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66e62a11-cdb7-3a10-9748-876d6e9ca038 | -10.87129 | -54.09318 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b8cbbe3-50f2-3bf6-9549-364ab716b0c7 | -11.05966 | -49.74607 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README92.md)
