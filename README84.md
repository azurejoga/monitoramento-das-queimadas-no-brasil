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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 129d7555-25f1-3e64-bad5-15c84a7a8774 | -6.6201 | -43.71954 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f15d082-15e7-3c20-8a19-56b6d97f81a3 | -10.94506 | -47.05859 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e9563ec-8427-3aaf-8643-0fc32e7ccdf2 | -8.87718 | -46.73231 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3dac4b1a-4052-3f2f-97c7-27ee7904a992 | -12.9692 | -51.03676 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f8e43d0-61a6-379f-bfe9-4fc217d6824d | -13.23816 | -47.26771 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2d24750-c6b5-394a-b229-6e40a6e8b514 | -11.27481 | -56.44207 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35d7505e-abe7-3388-b7a3-3c25f0c7eeb8 | -10.39907 | -45.39595 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84088c5e-5096-31c9-9cec-7dbd397b7b9b | -7.04701 | -42.75989 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18213689-9df1-3271-9426-fc212f8e8cef | -12.88894 | -47.30212 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8455ea56-19e9-3231-9221-4b4ece6ad051 | -10.63159 | -49.15958 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 206de36e-95a6-36c5-a69d-52f6d868a725 | -7.03621 | -42.80094 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e1f1db51-0500-3fa4-922e-a4c86724d560 | -8.2644 | -48.81691 | 2025-10-05 04:46:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 808bf777-b654-3855-992d-855c73f37c0e | -13.21778 | -51.15073 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e1e6867-7c6f-3af9-a2b3-5a3814dd33ee | -8.95671 | -46.76177 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cc95b81-d3d9-31ce-876e-5a2df3c9b001 | -11.17592 | -47.73853 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a95d9118-393d-31f1-aff8-daacc59d7d90 | -11.8549 | -45.05328 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1685113b-ef15-3c54-8eee-ee28b9b56d6d | -8.5839 | -46.30841 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c1991bc4-7f57-36a5-baf4-e5447d834126 | -9.04907 | -47.01527 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1317f4c4-c694-3483-a0e4-5c6b30d435b2 | -8.86959 | -47.6673 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 125f8678-4a37-3fa1-9561-3bf9e58a69ef | -7.87484 | -45.23238 | 2025-10-05 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 406e4cb8-2004-3217-9b66-066d1c7a7ced | -6.98221 | -44.37487 | 2025-10-05 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13b2bb6d-d757-347c-8af2-19ac829a8f46 | -11.80577 | -46.84094 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e197e660-cae1-3e70-9d07-6cda20ecc9fe | -8.58235 | -46.31944 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b81ceaea-0d21-3b58-ac7c-55f9b3a9658d | -8.62457 | -55.0011 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 112c0749-9525-3d8b-bbaa-46d431240824 | -8.04755 | -54.89986 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12833323-7243-3c07-964d-66f91eb53ea2 | -11.35366 | -47.66596 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b44e59b-2e73-3e31-aaf5-1738a5f75fdc | -13.37991 | -47.54261 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acd0cfd8-91ca-3e21-8d92-a2d361a8fee8 | -11.6355 | -45.05304 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e3217c2-e5fc-3f67-a05f-2b2140b56684 | -13.30288 | -48.11325 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12cca443-b927-3980-930c-043683112591 | -13.32067 | -48.07007 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5cb4b0f5-a2e5-349d-b55a-a4b4f9f85047 | -10.75675 | -46.61588 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 697b3f58-3cb1-3d0a-84c3-b16369497a1e | -13.34928 | -48.06424 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46f8c6b5-78e9-3591-ae94-3345a6387e21 | -11.45367 | -51.50776 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fecad02-11d7-376c-9d44-9ff002602987 | -13.09383 | -47.9439 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9538b7a-1b09-36d9-9d9d-674fdceb4eeb | -11.10793 | -47.7606 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ab815a3-ee6d-3b17-9d39-8c066f95a1ff | -10.74556 | -47.88813 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31789042-7a82-3762-be29-f661e14d5bcb | -6.28061 | -46.35834 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 118806fe-c845-3d73-8798-705ab489069f | -11.82366 | -47.68473 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad5590cc-cc7b-3865-bf7d-8725e61b8f11 | -6.60569 | -44.31567 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3913045e-a3bc-3559-9539-b5a851ba8b3c | -11.4518 | -44.95607 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 95f448af-5951-34f8-9367-70e813f9da95 | -13.704 | -47.35544 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c22eed87-6fb3-3111-b74c-5375d5bf4ea3 | -11.80039 | -47.91557 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f008507-6b7c-39a7-9a7e-b6b0f7983a62 | -13.29124 | -47.58213 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31314621-67d3-35e4-a5b8-32e76d8c744c | -14.01552 | -44.92757 | 2025-10-05 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e77a48a1-c92a-3109-8948-2d59226f069f | -13.35507 | -47.57565 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89ab64ab-d883-3ea2-bcad-936c390fa032 | -13.33027 | -47.56612 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67902bcd-b98e-3d89-9628-a007b5dd0a42 | -7.15947 | -46.08592 | 2025-10-05 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8183b34b-4f07-3f0d-99c4-0bd5bf950118 | -13.53003 | -47.28875 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bd99b2f-87bc-38fb-9423-bd44078dd438 | -11.45097 | -49.71613 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa686970-53f4-3c16-bf5a-2406cbb56a03 | -7.65002 | -45.42005 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 557ca832-269b-373b-af00-5f6768413e5d | -9.33064 | -54.51725 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cd82709-a8ac-318c-8158-c26dacf177ac | -10.01178 | -48.264 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b03f2a3-af05-3c00-93c1-ca7aca9fcb5c | -7.02341 | -42.78096 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 04ea4fe2-3061-3e11-9f76-34bd15c20b72 | -8.59256 | -46.30602 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 65213465-fd1e-32a5-a0c2-6a133c61094e | -8.57027 | -47.65467 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f61e8e83-df7b-38bd-817d-1f9652b94ae5 | -13.32326 | -47.79173 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cffb5db-14a7-3fd0-bc9f-43abdd843f8e | -12.96678 | -50.99548 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfa612c9-50ae-30e8-b75a-e869b6e2051f | -8.67959 | -47.21548 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9344fd25-49d6-3b73-bee9-5fa526a241dc | -10.31033 | -50.38292 | 2025-10-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e583a9e-83e6-3a5d-966e-484916da36e3 | -7.31549 | -45.9856 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e9fa37b-f410-3983-a50c-3f97f3b8dba3 | -13.86231 | -43.99044 | 2025-10-05 04:46:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d13b3305-910f-3f8e-b934-944f21a75e60 | -7.60847 | -46.09036 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c910ea3e-c748-363b-a4e0-52837d2c0fd8 | -13.13277 | -50.87667 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 39ff0740-a79a-318b-8ab2-33230da4402d | -7.45853 | -47.1785 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a472cede-0854-3a03-93c0-da278bf794ac | -8.75639 | -47.20221 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22cf74b6-f572-3e8a-8876-8ec9b7968e9d | -8.63524 | -44.90913 | 2025-10-05 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f59552c-2071-327b-bb37-55b72140157f | -13.58023 | -48.1585 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54f68806-eab1-3c4f-8bbc-bb8477d23aec | -13.1616 | -42.35339 | 2025-10-05 04:46:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 02dfcec3-0630-363b-9b7d-19b4cf275d81 | -7.6587 | -45.45084 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6b0c1b0-6c55-30b8-9c38-cb2b415d8afe | -13.48801 | -47.23378 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c54f3ccf-73fe-3338-bc7b-0d5cf05a4aa3 | -9.67957 | -47.76859 | 2025-10-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ac74c7b-7bf5-3427-a67b-a09a5d9e5c2d | -8.90514 | -46.6795 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23ac106a-b92e-3122-ac12-b850dae61536 | -11.7932 | -47.9393 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d19a3ea9-cf30-3c20-b425-9c1f2efb9abb | -12.82267 | -46.86414 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 767e1d36-a84e-303e-af12-3842c0254cde | -11.50976 | -54.47432 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d91e5549-c54b-3199-82e9-aeef9cc65c51 | -8.50772 | -54.59549 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 931edb66-76c1-3491-9155-85256e8573f8 | -12.59375 | -48.13621 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 203357b2-4f36-3c68-9b76-048a51053df6 | -12.32147 | -55.15163 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cde0716-a60f-3994-bb4b-f39584ec9e54 | -10.44903 | -48.36921 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d333941d-f2d1-3894-917b-4cd48a18a93b | -11.85619 | -44.9482 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3b5afcb-0971-33d7-9cb5-bf59f8b37029 | -8.56041 | -46.26776 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ae052d4e-f16d-39f6-a28a-ff33fe2345f4 | -9.2939 | -46.01874 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ac345fef-be64-3e26-906c-19952b83bf8f | -6.68165 | -42.84996 | 2025-10-05 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 859c8298-0842-3200-981a-3b7fdef343de | -13.278 | -47.61953 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4cb52ed2-08f4-3594-a6bf-aa4c06787a40 | -13.09798 | -47.8533 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef142a0a-fd67-3c1f-925b-d15c44695d37 | -7.02894 | -50.73729 | 2025-10-05 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 042e6ec7-2fe8-3b3f-ba79-5d34273d48ff | -12.9042 | -47.3117 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccc28f27-2d8b-3b8e-9b85-82f2fff742ae | -9.25426 | -46.78001 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 800a8e23-5f7b-33c4-a340-16e8197926d5 | -11.88421 | -44.97221 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61b73690-2f6c-3a50-83a0-a379db5f9998 | -6.43245 | -46.02373 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b89f1efd-50d3-3c91-ba17-83e4ffd4ed82 | -10.45856 | -47.81345 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6858f19a-cc4a-35a4-b7e6-6f666557c38f | -7.76973 | -42.61721 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f1b3d50-0c6e-339b-af31-34151d147978 | -13.00064 | -43.99705 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89a1a4c0-164f-352c-b51f-31a51636f993 | -8.6336 | -44.9065 | 2025-10-05 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 190a24be-fdb3-3c1b-8638-f1d246075966 | -8.61993 | -54.95759 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 541ebf3b-0596-3dfa-be3c-75907a982450 | -7.75292 | -46.3287 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b1fec78-b2ea-3b98-bf8e-142456f0aea6 | -7.00794 | -42.29998 | 2025-10-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91245255-0f52-3168-b426-5e2339f0ba70 | -13.25198 | -48.48452 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6a4abf4-a3aa-342d-9db8-a6ec92bbae69 | -12.69568 | -45.84861 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dfa2f531-89d3-3e6a-b9c2-365aa57dd935 | -10.18854 | -46.72469 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README85.md)
