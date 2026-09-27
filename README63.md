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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c901cf1d-990a-3802-ab55-6f14ca3c80b4 | -9.99 | -50.13 | 2026-09-27 15:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12849066-472b-38dd-8a36-6711acf501a0 | -11.05 | -54.07 | 2026-09-27 15:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8b5eecc-aa9c-336b-9d07-c0d234ec3c51 | -11.02 | -54.06 | 2026-09-27 15:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0c73c8-ab9a-37f4-bb19-a881cb025a74 | -8.24 | -45.43 | 2026-09-27 15:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea328132-3f92-3bd3-ad93-dca29af20252 | -8.24 | -45.39 | 2026-09-27 15:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06332127-e1c8-3f6e-a709-dbc7ac629325 | -6.7 | -45.6 | 2026-09-27 15:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccfe7fe4-416e-3d8b-b704-bc7020fbb6c5 | 0.3219 | -51.4389 | 2026-09-27 15:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5d3e6971-5573-3697-9bc7-ccb4ae351a68 | -12.9457 | -51.0695 | 2026-09-27 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 421eb20d-7833-3a32-99af-89354ba04890 | -11.2088 | -51.3958 | 2026-09-27 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 17dc8f9a-ecdc-3af9-8915-713e5eee9d41 | -11.9971 | -50.7135 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 271489e6-c22a-3273-9c45-fc19e8b08b34 | -10.3016 | -49.9587 | 2026-09-27 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 793e7d22-389f-3c9e-b534-57fd0efd8f0b | -11.6764 | -50.5367 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e73028cb-0fb1-38aa-829f-add8d32514c1 | -12.205 | -50.8173 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a635d81f-a81c-3639-9ac8-f0c45b8fba7e | -11.3048 | -51.3011 | 2026-09-27 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 20c7d227-0bd0-3b40-98e0-1b324548ed79 | -12.1751 | -50.2851 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3ad8396b-59a9-3904-8e4e-6014303ee160 | -12.2633 | -50.7463 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 92e65a06-b491-32c2-afb5-14845593eb65 | -12.1115 | -50.7001 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ca0ec525-1c28-3d2c-bd76-278f29dfd780 | 1.6565 | -55.9621 | 2026-09-27 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| a4dce0ab-6c19-3b5a-b9c5-0aa0613a0f35 | -12.1306 | -50.6978 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 81551ec3-71f5-301e-a1ec-02abb111c8d1 | -11.3845 | -63.4178 | 2026-09-27 15:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6ebfb806-8b28-3354-8c1d-93db9b63051c | -2.6629 | -56.4575 | 2026-09-27 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c2de0eaa-0a94-39d9-9146-f586c9ac4b84 | -11.2281 | -51.3727 | 2026-09-27 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 664eb32b-05ad-37b4-a228-19cb99629149 | -11.9622 | -50.5036 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| c90a0bd3-9074-37d2-b437-34b4f1a50715 | -11.6186 | -50.5861 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0a7a0146-cdfd-3cc9-83b9-5bcff3b344f1 | -11.0583 | -51.327 | 2026-09-27 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 7b7a9332-6d31-3973-81e2-a2384c556357 | -11.1714 | -50.0151 | 2026-09-27 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 13c2318d-a930-3f73-bdcc-fec2c41831f2 | -2.9525 | -57.72 | 2026-09-27 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b9166701-7cb8-30b8-bbd9-f203fa2fc188 | -11.2859 | -51.3031 | 2026-09-27 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 72ddc23c-d09f-3f8b-b1c6-70a8158a797b | -12.2693 | -50.3597 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7699eccb-a394-3229-b99e-3b3abdb85b4d | -12.1188 | -50.2274 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ab2e4ab8-23c4-35e4-bd36-c209d677048b | -11.9783 | -50.6943 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d8dc4ce8-949f-3794-8bc2-286d90356ecc | 1.6017 | -55.9234 | 2026-09-27 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e591d2fc-4863-352b-995e-85859f76341f | 1.6566 | -55.9227 | 2026-09-27 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 510cc3b0-0a65-3e8a-b072-3d8188bbd998 | -3.0788 | -58.4141 | 2026-09-27 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e87adae4-79e9-3cda-98f4-9b831f55af62 | -12.3015 | -50.7417 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c941890e-7814-3eb9-9108-e770300aea13 | -11.8281 | -50.562 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| e3126e0f-2c06-3c0a-aa69-a46d87b4d4e2 | -3.4511 | -56.4796 | 2026-09-27 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 16a2c33d-76d5-371a-b8c8-76ae2e432b88 | -11.5993 | -50.6096 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 57d80389-576f-3f2e-bf39-64b4ce656997 | -11.2091 | -51.3746 | 2026-09-27 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 55808c00-a9b2-3ed7-bf4d-d8365453b88d | -17.0529 | -56.59 | 2026-09-27 15:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 0490a0d6-710e-33d5-8da4-4399e1a4ed9c | -10.8851 | -50.1539 | 2026-09-27 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ac937608-d9ee-3b8d-bde1-7ba94cf5f040 | -10.0531 | -50.1978 | 2026-09-27 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 470b410a-c4a0-39e6-9cb8-f4eee0f1ca05 | -10.4237 | -53.7809 | 2026-09-27 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| afe18902-875e-3632-a45e-812d090dc994 | -12.054 | -50.7282 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| c8f3830f-e505-3859-9730-b8a74e46cd72 | -11.0991 | -54.0285 | 2026-09-27 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 3bab8a71-5a78-3b60-8c14-4c4488e2f35b | -13.4325 | -57.061 | 2026-09-27 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7b94e030-a409-3aaf-86d4-b2ab751bd93b | -12.1106 | -50.7643 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| fa3a95cb-98b2-35e1-bedc-6f41eeb3f717 | -12.0352 | -50.709 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3874923d-35e7-31c1-aeac-8e2ebc7e3157 | -12.9649 | -51.0671 | 2026-09-27 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 06da0dfc-9f6f-39dc-bc8e-139224d37961 | -10.6889 | -50.6658 | 2026-09-27 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5e96edbf-d7ff-3a25-9600-f720011166ec | -13.3439 | -51.3187 | 2026-09-27 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6992c073-97ca-31ca-be2a-0d10e45cdcbc | -11.1524 | -50.0172 | 2026-09-27 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 00a6b1a9-2241-3960-a1a3-e37d8eb224d1 | -12.7868 | -54.0275 | 2026-09-27 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ddf19d37-4c4e-31a2-91a9-4da9d3860f38 | -12.1372 | -50.2682 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 504579ad-3c72-37a6-af65-3153501007e3 | -8.5982 | -54.6341 | 2026-09-27 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 2b27e7fb-fc31-312e-97c8-a727d2fb6edf | -12.1754 | -50.2635 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 79d21c53-2891-3b0b-ba36-9727293bf464 | -11.2118 | -54.0797 | 2026-09-27 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4ea5e358-50f3-35c3-a981-d39142e6058c | -11.9619 | -50.5251 | 2026-09-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 5f4824c4-a63f-3c84-bc5a-74fc3eefa603 | -12.1099 | -50.8071 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 2b5c5061-16b0-3182-aa01-086244a62892 | -12.1872 | -50.7339 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e97a8151-f3da-3809-aaa6-8f8c5a98c197 | -12.8059 | -54.0255 | 2026-09-27 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d7ab9986-b1d7-33cb-8068-c4c7bb67792d | -12.2623 | -50.8105 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 1961ab93-243f-3ef6-b382-1f2ec805f2ef | -12.1681 | -50.7362 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 19da712b-f546-3d8d-b59f-2a7e3aa70fce | -8.5984 | -54.6139 | 2026-09-27 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| af45918f-f3fb-38c2-9fa4-975f9f29a1ec | -12.0921 | -50.7237 | 2026-09-27 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ae557879-e8bd-3144-ba84-886f4c816584 | -2.7151 | -57.5303 | 2026-09-27 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8aaa5d7a-1b06-34d9-8fe3-7096e42ab683 | -9.1528 | -49.9425 | 2026-09-27 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a6a52d36-74aa-3d18-a3e5-281419093725 | -11.171 | -50.0366 | 2026-09-27 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 762517ed-3175-3913-bef9-4a7a3d9a822a | -11.9622 | -50.5036 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 87ffdc28-f3bf-3672-9993-28172a2e6035 | -2.6812 | -56.4572 | 2026-09-27 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 495dda2f-f3ca-37b2-bb85-f6bea2774060 | -3.4511 | -56.4796 | 2026-09-27 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 5681158c-ae14-32c0-9549-1d2ce285665b | -11.9783 | -50.6943 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7fe8d512-1497-3e62-9d34-2c48a45cdd07 | -0.8215 | -48.6609 | 2026-09-27 15:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 423bbec1-664c-384c-bc36-58ac3938b2bc | -1.3008 | -49.0613 | 2026-09-27 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d5ce2f4f-0b27-3e70-9403-1c4c9b03e6c5 | -12.1115 | -50.7001 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 26d1cbf7-86e3-37b7-9884-61f9f6873385 | -12.0349 | -50.7304 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 16efb79d-e059-390b-857b-fae1128c06a4 | 0.5246 | -50.795 | 2026-09-27 15:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a2ead075-1d6a-3612-aa88-4b72e1f5397e | -11.0583 | -51.327 | 2026-09-27 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 20ae11ce-2c53-3c90-987c-d7b6be57604c | 1.6382 | -56.0017 | 2026-09-27 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f282bae8-e079-37d9-af29-5c5b1a5bb563 | -11.9431 | -50.5058 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8d5b92fa-e597-3eab-9e8a-ddec6f7e170c | -12.1932 | -50.3474 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b822268d-121f-345a-a6f9-7e1731356298 | -11.2859 | -51.3031 | 2026-09-27 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 972e21a3-5baa-3865-8377-481dd0ee72f5 | -12.2502 | -50.362 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 03a118d1-0b13-3903-bfa4-ae9a95066e0c | -10.4237 | -53.7809 | 2026-09-27 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 578473c1-fc10-3b73-8083-e331c6434ece | -12.6608 | -50.9549 | 2026-09-27 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5233d7ca-e82e-3728-b1a1-103bbdd7f6d6 | -11.9615 | -50.5465 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 88222185-7932-3faa-bf8d-30e2eec8f589 | -11.9619 | -50.5251 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 4300623f-af8d-3802-be5b-dd58ecbb0bc0 | -10.3363 | -50.1905 | 2026-09-27 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5a74ab3d-c33a-3747-b037-834652853c0c | -2.7151 | -57.5303 | 2026-09-27 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9a7adb97-b73e-3a13-96d8-a685ff26f617 | -9.7874 | -44.8289 | 2026-09-27 15:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 4cba7359-2df0-39ce-a975-1fb4b7d069bb | -12.9649 | -51.0671 | 2026-09-27 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 910e14de-9749-3322-91eb-b38d629883ec | -11.5993 | -50.6096 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| a3fdd3d9-4ca5-3922-958c-661a869634de | -12.0468 | -49.956 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| e88c8c72-873e-3666-8bd3-8e00baadbb17 | -12.2053 | -50.7959 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 1a349ca1-2cde-3005-8d79-9b88f85f28e6 | -12.7868 | -54.0275 | 2026-09-27 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0a9706fe-4a87-386a-9061-78c177c8f50c | -12.1109 | -50.7429 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 07bdc420-4d61-37a4-a1be-fc0926b28ba5 | 1.6382 | -55.9624 | 2026-09-27 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 4898d141-5f1d-32b7-b081-045a54333d68 | -11.2856 | -51.3243 | 2026-09-27 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 6f85c343-5609-3863-9232-75132bb0f954 | -12.0915 | -50.7665 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| b03ac798-471e-3224-b68b-1e623ab6d924 | -11.3845 | -63.4178 | 2026-09-27 15:30:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |


[Clique aqui para ver as próximas entradas](README64.md)
