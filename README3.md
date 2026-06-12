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
| fac020ff-78b3-355b-bfb9-1f99050e9d99 | -6.99845 | -43.86477 | 2026-06-12 03:51:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1e664e0-775e-3dd3-890a-68e66b19bd37 | -9.3061 | -48.97725 | 2026-06-12 03:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e160204-2fa8-3415-811a-94f299eca93c | -9.07012 | -44.74451 | 2026-06-12 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5093658a-5873-3b27-9f36-781327198242 | -6.56855 | -47.92199 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e739d00f-6079-3098-8ddb-2b781c157dff | -6.43603 | -44.56519 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 509156e3-b4a4-328e-a724-e4970812a77e | -7.35303 | -47.01374 | 2026-06-12 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2445e38f-f82d-3c65-9f4e-eac34a8f1fe5 | -6.56451 | -47.92147 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33fafd06-39bf-3fa5-a505-fcc5eca77d9d | -6.44396 | -44.56835 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe722d9a-717e-39a0-aa06-8950982863a2 | -3.50627 | -48.03621 | 2026-06-12 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b382df95-4d17-36bd-8ed6-ea7e7082d358 | -6.43722 | -44.55837 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 034a7053-b602-3906-a398-e0bab970f69e | -7.72201 | -44.16731 | 2026-06-12 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baefc4c8-fcdb-37c4-96ea-26d334bc547c | -6.18654 | -44.86374 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02efc81d-d7b6-3b10-9a36-4d92d98d4f59 | -9.31399 | -48.97255 | 2026-06-12 03:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 982d4078-9371-314a-84c0-bd8e994bde5f | -6.44678 | -44.5667 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ece35256-c84b-323b-823e-a5c4743644ad | -7.33287 | -47.05355 | 2026-06-12 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6255829d-8585-319c-99a3-cb3eff7c6ba3 | -3.49802 | -48.04235 | 2026-06-12 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4953a73-5455-3d06-a43c-7bbc14ced208 | -3.49999 | -48.03857 | 2026-06-12 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b247e8ec-f766-3151-89b2-55b184a5ca59 | -9.06498 | -44.74344 | 2026-06-12 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3125a42d-34ad-3b6b-b2a9-f637c80c6f9a | -7.72255 | -44.16433 | 2026-06-12 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e3626f9-e29e-3f81-ac0b-a94ef739e786 | -7.63882 | -45.30294 | 2026-06-12 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f6f94b2-27aa-3797-a72c-3a1dcd5ea85a | -8.03166 | -45.03994 | 2026-06-12 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13e8c0ff-8522-3f19-8a54-c35ecf72924c | -3.50695 | -48.0397 | 2026-06-12 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52aae78b-c0e4-3c90-b5a6-c80295ba4965 | -4.48805 | -44.21472 | 2026-06-12 03:51:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 124de5e3-7fc3-3a89-a21f-09b8dd78a713 | -9.21052 | -48.58686 | 2026-06-12 03:51:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d99bcdcc-20da-3767-b0e1-ba335cc76674 | -7.32764 | -47.04736 | 2026-06-12 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d21f90b-2a3f-3e71-b894-e57c9db527d8 | -6.58295 | -47.91787 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a54e9e5d-b26f-3dd7-adf3-5a2d0344f4e4 | -7.00717 | -43.86596 | 2026-06-12 03:51:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b167af46-df16-3e39-98e7-0964113dbab7 | -6.39726 | -44.17239 | 2026-06-12 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f3918f7-1ab4-35d8-bfc8-c16abf7920bf | -7.33198 | -47.05831 | 2026-06-12 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0363cd09-316c-3e80-9446-3d20074b03ba | -6.5723 | -47.91614 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87224216-1a34-3fbd-ad60-875bb888d5d2 | -6.72579 | -44.38047 | 2026-06-12 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ce6d420-01ae-36f6-8a8e-2d04522c6401 | -3.49873 | -48.04591 | 2026-06-12 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd5e2b25-3222-3fe7-a449-049d202863bb | -6.57112 | -47.92255 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9965d51-6b19-31a6-9ff2-f71cb3dfe80c | -6.44619 | -44.57008 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6ab4414-3ff8-307e-8ac6-4017d4b28f74 | -7.00349 | -43.8657 | 2026-06-12 03:51:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b607507-d373-3900-9dcc-697fd3e1b274 | -6.18719 | -44.86014 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c7e456a-e1d5-3e0f-89a8-8ce2d92022f9 | -6.5789 | -47.91722 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b23877c-7063-34c9-ad2f-6d1e7038a838 | -7.34603 | -47.01714 | 2026-06-12 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c545ebde-aed7-32d6-a8c1-617af9d641fa | -9.21267 | -47.92107 | 2026-06-12 03:51:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cedb992e-954d-368f-88a5-74c6fd8087a0 | -9.31275 | -48.97878 | 2026-06-12 03:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8edb737c-f33d-3e5a-b4bf-ef3408b6a6a4 | -6.56979 | -47.91546 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0960c21d-a2cb-3586-8e31-4cbe560935f8 | -6.99895 | -43.86185 | 2026-06-12 03:51:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a749a67-cc88-3242-950b-d35bed796098 | -7.3381 | -47.05975 | 2026-06-12 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01033dc1-4290-35cf-8271-9f3e29b162db | -6.57638 | -47.91661 | 2026-06-12 03:51:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fea6b93-e3b3-3319-ac0d-aa07773d94fe | -6.43781 | -44.55497 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76ed528f-da81-3fb7-b09c-3c79752aa826 | -6.19169 | -44.86477 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a648250-256a-3e4a-8adf-e21af11a5aec | -10.30603 | -40.72139 | 2026-06-12 03:51:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f1681e2-33d8-3607-8503-e2e8d0cd7ad8 | -8.03105 | -45.04327 | 2026-06-12 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01864485-1dc0-3627-a44b-d17faceb0076 | -8.02569 | -45.04229 | 2026-06-12 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ca7c945-cf6f-3c29-9ee6-c4531355b17b | -6.44141 | -44.56593 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40fd2aab-850c-3c1f-b594-b28a3eb5eae6 | -5.79875 | -45.11397 | 2026-06-12 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48e7525a-6232-353f-9d50-fdef47540339 | -7.00212 | -43.86506 | 2026-06-12 03:51:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 423faa28-9313-3222-971c-70679760d7b5 | -7.72147 | -44.1703 | 2026-06-12 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35275ef4-093a-33cc-b10d-c5f474c4b42d | -7.64565 | -45.29665 | 2026-06-12 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26a6bd67-9172-372e-b5e9-749f1f4cfe58 | -9.30733 | -48.97102 | 2026-06-12 03:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04ff8a71-cfba-349a-8a09-d50b0bd6ca59 | -9.06442 | -44.7465 | 2026-06-12 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a54d7be-75fd-3436-81df-45e333343226 | -9.21166 | -48.581 | 2026-06-12 03:51:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2773003-ab1b-3976-b148-eeef157cacfe | -3.50497 | -48.04353 | 2026-06-12 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3dee5335-e8bf-31d5-99dc-20a1b427c6ec | -6.19203 | -44.86458 | 2026-06-12 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 288026f3-e07f-36c5-8b0a-3583a3d7f5e7 | -10.93068 | -44.67291 | 2026-06-12 03:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c2e873a-6751-36e4-944a-021d05c2e909 | -16.62165 | -43.41374 | 2026-06-12 03:53:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c03eadc-1603-3534-b59a-76a0ca09dca0 | -11.79435 | -40.08109 | 2026-06-12 03:53:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2e471bf-ec1d-3fd4-8c01-06ea4fad4c23 | -11.79802 | -40.08173 | 2026-06-12 03:53:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8971e34d-f446-32e5-a524-f391b887bc12 | -11.54438 | -48.26999 | 2026-06-12 03:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70388e81-5e53-3407-980c-56221e7b3029 | -12.92819 | -43.62061 | 2026-06-12 03:53:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01b53a0e-3046-3ac7-bc04-33bfc2a90de7 | -11.5456 | -48.27317 | 2026-06-12 03:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d186565d-1ded-3e84-8a51-6de03f32d2d4 | -12.85576 | -44.37515 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| e5f1691a-5826-304f-b485-0557fe91c69a | -9.45614 | -48.38919 | 2026-06-12 03:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b299465c-47a4-37d6-bd3d-3f0d51c4e5e1 | -12.86141 | -44.37096 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 51425583-8db8-301f-9af9-f276a667bf62 | -15.19351 | -42.29016 | 2026-06-12 03:53:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0dc6e60b-0743-3aa5-92b4-761ee9fae14d | -11.80332 | -44.95388 | 2026-06-12 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc5f1947-8a21-3efd-8ed4-7fa19b7f3743 | -10.71965 | -49.48659 | 2026-06-12 03:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af1d0971-8944-3c5b-aaf8-8c46385284f0 | -9.46259 | -48.39053 | 2026-06-12 03:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f8bf747-1714-3108-931a-2816de099088 | -15.83702 | -42.00021 | 2026-06-12 03:53:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 51d38306-7a74-3be2-ad17-98ef3b19d426 | -14.07607 | -39.50226 | 2026-06-12 03:53:00 | NPP-375D | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 52229383-1faf-31f9-9177-bb84360fcde6 | -10.71288 | -49.48537 | 2026-06-12 03:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f76a44c-624a-33e4-9702-b3a22f3c4edc | -15.07039 | -41.974 | 2026-06-12 03:53:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 203492bf-ac66-3209-803d-fbb3dda40b74 | -12.852 | -44.36906 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31f6b65b-be2c-390c-a3c8-106bf725309b | -9.69718 | -47.69761 | 2026-06-12 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67a9826c-bb72-3af7-b2c4-6caaad112455 | -10.89617 | -49.4866 | 2026-06-12 03:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5c845f0-7255-35a3-a79c-00421c4fe957 | -11.00285 | -46.7468 | 2026-06-12 03:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e408738-4e31-31ec-bba2-3cbca867c56c | -11.90869 | -43.73881 | 2026-06-12 03:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8574a6d-8a61-31b8-959f-f1fa862f417f | -15.07246 | -41.98493 | 2026-06-12 03:53:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5ed4576c-a575-3a9c-83fd-f21ec229f3b6 | -10.9898 | -46.74549 | 2026-06-12 03:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe7a0d3f-583e-38b2-8eaf-2e2cba774d0c | -12.3155 | -46.07333 | 2026-06-12 03:53:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e006919-5080-34eb-abe4-33b6862fff74 | -15.84297 | -41.90029 | 2026-06-12 03:53:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06bad8fb-e4fe-3874-a0f6-88d0c2312e6b | -10.7184 | -49.49268 | 2026-06-12 03:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b359c26b-10ac-34a6-8e55-01ed8117eebd | -12.8567 | -44.37001 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| f7217f6d-66c1-3f76-a6fa-2026366e6640 | -12.85693 | -44.37123 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| b1e66745-92d7-3742-a1c6-283d769880ac | -12.86261 | -44.36707 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 29da7335-4360-3375-9caf-45f68c6a43b8 | -15.4355 | -41.37942 | 2026-06-12 03:53:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d47b80d7-470d-3098-bc12-d9a879e8960a | -12.31483 | -46.07675 | 2026-06-12 03:53:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 45b90049-65c3-3906-9e71-eaf544869c8b | -15.84709 | -39.02935 | 2026-06-12 03:53:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4aebdc01-a94b-3032-a336-3ae6b1acd299 | -11.0012 | -46.74764 | 2026-06-12 03:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2f913bb-e506-3ab7-9fd2-85e7c55eb931 | -15.07337 | -41.97985 | 2026-06-12 03:53:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c04f58cc-5cd0-3eed-9ca0-01e13a14049f | -12.85791 | -44.36613 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 712c81d1-216d-3a02-9453-60e8cd56d38a | -12.86164 | -44.37216 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 6ecf2688-06a9-3e00-88b2-c5d690a808f4 | -10.99551 | -46.74652 | 2026-06-12 03:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a6163ca-8b09-3a74-9b32-9ae1b932a7ec | -12.85223 | -44.37029 | 2026-06-12 03:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 514c28c1-29c7-3cea-aeb7-00b22849e934 | -15.83916 | -41.89944 | 2026-06-12 03:53:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README4.md)
