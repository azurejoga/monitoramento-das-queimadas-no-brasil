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

## Dados Diários - Página 285

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f00aa6e1-a9e1-3126-bb86-cc1df21bc34f | -7.16348 | -46.51236 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 178a8549-89d3-3858-a891-7155591e8510 | -4.35706 | -43.80215 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e1f8bf44-e7fa-341a-b999-f276e6cb7290 | -5.69807 | -45.28917 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 831cbe0f-f10d-315f-9637-cffd7cdecf07 | -3.09732 | -53.94757 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 3f610be4-cede-3346-94af-34a0887fc7f2 | -7.19104 | -44.33783 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 21da704d-be65-3bdb-9344-15a086a2c006 | -6.8228 | -39.3133 | 2026-10-08 16:20:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 3a0b63f1-975b-3cb0-9f4a-6fed148ed404 | -5.95625 | -40.94794 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| bc5b4c20-ffcc-3f99-bea7-7065cc9d5dfd | -5.93191 | -51.82948 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3dd389e1-1294-3dc0-b6b4-7732576230a9 | -5.88971 | -45.96885 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cde1ca9a-ddc2-3e64-9006-2726345a9d82 | -6.4278 | -44.83307 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 172ac717-1aa8-32f4-ab56-4a1d7159e95a | -5.39388 | -45.90789 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| d3f2675e-f627-3d0b-bcf4-d5cdb04f4236 | -6.91001 | -45.46957 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a65ee328-da3d-3888-b32c-aa6e34798825 | -3.42772 | -45.04362 | 2026-10-08 16:20:00 | NPP-375 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2eeb6a76-c562-34a9-8e87-c6436ca6ed30 | -3.25487 | -43.58723 | 2026-10-08 16:20:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a273748-e383-3bea-a77f-256e67594a66 | -7.20606 | -46.53456 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5a154f95-6172-344f-90ee-69102f0a3816 | -5.92539 | -51.83112 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 0197cde8-bc1b-3a51-bd10-a458ae89535c | -5.70812 | -53.48638 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| c4530d29-8457-31a3-b165-fc33cd682e14 | -3.21103 | -50.55047 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7a827b2a-efde-3323-bc79-f7589b685735 | -6.29823 | -43.87165 | 2026-10-08 16:20:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4b518c5-a924-3915-9ac9-d272144ff0d9 | -5.71265 | -41.66797 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8a048c95-6e19-3bf4-9a7f-272fd8021aae | -7.25816 | -45.34099 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e484af11-e0eb-35ff-a59d-791b168858bd | -3.28718 | -53.70581 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 4105110d-104e-3312-b15b-ebba513d44ec | -3.26253 | -41.63105 | 2026-10-08 16:20:00 | NPP-375 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 24a048aa-c11e-3f89-8b6b-2f0a8054d883 | -5.74903 | -41.72104 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| 70b7c8b2-76e4-33a0-ae01-2b583dcb92e6 | -7.16963 | -47.79631 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a83b414-0877-3367-a934-b1bdacadb97f | -1.79165 | -48.19146 | 2026-10-08 16:20:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4bba33e7-2ddd-341a-835c-ed9fef69fb6e | -4.79225 | -43.33371 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 06be41f0-6b26-3ac7-9f04-bc90ac6038fc | -5.30452 | -45.72475 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1b4d2979-026f-3c5b-9b59-d7ff87a60353 | -7.51686 | -47.33579 | 2026-10-08 16:20:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2e5e0874-7c77-31be-948a-6f87d77f3568 | -4.76717 | -42.666 | 2026-10-08 16:20:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 688e211b-5266-3b58-a2bc-e9230764850e | -3.70844 | -38.83297 | 2026-10-08 16:20:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0094c407-7ad4-32c2-b3a8-eb4e529a6470 | -6.85155 | -41.74958 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 3bb53ac9-66e2-3418-977b-6570a67ccf1e | -6.86223 | -41.79625 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 78f097d3-e038-303f-8315-68bc69cda61b | -6.05245 | -45.09465 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| db047ae5-0189-307a-961a-5ac6e33be3b6 | -3.82064 | -44.60099 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bb8bb58e-b268-3156-8d99-4288de983621 | -6.16718 | -52.65337 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| fa85af69-1043-3103-88fe-c1a3e933a111 | -6.55011 | -45.36123 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c1c8835a-666d-3825-992e-14fb262068eb | -7.76582 | -44.16521 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdcbae27-63c3-3b25-af34-c3ae2629d2cf | -6.38754 | -42.55272 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| bd86cee1-5650-3193-b8ec-dd22760f3c61 | -7.21468 | -44.27109 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f53898cb-7d7c-3e5a-aa24-b1c3ea20f24e | -3.65979 | -45.40955 | 2026-10-08 16:20:00 | NPP-375 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed06a41b-9825-39fd-877d-afbcb1025fbb | -7.34178 | -50.03116 | 2026-10-08 16:20:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d93f9c29-fceb-3800-995e-b53965592790 | -7.09821 | -44.53002 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0e9fcde-a7e2-32e3-baaa-71518255bdf4 | -6.32823 | -43.83407 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d11bbf25-6852-3d71-a083-0bcec40a35de | -5.23749 | -40.57724 | 2026-10-08 16:20:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8d8d2b4a-159d-34b0-95db-c519c6c79cc9 | -7.26059 | -44.21957 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d5f4df46-8b7b-3b21-92ef-2e1408f7e983 | -6.67369 | -45.34867 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9793f423-5e60-3030-90bd-fa133ec42232 | -7.18788 | -42.00284 | 2026-10-08 16:20:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| dc676455-ed52-3fcd-9a39-c0b632b8ec16 | -3.02426 | -54.0627 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| df8c83fb-6b0b-3df5-aa72-4564f4a37d87 | -3.75299 | -40.04078 | 2026-10-08 16:20:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 346c970b-9469-3280-8023-e129de51c8ed | -7.59823 | -42.38854 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| 0bcab9b1-55d6-3c8b-a460-ade7be29e021 | -6.14895 | -39.43818 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 8d9c461d-4a2c-3e14-9301-2b5b58ef1f51 | -6.79526 | -45.06087 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a776c695-5669-3654-bcaa-6664051d22a4 | -5.67945 | -42.59621 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 90b2090b-d80b-3e4d-9e02-7053b9143b83 | -3.29979 | -49.13145 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 803f7a91-8fb2-3dcb-bb7b-f9094271656e | -7.18745 | -44.34188 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1ef705a9-d419-34eb-91f6-ba82bd3264e9 | -3.90848 | -44.39219 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9d4279cd-98e7-3f30-a7de-31ea66c01bfa | -4.75269 | -42.59327 | 2026-10-08 16:20:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4bc1cad5-778b-3b65-b075-edcadb44b201 | -7.40728 | -43.74071 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 98364096-d270-33d1-aff7-a18667f7ace7 | -4.0951 | -44.11312 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 44f1e35d-0219-3610-96af-71ad5d2afcd5 | -3.0059 | -54.05155 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 42fdcf02-93db-30fb-9e89-2eda6ec84534 | -6.14877 | -47.92845 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2dc96235-a3ea-348e-91a0-99d01eabdfa3 | -6.40562 | -44.94576 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 37eae9ab-6226-3674-99fc-43121d81833a | -6.22728 | -35.34558 | 2026-10-08 16:20:00 | NPP-375 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| abba83b4-cd29-3f11-963f-47773cb43d7f | -6.13983 | -47.95374 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65795f64-77f7-3728-8fbf-0c424143fd2a | -6.44705 | -52.69764 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 65eb438d-0d2a-3ac2-9a0f-30595aff1b44 | -3.79225 | -44.81948 | 2026-10-08 16:20:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 871a9275-389e-3d7c-b4c1-f677a706172b | -5.94775 | -45.37777 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfd188f8-df9c-345a-aa2f-0e0d0fd4c649 | -6.18961 | -52.87844 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3011a260-e702-3e96-876a-6cc3f7832738 | -6.20426 | -46.64421 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5989a2f0-be61-3f4d-af68-78a394de7bda | -7.04848 | -45.43846 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 711f7d57-ea1f-3b9a-8b79-d8f1787b956e | -6.3693 | -42.90196 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dd461c8b-8575-38e2-b14d-7a0b2655f0fa | -5.77347 | -42.05081 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| ff0c8cc9-5d59-3b04-b268-128a5a098cbf | -7.04946 | -44.33498 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b8f00c9-3eac-36db-8940-4149d8a2eba5 | -2.08433 | -46.5722 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| ce26c5fa-f40c-3ea6-89c6-b175b2eab804 | -5.38885 | -42.96849 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6d1a2da4-4ee9-3e89-844f-ec26e6d4344c | -4.84604 | -44.09293 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cdbd626a-e31c-3454-b672-7f6ff48eb83f | -6.98191 | -45.12944 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ede4f3d3-5052-3213-bfde-019e8cc49eed | -6.52926 | -45.40223 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2fdc4634-f661-3ca4-9f24-e89d3d24db62 | -6.21731 | -44.83578 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a95c5c58-ab81-337f-a431-7f71292b91c5 | -2.97907 | -54.07016 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| bbd13236-dd8f-3b34-9e33-29edc11fb50a | -5.95918 | -40.92159 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| cb0d17e0-16e0-3c92-81e3-ee205e3665be | -4.62778 | -42.75328 | 2026-10-08 16:20:00 | NPP-375 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| db5cfafb-1808-3c9f-bc63-f5fd558da1b1 | -6.77171 | -44.13116 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9707262a-0e84-37e0-96ce-61f56ce7cbf7 | -6.15665 | -39.44409 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ff77f930-9547-3cde-91f5-c13f4d91343c | -3.30787 | -54.05741 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d5c16059-d6a2-3d2e-a01f-b01f28991432 | -5.97971 | -41.35879 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4adada70-e8df-395a-9b41-58320b3a7daf | -5.37159 | -38.28225 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bc0e2264-d2d5-3bff-8ee3-19d0892afc12 | -8.67208 | -50.20602 | 2026-10-08 16:20:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c9f717d8-fc11-33b3-82d9-3a2432d1027f | -7.34254 | -50.83297 | 2026-10-08 16:20:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 77762989-81a2-3efb-8f56-b7b0e1e830f3 | -3.55484 | -44.56319 | 2026-10-08 16:20:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 90508b3b-80c6-3f61-b7f2-c8e89078df9a | -7.51201 | -45.77414 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7751c25a-a522-3c27-a295-068fb3207dde | -7.05606 | -44.32286 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5c80a6f6-8a34-3c58-be33-87ff58a3f1b0 | -6.61739 | -44.92369 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eeb4ab2e-5b95-34da-bd72-d7a3406f30dc | -3.30177 | -49.12337 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 51315139-679f-3cb5-8380-d4c9c7c5090d | -4.64002 | -50.96078 | 2026-10-08 16:20:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dd8cbf47-e138-3170-a8bd-aadefd476f55 | -3.45719 | -45.1012 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12155032-8034-3064-8607-1c57f2d65268 | -6.12322 | -44.13118 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bb2d4263-af55-3a70-9e05-41030584cd93 | -6.97797 | -47.67318 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 5528f0c8-9148-3096-a9b5-2b16e123f3fc | -3.9443 | -40.72093 | 2026-10-08 16:20:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |


[Clique aqui para ver as próximas entradas](README286.md)
