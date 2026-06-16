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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af553849-75f4-394e-9913-38e7bb5f6e7a | -6.17699 | -48.50743 | 2026-06-16 05:23:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f30070b-48f9-3241-8295-8e1e96770a8c | -11.26615 | -53.95383 | 2026-06-16 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 445b8aa6-edb8-3ab3-aa3a-0c912056cc5c | -6.18275 | -48.51272 | 2026-06-16 05:23:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47de9fb2-18e4-3e71-a94b-e2d97efde96c | -6.14175 | -48.52916 | 2026-06-16 05:23:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6b7e3d1-53c9-33f4-90ee-efef566ee60c | -6.1425 | -48.52348 | 2026-06-16 05:23:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1821ab8e-46ad-3809-97c4-593790c20c39 | -11.58677 | -55.34159 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6ae8596e-118a-30a1-bed3-aa6f4279cd1d | -3.50587 | -48.04031 | 2026-06-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b7f7d52-e78d-3cb3-95b0-0247f3633d29 | -10.14949 | -56.59759 | 2026-06-16 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9644ecc-bdf0-3e09-8ea0-5a3d89139dea | -9.74492 | -59.31459 | 2026-06-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf6acfa8-3fef-3631-a793-0e0e1b0e7729 | -11.3573 | -55.82269 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2a74dee5-b461-3132-9e69-1f938a3b0451 | -11.59111 | -55.34221 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bc075c9-3fd1-34fa-b45c-a1cccf1e0636 | -10.88278 | -49.54487 | 2026-06-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 122bcdb3-ef44-392a-9c91-f343f5592f4e | -11.55476 | -52.77863 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26b8d90a-823b-32ea-b57d-8ef4b359e10f | -11.5492 | -52.78107 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b70118d4-3744-3b75-8289-3a336c15ca55 | -10.80663 | -54.1737 | 2026-06-16 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9350256-69bc-333a-b279-36d83e27ba04 | -10.1353 | -52.40484 | 2026-06-16 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd87b289-4577-3816-8019-e64910152fde | -11.53886 | -52.7795 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0562f48e-95b2-385c-b8a7-55efb12658c3 | -3.51001 | -48.03385 | 2026-06-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61e16e37-5b88-3eed-bec4-2ff9c3057a56 | -10.15733 | -56.59876 | 2026-06-16 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd6a9646-cf1d-3db9-b176-fc961b631f9c | -10.591 | -51.77665 | 2026-06-16 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51263e5b-4286-34eb-8cbc-dfb6aae852e4 | -11.35848 | -55.82218 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d687fd7-a61f-35c2-a9c4-f002a689cb54 | -8.97698 | -47.97848 | 2026-06-16 05:23:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3517073-39a3-3efe-87c6-dd51abadc722 | -11.78522 | -54.01735 | 2026-06-16 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39805a80-d146-3ded-8950-8f3106593d12 | -10.71583 | -56.24696 | 2026-06-16 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3332ae62-71b4-3178-8271-3349b0dcbc27 | -10.15341 | -56.59819 | 2026-06-16 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e65813ee-bffb-3c84-bf5e-8b131cd39787 | -10.15196 | -56.60825 | 2026-06-16 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 25df1fca-0363-3282-9048-813b9e3f62e2 | -10.82101 | -56.61265 | 2026-06-16 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 877f88cc-5fc7-31f3-b911-9b3a9aa402da | -11.54958 | -52.7779 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e8ae69b-4879-3fd6-9984-4479e9e460ed | -11.54217 | -52.78067 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33f91eaf-674f-3239-8b99-3e15c0775eb0 | -6.18384 | -48.50472 | 2026-06-16 05:23:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9c805ac-67de-3e9e-bea0-be7c07fe0dc4 | -10.80596 | -54.17865 | 2026-06-16 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20f5c457-2186-35d9-b525-5324fe27d03f | -10.90464 | -54.13797 | 2026-06-16 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c578c5cb-8129-32a7-8098-5be701a55fd0 | -10.90063 | -54.13233 | 2026-06-16 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2df9df0-f05f-31ca-aa6c-507bd92460c8 | -8.98375 | -47.97964 | 2026-06-16 05:23:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52e9412e-f5f5-3679-b5f2-03459411e9e1 | -10.81762 | -56.60283 | 2026-06-16 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73ebc2f-ef56-3123-bc98-ef81caeb730b | -11.53848 | -52.78262 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5977654b-9843-3d4b-82ba-9ece7436954a | -2.73714 | -58.18922 | 2026-06-16 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a46d9c8-eeab-3e53-b554-90283ed12559 | -10.36226 | -54.10117 | 2026-06-16 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09899c77-1172-3fda-88c1-a3a64f3b0533 | -10.15268 | -56.60324 | 2026-06-16 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0a0bd7ef-c607-3263-892f-624cbeb9639b | -3.50299 | -48.03778 | 2026-06-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf827397-39f5-32f3-b915-b49982006f70 | -11.7228 | -54.49178 | 2026-06-16 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80fb0410-48c8-34dc-8463-0ab685ad0af0 | -4.35422 | -47.7627 | 2026-06-16 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 874ce527-057b-3662-99f0-9528e879e9a8 | -11.537 | -52.77987 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5788390-470d-3cf1-ae90-8f1fad206ad5 | -3.50928 | -48.03887 | 2026-06-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 127fa2ac-8c3a-36c7-b405-88893b4a82af | -3.51283 | -48.03666 | 2026-06-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 092cf42e-97e8-3205-ad26-992449b018ac | -11.35915 | -51.38503 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f96a69dd-a69f-3ce8-9e8c-5f0238d3cc5d | -9.37551 | -50.53844 | 2026-06-16 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5638c2b7-8cdf-3935-8a07-7ada2f540460 | -9.85492 | -62.37425 | 2026-06-16 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2a1abf-bc4c-36d9-a22a-4ee62bcd6cdf | -11.54402 | -52.78032 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7076d1c4-1f25-39e3-9298-b233e8e4e0a2 | -10.71534 | -56.25045 | 2026-06-16 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe977b3d-6ee3-341b-a689-4dcc15af5490 | -10.14091 | -52.40242 | 2026-06-16 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc0850bc-9a6b-3663-8f3b-d58a964c2a5e | -10.9053 | -54.13303 | 2026-06-16 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84b87d02-fa1a-3399-ae85-82b6c285d001 | -11.54257 | -52.77751 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12d280ac-4aa9-3571-8bf2-513330afca15 | -9.37518 | -50.53791 | 2026-06-16 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95b49cd4-60f7-39ae-b4b2-e80465e14402 | -9.94679 | -65.01044 | 2026-06-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d8fbe75-973b-333e-b6b0-57bf8eff4e58 | -10.81853 | -56.60181 | 2026-06-16 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24b774b0-f723-303a-b9b3-e9aab7902fc6 | -11.59168 | -55.33797 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe73caf9-0475-3635-aa06-b1557cd280b8 | -9.22633 | -48.59214 | 2026-06-16 05:23:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 655aaf88-b3d6-3720-9b6f-c2cf419c96f4 | -11.59225 | -55.33372 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecbf8599-a5c2-3bb4-96d2-137f2b1d3e4d | -11.359 | -55.81823 | 2026-06-16 05:23:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d3de392-cb29-3dd7-8fc8-b32f1533ca1e | -10.71524 | -56.04123 | 2026-06-16 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d20d0564-d387-31dc-961d-4858b8fa0e88 | -11.54441 | -52.77714 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aee1776e-7c2b-30a8-b284-2b82bbd5c58b | -9.22702 | -48.58642 | 2026-06-16 05:23:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97f20813-595d-333f-a574-a1ee4497af11 | -11.55283 | -52.79439 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25bffb0e-af0c-351a-bb2b-d42fc4a63443 | -3.5163 | -48.03493 | 2026-06-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e805fdeb-aae2-3649-ae5e-50804dd7ca34 | -10.15734 | -56.60013 | 2026-06-16 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8839a746-0674-37e6-9c24-687eccf501ea | -11.54364 | -52.78346 | 2026-06-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 366c3e9b-2dd3-3f4d-a930-60cea5bfde59 | -11.72216 | -54.49658 | 2026-06-16 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dffc95f8-c562-3661-a529-1d5c880b25c5 | -10.49878 | -53.58625 | 2026-06-16 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fff65160-d75a-31a8-8481-79b80d7f91a1 | -13.51987 | -54.30348 | 2026-06-16 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e393954-9f4f-3ade-b01f-cf09546179d9 | -14.10518 | -59.45744 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 141397ce-c24e-3d0d-8880-b722b60ab3ee | -14.09168 | -59.45131 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b4424d7-27ab-3f30-ae3a-8c5b7e73f83b | -15.06882 | -55.81582 | 2026-06-16 05:25:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a8e2e65-f7ff-39ac-939a-4f561fdb0aee | -11.48202 | -57.12168 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 396eb503-6de4-31f3-b314-3f884f82a873 | -14.11631 | -59.45507 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aaee3d3-99d7-3f89-8d79-38118cbbf5d6 | -14.09442 | -59.4524 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d030161-9b7b-38b2-84eb-29e2cb1bb3f2 | -11.91905 | -57.03638 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4f79f85-d13e-3428-a491-2b7fdbcd8c3e | -12.90995 | -54.22867 | 2026-06-16 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56c912ed-559d-3268-948a-39a59875c394 | -11.79265 | -56.99501 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 141bc9e0-8c86-3f1a-82e5-e9eba685fb34 | -12.72024 | -56.567 | 2026-06-16 05:25:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f4be9f4-8c56-36fd-93f4-f8650468487b | -14.09872 | -59.45234 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63afa7d8-4366-322f-8d4a-1ebee95baecb | -14.10576 | -59.4534 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87444532-4b82-35bc-94cb-a3baca8ab0af | -14.10812 | -59.46204 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fff6890-9eff-3d45-a439-d55aed949115 | -11.78875 | -56.9944 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 97eb1204-de07-330e-9d8c-4542d1cd1f90 | -11.48341 | -57.1119 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 27e90a58-69f6-392e-9e5f-9224e97557b7 | -15.07321 | -55.8167 | 2026-06-16 05:25:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5096a4a-67e5-3175-82ad-d11a293e167b | -12.80594 | -54.86303 | 2026-06-16 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b98cf82-324a-3f7f-bdd4-9b34c07cea0d | -13.49606 | -56.57357 | 2026-06-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07b66e19-9555-3dbe-a6fe-4e084ee4e67f | -14.11221 | -59.45856 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55279883-19d7-34c9-bd5e-810c5120e1d8 | -12.92018 | -54.22474 | 2026-06-16 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e2faee83-d5fd-3eab-bf71-c796d972ffca | -11.48024 | -57.10646 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf26855e-e2b8-3ba0-b141-049baf97e61c | -11.79126 | -57.00502 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 294c5b3f-e4d4-3b0c-a922-229aecd6f09d | -12.80137 | -54.8624 | 2026-06-16 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dca174d3-52fb-3782-8e1e-a748dae4d194 | -7.36052 | -49.8675 | 2026-06-16 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26d6447c-6cf6-3cc8-9633-0b0815e0dccb | -11.91099 | -55.91436 | 2026-06-16 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d42cf786-c9de-3faa-bc45-8427bbca9ea3 | -12.59542 | -52.91528 | 2026-06-16 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20e3dc27-5bbc-3cba-84b5-f49a32c34250 | -11.9152 | -55.91493 | 2026-06-16 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7e12255-b4ae-389d-8255-185dc32131f2 | -11.51315 | -56.13257 | 2026-06-16 05:25:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f689d4f-1899-3a48-b018-fd7a49b83739 | -6.83418 | -47.90792 | 2026-06-16 05:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1d7bce1-3513-3ab3-b234-7a0af8cfd4e2 | -11.91834 | -57.0414 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
