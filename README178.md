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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9e13766-e2b0-3dc8-90a4-6031c28b7fcc | -21.65478 | -41.35289 | 2026-10-07 16:35:00 | NPP-375 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| eaf2a110-faca-3f18-a063-ac1b20735a69 | -12.22716 | -44.73966 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| e2e3db48-d18a-3958-a99c-0dd331e826f0 | -12.58246 | -38.98133 | 2026-10-07 16:35:00 | NPP-375 | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 80de2f35-7c0f-3668-8caa-0c84e5150ac2 | -11.85661 | -47.33377 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f6f13561-513c-30d3-8755-94f6680cfa5b | -14.9156 | -48.08615 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2b5b87dc-db51-3600-b717-b123c3ce6ec2 | -14.91079 | -48.08261 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 374a5057-4ffb-3fba-b746-155a44858372 | -14.25072 | -41.62214 | 2026-10-07 16:35:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 44bd8b52-0ea0-39b5-9e46-67f61b6780ad | -17.28568 | -39.29263 | 2026-10-07 16:35:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fc6cddd5-5f1b-3db4-94a4-8da193ad1c92 | -12.19996 | -44.65071 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c0dbdeef-e144-385e-b276-f22b97e32e02 | -18.33827 | -42.24084 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5dd7e927-0152-38d7-be87-3566ce839906 | -11.84662 | -43.55914 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| df679996-7956-3d73-99b4-3be8edae866a | -19.01766 | -42.91565 | 2026-10-07 16:35:00 | NPP-375 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| c2c6fed4-e482-3b08-9ead-4044984317cf | -13.66291 | -42.45467 | 2026-10-07 16:35:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 58.6 |
| aaa2d55c-9a59-3f20-937b-cc22117d805c | -11.86383 | -48.03392 | 2026-10-07 16:35:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8deda31b-4c3f-353e-b9d1-86408c5df5db | -11.61078 | -44.15155 | 2026-10-07 16:35:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4467f20-5550-3468-b998-58cd9d17378c | -11.84275 | -43.5561 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ce3eb06d-273d-3c9a-a1e2-5221182a6e1d | -13.69895 | -49.10274 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 3a8f72a3-a5f8-38ed-9ec3-28da09fceb15 | -18.03986 | -42.54011 | 2026-10-07 16:35:00 | NPP-375 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 96f0596a-494f-368f-b9c8-b2efa3d27764 | -11.64488 | -43.6783 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b240c916-3f7b-3f3e-b670-0af1c43f8d3d | -11.22361 | -44.85981 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5f1038e-28ee-3d4d-9bf9-bdd1afe0e555 | -12.18632 | -44.77297 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| ee1f574b-14e0-3daa-a5e7-42ac51bb3409 | -11.85975 | -48.03446 | 2026-10-07 16:35:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f063efb4-286b-393a-8be6-71c6145fa843 | -16.76628 | -39.64279 | 2026-10-07 16:35:00 | NPP-375 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 350e6ace-962e-35b1-a321-66efcd018f0c | -11.77023 | -46.70259 | 2026-10-07 16:35:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2d553be4-a70c-3b7f-931f-08b213d7947d | -11.74772 | -44.94411 | 2026-10-07 16:35:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ba1c54ad-0fde-3592-8af5-967b90effc2f | -11.96227 | -41.28796 | 2026-10-07 16:35:00 | NPP-375 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9958a7b8-ef71-355c-99c1-810720db875e | -11.77007 | -47.74087 | 2026-10-07 16:35:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 94a1ab76-8bc4-3810-a5c9-5db7c06b2f50 | -11.62714 | -43.64187 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4603f1ed-3474-339b-9b0e-46b4dc82eb2c | -14.76828 | -47.15564 | 2026-10-07 16:35:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 37cd1cb9-9c27-3bd5-8a6b-417669864ab1 | -13.68384 | -48.80381 | 2026-10-07 16:35:00 | NPP-375 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2ae82e47-2d51-36bf-9268-c12fef166f9d | -12.23054 | -44.72344 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 88d3bc76-f130-3c4a-aedd-b466eea970c6 | -14.37412 | -55.02521 | 2026-10-07 16:35:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d368ab21-0cfc-306d-b49a-cdd7c9c1663a | -11.87288 | -44.77391 | 2026-10-07 16:35:00 | NPP-375 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8b78a941-ecf4-3bba-a82a-41b83aaf95fb | -11.2205 | -39.98064 | 2026-10-07 16:35:00 | NPP-375 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3292fa64-5b69-39c2-8aa4-6747e945d15a | -11.71783 | -43.42014 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 691fdcd1-3332-3bb1-89d9-68fbb9903050 | -12.2282 | -44.7316 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| d3b29e39-d1b0-32ed-8e3b-ceb292738a01 | -13.68837 | -49.10288 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 7582033c-8604-3062-bd8d-0050dfdd2f32 | -12.17665 | -44.75496 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 469dc349-c258-3a53-b4c3-c185d2e0dfa6 | -14.10797 | -48.42968 | 2026-10-07 16:35:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5190b69-baf5-3856-a40e-7b0463b8c3fc | -14.24556 | -42.00105 | 2026-10-07 16:35:00 | NPP-375 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 611daa87-a80d-38c5-a3ae-f9cb002a17e5 | -11.71326 | -41.7658 | 2026-10-07 16:35:00 | NPP-375 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 1de8ae04-07e6-35ab-b561-e32565dbf6bb | -11.83728 | -47.36869 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 76063d18-5a29-31b7-a9af-87531b6ed6b7 | -11.85395 | -43.53968 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fff46aed-1456-3de9-ad72-c4ef946880de | -12.71751 | -48.84571 | 2026-10-07 16:35:00 | NPP-375 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4129603c-28ae-39b6-9b75-d8b022772c54 | -17.89446 | -42.49493 | 2026-10-07 16:35:00 | NPP-375 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ff14fa4f-bf8b-30ec-9952-72f0e31ed654 | -11.8451 | -47.36763 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e9344495-cdb5-3ddd-91ab-b3317e6cef9b | -12.2253 | -44.73593 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 6d6313a9-ce6c-32eb-8f14-6c552b30abfd | -12.29446 | -45.29428 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 393994cc-68ff-38e8-92d5-8eaeda0cb2d7 | -14.43537 | -42.28715 | 2026-10-07 16:35:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 8ede27d8-4cee-3890-81e1-a096e7aa9cfd | -19.54193 | -40.19035 | 2026-10-07 16:35:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 49c6c4be-415a-36aa-9473-97dd537e7de8 | -15.32149 | -48.01389 | 2026-10-07 16:35:00 | NPP-375 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 98c43718-e156-36b3-9183-65b0f07d14ba | -13.33741 | -38.98557 | 2026-10-07 16:35:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 559de45b-da4a-3039-9c8b-24b3d9da4716 | -15.14842 | -47.18982 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 202079bd-a877-378b-8cd3-94309f9c2f5e | -11.82528 | -44.68848 | 2026-10-07 16:35:00 | NPP-375 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a112930e-0761-34b8-b745-df33519d95e6 | -12.22256 | -44.71689 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3f263669-0bff-3965-a8c8-9408c675cf01 | -11.55387 | -41.95471 | 2026-10-07 16:35:00 | NPP-375 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 3f6e6471-f21f-3be7-9894-b566eb3313f3 | -10.44915 | -36.84252 | 2026-10-07 16:35:00 | NPP-375 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| 3faa478c-f654-3c42-acd8-4fbd98f3ff94 | -13.58877 | -43.16712 | 2026-10-07 16:35:00 | NPP-375 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 6d387779-8586-3347-a575-d9ed57ec1bbb | -11.27662 | -45.22165 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 40f19947-827f-3fbe-871a-5d3a5432533f | -11.62445 | -43.6241 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| b207fa16-06cd-35a4-9b8b-f0539fd7d3af | -13.7733 | -43.53782 | 2026-10-07 16:35:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 528e3ea9-b573-3c44-96ef-75ded36f919e | -11.72836 | -43.42212 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f4c8fc13-3c2c-31b3-89bd-14ced21308fe | -11.83941 | -43.55663 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2fb1f117-72ad-32f1-9b05-8df03b8f765e | -11.83922 | -47.38207 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 41867793-f2cc-34ef-84de-15b4f4eaa853 | -18.3135 | -42.24527 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 929a4eaf-654a-3a18-8cdd-18313e2789d5 | -11.84222 | -43.55252 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d71e9e27-c1c4-3e07-a529-7e55163d512f | -14.94534 | -45.45478 | 2026-10-07 16:35:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9ebbc15f-3736-34e3-a9d5-d367de3e0232 | -11.26118 | -45.18873 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f482ecd0-7d0e-3db3-a191-6926097e9350 | -11.62046 | -43.64291 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 37c97ff8-d8bb-3213-981a-ff33a03ccfdd | -12.16755 | -44.74082 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 80c7be33-f1b0-3835-b4fe-972002793afe | -14.79754 | -47.12981 | 2026-10-07 16:35:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a1531b3c-294e-3e08-a72f-25f85c52b4b5 | -11.7117 | -43.42471 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5e78c2da-63c6-3f06-b6d8-6fc95949cc24 | -12.19792 | -48.41596 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 6eded759-d206-3b1a-a7e9-f6bb9e5a860f | -12.18799 | -44.78442 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4a985806-ff0e-3cf8-beca-64640d6ac4b0 | -12.9976 | -47.06182 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 3d6d4a92-5da6-36c4-9727-f4d390ae9435 | -12.17553 | -44.74736 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1fd738a7-e23d-3b95-b52a-35236605ef48 | -11.64207 | -43.68239 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 4b9cec3a-c284-38b3-9330-8bfae14edac1 | -11.23051 | -45.29602 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 95dbac20-f076-34c6-a392-9d71e2f6011e | -11.63636 | -43.68034 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 125d02ba-dff6-3836-9f84-e2c20d09b414 | -16.85356 | -40.59719 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 901624e4-7dfa-37bc-a521-0baae6e80130 | -12.16133 | -44.72233 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d3ad69d1-7ae8-3083-b502-7d5f16d3dd53 | -14.35918 | -41.2755 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 98ac7fab-c35c-3463-b5ae-311a0d99683c | -12.82969 | -45.57089 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 66b387ec-2548-383b-9abd-67dd937d7660 | -12.03134 | -42.94595 | 2026-10-07 16:35:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b20ebc95-8aae-3c82-9151-58aaa73b0851 | -12.226 | -44.71637 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a7ad4a20-cb47-3acb-975c-f2a217f8dcc3 | -12.84374 | -44.62359 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6ec8562f-0e6c-3d50-91bd-c7b4be2e46f1 | -12.29855 | -45.29772 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ed1950b6-e5ee-3d74-9cba-44cb4fea3e92 | -11.72889 | -43.42566 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2e6f5e3e-0e0e-371f-87d0-ef11f4fe7e09 | -13.57117 | -47.24397 | 2026-10-07 16:35:00 | NPP-375 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 22ba777a-b5ab-3182-acc4-80aad269ee9e | -14.84754 | -47.31782 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d6f5fc38-d99f-3679-ba3e-78e2a13ff73c | -14.91234 | -48.09457 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 0852b94c-128b-30e3-875c-c909aa6dde70 | -13.47729 | -42.47767 | 2026-10-07 16:35:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 462f354c-bb6d-314c-bcb3-a83bbee1c3bd | -12.44496 | -47.80861 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c4389191-168c-304d-98f9-e1c7b7185cd3 | -16.85968 | -40.59229 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| ed7bbc22-3ba6-369c-8f39-766576ec328f | -14.35526 | -41.27241 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| f54f46c2-640e-3358-95d6-7214e208a010 | -19.90294 | -42.08693 | 2026-10-07 16:35:00 | NPP-375 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e6da1ade-c5e1-370b-94a0-0f2698dda343 | -12.16411 | -44.74134 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| a76f29fd-ab13-348a-9232-9ec53b924c59 | -13.0729 | -43.60324 | 2026-10-07 16:35:00 | NPP-375 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e98cd00c-9f34-3f3c-8a4a-6d165b562ee5 | -14.74326 | -47.4617 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85cfc56c-250c-3563-a61d-e89a2dba8177 | -12.22091 | -44.70547 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |


[Clique aqui para ver as próximas entradas](README179.md)
