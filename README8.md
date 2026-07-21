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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6cd0400-73e3-3844-9f03-e3fdfddcb0d3 | -11.83313 | -44.77375 | 2026-07-21 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96ef758a-17a9-3baf-9a44-690dd00e7f38 | -11.41716 | -47.51823 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00acbd40-cd7d-39ca-a244-e37e0c38cb32 | -13.31117 | -45.12672 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 877f054d-5281-3551-b713-5a7168ab0245 | -7.88659 | -46.90835 | 2026-07-21 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 674fc484-5a25-3639-a402-eb91e0c99470 | -10.62964 | -47.48726 | 2026-07-21 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8870818-c6be-38bf-92a3-dfdc5647d991 | -12.66401 | -48.20086 | 2026-07-21 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11dd4db5-1687-3cfb-9481-2c664d82c05b | -11.34158 | -47.99902 | 2026-07-21 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 553ec116-ff90-34dc-ad85-ce5c7eab3907 | -7.6462 | -49.75526 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f477b88-a151-389d-9b59-9def637e4447 | -9.61944 | -47.1818 | 2026-07-21 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e43d8bec-7843-3864-a4aa-fe8ff480e203 | -11.37368 | -47.49331 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cce7a317-8708-3252-928e-5720996722ae | -10.85856 | -50.42407 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 825e8848-ea11-39b0-a3ca-958372b9aa1b | -7.64259 | -49.75466 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8083147f-6517-304a-9e4f-376246f0c0b2 | -10.74218 | -44.83587 | 2026-07-21 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c86c119-eeeb-3546-9b62-6816027c0110 | -6.21325 | -57.75531 | 2026-07-21 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8153cfd-d90e-344e-bc55-2038053837cf | -9.08249 | -50.58518 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 811ecc6a-31ba-3d09-a846-d5493882732b | -7.63107 | -49.75708 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9d79e70-d58b-3fd4-bc1e-f823b3073703 | -13.30353 | -45.12974 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d6b32805-3b60-3af4-a1b1-78429ef803ea | -12.08446 | -53.33883 | 2026-07-21 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42d905f7-f6a6-37d4-9da9-053a1a51d515 | -11.3427 | -47.99198 | 2026-07-21 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18c74b88-329e-3e82-9225-be425f0fe808 | -12.52288 | -48.25357 | 2026-07-21 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdd906a6-3db9-3501-8ccf-195119d18b75 | -7.86404 | -45.98125 | 2026-07-21 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62db8012-eaec-34a2-9a37-bdd7e39f5b7b | -13.56638 | -47.78045 | 2026-07-21 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2256d23-93dc-362a-a47d-96e387beffea | -14.22547 | -42.79968 | 2026-07-21 04:27:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df2f4abe-712e-319c-8998-f14ee7d93dd3 | -12.5262 | -48.25411 | 2026-07-21 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6773a5e-f23d-3cf4-ada0-365e2a1b77f8 | -8.75439 | -49.0837 | 2026-07-21 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c5fcfd3e-9478-3480-ad5b-8e239d1283cf | -11.41661 | -47.52174 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0bb483b-9624-3928-b019-dc4248b546a0 | -7.683 | -55.36588 | 2026-07-21 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a171baaf-1e13-3877-98eb-8554995d1f86 | -7.63829 | -49.75825 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b0e8eb66-e7b8-3248-aaf6-f2705b3e3983 | -10.85137 | -50.42286 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3456666-ef2c-3be0-8f02-a03f14698649 | -7.65102 | -49.726 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f716cc-c478-329e-a3ba-ad0102d2a390 | -13.55775 | -46.11486 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea4fa54c-0cab-387e-93cb-78f68ba60419 | -11.59838 | -58.50656 | 2026-07-21 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebeaa1e4-c0a3-3f6b-a083-d7772a6339a7 | -11.39624 | -47.50053 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e505631-5e1f-3671-807a-478319610a20 | -8.75786 | -49.08426 | 2026-07-21 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fde9df5c-6a97-3517-a80a-4515d25672ae | -13.52888 | -52.74031 | 2026-07-21 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 407252da-5598-3175-9b52-ed2d2b300af4 | -10.60082 | -46.53364 | 2026-07-21 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72ec98a2-6ddc-3460-a00c-3accf7f43014 | -11.39018 | -47.49596 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d28ff8db-63a6-3faa-a988-5c41657b8fc0 | -13.30587 | -45.13834 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 63623112-7846-33d9-a49e-a87a11c12644 | -13.52863 | -52.73713 | 2026-07-21 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d90814e-fe85-3a3b-827a-a010cee4b498 | -9.08175 | -50.58963 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57e54907-6af4-326a-8da4-653aa90904a8 | -7.63468 | -49.75766 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1ba3439-040e-30bb-acb9-c9b96999fe08 | -12.69677 | -45.3263 | 2026-07-21 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bb24813-8b9f-3941-a43f-78ec573e9e13 | -13.30412 | -45.12569 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 49acec17-ead5-34f9-9fd0-fa18e4cedf3d | -12.14073 | -48.25989 | 2026-07-21 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 090bd6fe-0dc2-3d66-a068-908229a95c21 | -8.8342 | -48.33179 | 2026-07-21 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e92d3445-9f1c-3a7e-8fd0-71aab9a9af2a | -11.39294 | -47.49999 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9674a7eb-50ed-317c-8689-1d85c836399f | -12.51957 | -48.25302 | 2026-07-21 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b23ab6f-29f9-32f3-a2a2-7f3bd3568563 | -12.46259 | -46.51582 | 2026-07-21 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 167ed597-ad74-3304-808e-3a07907fc363 | -11.83373 | -44.76962 | 2026-07-21 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cc13197-02e1-398f-a5d6-04adc3a69600 | -7.83837 | -47.10715 | 2026-07-21 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00b62969-7c61-3d56-b4f9-f941da61b17d | -10.51371 | -50.28759 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5c942b4-4f08-308c-87bc-5401891fe3c5 | -12.01667 | -50.55452 | 2026-07-21 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eba35f45-ee4b-3e92-be06-8ff58b322cb7 | -7.73634 | -49.47363 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd719906-2b1d-361a-aeef-ea5e58613945 | -7.68819 | -55.36671 | 2026-07-21 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8e3ccf8-3fb8-367a-a715-a7a805d7722d | -7.63537 | -49.75348 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3d649b91-3a1b-3352-9660-73ec89ae2722 | -13.31058 | -45.13078 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 1d58f3b9-0010-32e4-8d2c-c936cfe8f1d3 | -13.31644 | -45.13989 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| accde12b-9be4-31d7-ac7b-7fd10a6ec403 | -11.83728 | -44.77 | 2026-07-21 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98d6311f-0560-32a3-9ebe-f438dd3c8c55 | -8.94401 | -47.60365 | 2026-07-21 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 619ce873-2c1b-335d-9a74-eff6e31991f6 | -10.54872 | -56.33492 | 2026-07-21 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f012cf50-5043-302d-a925-613cfc6d618f | -7.68357 | -55.36269 | 2026-07-21 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26a58353-c069-3c75-89f5-e0c8e23f034d | -9.0899 | -50.5864 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4427662a-4695-3780-b7e1-50eaa2d2cb20 | -6.57754 | -55.16253 | 2026-07-21 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875395df-b8d5-3515-bf44-0ab3b6a9b9ea | -10.79966 | -50.42275 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5a429d27-f5e7-3387-b924-ccb7509f8b8c | -10.51302 | -50.29176 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c0a3f7b-cb53-3b32-9bc9-b07c9a962373 | -7.6498 | -49.75586 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57cf1b61-d65f-36df-8351-750f55b05f2b | -13.5583 | -46.11111 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 361f01f6-6d1e-3244-b200-67cbab3f6a2a | -7.65049 | -49.75167 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2213f297-8555-3574-8729-959666d816df | -11.65906 | -49.75739 | 2026-07-21 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 596b916c-60f2-3dec-8af7-f7ca3167a173 | -10.79606 | -50.42214 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cbc9020a-0934-3ef9-9561-6529315d4bc2 | -11.41165 | -47.51017 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1840c43a-7b70-3be0-ac19-75272318a303 | -10.63019 | -47.48376 | 2026-07-21 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bce8899a-bb19-3c50-90e7-b2fa57f3657b | -10.85883 | -47.37055 | 2026-07-21 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acde9f7c-7aeb-3d0e-b3fd-5215c5176d15 | -7.35174 | -49.60359 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 906a84a4-fea0-321f-9022-9e8f2620e4f6 | -8.83361 | -48.33542 | 2026-07-21 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 293754e0-d359-31fe-a504-7242353b51e1 | -11.63083 | -58.28358 | 2026-07-21 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e90c317a-8d0e-37df-b03a-b578acb5242a | -13.5685 | -46.11271 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c37777cf-4bab-3d82-a24a-b8c22dca503e | -12.36296 | -47.43038 | 2026-07-21 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13c9eae3-d4b2-33c9-a958-bae772692085 | -12.66069 | -48.20033 | 2026-07-21 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 548c2e18-205e-3e8b-b66c-053b457562f3 | -10.5546 | -56.33255 | 2026-07-21 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb7e549f-3d6a-3d41-a903-fa55b8a2f61b | -13.30647 | -45.1343 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 0941fffd-419c-3cf8-83fc-b3cb7301baab | -17.58301 | -47.50767 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0497cb09-4ff7-3ee8-83a1-9d340b6dc906 | -17.58637 | -47.50821 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8632224e-1d5b-3f58-976a-7f4a53157597 | -18.55294 | -56.81227 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 0857d829-adf0-3f6c-b836-baa88a19624b | -20.78756 | -50.51963 | 2026-07-21 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 377b7cf3-4c2c-3647-909d-bbc6f141f548 | -17.57294 | -47.50605 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c3b7303-82e9-3f9a-bf3e-991998c80be2 | -17.67168 | -44.46717 | 2026-07-21 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26060eb2-9adf-34f7-aee3-09ce8fcbf448 | -17.86651 | -50.51413 | 2026-07-21 04:29:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 21851f83-8054-3a81-a4e5-1f337296d747 | -18.55761 | -56.81329 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| f5a7985a-51b4-3b16-b3a7-ea138172a353 | -16.41239 | -49.47099 | 2026-07-21 04:29:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86861a4e-e6ac-3753-b7d9-829a24d1d071 | -18.54623 | -56.82168 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.6 |
| e5849e32-e4a3-353d-b28b-c17f6b2e4205 | -20.36916 | -46.60368 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3facb214-1184-3f75-9e6f-fb1f7238f89a | -18.54766 | -56.82401 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.9 |
| ac999702-446f-3a45-b6d6-4be2ddd02438 | -16.52401 | -47.73354 | 2026-07-21 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f994b3fa-bcf8-336d-9432-9717fa9dac80 | -16.0223 | -43.04246 | 2026-07-21 04:29:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed9e370a-aacc-39ac-8ba9-41cb41d652dd | -17.34271 | -48.68528 | 2026-07-21 04:29:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc38e3b2-0b59-3bf8-bf16-6d8d15a9677b | -17.86313 | -50.51352 | 2026-07-21 04:29:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a097aabe-70e8-35f7-8143-3d10ce7bfe5e | -19.71512 | -53.23971 | 2026-07-21 04:29:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a14fdd4-a13a-3309-9198-23e38cf4a458 | -20.43719 | -46.47413 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e9bb48d-4dd0-36ff-a1e8-af0f9cbfdae8 | -18.5566 | -56.8185 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |


[Clique aqui para ver as próximas entradas](README9.md)
