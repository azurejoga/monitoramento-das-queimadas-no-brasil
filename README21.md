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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3a2fdd5-e72b-3c0a-8f30-a017a41915c7 | -11.58058 | -52.10962 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a21a223-ed07-3161-8012-2edae6f19c9f | -10.88122 | -53.77536 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f5e670e-313b-3541-a69e-9a67c9fc9636 | -9.07019 | -49.41932 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ec5367d-74e6-39b3-859c-e404561a32e8 | -8.2249 | -47.219 | 2025-06-27 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8543d9bc-2f06-38af-a654-d01db96244b3 | -11.77876 | -55.03661 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c54899-57dc-3cc3-948c-c5c22218b147 | -13.70405 | -48.40024 | 2025-06-27 04:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa25e512-2722-3648-992b-67c4853bc7b2 | -11.80924 | -57.35268 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e21a574-bcdb-3f92-aa6f-42dd03f8ec6d | -11.06343 | -55.37373 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b16d353-7528-3e82-b843-0db9415014e2 | -12.01205 | -47.16008 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b775f9e3-8ea4-3677-9485-8e60ad79cb9d | -8.61915 | -51.58122 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 579a8177-dde7-3ed6-91d5-b7525d757964 | -12.0358 | -48.75273 | 2025-06-27 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ac04a36-4902-3de5-8c90-2e3fd22ecfb2 | -12.00798 | -47.15945 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3b24f01-5303-32b9-a515-120cf58d1897 | -10.60231 | -52.83749 | 2025-06-27 04:49:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80bcd62b-46aa-3f3e-8de5-6475482974de | -14.21006 | -45.50893 | 2025-06-27 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbd5a13b-b486-35fc-9362-638acce20305 | -11.43168 | -54.47983 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beb817be-f90a-31df-a4c6-5978790e3667 | -9.16997 | -61.40373 | 2025-06-27 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6977a46-15a9-3a4e-9275-dcd178c296d6 | -10.62597 | -46.70562 | 2025-06-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 490beb02-1488-3ed1-b626-44762c66515f | -10.25981 | -44.63665 | 2025-06-27 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 226b6d7b-f745-3f1f-8b0a-97c3314cc5a1 | -10.52375 | -53.62976 | 2025-06-27 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cce8221-c18b-3946-8338-665047490b4a | -10.80527 | -57.75483 | 2025-06-27 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f2c5822-1aec-33b1-9a7b-2d6c516fd225 | -9.12101 | -49.44661 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bd67a85-b723-3c51-932c-e5e80e1264fb | -12.00292 | -47.16615 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8e21274-43e9-35f9-80a4-ceda2df3170e | -10.86183 | -54.29634 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e62de59f-6248-3144-ac76-589d5c1904f7 | -12.1367 | -54.66739 | 2025-06-27 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f7d8ecb-ebfc-3d85-913c-1bb000f7e789 | -11.57892 | -52.12017 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 9440f543-b9a1-3b5c-abeb-438a915892c1 | -10.37213 | -51.81087 | 2025-06-27 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7833ed53-334b-3100-8b66-0e00071f71df | -11.67498 | -46.73122 | 2025-06-27 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c4d78a6-d732-39fa-94b3-3134f336bc64 | -11.89529 | -48.25663 | 2025-06-27 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 348e1e65-3efc-3bb4-91cd-73958844f8f5 | -14.20577 | -42.78105 | 2025-06-27 04:49:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a97122a-a184-3580-9c4a-a80d69a95495 | -11.05836 | -55.38281 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36003f33-f845-3647-a7a9-a96173339019 | -10.85579 | -54.03257 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d46336f2-d28c-3432-b0cd-f842dd950249 | -12.02356 | -47.77515 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97042bc3-ef31-3ab2-bc8a-a442be8732a5 | -10.52836 | -53.62295 | 2025-06-27 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbdaba4c-e622-3192-b634-fda9befbc73c | -10.4196 | -48.619 | 2025-06-27 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d57c8d5a-b8d9-35cf-9941-d052131558bc | -10.86467 | -54.30077 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7331148-1a11-3314-91ca-672107f20d38 | -10.70892 | -59.13461 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28b78de0-0e74-3e65-b9f8-1463e6c444de | -11.06197 | -55.38222 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f16832b5-ec79-39c2-ba49-8d4ff0011aa1 | -11.77522 | -55.036 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b087eaa-91ca-3234-b389-1557d8ee229f | -13.28783 | -44.60791 | 2025-06-27 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e123829-ec4d-3fd9-8717-470fe2bca79b | -11.17869 | -55.91518 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9af39d9f-a30f-3f74-bb94-27b384e6a2b5 | -10.82913 | -53.75128 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b0d28e0-3a5b-3dd3-90e6-b0ff629a36cc | -12.00033 | -47.15459 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a4cc206-1879-3ded-a247-8ca89380275d | -11.06199 | -55.38343 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e8fa18e0-6760-3478-843b-408f420ab113 | -9.07131 | -49.43526 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b5e687a-f111-3831-9c06-75073525e071 | -11.05834 | -55.3816 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5f45736c-52b8-308c-b6a0-5a9c93925068 | -13.58715 | -45.25923 | 2025-06-27 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a7e25dc-7b4a-39e0-a399-ac52a70e8a74 | -11.81546 | -47.52927 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5751c35-d278-3e74-9ab7-e8ccd446eb38 | -10.86819 | -53.76932 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bb2ef92-aac3-32dc-9d5f-73f404b7804b | -10.71355 | -59.13536 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5fd0e99-c2f7-3c13-953c-cf7391b2f1aa | -8.61748 | -51.57023 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72d8f33f-2c57-319e-80af-2bfb1e1efb05 | -12.02821 | -47.77063 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e5aa392-566a-32c7-ab19-104315ddba0f | -11.17794 | -55.91966 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 871104bd-20a9-3da8-b048-d57019736a09 | -9.07367 | -49.41985 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a0aabbc-f5dd-3166-aea6-b3ff53af106e | -13.16418 | -45.22698 | 2025-06-27 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 083c38dd-4857-3032-9035-a03db3fc9e07 | -10.29839 | -57.13321 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed29b87a-8c82-313b-8c56-e67da5d1d121 | -9.35074 | -58.85375 | 2025-06-27 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7caf50d-ae68-3b97-87f1-bd6c3bacac9f | -10.52775 | -53.62664 | 2025-06-27 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a23a5cf-85b1-3b25-93be-812210f9fd34 | -9.06624 | -46.91384 | 2025-06-27 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99434ead-222b-3fca-82ee-f7dfba83e6bd | -13.5777 | -45.25782 | 2025-06-27 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e74e0e54-e3ab-32c8-89ee-69ae281c0217 | -11.57837 | -52.1237 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| bac32636-9172-36de-8d47-a817e2d173c9 | -12.28545 | -48.80444 | 2025-06-27 04:49:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fdc0ba6-ccb8-337c-8aeb-da4b98a853a0 | -11.83823 | -43.79743 | 2025-06-27 04:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24ff2da2-c7d6-348d-9e96-0137c62f833f | -11.57061 | -52.108 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cfd261f0-1721-3c2b-b333-b0cb3175192b | -11.26827 | -52.45614 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c651abac-79a7-3afe-82a0-780f00efba62 | -10.70805 | -59.13947 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a145688-30be-33b1-886f-7e58b118c53b | -10.29777 | -57.1368 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c39c394-0f19-37eb-900a-f1dbdd3d62c4 | -9.37466 | -48.54345 | 2025-06-27 04:49:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79f18af2-cb99-3ba7-bc11-8c3faa6cfa43 | -11.8084 | -47.52194 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ec476d7-76ff-3ad0-bb2c-52eb0ad6f2dc | -11.0598 | -55.3731 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 72c3e2e4-5262-37b3-b084-d9af63eb5800 | -9.24052 | -50.03705 | 2025-06-27 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1be39456-158e-34aa-9e68-7e9b64a0a493 | -10.81793 | -53.7342 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26b85544-ec2d-3459-a9a5-39bfc59a73c4 | -11.77945 | -55.03258 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b078d9b-bd97-3b97-a5cb-e1a89f11735e | -10.82633 | -53.74701 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06665a52-dbe3-3728-b502-853912bae007 | -10.86759 | -53.77304 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8470d77-f6a0-3b72-b291-a2af439fdec7 | -10.29369 | -57.13616 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7afbab70-758b-3b9b-9b33-9b168f65f33e | -9.11927 | -49.43455 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25967728-fde6-3efa-88cb-a77f4521dbb8 | -8.61583 | -51.58069 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf98902c-b6e7-3ee2-81f1-1d056781c056 | -12.00008 | -47.15902 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2792dbd-d265-3897-b7aa-5df33fdc9d8d | -11.80499 | -57.35226 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcd14ae3-dc89-3b36-b61b-82bf87a02ed6 | -11.80459 | -57.35545 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22c94da1-644b-36c4-964b-25b30f4cce73 | -11.91873 | -54.80866 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 008bb4c2-79e5-31f7-a1e0-68c1b57201eb | -8.47845 | -48.26709 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d5e01e1-60d2-35bd-b48c-1d36aaf46fee | -12.00311 | -47.16693 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dbc9d92-cd64-34af-90f6-97786e25eeaf | -11.05977 | -55.3743 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9474d16-ed96-3178-9001-d1572fa85eae | -11.57172 | -52.12262 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 930722c7-7a02-3f25-bb60-42f9509942a5 | -11.17495 | -55.91457 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f22853a0-26e7-378e-8d62-1d9ac40fb7aa | -8.33434 | -55.09734 | 2025-06-27 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be3ad6de-5510-3be0-bd82-436a3bf57ccd | -8.62669 | -47.44781 | 2025-06-27 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9bb0fa1-cc4d-34ac-9de7-0ed436892d78 | -8.67398 | -49.95575 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32d7b7f-52a9-3329-8602-bbcf1e3a6a8d | -11.43928 | -54.47712 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c787223d-1e82-353e-a57b-72b6d17864f1 | -13.58242 | -45.25854 | 2025-06-27 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b336d086-fd77-3bdd-90d4-16b6d301636e | -9.16932 | -61.40722 | 2025-06-27 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 626cc526-b957-310e-93eb-6c7b99650f3e | -10.2592 | -44.64117 | 2025-06-27 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 048bb16e-e72b-30f8-afe5-2becee23f2b9 | -10.62492 | -46.71305 | 2025-06-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 112af729-0ec3-38b1-9764-0d37cdc89de3 | -11.5695 | -52.11504 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db3dc08a-df28-3277-a1bc-042331a1a3ef | -8.4438 | -46.97459 | 2025-06-27 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9d6c81c-bb15-308a-82d8-c7779e3ddc53 | -13.04869 | -48.82056 | 2025-06-27 04:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9908c633-7f3e-319c-9501-6eee48fe61c2 | -10.63219 | -46.69135 | 2025-06-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0867296e-4db8-3aa4-a05e-5aa07963dc7a | -10.82117 | -49.1001 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 404eadf2-d70d-3c2e-8c44-5e1ca9857adc | -12.01155 | -47.16372 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README22.md)
