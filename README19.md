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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe24e06a-d22d-3afe-9a2f-dff7b6de06ed | -7.35009 | -42.4446 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a388df20-cb86-3a2e-a2ec-af657ccff85f | -6.0786 | -42.15091 | 2025-10-26 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 86b28eea-a72a-3c8c-9605-ef539b878e86 | -6.55401 | -43.77906 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2ff2e7a5-a46e-3b15-bdf3-8930fb4dbe5f | -8.299 | -42.30964 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 663bcd62-b8ed-3799-b2f0-cb4e8bba0859 | -3.75996 | -47.57175 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1437c504-f581-311d-b0b0-490a69af0fe4 | -4.8978 | -43.2507 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1b5da4ae-12e2-3c96-8b5b-01e343e10142 | -6.15809 | -43.10002 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d276ed7-b451-38c5-a0ec-9b4af7ce607e | -6.15976 | -43.13523 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2845b6c8-64ca-350b-bbc2-58d7593fc036 | -6.57706 | -41.45718 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 402ed222-53ed-3ab4-82e3-9a41e645c03f | -6.80284 | -45.41239 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d480b682-6978-3620-bc70-3e995130afbd | -4.0023 | -41.02151 | 2025-10-26 04:00:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97fe3cfb-97d0-34f7-9f15-7c22433cdc76 | -8.07253 | -42.06178 | 2025-10-26 04:00:00 | NOAA-20 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b3f5129-4bf0-38c2-90da-90acc2e59b2c | -6.30567 | -42.95397 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2193519-f2eb-34aa-83b2-93b35d4cb460 | -8.32611 | -49.31604 | 2025-10-26 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd425b2-518e-3d50-a415-62cf23993dcc | -8.1269 | -45.47863 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d7d1424-cc09-30c9-bf36-a831d0ca0a33 | -3.60907 | -42.87716 | 2025-10-26 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43f81ce1-e06f-3040-bc96-58ff24fd8fc3 | -6.43364 | -42.32544 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 75544994-a373-36c4-aaa9-97e169e0e54b | -6.1775 | -49.87146 | 2025-10-26 04:00:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afbc476e-1f7d-3c09-aeb2-3a1f9776d3c6 | -6.03123 | -38.87717 | 2025-10-26 04:00:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc600258-d011-3147-8fc4-aeadb41f8f30 | -6.30786 | -42.8062 | 2025-10-26 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a44bc94d-e6d1-3a27-8342-8b5f1846d6f3 | -6.38571 | -45.77782 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1a5e444-8e0c-3047-a60e-e8c44f8780c3 | -6.71395 | -42.04614 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b957aa86-fc64-307c-8b80-c4b555a715cd | -8.65567 | -45.29398 | 2025-10-26 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71d205af-c5e3-3e18-9085-79d4acf18dbe | -5.52796 | -41.72118 | 2025-10-26 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4af95330-46c2-3562-85fe-ace631b38936 | -4.89479 | -43.24562 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8234a609-62de-3a7f-8eba-7ae1c548ec60 | -8.30244 | -42.3102 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ebb9a694-855c-3776-b16a-4a8c524587f0 | -5.88971 | -49.65692 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a29ac67-2515-3ccf-a060-a777a2d7b126 | -4.30887 | -48.06737 | 2025-10-26 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7089280d-df41-340a-a18e-55a711588acb | -4.83263 | -50.93314 | 2025-10-26 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4d77c4d-9d5a-3dff-a2ef-d0e3ca7bd2c0 | -3.72212 | -47.39497 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 650e5d6c-2014-3614-b5ec-7e66482a4645 | -8.32145 | -46.81522 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09a1a306-fbeb-3e03-9e17-6236905e8f10 | -4.90369 | -43.23788 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e33b3c84-2aea-3a01-bb71-c0bb8a1851a6 | -6.47907 | -44.13989 | 2025-10-26 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5e83022f-9f05-30e1-b0f1-28f8ec7ee116 | -4.70786 | -46.42419 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d989459-194e-3ede-bbec-4738e2d2fd3d | -2.97105 | -49.12216 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5b286c6-bb39-39e0-9a9d-6ff385cbf5b6 | -6.47069 | -47.5551 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d759045a-8d92-3072-8caf-fe522a5deb81 | -5.88024 | -43.93839 | 2025-10-26 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab7b5f77-baf9-3f4a-a1fe-75442f4d12ab | -7.85334 | -46.41591 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b6f57bd-d8aa-3b2b-8f64-254446f5344a | -3.09867 | -49.4563 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d044cc11-1d6e-3723-8734-10d35d7b0ed3 | -5.11637 | -40.34675 | 2025-10-26 04:00:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc49ce7c-155f-3953-a474-912259073a34 | -6.38973 | -42.16785 | 2025-10-26 04:00:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 475c9ef0-bc85-3ef8-9af9-6241ddb39c60 | -3.27261 | -44.657 | 2025-10-26 04:00:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa4750e-ddc1-3cd2-ac7c-943115457df1 | -4.02013 | -46.0039 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d51c3b64-0cc2-36e3-8408-05c67a421ce6 | -7.34661 | -42.44402 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5af677b-5d21-3674-aaf1-5c7b06ff5ea2 | -9.20865 | -44.54805 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08187c9c-ea51-3f92-a810-15c55aa4bb55 | -5.74661 | -42.80086 | 2025-10-26 04:00:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 815ca5d6-c2cd-3585-b185-e308747d7724 | -6.25336 | -41.81169 | 2025-10-26 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eaa9eee7-5df4-36c9-975b-47bb0c61ff0c | -6.21796 | -42.53808 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ccb6295a-ffef-33c6-8e82-c03c15bd49ce | -6.44701 | -42.33153 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 35e6e858-d0d6-36fe-bb50-3760d2adc141 | -5.83249 | -42.93812 | 2025-10-26 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6e88b134-71bb-3e31-9f0a-add8f209af13 | -5.89291 | -41.30856 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 214513db-7c4e-3a08-9ea3-80ab64098892 | -5.23274 | -48.53003 | 2025-10-26 04:00:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84eb6f56-896e-339d-b9d9-e67ac26d3b15 | -6.54692 | -41.5799 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61dfcff3-bbba-3960-9cbd-5214973bfa79 | -6.16901 | -41.55434 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25709c08-c9e9-3b84-ab51-2365a4b74ed6 | -5.10572 | -43.18975 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0135ec5c-d8a3-3abd-8958-6e5df21f0735 | -6.70422 | -42.04066 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cd240961-4a73-37e9-b847-0259e277bd8a | -5.82844 | -40.82696 | 2025-10-26 04:00:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40c60e6a-6ea3-34b7-8fdb-620d2e5d2f72 | -6.43261 | -42.0249 | 2025-10-26 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 228cd892-5035-3257-a5dc-1df891e299ef | -5.46371 | -40.87535 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d261bbc4-abf5-3b39-af36-d202e04eedf2 | -7.00501 | -41.07296 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3f6cd598-fa06-3226-993f-f40bc4ffb65b | -6.99457 | -45.99788 | 2025-10-26 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8d1c115-a251-3c7e-82ae-d412a1f09240 | -6.4755 | -47.55608 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7e52750b-13f8-3641-a3b7-3738d635b766 | -5.12121 | -41.19421 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f06ec3e-adf4-30b7-b2c1-fabc70cfa4ee | -5.52869 | -40.97624 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 71b41626-834f-3ee4-ae8f-c39cb444e20c | -4.02915 | -46.06834 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8567e829-9899-3bc5-9d55-607f8a7958fd | -3.3122 | -50.11379 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7f2a8ed-1c64-3b4c-abc3-21b2b46037ed | -6.46947 | -47.5557 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 815a4cd0-1915-3852-bc37-96801757653a | -3.31088 | -50.11143 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da1493dd-0e0c-3baf-9939-da783e97ca7e | -4.2688 | -40.69412 | 2025-10-26 04:00:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8b9a1767-4bf6-3ef2-a9f9-6d185c201239 | -3.23152 | -45.94033 | 2025-10-26 04:00:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f97219e1-a219-3de2-b370-a989885ea7af | -4.15715 | -46.7929 | 2025-10-26 04:00:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23d3ada8-d4f3-3b74-8dbc-07a3150cf0be | -6.51485 | -44.1968 | 2025-10-26 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a71c19db-f177-36cb-a9e9-2499bf00595d | -5.54899 | -41.39616 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eeed19ab-9ef9-32dd-9183-718815315b3d | -7.051 | -43.86917 | 2025-10-26 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 269eba22-122b-3937-a2d6-c8b73f428891 | -6.1299 | -42.45602 | 2025-10-26 04:00:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 272b3c19-25af-38fc-be61-10f970ad1991 | -5.829 | -40.82347 | 2025-10-26 04:00:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f26611e-504c-3fb7-9b7d-f0437a46996e | -6.02356 | -43.30127 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0e77eda-a98c-313f-a5c9-13a58ed82033 | -4.71098 | -46.4369 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9b6f736a-3a25-3faa-ba94-5f2ac5bef671 | -5.11169 | -43.19989 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 25d70077-82f7-3778-8517-e1ee77c8e5ad | -6.02283 | -43.30564 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e788863d-0479-3a8e-ac30-f9242b9f54b9 | -7.04844 | -41.64834 | 2025-10-26 04:00:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b90a4860-8fe3-367d-bb3a-868df048462d | -7.09013 | -39.57462 | 2025-10-26 04:00:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcb30387-a707-3e75-85ec-f77cb5ba7d52 | -5.65627 | -41.09616 | 2025-10-26 04:00:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 080151d6-14ec-300b-8cb1-29c9cc4bd795 | -4.26347 | -50.51359 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25f95d68-e742-3285-8040-04bee4ea7dab | -7.52473 | -40.58788 | 2025-10-26 04:00:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9f372a8b-2a20-32ba-9135-c2357cefa4b3 | -6.22722 | -42.54798 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a0335cf-190d-375b-8efb-ec638526b26b | -6.69957 | -42.04759 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| eb485931-0853-3a33-8ee3-cbcc7496b29b | -5.32355 | -35.93694 | 2025-10-26 04:00:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 46.9 |
| ac110cc1-7620-317e-91f9-75016b6acc3d | -3.10001 | -49.44823 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd29dc1e-754d-3cc8-aa80-4e5c62056e67 | -6.25153 | -41.82291 | 2025-10-26 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e46d1f25-b68d-3b21-9fd5-19459c53268c | -7.79542 | -45.39226 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a081601-e5c9-30fa-9b2f-7efa891c83a0 | -6.43111 | -42.34105 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a4299ee-aa50-3dae-baa1-e6f7696f9e24 | -8.49072 | -44.72499 | 2025-10-26 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4135ebe6-34a5-37b6-a3b7-cece37c74041 | -7.11946 | -45.3896 | 2025-10-26 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4632569c-dd14-3020-84c9-417bdc6cdab5 | -6.10913 | -41.75022 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72eede73-34b7-353f-88ab-88de9c4991db | -7.80231 | -45.40129 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5f51fab-6990-3c0f-a726-80eb76a78caf | -7.33187 | -47.12815 | 2025-10-26 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f49dd8f5-1739-3a8b-8c07-7b685947b393 | -2.97442 | -49.12275 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d0d0c6b-d712-3dd4-bdbe-fa987de2fc23 | -6.33616 | -44.32431 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a74d9a95-f6da-35c7-9bb0-a303ae160046 | -7.38431 | -43.94186 | 2025-10-26 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README20.md)
