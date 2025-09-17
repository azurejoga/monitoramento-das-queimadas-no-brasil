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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 675fe43b-976c-30b0-9b3e-7dbdca1dc7cc | -8.15572 | -46.75505 | 2025-09-17 06:03:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| cb390f56-9e32-3cd3-a099-65c6218e4e12 | -7.88289 | -48.16376 | 2025-09-17 06:03:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a28bd314-e420-3492-b64d-36deaa91250f | -7.06341 | -44.34073 | 2025-09-17 06:03:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8f7c5e5c-e85c-3b14-abed-be66f575693d | -2.82935 | -48.65752 | 2025-09-17 06:03:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 11c82c92-0faa-305c-bcad-43ca64141924 | -9.06832 | -47.01995 | 2025-09-17 06:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6769e568-415d-30a6-a008-d60f57b681f6 | -8.65746 | -46.40177 | 2025-09-17 06:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 952748e2-2b52-35fb-b0a3-af1842ce46fa | -6.68122 | -46.30499 | 2025-09-17 06:03:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cfc19075-f8e7-372f-8b9f-80037e3e3b79 | -6.20983 | -45.11469 | 2025-09-17 06:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| ad12b928-d04f-3019-b7e3-7177e8fb9117 | -7.40222 | -50.0056 | 2025-09-17 06:03:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 007b3ae0-6588-3177-a6c1-f1de7c78d64f | -6.39765 | -43.33917 | 2025-09-17 06:03:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4deecb78-d7ea-3ad9-bbd2-d49c19e1df22 | -3.68846 | -49.01387 | 2025-09-17 06:03:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05b4d0ce-b70c-32ae-bf12-fd0a00874e99 | -5.62691 | -44.82804 | 2025-09-17 06:03:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a6e6ceef-5268-3d73-a8ed-889835c80717 | -6.2104 | -45.12032 | 2025-09-17 06:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 340.7 |
| b6c68c1b-798c-3bf2-b98e-296ada38873f | -9.08168 | -46.92866 | 2025-09-17 06:03:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3c75044e-e84a-35a9-ae7f-d3b9ec055d33 | -3.17656 | -48.8063 | 2025-09-17 06:03:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 606ef62c-06ac-305d-8550-98f1de487065 | -6.20867 | -45.13212 | 2025-09-17 06:03:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| ce83feb4-8ab8-32a1-9d97-1df96e858b6e | -7.57133 | -44.55392 | 2025-09-17 06:03:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| aaeb145c-cab8-3f79-82d7-6cac1847fb23 | -11.57804 | -48.28326 | 2025-09-17 06:05:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a449ef81-cdf8-3517-9793-8acacfebf4cc | -12.73255 | -48.01079 | 2025-09-17 06:05:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f0a0b01e-1aa4-33d3-8370-4b5c20c6c39f | -12.84602 | -47.19626 | 2025-09-17 06:05:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c57190c5-032b-38d6-b028-9742b2ef3806 | -12.2839 | -50.12303 | 2025-09-17 06:05:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1685b413-1c17-3db6-b2da-19c140fc3a5f | -12.7233 | -48.00943 | 2025-09-17 06:05:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 742eea06-79e5-3a2d-a74f-224b003cf071 | -11.60035 | -49.81336 | 2025-09-17 06:05:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 636bf8f1-04d0-38da-ae56-5481babb2750 | -13.22012 | -47.29689 | 2025-09-17 06:05:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8e78e3fe-1477-307a-941e-b07eab48c93f | -12.39223 | -51.40871 | 2025-09-17 06:05:00 | AQUA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 45d3ed45-7fdb-340a-a019-f30cc129e190 | -13.22164 | -47.28595 | 2025-09-17 06:05:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a9a41baa-d5fa-3f98-b31d-eb8f69a5fdf8 | -11.01389 | -48.92311 | 2025-09-17 06:05:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 478b45ba-ba61-313f-a98e-6fc49a56d498 | -12.73115 | -48.02073 | 2025-09-17 06:05:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8272830f-e0ac-313c-ba59-c33a51dc83af | -11.57941 | -48.27377 | 2025-09-17 06:05:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2899062f-dccc-3273-8db3-9a3097c07d35 | -12.40125 | -51.41014 | 2025-09-17 06:05:00 | AQUA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 317ae2e8-8225-3bcf-b2cb-73c71fb5c17d | -12.7503 | -47.95215 | 2025-09-17 06:05:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b747a065-14e7-3f69-8a6d-2b708fd10269 | -12.85514 | -47.12981 | 2025-09-17 06:05:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| df33e079-9329-371e-a09c-646f4caf0bfb | -10.80781 | -50.70785 | 2025-09-17 06:05:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b21b5b36-8709-3abf-b34a-d64d486890d9 | -10.55036 | -51.4749 | 2025-09-17 06:05:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2455ce4a-5f11-3fc4-921c-42e09920e1c6 | -12.9935 | -47.93922 | 2025-09-17 06:05:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3bc78128-86f2-3f19-9d0a-9899ee3cfcd5 | -12.71684 | -47.98815 | 2025-09-17 06:05:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0df4c254-ab87-3f8b-8340-b999dc6ebc39 | -12.38199 | -51.41099 | 2025-09-17 06:05:00 | AQUA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 273ad758-4c69-3ad7-8370-c455116eb882 | -10.55191 | -51.46511 | 2025-09-17 06:05:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0713fb62-6e21-3f21-a59f-77ad9a2c0556 | -12.86322 | -47.14324 | 2025-09-17 06:05:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b332735b-fc54-3db7-aaee-8c18311ff88b | -10.80734 | -50.65142 | 2025-09-17 06:05:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d236371d-85c2-3f14-9474-7f3a8b42b3a6 | -12.2927 | -50.12439 | 2025-09-17 06:05:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2028fef5-ec53-32dd-819f-f402eccf46ff | -12.7247 | -47.99947 | 2025-09-17 06:05:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b61ee35a-80c6-3eb5-b534-521c02cf68df | -14.81712 | -48.11426 | 2025-09-17 06:08:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 325777c4-7c99-352e-9c2f-715fdb0caa37 | -15.41733 | -46.14994 | 2025-09-17 06:08:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 92c34c8a-4b58-333d-a761-519d43b78315 | -15.42821 | -46.15107 | 2025-09-17 06:08:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 792d25be-c402-3e24-b6a8-565c341c5eee | -15.55832 | -47.15938 | 2025-09-17 06:08:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8f76118f-9aab-3e53-a502-94b4f15e0175 | -14.5505 | -47.35514 | 2025-09-17 06:08:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a562716f-d8e8-31d2-8662-c5bd7f1a0bdd | -18.01971 | -50.93678 | 2025-09-17 06:08:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| f6a02eac-383f-3001-9dce-ee11a94c16b9 | -18.37655 | -43.31747 | 2025-09-17 06:08:00 | AQUA_M-M | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 4b4fa10f-601b-34e7-a526-8f1e75ca2ca8 | -14.70587 | -50.2421 | 2025-09-17 06:08:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4c7d86f4-29e2-38d7-a939-0ac36f0a8d6a | -17.18918 | -45.90926 | 2025-09-17 06:08:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4d5ab47c-1be4-3dad-80a6-02cbc21e6d4f | -14.81857 | -48.10366 | 2025-09-17 06:08:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 1af4e57a-dc44-320c-9165-d399d8c90c44 | -15.5567 | -47.17139 | 2025-09-17 06:08:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5a4dec4d-86fe-3a51-a3fb-40baaa6be4d0 | -18.01834 | -50.94599 | 2025-09-17 06:08:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 96208b6b-aef1-379c-b2de-fe98bdf1186f | -18.31678 | -43.30124 | 2025-09-17 06:08:00 | AQUA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| aa67a4b9-796a-35db-a007-eff252b3319b | -14.60803 | -46.39309 | 2025-09-17 06:08:00 | AQUA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a1cc6dd9-2d67-3c60-953f-ceeb076a6606 | -18.02852 | -50.93819 | 2025-09-17 06:08:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| fdc86f55-3649-3c45-8e6d-8595486e9c25 | -15.43541 | -47.31716 | 2025-09-17 06:08:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1f7c0575-43b9-3113-8f3a-1842fff1a8a0 | -14.60395 | -49.36585 | 2025-09-17 06:08:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8eb7640-bf24-3b1c-b0f5-d99de1dd7788 | -14.7981 | -42.92489 | 2025-09-17 06:08:00 | AQUA_M-M | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 21.2 |
| de6c4543-1f54-3f54-a12a-d03caf42f0db | -18.12565 | -44.65067 | 2025-09-17 06:08:00 | AQUA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b745cb98-d494-3a0d-8ca3-b47dd0987559 | -18.32002 | -43.30811 | 2025-09-17 06:08:00 | AQUA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 903fedc8-1337-3bd0-b89c-0ec698c25b74 | -14.81309 | -48.10682 | 2025-09-17 06:08:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 81d7405a-64bb-3348-8ef0-2884ae8d8aca | -14.55251 | -47.35019 | 2025-09-17 06:08:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0d7eac3e-df4b-3a83-8625-8e8c071e701c | -19.27832 | -47.42265 | 2025-09-17 06:08:00 | AQUA_M-M | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 36.2 |
| c1c648cf-b830-3af8-b4e9-a46a4c4359c9 | -18.02715 | -50.9474 | 2025-09-17 06:08:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 336348d7-2ff6-3ec0-8fc9-8effa2860ed4 | -18.0303 | -50.9385 | 2025-09-17 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c79ca448-6eaf-36d0-8150-7540a90c12b3 | -8.64771 | -62.67622 | 2025-09-17 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76993391-de1c-3050-9fa8-c2e9fce270c6 | -8.84645 | -62.93013 | 2025-09-17 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e9de3a-147f-3b1f-b8d5-e35835c33861 | -7.87677 | -72.85924 | 2025-09-17 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dd8c0ef-410c-3324-8aec-109a8e4391ca | -9.55982 | -67.46131 | 2025-09-17 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6614129b-3a63-3bb1-a636-319eaa5b0f86 | -7.43518 | -63.63116 | 2025-09-17 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e643e45c-31b5-3849-ab04-b35b28aefc11 | -8.23071 | -71.03288 | 2025-09-17 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d64cb36-98ed-3948-808b-4084d810a49d | -10.60687 | -69.25838 | 2025-09-17 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b0eb235-b57d-3b97-8938-4bace7194947 | -9.62574 | -68.65458 | 2025-09-17 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 192e5aa0-88d8-377d-a1af-772ae3bb7674 | -10.06512 | -68.47769 | 2025-09-17 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 049d2457-5d08-3e38-bc0d-f206a943c65c | -10.89103 | -69.03711 | 2025-09-17 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1e76575-c65a-3849-9124-da0668b2dbae | -7.44025 | -63.63564 | 2025-09-17 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74b2d00b-81ed-3ab5-a751-46cde593ee58 | -7.97934 | -70.3535 | 2025-09-17 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a72ec04-1ead-3c4b-a761-10c3fdfb05b4 | -10.17114 | -68.42962 | 2025-09-17 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75821683-18f4-3441-8499-bf734dbefaaf | -10.05163 | -68.45221 | 2025-09-17 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cfa80045-4cab-3820-9247-a1e9e6e4bb39 | -10.21283 | -69.05026 | 2025-09-17 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33638c2f-0402-3061-ac3d-efedd24cbf4d | -7.84446 | -72.85062 | 2025-09-17 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2159a30e-b7e6-3d39-b149-b42845d8eb9c | -9.31964 | -68.23062 | 2025-09-17 06:14:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a869865-dbce-3ee9-803f-ef5b33b4bc09 | -8.8459 | -62.93449 | 2025-09-17 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61b38ff2-19ce-3715-bf96-e1d23e836fe2 | -7.43974 | -63.63938 | 2025-09-17 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b5f234e-6285-3f8b-a7aa-404fe1137abc | -10.05598 | -68.38977 | 2025-09-17 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e485609-378e-3523-98e5-531bb57c8cf6 | -7.43467 | -63.63489 | 2025-09-17 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d288891c-8ac1-3dc3-abea-1d212c997825 | -8.65432 | -62.67249 | 2025-09-17 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29f358ea-bfcf-3487-9fc5-6f8a61317de0 | -10.06017 | -68.39039 | 2025-09-17 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6982fb73-d095-3104-b4cf-9d735d05cd88 | -8.6525 | -62.67466 | 2025-09-17 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a668960c-dcc9-3723-8e0a-fa588afc6bca | -11.08239 | -68.72906 | 2025-09-17 06:14:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c8b2448-d9cf-3252-84f1-a8e9510c0af7 | -18.386 | -43.3113 | 2025-09-17 06:20:00 | GOES-19 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 780e760a-d924-3970-a06a-d1617cc52f22 | -15.8417 | -59.4799 | 2025-09-17 06:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2cd7e073-7d44-3663-b751-d823ef558db7 | -18.0303 | -50.9385 | 2025-09-17 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e6e1131d-a67b-3b6c-97c4-b7b3c76b133b | -18.0303 | -50.9385 | 2025-09-17 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ee1ee387-69c5-32e4-9d50-8042432416df | -21.5991 | -50.3262 | 2025-09-17 06:40:00 | GOES-19 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 219.7 |
| 538a6330-2ccf-3e54-8057-e2c98d3ad42e | -21.6198 | -50.3216 | 2025-09-17 06:40:00 | GOES-19 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| 7512fc77-ea05-3239-b33b-86add088da32 | -21.5998 | -50.3033 | 2025-09-17 06:40:00 | GOES-19 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| f1dc2ca2-691e-3ae6-bd29-9044e293be26 | -18.0303 | -50.9385 | 2025-09-17 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |


[Clique aqui para ver as próximas entradas](README56.md)
