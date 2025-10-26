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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 673a8a04-5a89-3e23-a2cf-fb797b25cf37 | -8.72237 | -48.00956 | 2025-10-26 04:02:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af3871cf-655e-3c9f-a023-47c186b8b24c | -13.53512 | -49.55205 | 2025-10-26 04:02:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e17b9483-42a9-3e94-8bdd-04165eb901c2 | -12.91239 | -43.70208 | 2025-10-26 04:02:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6806ec21-38e0-3f53-9c7c-abc55e0d8dde | -14.02979 | -44.02996 | 2025-10-26 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a7555a7-fcff-3581-b4f1-971faa0cc8a3 | -11.32409 | -53.93718 | 2025-10-26 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e965e431-68ad-3ae3-8823-d03021b209f1 | -11.47957 | -43.24223 | 2025-10-26 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 943743be-5521-3b55-919e-864da92deb44 | -11.02488 | -47.86617 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce6755a8-4ecf-39c1-add6-52bb310f633f | -9.68514 | -47.44359 | 2025-10-26 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1663311b-c990-3f0b-8887-02bae15cbc17 | -13.532 | -43.01247 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a13f1ed-3390-3efa-9e3b-f3336892a73c | -10.94916 | -48.07367 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f9ea19fb-84d5-3f1a-aa7d-0f9c116071a0 | -11.14067 | -49.94547 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 216038d9-f600-34ba-8b58-f4ac90da2145 | -13.86497 | -43.31748 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 708bcd76-b106-34cb-8bfc-3d2c3b02141d | -11.43113 | -46.07179 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0e6e125-fcb0-3244-8c76-e373b6c3b4e8 | -13.91506 | -48.37817 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa8db0dd-2b06-3c2c-a408-d796f52676b9 | -11.48239 | -43.24668 | 2025-10-26 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e68a12f-3879-3148-bbb8-fcb55e6267e8 | -13.53598 | -43.00936 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f07af5fb-c330-3eb8-99d4-c6dc84dd5d99 | -11.02044 | -47.8647 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9e884aa-2471-3cef-ba30-5e3b07e6ccad | -15.11701 | -43.25807 | 2025-10-26 04:02:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fcf9fbc3-db67-31d3-b705-138ed89fe4f7 | -15.48001 | -43.1302 | 2025-10-26 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 089dcae4-bea1-3ff7-868c-071be478797c | -13.31424 | -46.77908 | 2025-10-26 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b553f30-924d-3faf-ac1f-2b9c7de8a648 | -10.57298 | -47.9919 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11c47070-1297-3ac9-b554-4c0d92c95bf7 | -8.71759 | -48.00862 | 2025-10-26 04:02:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 001307c7-8697-33a8-883b-b91df2b335ab | -15.97395 | -42.98162 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b52800f-2837-3dd9-8212-a2d9c0532efe | -10.08579 | -43.99166 | 2025-10-26 04:02:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5c2f089-995d-3c09-9335-d5a94565b351 | -16.61566 | -44.57409 | 2025-10-26 04:02:00 | NOAA-20 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81ec10b1-ea33-3dca-8505-e9b4236d3f16 | -10.4172 | -44.49718 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 683c746f-b96f-35aa-ab22-2153dbe0365c | -10.91516 | -48.03078 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32cb0507-d59b-32a2-bc11-669a58f01cb7 | -11.14129 | -49.94223 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e2ec575-428c-3f6c-bf59-da57b4019397 | -13.8502 | -44.36048 | 2025-10-26 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77720c36-aedf-383b-a533-24fb9444452c | -13.89026 | -48.41233 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93af2df2-ddfc-3e8a-bd1c-1af8a07298f3 | -10.41767 | -48.01157 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5963544-af32-3700-bf22-f6a59197aa86 | -12.13492 | -47.0063 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ec4781a-4b88-322c-82ae-38c0105e27ab | -13.00691 | -43.85196 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb36a890-e441-3f70-861d-23bb62816fdf | -12.30656 | -47.45786 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 370c7b4a-4f44-3017-87de-463d60423ed5 | -13.53659 | -43.00564 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 54.1 |
| e0a41aad-d2a2-393b-b686-8f99d6ced80f | -15.29803 | -42.93379 | 2025-10-26 04:02:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 33557573-bf53-3b0b-87ec-37bb1c69d0ad | -10.61102 | -46.60395 | 2025-10-26 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da0b40c2-94b6-377d-80db-8996cac83ea5 | -12.3049 | -47.46718 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11bc5f58-4a15-33f4-afe6-bf0a49b3d0ab | -15.11761 | -43.25436 | 2025-10-26 04:02:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 574ca4e2-963a-30c5-b214-5381b7047880 | -13.32446 | -47.93918 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f0f506a-78d4-347d-b653-9670349f3cee | -10.60908 | -48.00402 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e69f2cbb-c440-3648-8530-99f0e1280bb4 | -10.87549 | -50.14204 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8654aacb-c93e-3fc3-83fd-b09600cf36fd | -11.04286 | -47.8709 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc520496-65cf-3ff1-ab81-60d37ad810ec | -9.26895 | -45.59331 | 2025-10-26 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72d84682-006c-3375-bf19-855e5de01f35 | -9.3352 | -49.26805 | 2025-10-26 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d686bffd-76c9-3af7-a219-c6f3a4a69be6 | -12.32005 | -47.48276 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c25cd16-4195-3a60-911c-db54fe325e93 | -12.17218 | -47.01733 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 599ff322-e15a-369c-9f0a-4bb56e698e2c | -13.53779 | -42.9982 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 7b341b1d-c2ff-30f6-8bf5-89cf8a636fdb | -10.00651 | -47.11152 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 501f7dbb-b8fe-3025-a769-ea87bba53eb4 | -10.86464 | -47.94195 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fc505af-bad2-3b7b-99f8-e760b4eecf90 | -14.43398 | -49.96106 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 40f57550-5be8-3d64-805c-528868658e0c | -11.32777 | -53.93578 | 2025-10-26 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f736e08d-c917-3b1d-9382-c87007d44dbf | -15.04678 | -46.20714 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6914c0fc-80e6-3819-b96f-1a9639177f20 | -13.87404 | -48.47525 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd473ba2-928f-3909-a2f7-ff8cabeb066f | -15.29781 | -50.76099 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 935b75dc-c4c7-3cdf-b01f-55f8058582f9 | -15.8274 | -49.0787 | 2025-10-26 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0aac0ab-6db0-369d-a273-7794aa130166 | -12.02008 | -43.30748 | 2025-10-26 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcbd9fa2-539f-396a-b633-062b9b02ca43 | -11.89154 | -44.80659 | 2025-10-26 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afe87f9d-79b4-3ceb-9679-cb4bf65ca30a | -14.76803 | -46.61738 | 2025-10-26 04:02:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2af171b0-95cc-34b6-9ac5-28f81bfed808 | -10.82813 | -47.62396 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2294a9ae-8a4f-3dda-9274-7e49f5eaa28c | -11.43246 | -44.67799 | 2025-10-26 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71f76993-525a-3d99-b4c7-7ab9e9ee36ed | -14.9347 | -41.66022 | 2025-10-26 04:02:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66b65d19-f6cc-37b6-a868-2ad08ae0635f | -12.13412 | -47.01072 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4bf4cf6-1f9e-3a4e-928b-0349ce2e8cd1 | -10.81898 | -47.07074 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5365f1a-e91d-3e13-ba98-ffbad9446610 | -15.26782 | -43.18069 | 2025-10-26 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 87eac9ff-2c26-3cd3-8836-fc8a45114714 | -10.42462 | -44.49852 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 86511502-de67-3f31-ac97-d60f7c1b9e0c | -15.29743 | -42.93743 | 2025-10-26 04:02:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 554440bf-0197-3098-b853-840c080ef6a8 | -14.77863 | -44.97917 | 2025-10-26 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dc0762f-80d3-34ae-9571-33950db790ef | -13.80708 | -43.051 | 2025-10-26 04:02:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e77ab9ed-e528-3dc0-b672-29169facdf75 | -13.88115 | -48.46975 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1622d407-83b6-33fd-bfa5-47bdd07bb36c | -10.88159 | -48.03184 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4adb7d9e-abae-38ed-a0f8-992a21dab588 | -10.56835 | -47.99102 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7b6060b-825c-3f4c-9089-a5a3f9a2494a | -10.87248 | -50.13977 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6b1a2d7-54ce-3c2f-b05b-23b42aaa0052 | -11.95089 | -46.8441 | 2025-10-26 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50fe3433-c090-39be-85c7-d2413a5d83c3 | -17.16323 | -43.34355 | 2025-10-26 04:02:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1352f363-527a-3672-9d03-dd8459a78d33 | -13.32099 | -46.57545 | 2025-10-26 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 183267a0-f905-33d7-8561-5f6d65f473a3 | -12.53668 | -47.81277 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f32f6a5-6afe-3e51-9908-dcae5655c0f0 | -15.83616 | -49.08522 | 2025-10-26 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31dc42dc-d727-3b19-bbd3-e743da30df94 | -15.08164 | -41.17544 | 2025-10-26 04:02:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9df55046-4d7c-3920-874b-b9308c4a0496 | -11.16926 | -47.79659 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79f7973f-d208-399d-b039-57c0b1bc6f65 | -13.53128 | -49.54568 | 2025-10-26 04:02:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2596cd29-039d-35f7-8c02-1d35bfaf8d92 | -13.29437 | -47.50305 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ce16df-00fc-346b-adaf-94925643241a | -15.33152 | -42.8126 | 2025-10-26 04:02:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1c6a6d0-165a-326c-8c88-bcff06d316bf | -16.13968 | -45.10559 | 2025-10-26 04:02:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2afb8b2e-44ad-3bd5-81a4-6add105135c7 | -11.04659 | -47.87637 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce68232f-fc6d-3f72-b119-5b9349da97d8 | -12.00443 | -46.78548 | 2025-10-26 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba1721c0-9ee8-3bf8-97d5-417e8daa4573 | -14.65335 | -50.1908 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32e87f3f-057e-3822-87c0-bc8081096b5c | -13.73547 | -43.14187 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d344b1be-4586-39dc-927c-3e9a3e6e1539 | -12.14113 | -47.02026 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a225e6cc-1721-3300-93c6-85cbe9bc6c1e | -10.40771 | -45.31039 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05c45dd4-5ba9-30fe-93a6-fb86445c82d8 | -9.0879 | -49.64431 | 2025-10-26 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 301ff452-2e67-30a4-8ca1-27c879c27d7b | -11.08953 | -45.42213 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45560ae1-53e9-36a3-ba8e-d1bf6632570c | -12.664 | -43.21336 | 2025-10-26 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a1f136-cd76-3a28-9694-8d8156ceb317 | -15.50635 | -40.75529 | 2025-10-26 04:02:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8ebb11d7-2b38-377b-b281-aaeb57052e45 | -13.53624 | -49.54614 | 2025-10-26 04:02:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47808b3a-4f37-3f92-a4b6-4e98e1c0e54f | -9.67003 | -45.45311 | 2025-10-26 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db0a2b8f-5b2f-3723-814f-169ee091610b | -14.16826 | -47.31196 | 2025-10-26 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec6d6a94-a260-3a35-8623-b5da09977463 | -16.31402 | -50.0526 | 2025-10-26 04:04:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc9e3a13-28c9-3ac2-b13f-761dc4d06831 | -17.43503 | -46.88765 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bcf5261-ad92-3cc6-8664-c988adaffc8e | -18.65426 | -52.09429 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
