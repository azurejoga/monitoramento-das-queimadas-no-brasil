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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac180cad-bcc9-3bed-92c6-5dbfbd2cd0bd | -4.66395 | -55.96742 | 2025-07-11 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d43f8ca-e5f1-31dc-ace4-ccc4626a7fde | -3.75222 | -47.10554 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f0adb0a-896d-33c1-b8f1-b86976405fae | -7.20455 | -43.11655 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f6a931ac-af5a-3b53-89a2-516743ee1d7a | -9.86524 | -47.87 | 2025-07-11 04:57:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5ee5e6c-1457-3f6a-9513-08159512b2d6 | -9.53982 | -46.2929 | 2025-07-11 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80bd7121-f228-380a-b193-8727aec4ed6a | -6.6724 | -46.30459 | 2025-07-11 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e122a9aa-ca19-3607-b380-a462801713a8 | -8.22963 | -44.92273 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fa84867-607f-3c25-9c27-dcab06b2a50b | -7.19652 | -43.12305 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 48965cb6-447e-3b13-b27b-09255f712c5e | -3.74949 | -47.10794 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c09c9f30-5e11-3140-955c-44addfa3cb1b | -4.81851 | -47.32113 | 2025-07-11 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cec457d0-44b1-3809-9e61-2d0ff9b91efe | -9.61287 | -49.01794 | 2025-07-11 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c09b926-696a-3f8c-84a2-0a67e4e96a61 | -5.03398 | -48.51735 | 2025-07-11 04:57:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98f4d4e1-9c6b-3ef6-8ea5-44f449948fa2 | -6.61165 | -47.98774 | 2025-07-11 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21956fcf-ae86-3ccd-b35b-86d435d37176 | -7.19035 | -43.12212 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bf46afdc-6761-3f76-896d-1581c04322cf | -4.54683 | -48.01149 | 2025-07-11 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| df4790a5-9574-3954-b1c1-85137d1f4ede | -7.19097 | -43.35514 | 2025-07-11 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6feabc15-d309-31bc-8a47-60f0294ba22a | -7.65626 | -45.35102 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a1b12f56-f85a-3d62-b458-51199f62a333 | -7.27551 | -49.5727 | 2025-07-11 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f697ad88-1300-3fb5-939b-a5c992919342 | -6.98815 | -44.45152 | 2025-07-11 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5898758b-70f5-30c3-9114-47be13cc271a | -7.63806 | -46.00924 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 133eeecc-f44e-3887-b7bc-fdb0ed0afa18 | -6.62735 | -56.27515 | 2025-07-11 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8d2af14-0c72-32fb-b8b1-27e27408a11e | -5.55078 | -43.89976 | 2025-07-11 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d7d7a084-7dc8-3bf7-aabe-64970e88c4db | -7.95252 | -44.85243 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e52922ed-97c3-32b9-8177-4bd01480d713 | -7.65321 | -45.35175 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5cc65218-48f6-3460-89ef-1039affea4c8 | -7.55871 | -49.90593 | 2025-07-11 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50af7545-b1f5-37e3-9947-fd627b9b70d6 | -6.67631 | -46.30497 | 2025-07-11 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c1ac3368-2724-35e1-b0ee-6551a9ca4cd4 | -7.65669 | -45.34778 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 71db4312-2151-37e2-964c-fab51a1324ec | -13.13965 | -47.27805 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bc21125-130d-3555-b41f-3574e25312e7 | -11.85107 | -46.75394 | 2025-07-11 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f092fade-9924-3b5a-8bfe-72d71f5f396e | -14.31851 | -57.59763 | 2025-07-11 04:59:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47aa21be-81cc-390a-bf4a-7d6efb5a01c6 | -10.68136 | -49.49474 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 019688dc-da3a-3d0f-a18c-494624416833 | -12.47144 | -44.49844 | 2025-07-11 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b808b38f-8552-33f1-880b-2c9f7448475a | -12.39747 | -45.36691 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8306d344-35cf-3893-adf2-2e1834b5e7b4 | -9.86965 | -63.304 | 2025-07-11 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1cda131-7894-3c0c-8d2d-f1a78a28ec0f | -10.68244 | -49.48676 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f836b7b3-cb12-340d-bc9a-4b90b4bed512 | -9.94725 | -64.95768 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecbb9eda-1a34-3b61-b8ea-0e079835f38e | -13.14742 | -47.29907 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b05bc094-a0c4-3fb7-9529-b9c74931fa83 | -15.36004 | -49.48728 | 2025-07-11 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 46d4a857-5459-33b2-85cd-e95497113b14 | -9.96947 | -64.96196 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41863264-8655-3e05-8f5d-04c921f63a24 | -10.90285 | -49.20846 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40849f3e-e851-37fe-9902-a8abc59a190f | -12.99131 | -44.87248 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30a34dc6-80f0-3735-bc61-df3cd551126c | -13.14257 | -47.29649 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0f6fb84-1e5b-396f-bbd5-0c083f20d866 | -13.15294 | -47.29632 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d81c6eed-00cf-393f-8da5-11c57c9b2c14 | -13.35489 | -47.89597 | 2025-07-11 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6f43603-4dbb-33f2-b93c-6abe45883e93 | -9.95755 | -64.96339 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea438e0a-bc54-33c9-8322-3967b146c4a5 | -12.99306 | -46.29676 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cee576ec-a272-3af7-959c-2d33d114bc78 | -11.57674 | -47.42738 | 2025-07-11 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d50860cc-8528-3b97-9047-87f8f4527842 | -10.85238 | -49.12466 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e48dbe44-c7ab-3a00-8f94-fa6bd72ec77b | -11.93641 | -49.30698 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9933d2c-9d3b-3c4d-babe-0aa149b173c9 | -12.46746 | -44.49344 | 2025-07-11 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e112fd9-8cb6-39e3-acd4-b77efdc1cb87 | -12.07253 | -47.98414 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75afd72f-117c-3ff0-afe3-fac97254711f | -12.99183 | -44.86786 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b311780f-cc36-385e-82fe-c970321d0a9c | -12.46539 | -44.49759 | 2025-07-11 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a6aad91-b34b-3a52-8513-828c729b1e3e | -9.94176 | -64.95667 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3afdf901-3301-3f9d-abca-41863ad0b398 | -12.41037 | -45.35622 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70bf51c1-efd6-3c0e-ae08-9e5b4c72b597 | -10.67288 | -49.49363 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6d12e57b-d688-32e8-ab40-9a8c598aff38 | -13.00397 | -47.83326 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9abeee2f-d26c-3a25-87b6-c1e3ccf32446 | -10.85295 | -49.12039 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5bd08504-e337-3ee1-a69a-d7bbfa68af6c | -15.36461 | -49.48757 | 2025-07-11 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ac93b7e-f24a-3be0-b943-f68d76f56e80 | -10.67766 | -49.49018 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a9e1c3f0-b19a-3bd0-a6d0-306a8a35d4dd | -13.13674 | -47.30184 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee2400b4-1ce2-37b0-8bd9-c7c8935868bb | -14.42903 | -58.72512 | 2025-07-11 04:59:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5b9cce4-ae2c-39b1-b6b5-687337fed416 | -12.99885 | -44.85925 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aab2683-7aee-3b81-9f37-55b1dcfd5c06 | -12.66448 | -47.09059 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2eb98621-f66f-3181-ab99-42e7af4cae39 | -13.00464 | -47.82802 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 007442a5-959d-3685-b002-163f7009ef7b | -10.3585 | -49.91668 | 2025-07-11 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bc29422-3ee7-3602-b85d-9759b251f169 | -13.00749 | -47.82298 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 225a1597-460f-3091-b7b1-7cd76024200f | -12.99262 | -46.3003 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9bea4eb-738f-3ee6-a639-d56d46cca9f0 | -10.53782 | -56.23335 | 2025-07-11 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54ca7c84-5f48-3d77-8509-678d918123f2 | -10.90482 | -49.20692 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32da23f7-faea-3221-bedd-2c1dd32af226 | -14.43667 | -58.72232 | 2025-07-11 04:59:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b11d9863-a740-3558-bb28-9f9fbcf618a6 | -12.66409 | -47.0937 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0543df7a-bcd8-3c6a-bedd-28881c6ad99f | -11.0607 | -55.37823 | 2025-07-11 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed6e46fe-4c60-3c45-9b14-720fdaa3c749 | -13.13706 | -47.2992 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82e7114b-701c-34ca-b918-ad9ee4f3391a | -12.46694 | -44.49809 | 2025-07-11 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce5f2a2f-521a-37ab-8c6c-2cea07ce08c1 | -9.94108 | -64.9603 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b56203a-cdf1-3cb5-a604-504f73afa37e | -9.96237 | -64.96808 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0800d2d9-26ca-3252-9433-e22a15115e99 | -14.05937 | -46.24745 | 2025-07-11 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d9d31ec-ec3b-3e9b-98fc-2acadd3dfdd9 | -10.58073 | -49.134 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d1f1cc3f-e94e-346b-a556-009dc1c4a339 | -12.40942 | -45.36428 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac610d91-791c-30f4-9a7c-f3531f0b6879 | -9.51212 | -55.96482 | 2025-07-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e796396f-2ab3-37f6-b36f-d5d34460b338 | -9.94657 | -64.96133 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13eef3e6-bb1d-3943-9c50-843f9c8d9b81 | -10.67342 | -49.48961 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 35fef3b7-ff71-394b-8a19-92cc8ed534f0 | -12.99162 | -46.27524 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9dbde0ad-d960-3b22-99f9-815c597a27d7 | -15.36403 | -49.4922 | 2025-07-11 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b731b8c2-b8b8-31d5-b9d3-57863dfd1076 | -12.40368 | -45.3636 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02fb6cd1-618e-3a18-abe3-211435beec3f | -12.9864 | -44.86235 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b989b6a0-a002-3df8-8136-c06bad722f7f | -12.05585 | -48.54853 | 2025-07-11 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7008b7a-b3f8-39b9-9fcd-e867c5e9e166 | -14.31474 | -52.74368 | 2025-07-11 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef0a5de1-9f0f-3656-9f95-735ff6168a00 | -9.96921 | -64.96181 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 648c3b4c-5037-3161-8c63-ae302cdc4748 | -13.00679 | -47.82883 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 642d1f20-3d45-3a26-8a39-65b02dee4ad6 | -13.3654 | -47.89161 | 2025-07-11 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63108808-2904-3ddc-b227-f957d760ce6e | -10.57698 | -49.12918 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 663b9201-f9a9-3629-8264-b50fcf727835 | -13.15402 | -47.28756 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd580755-7968-3232-9a3b-2ea8c8c961dd | -12.06774 | -47.98341 | 2025-07-11 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| effae17c-4204-366d-9476-9d88694a7fcc | -12.02405 | -49.52002 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4911f782-ac1c-338c-9637-7782e65a7679 | -9.96508 | -64.95345 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4613d950-a557-3bbd-87fb-181f84c997cf | -10.84917 | -49.11552 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99cd4489-11f8-3d0c-8c7e-1c75c8f5f1a7 | -12.03722 | -48.76107 | 2025-07-11 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 963d9b2c-fd80-39ac-b0a5-a39c661ca24c | -13.15365 | -47.29056 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README19.md)
