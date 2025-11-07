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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4219af5c-d3b5-31d0-850a-9a21b90065d0 | -3.77468 | -43.98527 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd09e373-31b1-311f-8ea8-c42a835de7ae | -4.29109 | -45.88641 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 9dc636af-2749-3641-b023-6dc201166904 | -3.17272 | -45.6602 | 2025-11-07 04:23:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cf8ab82-6031-3344-a333-8e0e5ceb81bc | -2.73898 | -47.14558 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a909824-ff46-3d16-ae0b-a200194c7813 | -3.12123 | -50.14082 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d0daeeed-6862-359e-a29c-b67c0298bb6a | -4.29385 | -45.89037 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 47f591fa-dde6-35e7-9185-5259364d8a20 | -4.46335 | -43.22591 | 2025-11-07 04:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e3048a5-e1ba-36d9-8276-bac827e9adcf | -5.0002 | -41.04141 | 2025-11-07 04:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3f6226d4-886f-3430-ba0f-66f50d3b8fb3 | -2.98734 | -52.82185 | 2025-11-07 04:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22a1b86d-4730-3b68-9f77-8f5058e15358 | -3.27661 | -46.47247 | 2025-11-07 04:23:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84a3a976-4cd9-3a71-8990-047b5e40a51a | -2.55254 | -48.3917 | 2025-11-07 04:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fffdf88-1dd6-3bfa-b5d7-b48375d96ba9 | -2.44691 | -44.14412 | 2025-11-07 04:23:00 | NOAA-21 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d31a9ba6-c93d-39cc-810e-679cdd4d1c60 | -4.10082 | -43.58226 | 2025-11-07 04:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5056a96-2ded-36f7-96e9-be5e50e29501 | -3.0026 | -40.23229 | 2025-11-07 04:23:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a61cb8f-dab1-3a80-8cce-ac15f8b145b5 | -4.86226 | -40.64145 | 2025-11-07 04:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fbff2118-5044-3e18-b3e1-bc7b3ac9837d | -3.35251 | -40.42218 | 2025-11-07 04:23:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 081f3013-2d0a-31a4-b605-009d69cc2e51 | -3.4953 | -41.2261 | 2025-11-07 04:23:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 338a39f8-0bc6-38bf-b73a-91afee708dc9 | -3.52587 | -47.54483 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67d06a12-5214-38ff-80f1-3b49da71cd7a | -3.43079 | -45.36004 | 2025-11-07 04:23:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 03f419e4-1df4-3a19-b87a-d8a1d341cb06 | -4.46683 | -43.22645 | 2025-11-07 04:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2fc755a-20b4-3d1e-9178-3c44ad87f74d | -2.32685 | -45.64978 | 2025-11-07 04:23:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bebac940-3ae4-3edc-af40-92d3ff49a12d | -4.3373 | -45.72117 | 2025-11-07 04:23:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78703152-619d-3690-9a1b-812cd7636af6 | -3.28263 | -49.46698 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b72aa99e-1b4f-341a-9f76-5d49ceb19fc1 | -4.74273 | -42.93384 | 2025-11-07 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cefade8f-c8dd-3cde-9265-7f7ca259c5cd | -4.74395 | -42.92579 | 2025-11-07 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 77548639-9887-32e1-a4a3-2355bf3e1de6 | -1.152 | -47.71511 | 2025-11-07 04:23:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cf7d91d-6e7a-358b-9f1d-2d3c6f21b8cf | -3.42564 | -50.09776 | 2025-11-07 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf6869e1-7e3f-396f-a4a3-0cc44cf80582 | -3.14878 | -49.21119 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edc11616-618a-3230-8d9f-4685c1bf2f0b | -2.32408 | -45.64583 | 2025-11-07 04:23:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b950b4fe-4361-3c81-9e99-631e7b7f928a | -3.37732 | -44.17604 | 2025-11-07 04:23:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57a4fe34-2d44-3731-8c08-442447b48206 | -4.28947 | -45.89674 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63666eb4-d561-3c93-a084-9c2cc26f6b3a | -2.66895 | -49.44471 | 2025-11-07 04:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e91e273-ccc5-3d1b-ba97-85d5281ae8cb | -1.06699 | -48.09934 | 2025-11-07 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52a2f683-cd45-39d3-9311-8cf7ad81b781 | -4.74041 | -42.92525 | 2025-11-07 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9a653e91-a284-3c75-9b4f-5e0b58ea3c4c | -3.24282 | -41.75913 | 2025-11-07 04:23:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 884feee9-3cb0-3bab-9f5e-728da9cbd8e6 | -2.49353 | -48.15207 | 2025-11-07 04:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83f2308e-fa10-3743-857d-1809dd755500 | -3.33697 | -50.20111 | 2025-11-07 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9282b43-c88c-35bb-a4f5-63b3b50cf17f | -3.76795 | -44.00631 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 146521b9-e4fe-3237-b437-5e637a6960b9 | -2.85679 | -49.8829 | 2025-11-07 04:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06c42217-3eba-3039-b531-c52a40215fce | -5.00048 | -41.04414 | 2025-11-07 04:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 424d80be-fb07-3d74-9f43-0e0701e37838 | -3.38067 | -44.17656 | 2025-11-07 04:23:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02b4d6c8-b7e7-3065-94bc-545fdde9d674 | -3.8443 | -47.41922 | 2025-11-07 04:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0151d16c-1f07-311e-b9be-e104c7c57bfc | -4.29001 | -45.8933 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d819cbe-0f3d-3e3f-888d-fa428456096d | -3.64149 | -45.64243 | 2025-11-07 04:23:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8fd0e31-a3dc-3b5e-ada8-9447dab95c12 | -2.50872 | -48.26285 | 2025-11-07 04:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7699c501-431b-3100-9745-4b3f664f6e92 | -3.54352 | -49.43846 | 2025-11-07 04:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0f39177-bdbd-386d-bf46-1c146662c70a | -3.17263 | -48.61112 | 2025-11-07 04:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cbf0d39-e0e5-315b-813a-c2522d7c2318 | -3.60906 | -43.51621 | 2025-11-07 04:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd7c640d-efd9-3890-af61-f344e7157123 | -4.54273 | -40.15659 | 2025-11-07 04:23:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51473ad0-f4c1-39b9-bcf3-2d14cd197606 | -2.78963 | -50.31524 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7898049e-5496-32cc-9bc0-1be7fcf826ed | -2.31855 | -45.63792 | 2025-11-07 04:23:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b92f7a12-3018-395b-8576-ae5b570b3a66 | -3.28339 | -49.46232 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce70cabc-9194-3cfe-a694-36a8adf73f02 | -2.55321 | -48.38756 | 2025-11-07 04:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2220dcb0-c134-3057-a69f-e409f08c0f04 | -4.52968 | -40.35677 | 2025-11-07 04:23:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2cae80cc-dae6-3f42-a844-b9d4742e30dc | -3.5293 | -47.54537 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 650006a8-3be9-3218-97ed-8932d8efd45e | -2.55158 | -48.38771 | 2025-11-07 04:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ab8624c-1f24-396e-9b63-3fe565caec92 | -4.52201 | -40.35202 | 2025-11-07 04:23:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef26dafe-cd93-3fab-adb6-8aec555802e0 | -2.29051 | -48.49955 | 2025-11-07 04:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b017189-7b42-3821-81d6-479a0e0576c4 | -3.60565 | -43.51569 | 2025-11-07 04:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1423967e-de61-3003-b8c7-75858ad01155 | -4.46624 | -43.23031 | 2025-11-07 04:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67bf25b1-4088-3d0a-847d-e800661e52eb | -3.25427 | -43.2915 | 2025-11-07 04:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba09eee3-e70f-3206-9a59-4ac53239f764 | -3.63819 | -45.64192 | 2025-11-07 04:23:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bbce232-cc73-3d24-9c9e-5295ff4284ef | -3.66859 | -44.79769 | 2025-11-07 04:23:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f54fb53e-a1aa-3fb7-b715-272d1ee8d08d | -2.85679 | -49.88071 | 2025-11-07 04:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a9d586d-d9d3-37ad-86f1-aa8a97a592b3 | -4.10138 | -43.57856 | 2025-11-07 04:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d285dd3-2748-32b5-88ed-934299351132 | -4.29277 | -45.89725 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7df8608-f4c9-31c6-8aa6-8f9d6c8761c7 | -3.53274 | -47.54592 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 62e5fee6-0ae8-3b38-af13-f257940d35a9 | -4.52144 | -40.35578 | 2025-11-07 04:23:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c44a8a9b-5240-39d7-8573-b747a3caf649 | -3.7674 | -44.00989 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c6c6dec3-e93e-36a3-a31d-58320dce14c3 | -3.12437 | -50.14657 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f89ea77-19d3-33e9-8523-36798d87e488 | -4.30045 | -45.8914 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b08764fb-f0aa-378f-bb51-13ad88311584 | -3.56725 | -50.41304 | 2025-11-07 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 525a2559-77b0-3c60-96f8-198fb8f9f349 | -3.60507 | -43.51939 | 2025-11-07 04:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3256406-4f4b-3ff1-83d5-92be353739ea | -3.5964 | -49.44944 | 2025-11-07 04:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aff7eda3-2f52-33cc-a03a-04c067e7a3a4 | -3.45258 | -48.83382 | 2025-11-07 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2361c640-5458-30fa-a20a-6c58d357a44c | -2.78842 | -50.31499 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaa75587-8c8d-3fd7-84fe-c95e5261f838 | -2.94382 | -49.35299 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a206cc29-0b38-3dda-88e5-b7d2341f6e69 | -3.82759 | -45.34863 | 2025-11-07 04:23:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2d063d8-b43e-3215-ac6b-2a1a19c77282 | -3.33777 | -50.1961 | 2025-11-07 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc7f37c6-ef1d-3f4c-85b7-ad96086b3f33 | -2.72689 | -47.39925 | 2025-11-07 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b6de55a-9605-3ac5-8278-294c5a0f2bff | -3.77187 | -43.98117 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40b2e1d2-4239-3f83-8c63-cc5de2b3c83c | -3.4265 | -45.23639 | 2025-11-07 04:23:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40cb1fb1-9e0e-3893-ab7d-cd202c23c441 | -3.4298 | -45.2369 | 2025-11-07 04:23:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a8db587-b439-3efe-94b2-f3ee0e04b755 | -2.61334 | -49.23343 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28c206e9-e76e-3f8a-97ef-df512f3956ae | -3.37826 | -44.1036 | 2025-11-07 04:23:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fef9c44-3768-3b19-8702-35c054d1c02d | -1.14338 | -48.09286 | 2025-11-07 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 257cf360-9a7a-39d1-bd6f-036b9de7bc9e | -2.94082 | -49.10358 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26fb5b3b-b03d-3f32-bf19-e857929bc948 | -2.73093 | -47.39603 | 2025-11-07 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c82769bf-943d-3445-9f9e-cefb1e76157a | -4.43443 | -43.39365 | 2025-11-07 04:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ac5c01-00c4-39eb-8508-492c596dd9a9 | -3.83775 | -44.51769 | 2025-11-07 04:23:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4c105ab-684c-3edd-85c5-04d5d8dca8cc | -2.78904 | -50.31878 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 114e2c1c-5ed4-39a6-bb24-4c0cb0a8451a | -4.25068 | -45.6226 | 2025-11-07 04:23:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d05eaf0b-4ae4-328a-9580-a432983ffaf1 | -3.12041 | -50.14593 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cdfc59c6-398b-372f-ac2e-65a4419702aa | -3.53215 | -47.54966 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9d5c1df-b05d-30a8-81f7-107a65503066 | -3.84489 | -47.41552 | 2025-11-07 04:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e138436a-7795-37ea-8169-2407f1a086b4 | -4.60157 | -43.33648 | 2025-11-07 04:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db81c165-d1bb-3f6a-ba6f-ba5c2767c175 | -3.47861 | -49.59963 | 2025-11-07 04:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57ac478b-2959-3bb1-b205-a069685cc19f | -3.04289 | -45.70692 | 2025-11-07 04:23:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28447ebf-5b2c-350e-ae11-f0bb958e9b30 | -3.04935 | -49.51592 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66b618af-d6d1-3b1c-8be4-6d93d6a4a51e | -2.62025 | -46.85465 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README7.md)
