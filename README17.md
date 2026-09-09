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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b60e2ea6-b098-3421-94c8-54f78bf31f8a | -12.35251 | -48.20402 | 2026-09-09 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3b9875d-03b4-3545-a364-f2c5a5885e44 | -18.02251 | -44.61498 | 2026-09-09 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ade557f-e2f2-3b85-959c-8c4f2a367739 | -18.02028 | -44.60692 | 2026-09-09 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4226c87b-aadb-37ff-9b02-37a012beace7 | -12.43703 | -43.41326 | 2026-09-09 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa491361-add3-359e-9982-912cc5cf29be | -12.35328 | -48.19953 | 2026-09-09 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eee0a2a2-02d4-3e01-86c9-13c356818a2c | -12.95445 | -48.61854 | 2026-09-09 04:27:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b61cd9f7-fac1-31b4-a84a-949b89261089 | -15.99556 | -56.41961 | 2026-09-09 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 14f7305f-495a-3b57-baf3-dd22cec65f84 | -13.4065 | -44.16017 | 2026-09-09 04:27:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26219df0-2d3e-300c-abe2-27e4727c09a4 | -17.59569 | -44.66798 | 2026-09-09 04:27:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffb4469d-2948-3ab0-9895-108ff3adb343 | -14.61927 | -48.86356 | 2026-09-09 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cab2ffb7-c299-3cf8-b7ac-64c8ca983a00 | -15.99465 | -56.42391 | 2026-09-09 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 228fdac2-61d2-3120-a3f7-2b792142390b | -14.90896 | -44.67544 | 2026-09-09 04:27:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33f4bded-3bf0-361c-a2e1-fbc0b23aa599 | -13.40984 | -44.16072 | 2026-09-09 04:27:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e9855f8-4d65-3cc6-ab13-c3824f1c31ee | -14.61844 | -48.8683 | 2026-09-09 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 975925bd-5610-389d-be94-52ab7d72ca1c | -12.43561 | -43.4128 | 2026-09-09 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbb28d51-6b35-374b-8f17-b6bf26ee0603 | -13.81396 | -42.17307 | 2026-09-09 04:27:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fcdc6b81-4ef0-36ae-9e99-94409a8bff01 | -14.91285 | -44.67241 | 2026-09-09 04:27:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd3c86ae-c1db-32cf-ba44-e3da27da51f1 | -12.2752 | -45.81536 | 2026-09-09 04:27:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a9311b2-d358-3c8e-8a30-e272f1626658 | -12.85578 | -44.39571 | 2026-09-09 04:27:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cf8260e-08aa-3c58-b780-a13725ed9bad | -14.91341 | -44.66882 | 2026-09-09 04:27:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4d0998a-8874-3635-8c78-35b2c1a5d23a | -14.29041 | -44.58922 | 2026-09-09 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c62c81da-1438-309e-b628-c5ad75bca917 | -12.49649 | -43.77256 | 2026-09-09 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe62a215-e117-3822-a0c4-fcb058ae0f20 | -13.41095 | -44.17555 | 2026-09-09 04:27:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a78f8366-5498-3520-bd45-2cf548cecb82 | -13.0489 | -41.41671 | 2026-09-09 04:27:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 780724e1-0ce0-3cc3-9f0f-e762435747fd | -12.85245 | -44.39516 | 2026-09-09 04:27:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a92f5b0-28ad-3979-8074-6df965a2bf2f | -13.77468 | -43.64523 | 2026-09-09 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4b302b9-4920-35fd-86eb-03c56a041a41 | -12.43505 | -43.41642 | 2026-09-09 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72e4785f-d4c1-3602-b06c-a44b7bf04c82 | -14.28375 | -44.58811 | 2026-09-09 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b04ebd42-2645-3124-a829-5054d9237b43 | -12.9515 | -48.61315 | 2026-09-09 04:27:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6eb55bfd-7cc6-3b9b-8949-5ac442cf6ae6 | -15.98791 | -56.42684 | 2026-09-09 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bb0af590-d1cc-3f9e-8c51-7405008de3e7 | -14.28708 | -44.58867 | 2026-09-09 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be04881a-b51e-3b49-9cd0-ab1e8cfc37db | -18.02084 | -44.60319 | 2026-09-09 04:27:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb6187c6-bb27-337f-bfb7-a1e9be5142b3 | -14.90952 | -44.67186 | 2026-09-09 04:27:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eba90137-8255-325b-aca1-eb930798ac95 | -13.41039 | -44.17913 | 2026-09-09 04:27:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96c671df-ea4a-33ed-8ee3-36027cd7f606 | -13.81322 | -42.17153 | 2026-09-09 04:27:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d89f739-725e-377a-9e98-41d430c785cb | -13.81677 | -42.17199 | 2026-09-09 04:27:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5d164185-3778-375f-b636-28956a78f086 | -14.91675 | -44.66937 | 2026-09-09 04:27:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a23da1-b9c8-3397-8e4e-bd0ca76a8433 | -12.95526 | -48.61383 | 2026-09-09 04:27:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5e10a63f-a0e0-3751-8dff-e91831a86a7e | -22.70205 | -43.36233 | 2026-09-09 04:29:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 06f80625-82bc-3824-8e0e-c227cf82201f | -28.56069 | -50.51434 | 2026-09-09 04:32:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 14e0bb2c-35ba-3bfc-b083-f19afbbbee89 | -29.11068 | -51.90983 | 2026-09-09 04:32:00 | NPP-375D | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d62993e-9368-39a3-b074-3b4f373550aa | -27.45613 | -48.45395 | 2026-09-09 04:32:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e82a20b-cfbc-39be-9f81-4eeb3de407d0 | 2.51585 | -50.85563 | 2026-09-09 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed34f9d-ff78-3a2a-a3c1-e1ef287fba0c | 2.5152 | -50.85144 | 2026-09-09 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8845ca82-d765-3984-9e48-4384b603b731 | 2.51158 | -50.85202 | 2026-09-09 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f33b1ec0-1839-3ef2-b36b-26beb5696845 | 2.51222 | -50.8562 | 2026-09-09 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9394016-c087-3c7c-b350-5fb3e91336f8 | -3.36931 | -59.42459 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8709df85-f62e-341e-89e1-a369b70a6c4d | -2.93658 | -50.47112 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04d6d2b0-3ad0-3558-95f0-411c8f579179 | -2.94452 | -50.46495 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b7ee9005-7c87-3197-b8e6-f645426b1905 | -4.02156 | -50.44223 | 2026-09-09 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 285ddce5-b5ff-381e-85a9-e36c519c0002 | -3.8131 | -47.4824 | 2026-09-09 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 410c662f-8b99-3805-b5f4-8d48eb5251a5 | -2.10696 | -54.38514 | 2026-09-09 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c12d7a97-6fb2-3c9f-9984-d61749ad9e6b | -2.76611 | -48.5733 | 2026-09-09 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd2e1bae-e69d-34e8-89a4-7a7c0cdf1a96 | -3.36282 | -59.42765 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d0c3afd-2172-3e8a-b544-9913d52d17e0 | -2.93716 | -50.4675 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d4d0105-6be4-3529-99e4-9e7cb41812ab | -3.80051 | -52.40667 | 2026-09-09 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48c05316-502f-325f-ad8b-ef113808fe71 | -1.03641 | -53.73825 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8822c4b6-b245-32f6-86a6-a51729a5d11a | -3.68318 | -58.52718 | 2026-09-09 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40adceb2-a782-33ff-937f-ec56cd8d82f6 | -1.11581 | -54.08355 | 2026-09-09 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7464afec-87d8-360f-a6ea-97c5d814ee35 | -3.06626 | -50.33981 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65cba9d8-ab85-3af0-a937-b743879ac0cb | -3.24322 | -47.24706 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89879e4d-cb23-3f73-ae1b-cc59a75f3229 | -1.03285 | -53.73416 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22144850-375b-3325-b2f6-923d1d3f4ec5 | -3.81193 | -55.89623 | 2026-09-09 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e41ae770-b089-35c5-b9a0-46a3d67bd8d1 | -5.20143 | -49.32841 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f676b58-2a80-300e-9bbe-68c93e1e5f8f | -6.25342 | -47.34774 | 2026-09-09 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04c0668b-5164-3a73-a2a1-90492b635249 | -2.55882 | -54.74593 | 2026-09-09 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e811d3d7-a69b-3899-82fe-b3504d9d2c46 | -3.24662 | -47.24759 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aef8d855-deeb-3c10-9df3-7cdcfbd7f663 | -2.9422 | -50.47946 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f6eac63a-ebe2-3046-8926-b10be5fa0673 | -4.53919 | -54.93207 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fbe74e8f-aed8-3227-b573-3b82cf11c4ae | -3.36072 | -59.43763 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28c1e035-71d9-36cc-983f-932c3b38e17f | -4.49361 | -45.91749 | 2026-09-09 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2857ea73-ad3b-3c13-99a3-994adbde6238 | -3.25168 | -50.82343 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 14b55cd3-7447-3fee-a644-60207980e375 | -3.83146 | -59.40704 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7450ac5-6265-32b3-869d-96b529c8efea | -3.72263 | -45.27319 | 2026-09-09 04:44:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3af1d4d4-8707-3dfa-8cdc-78722ae2aa67 | -6.83325 | -39.40887 | 2026-09-09 04:44:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a29201c-7dad-3d31-af95-f3d6d4b1bac4 | -5.55177 | -46.28315 | 2026-09-09 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d03a8df5-ced7-31eb-96e9-d6ab2a5c1a19 | -5.64488 | -44.30103 | 2026-09-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbee1b1d-bcda-344e-9ab2-e5b8a6418677 | -3.2404 | -47.2429 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 389a1420-4103-331f-83ae-1bced5e60d28 | -2.84132 | -53.99423 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07b70ce9-754a-333d-9f58-e3f6cbe6d884 | -3.238 | -50.60322 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13b1cb0b-d480-351d-9dc4-ac67f654f7a3 | -6.76063 | -44.56731 | 2026-09-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa6016b1-2c73-327a-8ede-7b86f0a1e4af | -3.54538 | -48.17842 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c24608a6-1832-3a84-81c3-589e77d43280 | -3.97096 | -47.58797 | 2026-09-09 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aae0827-16ec-3c5b-a43a-10c9ad72c352 | -4.43976 | -54.82584 | 2026-09-09 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b6aaa56-1e98-3b19-9528-9ace08b984d4 | -3.62188 | -53.38572 | 2026-09-09 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe1aee6-da87-36b0-82ce-2d24bc40ab4c | -2.72331 | -53.97584 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c5b8f7-b1a6-3267-a851-2669b74d2e07 | -6.16264 | -44.64579 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d170cf0c-3ccd-3616-97ab-78bccfadfd37 | -4.02321 | -50.45347 | 2026-09-09 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91ac37b3-3588-381d-9a17-78ba4550ef0f | -4.98476 | -50.64524 | 2026-09-09 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d42ad3aa-ac2e-39ff-8001-18b86ed45d23 | -2.79723 | -49.57836 | 2026-09-09 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ae9e377-eaef-3455-a456-11c5029a2b5e | -3.24265 | -47.25069 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0034f867-79fa-34e6-aa41-218f7c346593 | -3.80815 | -55.89082 | 2026-09-09 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb2322c3-5768-32c7-a393-ab27248a8d00 | -2.79778 | -49.57488 | 2026-09-09 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c6c6398-a351-36d4-aa17-528de2046cff | -3.67713 | -58.52974 | 2026-09-09 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02ad4269-b753-3bee-8c26-1682dbb31496 | 1.81979 | -50.954 | 2026-09-09 04:44:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff227ffb-e4ae-3679-a2d9-7862441c6387 | -5.7745 | -45.06743 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 692eb885-4853-3db1-903f-fdf0e075aa6c | -1.1905 | -55.7145 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ad6db64-be6d-3925-8aa9-5760d95c400e | -4.11207 | -49.06424 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 955d0167-0a50-34d5-9aae-87b2f525bb43 | -2.92981 | -50.47004 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 639b9eca-2486-3b60-aa89-d43337c59f2e | -4.48997 | -45.91693 | 2026-09-09 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README18.md)
