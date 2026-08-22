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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bebd401-a486-3f2b-b267-742750097793 | -12.10336 | -56.31458 | 2026-08-22 05:04:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1c8ac35a-1381-3ba1-b175-a9f00463dcb2 | -9.18212 | -56.99872 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47d637de-bf0c-3965-b537-5929b66a9286 | -6.79265 | -59.41282 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 19868ab7-f47c-3f3f-a666-8169d8e3683a | -8.63338 | -54.73447 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9627304-e970-3cbe-82a0-1ced948b4a3d | -12.75328 | -48.47522 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0eb0b035-4490-30e9-a960-25665e04d369 | -7.18034 | -60.64776 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9836a5b-f3db-3461-8e42-25e65058533b | -8.52275 | -54.81033 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 558557a0-4350-309c-ad4e-b152c8014da9 | -8.49619 | -54.86683 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7472ae4f-2f0b-3bd9-80b7-2d8cd6f32eb6 | -8.90462 | -60.54077 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b660c1a8-331a-3557-b29d-f385545a0677 | -5.91316 | -61.29541 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea1424b0-bdbc-332c-804e-53243e9f3b96 | -7.86791 | -63.77008 | 2026-08-22 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 844ec56c-b837-3a9f-9256-510d53182cb6 | -8.09385 | -51.65876 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3f0490f-1523-3b66-81aa-4d21e8db67b5 | -6.37838 | -54.95135 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf434ae3-e648-370b-b37e-ed9d8463327b | -6.76596 | -58.67244 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97710ad1-9c24-3a1f-9446-09d87c36965b | -6.38044 | -56.10349 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 747a3eb9-578e-31bc-89e5-2614e9e98ec3 | -7.08094 | -45.00089 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4d4a85a-9e96-3ade-9c24-d803d0f6ab02 | -8.53854 | -54.82043 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 40d867b7-b92e-3d7a-9a36-3a4647ff2156 | -11.384 | -46.34985 | 2026-08-22 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ffb37d1-aa65-3333-a653-6ab32b0b7d7f | -9.39883 | -60.55797 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f4a9494-c2d8-3f19-96d1-d6fc1f5fdeb7 | -6.43567 | -54.96008 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60faa539-b991-38e4-9771-a2862da7901c | -9.51115 | -51.67521 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9577cb5-57b8-3ef2-b28e-e7bc649f8b9f | -6.77143 | -59.45504 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 011a1144-6ecb-3779-84a7-312e65d0804a | -8.52555 | -54.81453 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| da913d26-845f-3757-a1ee-c2ecb28f6df1 | -7.86203 | -63.76897 | 2026-08-22 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb5f83a3-8115-3abc-a58d-0edf27e61c75 | -7.26061 | -49.87645 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 515ef18e-8780-39e6-8f2b-bb3ab928d534 | -7.68803 | -46.1712 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74962c1f-ec17-3d1d-b549-68975e0c6fd6 | -7.83904 | -61.77758 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 054a844d-026d-35a9-9860-ad75bbd07cd1 | -11.0501 | -49.10539 | 2026-08-22 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81870626-3e0b-38fd-a2a8-a19f0d3c994d | -6.55502 | -58.51223 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdc11600-a9d0-3213-ab69-35a6bef1be6f | -8.16478 | -55.3793 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2813e94a-e4a6-3199-a4ee-8933c76cc472 | -6.37415 | -62.90871 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8773ea6c-1a56-3cba-a202-b82edebb9ee8 | -8.02359 | -51.7998 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c015872-1cb2-39f0-915c-f4678919b3ff | -7.26362 | -49.88096 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92d97b54-a4f6-3fdb-ae2c-6b8f83134a99 | -10.89061 | -50.28757 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9769a48-6a43-3c50-b0ba-9e93ec305573 | -7.08774 | -55.45276 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36213c53-c3ee-3045-bc82-b366ddfc58b9 | -6.41682 | -52.73087 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3f9a6e6-c89f-3bb3-8cf5-d12ab7a8713d | -8.62132 | -54.71789 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c15a962-68c4-37aa-8e1a-601f3c7f24bf | -9.19078 | -59.45003 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0b9337b-3d9d-357b-8e07-e10cb5be291f | -6.96346 | -59.04918 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c9a997ec-f3e7-3e6c-90af-114a7f3014f5 | -10.29535 | -48.21265 | 2026-08-22 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5cd13132-e838-3105-90eb-c9984e36995c | -9.18574 | -59.45339 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 883b64fd-9d4b-39da-b265-8b5a296720ca | -8.63101 | -54.70079 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 74e15c35-30a7-37ce-a043-ff8d0821506d | -6.12637 | -57.71968 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a533df86-3eaa-38f6-bd9e-6ef29a61c4be | -6.25184 | -55.39396 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7752eb48-4eb7-3917-b72d-14da0f17ed05 | -8.58953 | -54.74249 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a118d07-16d1-340d-94f1-cfa70727feec | -9.46621 | -48.29085 | 2026-08-22 05:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa271053-a41a-3666-bb70-f2bd144b6631 | -9.43882 | -51.62608 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e38f6988-6df1-3a90-a52b-127c02bdc283 | -8.52536 | -54.83704 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa640628-8e89-3c9b-9a47-64f4c7517625 | -5.91778 | -61.29945 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17b396a1-1e00-349d-b713-e68962fedc44 | -12.72696 | -48.41511 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9007d516-5262-3fad-8760-668eec8d4d5b | -6.10105 | -57.87032 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db848f33-3902-3b2a-a13f-ff03ae3cef6d | -6.90486 | -58.99771 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 90302755-8ccc-349f-8e9e-344e42820d82 | -9.16994 | -59.4421 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6354c032-5d73-33a3-9cc5-6f92eddb0670 | -6.80904 | -59.42478 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 12aa9818-9100-377e-b3f1-aedf7cb6c3e0 | -8.99594 | -50.73358 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b303cb3-70f5-33fa-9c90-141cc23f2452 | -9.16988 | -59.46762 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96f88ac9-4c0c-395a-8a87-c65c28d71285 | -8.63874 | -54.70173 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f18edfe7-c0b3-34eb-9cbe-47aa96af1563 | -6.12087 | -59.91422 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e4ad31d-1346-333b-be99-c39b750bbdf6 | -6.66541 | -56.34529 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26c95647-b07d-39d4-a304-ff4a9cfc12b4 | -10.7367 | -50.26641 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26258316-13e4-300b-802a-ce262e4e622f | -9.43599 | -51.62175 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74bd9dfd-5ad9-39c9-909c-f0709d9905cb | -9.413 | -60.4269 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4c5ac76-fcef-3f5d-bd05-17e92f8c3154 | -10.90139 | -50.23994 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f157a027-fb6c-357b-b906-db5ccc1f3de5 | -9.44167 | -51.60769 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14c88ccc-a2b3-3bc6-9ccf-1a912c998d64 | -5.90338 | -61.29047 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f641d227-f463-3b51-84ca-c52e7af20713 | -8.10176 | -51.65251 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6915385f-fef5-3f79-ad77-7659bc092d58 | -6.13357 | -59.89609 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 974a068b-1885-3352-9c7c-5d72547df00c | -8.53492 | -55.3321 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6853591-38b4-338d-8802-7b5a8b48d9c5 | -9.52598 | -51.64716 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bec8d14-50ca-3f85-b4e8-46fa7c246dea | -9.51399 | -51.67947 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abe606bc-0a22-3dca-8b90-ad387d513739 | -5.99655 | -57.80029 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02de5b93-866a-300d-a75c-dd328dbd94d3 | -8.95037 | -60.59342 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50574371-5a51-338b-9cff-e0c7cd51e61c | -7.10492 | -59.77557 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a220b7e0-42b3-3dbb-9eea-928c5171b520 | -11.20014 | -55.07082 | 2026-08-22 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2150de61-2c4d-3992-806a-0ecb6aa773c7 | -6.94493 | -59.31429 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 605a60d5-d050-34e1-b1c8-c7301bb9774a | -5.74928 | -53.58508 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a854dcfe-6ce5-3bbf-8999-7b1e2bc8b9bc | -6.43754 | -54.94867 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1092fc9a-3bbc-34a8-998e-78ccaf3cefd5 | -8.59482 | -54.70982 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c363641f-5c97-364c-9b74-505546e2264e | -7.29372 | -52.53493 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f81b6bb-4fcd-35d0-857b-c3d4709df71f | -11.5926 | -46.57643 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4411cc40-93af-3035-b4e6-7236d0515383 | -9.44962 | -51.6428 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d626ad58-4686-331e-8456-71dd67282710 | -6.78035 | -58.69131 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 663e8c50-bf04-3510-85aa-b5057785c668 | -9.16281 | -59.66116 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cde73dd-35cc-347c-93fa-f034a53d3831 | -8.09555 | -51.67016 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22073ab0-e704-3cf0-a4f2-368c92819791 | -6.79915 | -59.45529 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 227c0a61-861c-3e35-a573-e3281e9aa014 | -6.97675 | -58.32101 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1b3e1b2-7a6f-362c-9ae9-f2a94ef623c7 | -6.08973 | -59.95517 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 764524ab-50f6-30d7-9a3f-f28a802a5978 | -8.59291 | -54.74305 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2951f1f-fb47-3089-ba8f-18212b1bbfe9 | -6.09239 | -57.69939 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9231e699-bb04-3eb0-baf2-4674fc135d61 | -8.89996 | -60.53989 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ecd65c7d-1aff-3b52-9d65-bcd0488cf03b | -6.89237 | -59.43241 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee0c9335-2e85-37de-a90f-0836512ecbbf | -8.59702 | -54.71765 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12f52189-cbe6-3a9c-a44e-b9c227605e76 | -14.4016 | -43.79914 | 2026-08-22 05:04:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d027b78a-4f8e-3907-9720-aabae9711d8d | -11.16285 | -54.02191 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98bbb9e8-e365-35ac-98c7-57ea5abd658f | -9.44282 | -51.62288 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c2a9f36-13f3-39b8-b45e-13f5e09db37e | -11.16505 | -54.02948 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84670788-0d67-374a-a4f3-00d5b893e1a0 | -11.16509 | -54.00785 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0905a1a-da2e-3284-861a-974fe494fc0a | -7.60217 | -60.94397 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbfb49f5-2a01-33aa-abbf-19e902da2356 | -8.08935 | -51.66547 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 942faffd-75a5-3e56-8761-21521ebb38df | -6.82199 | -59.67617 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |


[Clique aqui para ver as próximas entradas](README48.md)
