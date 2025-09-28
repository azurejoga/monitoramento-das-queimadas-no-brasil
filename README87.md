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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46d671dd-9fb6-3980-86c3-61c8ed7b5569 | -10.4181 | -67.51488 | 2025-09-28 05:18:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 022a3096-2a99-3537-bc29-2a7da5589b92 | -9.21852 | -46.77369 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 42cb507c-a5ba-3661-af67-37887d125dfc | -12.23507 | -60.84746 | 2025-09-28 05:18:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2f61c9d-2cf8-384e-b645-11013f8b2377 | -8.83277 | -46.00319 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58aebb91-d140-347c-8ef9-89deb7c58bc9 | -9.14886 | -61.19515 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75f998a3-aaea-345a-b73b-02c1a3b99763 | -12.23148 | -60.84632 | 2025-09-28 05:18:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fc5a3e5-1fc2-3c8e-910e-4bcac4c305af | -10.97543 | -54.09813 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9677ac5-e1b7-3bbc-8169-2cf584d0d001 | -12.99897 | -49.45186 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1049f522-9841-38e3-bba7-385cd9803a65 | -9.56195 | -63.20081 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d2766c7-cd0b-3740-89df-f4be4b3367ca | -12.01022 | -47.97388 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ef9c9a9-4a07-335b-b748-def5676f2a8a | -9.91264 | -58.56183 | 2025-09-28 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 390df8c1-88fb-35c4-a2ee-7093f8ada885 | -10.72342 | -53.79668 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df1ad44d-d456-3465-ad68-eac5c1e4e639 | -12.63726 | -48.15419 | 2025-09-28 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 29b245dc-4bc3-34a8-b7bd-ded458222b6b | -12.98218 | -46.85254 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1883c2b7-79f7-3577-9ebc-0fd185eb7289 | -9.47878 | -57.92886 | 2025-09-28 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de821d16-dfbb-3471-882b-23c43358437e | -10.39617 | -64.91895 | 2025-09-28 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ca8b659-053e-3446-b3c0-679306e2ed8f | -10.13635 | -63.13794 | 2025-09-28 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bde5a94-9547-3d3c-aeca-a40b88b8b7fc | -13.79265 | -48.32656 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0990e2a6-8811-3b87-a3c0-449e48fc529a | -13.61371 | -48.08252 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ccc740f-c3f8-3b7f-8240-dd75a463714a | -12.9885 | -49.43695 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e4df597-8f41-30e8-9be0-bfdf263bccd3 | -12.64515 | -51.691 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1600994a-a6f0-3b3f-b7b0-b60b8689dafd | -13.61333 | -47.32558 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0f338f6-56ae-3046-8d3c-168f53f84d2a | -13.40089 | -48.16648 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d753c025-e1fb-3f5a-b167-f831202725e7 | -9.93637 | -65.15491 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d044390f-2dce-3655-ad06-1492c046a740 | -12.64951 | -51.69804 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd6be13-a7f0-3b8c-9fe9-0bd5f8d503cf | -11.9954 | -47.04777 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9086546e-267e-38df-9ecf-d3f177c2a84c | -8.83611 | -46.20818 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87d3b9d6-56dc-328d-bc09-abfa74a806dd | -13.02243 | -49.4594 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 36c66ef3-3d32-3f33-a8cb-abcae6ab6904 | -13.7117 | -48.34269 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ce8540b-4094-3180-a9f2-5d9155cbec94 | -12.98803 | -49.4411 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a0bad80e-6d46-38a1-b0c8-3c7762f47905 | -13.24984 | -48.4557 | 2025-09-28 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66c3dac9-9d31-38de-827a-07338e3bf803 | -9.43878 | -67.20026 | 2025-09-28 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8f6c6b9-8a88-36b5-b8c5-382ddc81e276 | -11.15408 | -54.30973 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5067406-3e97-338b-bcf9-9867ed45ff31 | -12.88783 | -47.09278 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce022884-1851-3140-915a-5b728f74e129 | -9.77651 | -62.50538 | 2025-09-28 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e43f8d4f-9246-36af-ab99-c60c9f20c635 | -9.89716 | -49.11936 | 2025-09-28 05:18:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e3ecc1e-8c89-33a9-a47c-9505767a1fc0 | -11.14986 | -54.30907 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8559a52-7a12-37e6-bb38-e4f31186045b | -9.80314 | -61.49225 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3963aeb-6702-33b4-9ebd-a25380ce7b6e | -9.56061 | -63.20659 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e431644-2ec6-332c-ae8e-1106a1e2756a | -12.02174 | -47.92961 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 534c6c59-58bd-3794-ac7d-0f1eb7b64bd1 | -13.58501 | -47.32483 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9dd4f5d-1202-3c88-97ba-3f0b4904c014 | -13.79216 | -48.33119 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1eb81f3a-84e6-3c63-9548-d0b39094ab12 | -12.23203 | -60.84279 | 2025-09-28 05:18:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a12443be-8ad9-3840-a4e6-346db873056f | -11.48248 | -51.44838 | 2025-09-28 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ac8c128-154d-3200-9801-9342917f19ca | -12.41462 | -49.36615 | 2025-09-28 05:18:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27094f55-bdf1-3991-99ea-b516b2af79ea | -13.77229 | -47.89043 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f8efbd0-7e00-390e-a890-72f572f47d19 | -13.58578 | -47.32289 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d8bf7bc7-06ce-359f-ac17-7536d94905ed | -13.59852 | -47.32854 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9f1eb21-ef99-3d95-b092-814dce5d48c5 | -10.16133 | -64.74014 | 2025-09-28 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2144941-5e66-3a13-84e8-ab7f33978646 | -13.71874 | -48.3382 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4c31027-abf5-3dea-add9-70d6adee8ab2 | -13.00715 | -49.45747 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 94b4caa5-6501-3e68-a555-3c4ff34cc366 | -12.02112 | -47.93534 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fd4c68f-36c7-36a5-b235-f86524dd3448 | -13.03119 | -49.46015 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48311f1a-d3d9-30e8-8c17-f7837ed4ab13 | -13.02515 | -49.45977 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0da9ebe-cf9e-3792-842a-6ae6b678a0a6 | -9.43225 | -63.25699 | 2025-09-28 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7a2e5dd-e427-35f1-973d-87c40b1695a2 | -10.20226 | -58.22285 | 2025-09-28 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc3e64b0-6afe-3f58-b945-4ae39e128aed | -13.7122 | -48.33801 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8253558-a09c-3139-9263-b244cafe7108 | -13.60774 | -48.08489 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b48d7608-b600-3b7e-bac6-d16250772d28 | -13.40073 | -48.1676 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29c97a11-a727-3ccb-a859-72bec0400bdd | -13.0289 | -49.45613 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3bafddb6-1420-3017-a79d-ec8be1d63391 | -12.01041 | -47.97354 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b8367115-7ef2-3311-b5a1-961c72077478 | -9.45136 | -56.65823 | 2025-09-28 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c7d1ab0-5deb-3d50-93eb-4bf4efd8e45e | -9.89664 | -49.12357 | 2025-09-28 05:18:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1693a60-e22a-39dc-83ac-6e039cf60881 | -9.65175 | -62.84322 | 2025-09-28 05:18:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 2bb98e14-8560-3797-9415-21a6d13d734c | -11.09722 | -54.28202 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a530fa2e-e4e1-3a76-88ae-1acfc4ad77c3 | -9.2155 | -46.77736 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8dd0b4fe-e541-31f2-be90-ff0abe76ba48 | -13.40202 | -48.15604 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4d97f96a-0d14-3f93-9629-1d8619c4e0cc | -9.41537 | -54.68965 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69550866-16ff-3a96-88b8-5d346e457f2e | -13.60654 | -47.32399 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e737194e-243e-3833-b16f-b43b981827f5 | -13.40136 | -48.16196 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c76f554a-89b9-3a02-995e-6229caf68988 | -9.883 | -58.29053 | 2025-09-28 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b21b0a10-082d-3445-8983-c4be2d04ecc6 | -12.0 | -47.88974 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6313e19f-52b8-3b32-ba08-35ea2af86b29 | -12.88134 | -47.09096 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ebdcd81-fcd5-328b-82f4-aea70d2f3f06 | -9.78172 | -64.98181 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dd38c63-34d3-349e-9eac-a23e92ec8ea3 | -9.41036 | -54.69608 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cccffb5-fe0d-32ec-9532-29d12525ec9e | -13.5925 | -47.32523 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6aec16e6-72ab-3a67-9102-cf55159eabda | -11.14933 | -54.31307 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6bf49011-6ba5-3bf5-b167-690910b4b0d0 | -11.251 | -61.16859 | 2025-09-28 05:18:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fef1af32-bc54-3f18-b65e-236205f3f984 | -9.04833 | -46.71882 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4d653c2-ece4-3c47-8820-bbc698387c81 | -12.26025 | -60.31841 | 2025-09-28 05:18:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a3dc8aa-ec76-3d41-aae8-3140b0447afd | -11.9682 | -47.99633 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db81d395-77c6-306e-9f54-9bbd690de1e9 | -9.65106 | -62.84736 | 2025-09-28 05:18:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 1a6b1836-315a-39a9-807f-23c4f90b88db | -13.34961 | -47.29875 | 2025-09-28 05:18:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c45dccb-da32-3f68-81d4-4c2041190745 | -8.83574 | -46.20635 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13791ed4-e127-3f35-af24-bbe9c9f247f1 | -9.79578 | -61.49484 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55ec04b2-48dc-30d7-a7ea-ff677a887bd7 | -11.43746 | -55.03507 | 2025-09-28 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82492977-c429-3a71-b57c-b5ed7c8e38de | -8.6782 | -49.93334 | 2025-09-28 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a8fab894-833b-3828-b94f-2ae80495654b | -12.63019 | -48.1591 | 2025-09-28 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c05957de-bd45-3dc8-9b34-471cf577ff35 | -13.78638 | -47.88458 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0f929c9c-a905-363c-a291-ad40d19e1ffe | -9.79976 | -61.4917 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a28912dc-8c60-3859-a0c1-3fcc4a1a6699 | -9.41587 | -54.68612 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99757f31-4afd-3c9b-ba12-5be5766d25ea | -11.09777 | -54.27804 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54966c37-b21b-3308-bbeb-b4ff4068bec7 | -11.64834 | -52.87069 | 2025-09-28 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61da248c-d18e-3efb-bbad-2bb6ccb0cec4 | -10.95779 | -54.09978 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e4c7343-54fd-3546-a94f-4a60acf96100 | -9.91025 | -65.01223 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9793af9-7686-35a9-9258-2d714feda23d | -8.45038 | -46.92015 | 2025-09-28 05:18:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb9af924-9a1a-324b-b6f7-11413b9d1e64 | -13.76623 | -47.88391 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3267155-04c0-3f6c-a864-7edb5deebcf4 | -13.59176 | -47.32672 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f0b3a48-0c83-30b3-8162-2bbb26bb1ee0 | -10.18007 | -52.57356 | 2025-09-28 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bddb9a05-9b58-39e7-a717-f316c800785f | -13.02554 | -49.45623 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README88.md)
