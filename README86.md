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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c553ad29-544e-39ad-9463-57d0fe8aea3b | -16.12786 | -46.94903 | 2025-09-13 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8513e36-05f6-37c1-a863-caee2cd5131e | -15.58332 | -54.77512 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84b9da83-ec8d-3827-a8b0-aca71a55fd08 | -10.88133 | -47.23273 | 2025-09-13 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7499a209-a362-3a98-a21b-615b236765f4 | -11.72649 | -46.58203 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab24bd66-318c-3f1c-92b2-3edcc51a5c9d | -9.36869 | -59.48024 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28c71764-e94d-33c2-89cb-65effef7b941 | -14.17949 | -46.24268 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86c40eff-7078-3076-b715-9311e6ad0258 | -14.18593 | -46.23558 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 582b237e-9aaf-3174-83f5-11945b619e95 | -16.25565 | -50.06354 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a04e3dc1-b50d-371a-b58a-d30c1192a673 | -14.44973 | -47.34794 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bf2e39e-f8df-36f3-b344-ae2f9161f4de | -13.13307 | -47.13189 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f53869-26b9-3e45-bc7b-609459d35191 | -11.13811 | -45.31214 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ad2a557-2765-36da-8355-4fd829828c51 | -14.4363 | -46.39863 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dcb6eb19-28e0-3c2b-ad3c-bc410fab159e | -9.2773 | -59.41407 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 503dc1e2-ee00-3d26-8fdc-513a6acf649c | -11.70791 | -46.5557 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1e4f7cb7-effd-33e1-bcf7-95b5523c1876 | -14.63876 | -52.0913 | 2025-09-13 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab306f23-1a61-34f7-8705-9a08ff390fa7 | -9.8079 | -61.51547 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5613e37f-9f53-3834-a179-7bd1fd55d2e0 | -9.83446 | -64.2278 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf09a1cb-cc2a-3343-ac9a-ab1e722cd2b4 | -12.91664 | -54.76183 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50060028-7ae1-33cc-b259-4d8e253e3efe | -11.27667 | -51.12562 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a82f7a1a-3d2b-31fd-93cb-e9f95338f39d | -9.50168 | -55.96095 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7b9f5916-6443-3d0a-b349-9aaca504fc0e | -15.71245 | -50.58243 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a3ae88da-da47-3650-b9ec-7bb0a9e800de | -12.13278 | -44.83785 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8df83c99-b722-33cf-a42a-eda647420d0b | -14.39172 | -60.28581 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad053bea-0e22-3586-ab13-b001f21ac47e | -14.6205 | -52.08373 | 2025-09-13 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 066ab67d-17db-3c0c-91de-51cb7cd9fa9e | -15.21606 | -56.68817 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fb332ff-505a-34ca-8d7e-e4e0c78b397f | -9.26695 | -59.41483 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 0c36bb9e-76fe-3612-a15a-31b331bbb200 | -14.61188 | -46.33318 | 2025-09-13 04:59:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 129c089f-37f3-387e-b665-80622cf3a5b1 | -11.10698 | -51.4499 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 974c0412-3e86-3856-9a43-72026e2c5126 | -14.17437 | -46.23849 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76e90ebb-0ceb-3c52-a979-6ea55a4bb2a3 | -10.41658 | -50.60476 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb020d2d-71e2-3159-bafe-43d5975bfe5b | -14.17517 | -46.27982 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| bdeb8215-96eb-30c5-957f-36654bab5548 | -14.38717 | -60.28962 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 755aef1b-9706-38b0-85b9-b3a966acdf78 | -12.57505 | -45.67073 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b142945b-facf-358b-a9b8-f2c4ddad864e | -13.13568 | -47.13161 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef59280-131d-3a89-ac71-b1244ff25c8d | -12.12738 | -44.83263 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7a109bbc-d5b8-3e90-8551-372b897df4b9 | -12.81728 | -47.93247 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8149625b-d561-37d8-96b6-3df5f401cf17 | -11.93731 | -44.29604 | 2025-09-13 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21b6385b-d65c-31a2-b02a-daa68b2ccd03 | -12.80779 | -47.96802 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb19434e-2505-30f2-9f8e-f8d48779a569 | -15.26757 | -51.42525 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c766c4c1-697a-3e0d-b679-d01b3fe052e5 | -15.12982 | -52.4751 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b868e31-4762-368c-9485-bbebe0ae4855 | -13.0004 | -46.73618 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eecd2d1c-7d3e-35be-9a9b-dc6e70c9b1fd | -16.41269 | -49.04485 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 875d70b9-fb1c-3a43-9521-705129e98e0a | -14.20543 | -46.26064 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ad5f5155-0035-3528-976c-342e1b0fdfb5 | -12.09482 | -44.86773 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cd79f5f-9896-3c35-b10e-98fbfb73471b | -12.86061 | -52.97607 | 2025-09-13 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16749eb9-7ddb-3e38-ad1a-7a9e2ce412ea | -16.57118 | -49.31166 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4ac3486-7be7-3b18-8a08-a6534b859f7c | -15.37848 | -52.1062 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 75d41db5-a815-3a1b-a5e1-65273b9a1657 | -10.32889 | -58.02266 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af4c24ae-bc4b-35fe-a921-0318c706fdfa | -15.55376 | -54.80209 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a18503f-f23d-3a6b-bf1e-a36fc7f5514a | -11.41933 | -50.73832 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 62857071-46f9-337d-969d-ab6b880a1441 | -15.87211 | -49.94322 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c409b5da-7f6a-309f-b6b5-6ddd40d32bc1 | -14.19191 | -46.28058 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f013982-f136-357e-8398-e73988a5b57e | -10.0016 | -59.97451 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 08443755-554d-305e-9cfb-8367a810c71a | -10.42926 | -50.62948 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67f4cc92-f4b6-3dd5-ac56-9cac5e709fd1 | -11.63102 | -46.91201 | 2025-09-13 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 017e9ce5-b292-30d9-83b4-38d0acb75cd6 | -10.51945 | -51.53196 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 859cdd2f-373a-348b-bd26-a1c2de3e27b1 | -15.03167 | -50.1445 | 2025-09-13 04:59:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e60cc5b3-9b0a-3258-83a8-d746f0397237 | -12.86256 | -62.13147 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b832195-3ed1-3a84-b745-b9646b4ba2fc | -11.18906 | -51.41702 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 29735005-6411-3f91-8e8c-dfd7f9899b4c | -11.33972 | -50.79188 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c76c2cea-ba77-3863-a20b-9490a687fb9b | -14.17354 | -46.2456 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c86665ce-daf5-33a4-89fa-8ff73d1a3629 | -14.19117 | -46.28725 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf841829-d6a9-3de6-b3dc-88a72c2c0b0c | -16.43828 | -49.0434 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4face81-0cad-39ef-aebc-0252a227c445 | -14.46062 | -47.3445 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a19ab5bb-eb83-3b94-8f0e-248daeb1daa3 | -12.12287 | -44.83315 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6628b8e-595f-3c91-86c4-ceba3eed53e7 | -9.80352 | -61.51467 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f63f8b9-f16a-3fcc-b476-c33ac994e4c0 | -11.45616 | -43.57345 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcb8ea03-867f-3526-9b62-af61ecfdf4d0 | -15.07756 | -48.01754 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82ab489c-c96f-3d3d-b6ec-7f0be2149067 | -11.4265 | -50.74459 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c18e16e7-0360-36ad-a76a-120ac4bc0be6 | -12.93273 | -54.74596 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ee095f4-aba1-39e7-82e3-aa8ad2520fe9 | -11.77332 | -50.55147 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a7440b0-c3da-3e5c-ace6-9cf6d49c6c36 | -10.15858 | -64.73356 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 78e209d9-bb52-31d1-beb3-bd21b161a8ef | -11.10388 | -51.44473 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1fbdca9c-b87f-311a-abe2-79185be8920a | -10.09219 | -59.16586 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0deed713-9d2b-3740-a6ba-b6feb87be51f | -14.43795 | -47.31423 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a782fa2-81f5-3922-993f-22081bd015c2 | -15.81864 | -52.21349 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e546c1d7-1f1a-3d35-aa53-a3aa7228b865 | -15.70875 | -50.57787 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 671a7dc8-5e80-3935-a319-b480229a07a1 | -14.43988 | -47.34258 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dbbfbd5-b16c-3400-9a5c-e39191583b31 | -11.47418 | -43.61213 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 550519b5-8d23-3f16-9760-ff4aa121edcf | -12.9559 | -47.98731 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5a246c0-1fb0-3e88-a70d-125f4a0a7fdb | -12.93641 | -47.99421 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cca9a916-8b6f-3983-a6f8-7a3684d4eaa9 | -10.14777 | -64.7316 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 029f1900-1c4f-35ba-9d3b-92811b582483 | -13.9079 | -48.28945 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e7933bfb-fae9-3c22-a185-66f45b459ff9 | -11.43119 | -43.53777 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe29649e-3af8-31e6-8418-c3584b62e465 | -12.99852 | -54.78165 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17ff42e0-5512-3973-a242-82812705651e | -10.88603 | -59.23171 | 2025-09-13 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 452b12c2-29fe-3c81-a88c-585eb4237805 | -12.91609 | -54.76542 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee390e67-5a54-3556-bbac-e178bc87454b | -15.2315 | -53.75562 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e184abb-bbec-3a9d-96b5-0af98cbcdba3 | -10.33596 | -58.02383 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d5d8b71-f2a1-33b3-b157-62244c9b843d | -11.37998 | -63.36369 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36239964-ad70-303c-8955-edddc106b2a0 | -11.27598 | -51.13047 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eff3be3e-54bd-319d-9626-738451ac7a24 | -12.08704 | -44.883 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f3e11a4-e600-3903-923f-425be6d6d625 | -14.42609 | -47.32598 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccf7cf06-1a35-3dc3-894c-9aa4a65e6c8d | -11.44473 | -43.56153 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b79132f7-f44a-3ced-98cc-9e4909bee8f1 | -10.78275 | -50.53534 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 411cf5f9-a48d-3ce3-8db3-d371fdd0a5dc | -11.38579 | -63.35918 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0d7cddf-95fe-3f54-af9f-128f52e24a7d | -11.09947 | -51.44878 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8479441f-6c75-3c35-8c57-57059aeb778c | -11.86644 | -50.57151 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2fed2df4-d2c7-3c1f-b4a6-db291573fbc8 | -11.17759 | -51.41323 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f14f894f-5f31-3b73-b1d9-e0dfdde470f9 | -13.91967 | -48.27328 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |


[Clique aqui para ver as próximas entradas](README87.md)
