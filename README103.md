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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b70a683d-7630-331b-847e-6268c3cd65da | -9.51776 | -54.64073 | 2025-09-10 06:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 8a3ef112-79da-3bd4-b807-bbfa374d1fdb | -8.057 | -52.32502 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c9b50c97-3e2f-3b03-86f7-dce86956cb6b | -10.38063 | -50.53125 | 2025-09-10 06:29:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| aeb185a2-6615-3e92-84d3-e28931d6baaa | -9.05996 | -46.95834 | 2025-09-10 06:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 7863484e-628c-345a-a748-4c4f7f1b67c4 | -15.46955 | -49.60431 | 2025-09-10 06:29:00 | AQUA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| c63745f0-3c03-380d-9eaa-3df41c8a6955 | -11.12942 | -52.02688 | 2025-09-10 06:29:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0a23674d-fbc3-3724-8db4-500f61c0c4cd | -15.79749 | -52.25283 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 66c7c4d2-4bab-3ff2-acb6-4a69d2fbecbd | -12.93666 | -54.80728 | 2025-09-10 06:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f592bccd-ca8b-38ab-8cc5-67a07b468900 | -9.51908 | -54.63179 | 2025-09-10 06:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ddb5e8a3-4e5c-3c2f-a1a5-452f7369ec0d | -12.18479 | -53.86192 | 2025-09-10 06:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 114fc497-d8b0-3e5b-af34-055a1c51d972 | -12.99259 | -48.02781 | 2025-09-10 06:29:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| c8d9f0c8-dfbd-3a88-9b6c-941535790d76 | -12.47601 | -53.82801 | 2025-09-10 06:29:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 969c7347-14ec-3c22-9558-baca6577a29a | -15.80843 | -52.25461 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 2865647a-ba39-347f-88e1-5019c82c9976 | -9.03698 | -49.78543 | 2025-09-10 06:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c8914f94-8d31-3650-bcbc-3c8d2619d7c1 | -9.10345 | -46.96794 | 2025-09-10 06:29:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 718ce9d1-8595-368b-afd8-466906d7f1c1 | -15.13761 | -52.39562 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fb516b81-eebb-32b3-91aa-2194d875a5b4 | -12.17865 | -53.86475 | 2025-09-10 06:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20011a67-852a-3920-86cc-d05fc593e784 | -12.17747 | -50.6281 | 2025-09-10 06:29:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 44bf1e87-f869-3427-abbe-6ecce0047a93 | -12.18337 | -53.87211 | 2025-09-10 06:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 748169c3-5b36-3e58-84ca-4f1d8a9754ff | -15.47272 | -49.62107 | 2025-09-10 06:29:00 | AQUA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 38cd4c53-7b5b-3822-90d9-e99a66548ccf | -15.80822 | -52.23424 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| deb6d74b-2f51-3aa1-ac0e-6ca5f6eb9fcf | -12.04004 | -50.98178 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 91b1fc4b-1197-359d-818d-caae76e7bba7 | -14.92419 | -55.91479 | 2025-09-10 06:29:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a2a5e2ed-0484-38bd-8963-03246fc3ad28 | -15.10526 | -50.06639 | 2025-09-10 06:29:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 37a8a363-365e-3b44-bd33-df08603e17e6 | -14.89682 | -55.85417 | 2025-09-10 06:29:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0b1e8a8-2b37-340a-bbcd-9b46c7982d69 | -12.2035 | -53.86462 | 2025-09-10 06:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4a63034f-481c-3c03-955f-3c5287f5cfee | -8.04536 | -48.69652 | 2025-09-10 06:29:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 34.8 |
| cbbe9517-46b1-34b5-bf1e-0aea68c008dd | -8.04792 | -48.6771 | 2025-09-10 06:29:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3a877c73-0566-3a87-897c-dc0ab286c6bc | -11.13119 | -52.01414 | 2025-09-10 06:29:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d4628fe4-12cb-372b-9b84-ac38af239497 | -12.01987 | -50.97193 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| fea620a8-9d73-378a-b409-80a5dbe0464f | -15.13493 | -52.38746 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 95252f1a-3520-3c30-9ef2-90f09d2dd784 | -12.06407 | -51.06378 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6ae60c80-0bf8-3813-bfd0-13ac66e6655e | -10.37853 | -50.54704 | 2025-09-10 06:29:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c0f3dde2-335b-3be7-9f18-d6a14bf76f21 | -15.46694 | -49.6277 | 2025-09-10 06:29:00 | AQUA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 149.4 |
| e261eb82-8bf4-3786-be73-527f25110298 | -14.8866 | -55.86198 | 2025-09-10 06:29:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 56f05338-183e-395f-a30e-655cb59f5f16 | -12.92544 | -54.75716 | 2025-09-10 06:29:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 928adff8-381d-37b4-b5e8-ce5a7a03e8f9 | -12.04206 | -50.96616 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 33e807cb-39d5-3e60-b81b-a6d170d4e2e8 | -12.03063 | -50.96464 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 814caa18-c26c-3599-9a3f-d4766b43ea47 | -11.10514 | -48.45134 | 2025-09-10 06:29:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 48fa7ce9-49da-38ce-af82-aab55731c6df | -12.01054 | -50.95482 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c73188a-70b8-3e8b-825e-c54d8b5e5388 | -15.80628 | -52.24896 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e8d1f9e1-c96b-3729-95f6-157fc072d8d3 | -12.01722 | -50.97874 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 95513df7-7ec4-3e69-8f2c-7fbcc76d301e | -15.10298 | -50.08545 | 2025-09-10 06:29:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 574a83e9-85f6-3fd6-bb70-779a87f9f12e | -12.05348 | -50.96768 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4cdacfa0-df0d-3597-bc44-6601e5a32e90 | -9.4422 | -46.69711 | 2025-09-10 06:29:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 401f03db-e9ee-31e0-820a-31b92cc57d84 | -8.0375 | -48.65665 | 2025-09-10 06:29:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d96d1137-4bb0-3a14-86a7-fa2c6bba72ad | -12.00845 | -50.97042 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1bca2624-2213-3d89-a1f0-dfd06933f7d2 | -8.03798 | -48.65141 | 2025-09-10 06:29:00 | AQUA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 5340abb6-8bd5-3f73-bbd1-086dc99e1146 | -8.51816 | -51.38541 | 2025-09-10 06:29:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 26e22962-3150-3215-bddc-a97a723d2b2b | -15.45929 | -49.61919 | 2025-09-10 06:29:00 | AQUA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 0b5e6b05-40e9-3cf5-8b25-4eb130f0b8b7 | -12.84226 | -52.94441 | 2025-09-10 06:29:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7dbd2553-ab3a-3735-bc94-7aeaaacd0e36 | -15.09229 | -50.06517 | 2025-09-10 06:29:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c697e34b-836c-3b45-8f22-ddd1dcd5a095 | -12.05146 | -50.9833 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 033e6746-db7a-350b-9173-40cd726b9700 | -9.79643 | -61.51195 | 2025-09-10 06:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| eeb67d42-63ec-38ff-8c3b-2d088fc3af15 | -9.51643 | -54.64973 | 2025-09-10 06:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b1cc65b-98ea-349c-bfbf-791443944c27 | -12.0192 | -50.96312 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 45f7c1fb-f954-3d29-991b-b68779d0a43e | -12.03128 | -50.97343 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 273.9 |
| d32fac72-55fd-35ad-ac57-6cdc10f2ac1a | -11.99704 | -50.96891 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0ab489a6-b7d4-3d7a-9eae-5f8668eb9804 | -12.0334 | -50.95783 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e611c8b8-66f3-38f9-b956-63aca84e67ff | -15.0121 | -50.0869 | 2025-09-10 06:29:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 2c7d83b5-be05-3348-a083-1942c2c5a641 | -12.0661 | -51.04837 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 580d59c2-1a7b-38b3-a427-201e3d0042db | -16.51282 | -55.14066 | 2025-09-10 06:29:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 45c54939-ed02-3ee3-a6d4-b63078df7934 | -12.02197 | -50.95633 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 6bad0413-77d2-34a7-bd53-61c145a4153e | -12.02863 | -50.98026 | 2025-09-10 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 9f91e5f8-850a-38be-86d0-664ff25fe9cd | -9.05794 | -46.96555 | 2025-09-10 06:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 93f13a67-1fac-3c41-baf5-267394ac7ad3 | -15.47299 | -49.38517 | 2025-09-10 06:29:00 | AQUA_M-M | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 281535a1-9adc-3be9-9c2b-1f97e5d600c6 | -15.45658 | -49.64205 | 2025-09-10 06:29:00 | AQUA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 01d6f4f6-8012-37f1-8cb1-714dc1d5d5a9 | -9.5135 | -54.6494 | 2025-09-10 06:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ad6a0356-324f-3789-a320-31ffebfa640d | -12.0311 | -50.9869 | 2025-09-10 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| f6528f19-d640-3ba5-973f-66ae865101f0 | -9.5137 | -54.6292 | 2025-09-10 06:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| e40ddfe3-af36-3fb3-921a-47fc9b479747 | -12.0123 | -50.9678 | 2025-09-10 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 98207c3b-c1d9-3232-a5a7-caad6f41617f | -12.0501 | -50.9847 | 2025-09-10 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 330cccb0-ccf0-3e80-b606-9d50c8fb32a7 | -12.0504 | -50.9634 | 2025-09-10 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 55bae4a1-6373-3b83-be11-23825a14136c | -9.5324 | -54.6277 | 2025-09-10 06:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 32724844-094e-3489-8304-7bec938defd0 | -12.012 | -50.9891 | 2025-09-10 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| de8e7e24-4c49-33d5-afdf-6c874b3db8be | -12.0314 | -50.9656 | 2025-09-10 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 33785f16-3ae8-3e06-b770-b63ee22f4789 | -18.01867 | -47.13143 | 2025-09-10 06:31:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 37afccde-f706-3890-9276-2ce4b9974f16 | -9.5137 | -54.6292 | 2025-09-10 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0ef03b7a-0755-3d92-b96e-018dfffd4f48 | -12.0314 | -50.9656 | 2025-09-10 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| d5801a5e-a38b-364e-bf64-b15055364b6b | -12.0504 | -50.9634 | 2025-09-10 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 63496696-961c-33d3-be94-177d7bb4b9aa | -9.5324 | -54.6277 | 2025-09-10 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 40a394a9-d09e-3bcd-9e3d-14c2d2d4dee2 | -12.0501 | -50.9847 | 2025-09-10 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.2 |
| e3547b55-1dbb-3a82-be8c-65c13546765e | -9.5135 | -54.6494 | 2025-09-10 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 48925eae-18d5-3c07-a180-2b9af73ec375 | -9.5322 | -54.648 | 2025-09-10 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9a800a37-bfd2-320e-8e0a-fb7dd7d75071 | -12.0123 | -50.9678 | 2025-09-10 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 94b38150-e929-3bce-9c4e-61eee4b932d7 | -12.0311 | -50.9869 | 2025-09-10 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a7d10faa-43e0-3456-8ccd-d52ad69c19a9 | -8.44613 | -72.79697 | 2025-09-10 06:46:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d54a6ae-32aa-3dfc-bc83-b34e7c7ccdd5 | -8.44581 | -72.79651 | 2025-09-10 06:46:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5c28a05-4894-3bc1-bde3-e8e040233952 | -8.44571 | -72.80013 | 2025-09-10 06:46:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b3e6a51-c414-3392-876e-21db59a34e76 | -8.44537 | -72.79966 | 2025-09-10 06:46:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88136ddc-4579-330d-a711-96542e2684b4 | -9.5322 | -54.648 | 2025-09-10 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 1d88b34f-7270-37bc-bf6e-80ef49a20b38 | -12.0501 | -50.9847 | 2025-09-10 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 24dac524-c91a-388c-9647-2684ae6b3c28 | -12.0504 | -50.9634 | 2025-09-10 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 9c8bd848-dcd0-3f70-94ff-f01cfd4db215 | -12.0314 | -50.9656 | 2025-09-10 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 176.1 |
| ffd244ec-1f5e-329b-842f-7404ecbb9f97 | -9.5135 | -54.6494 | 2025-09-10 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8d4914fd-b2ca-3c6b-800d-75be5aa1dc4b | -9.5137 | -54.6292 | 2025-09-10 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b9506e81-5a85-37bc-a6d4-bc9c65776866 | -12.0123 | -50.9678 | 2025-09-10 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 21191e3b-a353-38bc-b7d7-c97e02d817d2 | -9.5324 | -54.6277 | 2025-09-10 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4732a864-381d-3776-b559-baafe81dbf25 | -12.0311 | -50.9869 | 2025-09-10 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 8d8bf5da-e036-376b-b21f-a448ed04df4f | -9.325 | -46.74 | 2025-09-10 07:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |


[Clique aqui para ver as próximas entradas](README104.md)
