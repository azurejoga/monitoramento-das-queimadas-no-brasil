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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61288c06-afea-3b1a-b85d-55d429915f96 | -12.6453 | -57.1881 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2e4d9c7-1373-3f69-a694-1328ab206a06 | -14.02006 | -55.13414 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 196b624b-07b8-3854-882c-1ea1ce6c256e | -19.11886 | -52.6908 | 2025-05-22 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f74644c-04b1-349f-be77-0155caab794a | -10.93645 | -55.32233 | 2025-05-22 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 015f4dc7-03ea-3efc-9b55-1cc775af1e57 | -13.38303 | -46.78789 | 2025-05-22 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41f87330-b0ee-3f29-9caf-441f9a4e1b01 | -16.84938 | -51.39841 | 2025-05-22 04:46:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfc35814-9183-3744-8e17-cb7c5ef06782 | -12.28624 | -52.49219 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a602f7b3-5414-31f1-a981-3ef9e149885a | -13.78358 | -54.31277 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93a9c824-2a9b-331c-8bab-bb0133cb273f | -10.93787 | -55.3138 | 2025-05-22 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfe96623-5ed1-3e93-860b-4da646e377e7 | -16.57551 | -51.54868 | 2025-05-22 04:46:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 800be756-7418-3003-b6d8-94ac986dca5e | -11.91755 | -54.41337 | 2025-05-22 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19a09023-849e-3045-8bbc-bdd40d1acb82 | -16.28091 | -58.66891 | 2025-05-22 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 29dc9041-86ad-3dba-9698-9177b54dabcc | -12.3469 | -49.97863 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5ea65866-0cbc-30a9-91d6-e0840a37fde6 | -16.2816 | -58.66517 | 2025-05-22 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| daa1bb7f-afa2-3130-aa10-edfec7d8e76c | -12.28457 | -52.50275 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d06c97f5-a207-3c86-83de-bee63cc0900d | -12.27992 | -57.27007 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93724d1e-713e-352e-ad32-643b85c1474e | -10.99983 | -56.91845 | 2025-05-22 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0edda581-05b0-3e9d-858e-431354beb267 | -13.75678 | -58.58801 | 2025-05-22 04:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a378829b-4868-38fb-bdbe-33533365645f | -13.80534 | -52.89357 | 2025-05-22 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cb4b32b-9152-3150-ad5b-1d27c0235867 | -12.8455 | -47.39465 | 2025-05-22 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d5be4f9-a080-34a3-8d44-4c9bb092dd23 | -16.57892 | -51.54924 | 2025-05-22 04:46:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6819228d-2179-3ba1-a60f-16290138c3f8 | -13.53182 | -43.6736 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c69327c-9c5e-3b1b-8a21-f4009500b4ac | -12.66299 | -58.21565 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d1c3384-c6ca-34e3-949e-905f08317a55 | -11.07839 | -54.77222 | 2025-05-22 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5e44299-8563-3cc4-a06f-69b73312c336 | -12.64137 | -57.18738 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d269ad0b-07bd-3595-b10e-7b8dabf5117a | -14.01658 | -55.13352 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ed08f40-c313-3b6d-9090-208422ec655a | -14.03148 | -55.13958 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74a09603-09db-3334-a5ac-45602d535aa3 | -12.28952 | -52.49296 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8e23dc3-24e2-309e-ae0c-8dfdfaef4620 | -12.29835 | -52.50163 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7f787bc6-32c3-36ed-b368-66764e8d8bdc | -10.82878 | -56.95713 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a2a7d1f5-529f-3ef7-bce0-c994197a981d | -15.51791 | -53.5074 | 2025-05-22 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7050543-69f5-3391-8fdf-26ff40a08de1 | -12.67136 | -58.2173 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60f756b5-30ad-3071-ba11-23c00c4e9065 | -11.57279 | -54.56801 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86e37866-1e23-3dc4-9109-2d270a3c255a | -12.2868 | -52.48867 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fa2a990-1b03-3fce-886b-53f42108985e | -10.93495 | -55.30894 | 2025-05-22 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76d30da7-c9b1-3caa-82f9-fafe1b482b52 | -17.34367 | -51.90533 | 2025-05-22 04:46:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 199d95b3-2383-3b04-93fd-29b85ace56ad | -11.57344 | -54.56411 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edaca536-0919-3dcd-874c-fc2c4ed51023 | -13.51893 | -43.69171 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85bf0510-0dc5-31d2-9001-7e14728c551d | -13.5372 | -43.67864 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68505c03-ed30-3be1-ae07-240ff66986ec | -14.07105 | -50.42702 | 2025-05-22 04:46:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6677c832-8b7d-35fe-868b-372dfc629ca9 | -13.66882 | -53.93767 | 2025-05-22 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaae0793-5163-3c67-b585-2e66450bb254 | -14.03214 | -55.13566 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8da4c649-8f79-31d9-8d5c-4ec1047a1e6d | -10.82418 | -56.95998 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e05e5c5f-ebbb-3019-8cad-1d9639c63ded | -14.03447 | -53.37323 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98ef56c2-b791-3ec6-ac8d-68f6b9a9c44c | -13.7567 | -58.59023 | 2025-05-22 04:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 921e526f-a074-37c3-9905-db504226d79f | -12.34885 | -49.97987 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d24e6d0f-7bd8-31b0-9059-b3e047ff3b05 | -11.29688 | -53.98476 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5484700-7b3b-3742-8892-316ee7b08d82 | -12.5673 | -52.15182 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77bb5c20-1c30-3991-80a6-056f605bb69c | -11.86254 | -52.27189 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88f9b820-e2f9-3b4e-b9fe-54d8d7a9a17c | -12.02927 | -57.09562 | 2025-05-22 04:46:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7893613b-ba37-3cdf-9625-622cf5f6dc84 | -14.04778 | -56.06787 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25743446-65cd-3bc7-8e33-70860cea28d7 | -13.53236 | -43.67471 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35c121c5-7ee2-34cc-b346-797c777918d7 | -13.19777 | -56.82416 | 2025-05-22 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 053915df-5e08-3cf2-9a27-dda683308375 | -11.57061 | -54.55962 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 274e024f-de4d-3222-9957-1e36cae95654 | -10.93716 | -55.31806 | 2025-05-22 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 981d04d3-158f-34e5-936e-2711af38b600 | -17.76587 | -56.31054 | 2025-05-22 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b0fac595-6ebe-32a9-8275-949c9c58f1ad | -19.36797 | -47.62097 | 2025-05-22 04:46:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b4fedea-d181-3c84-b70b-7dc2d39611dd | -18.81182 | -48.52406 | 2025-05-22 04:46:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea34ede4-594c-3509-9f57-426064a6647d | -14.03333 | -53.38037 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a810f7f3-7fe8-3c10-9285-0ef809ae3ac2 | -11.65724 | -57.35925 | 2025-05-22 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72c7b5e9-ebe7-3cf0-a5fd-c94e1f91afb6 | -12.50272 | -57.21776 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17dab23-f6d6-372d-8964-db6a630e52bc | -12.28841 | -52.50001 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dad09a24-c39b-3c79-aeb1-cc9e52f0e40e | -14.02223 | -55.14259 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a9b9a0-bf60-3060-88e4-385781c19079 | -11.6707 | -54.93826 | 2025-05-22 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46911905-37c8-3b38-991b-49b4e9476ab4 | -13.47735 | -52.2808 | 2025-05-22 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84637e2d-93ac-3bf0-8d89-d31b7bed8177 | -13.48232 | -56.55627 | 2025-05-22 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46430e11-6604-389b-b1a8-ece9fb61850f | -11.40789 | -56.7311 | 2025-05-22 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95d28ce3-e6a4-32c7-b777-d4c1216e539a | -12.30058 | -52.48754 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f98bcb3-e57e-30df-b8b3-78126cffbc2f | -12.02047 | -63.79004 | 2025-05-22 04:46:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32be33d2-d61d-36a7-995c-5bb43bafe0b7 | -12.35734 | -49.98026 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9c31b6c-bf37-3ca5-9d97-cd563e5894f9 | -12.42116 | -54.35936 | 2025-05-22 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cda72d9d-8c1a-3cf2-83a6-c04213158346 | -12.13414 | -54.65617 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee28d017-953e-3a11-9eef-271732db064a | -15.33859 | -55.13619 | 2025-05-22 04:46:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c73d33-8df2-3ce6-99b8-0b0644c86ca7 | -12.72383 | -54.97158 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23c22386-d26d-32aa-a814-07f247819bc5 | -16.68147 | -43.88684 | 2025-05-22 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4791840c-87ec-304e-9e71-7da42d305ff7 | -11.44807 | -54.09055 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d987d81-05d9-3f72-8d01-2ce9c84ef524 | -17.27758 | -42.64906 | 2025-05-22 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf346dff-0d2b-35bd-9f64-5489bfd00c89 | -18.81231 | -48.52028 | 2025-05-22 04:46:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa033221-ddb6-3bbb-81a4-1d6e91499c1e | -15.33917 | -55.1367 | 2025-05-22 04:46:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50a1d695-ccba-3d58-8b81-2de35a9618da | -14.01593 | -55.13745 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13e48ef4-bd57-324b-b588-33b65694832d | -12.30166 | -52.50217 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42a2679c-c717-3fc9-a195-527f0a6877e1 | -14.0378 | -53.37379 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec036ad2-b442-301c-b989-c7cac9b1e5c8 | -13.51961 | -43.69284 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 634fc0a6-5a1b-3e0b-a173-f7bb77c29c46 | -12.28735 | -52.48514 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85d7cf9c-1908-33ed-b661-1aad9295a2ff | -12.29448 | -52.50461 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fb64b498-c2d5-3b74-a218-f9d230f46142 | -14.03115 | -53.37267 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f0d6f26-77c4-3743-b8b2-ebf29c1ba6f6 | -12.48761 | -57.18832 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e466638-a205-3e0a-9a0f-86883791bd77 | -14.05011 | -45.53176 | 2025-05-22 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6767708f-6725-3e57-8617-deef020c9729 | -12.67065 | -58.22122 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9516b25d-a276-35aa-afaf-f7912ba07eef | -12.28085 | -57.26482 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7d59e638-6cf5-3b62-9eff-b1d2ee0ccb7b | -17.61971 | -54.17192 | 2025-05-22 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1da7980-db64-3657-acfb-ec6fa452bdb1 | -12.72318 | -54.97555 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86ae474c-3b15-3e4d-8af9-6c5fd091c0e2 | -13.89074 | -49.64066 | 2025-05-22 04:46:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 291ee4b3-9a50-3325-ab2b-b3e80b55aa96 | -12.29726 | -52.487 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64bc8db1-fbac-306f-ac0c-692bf3d6d4ca | -14.02636 | -55.13927 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ea3292e-3a89-3370-87f3-434197445e82 | -11.29346 | -53.98419 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a72c4a9-40f0-3920-af19-f64f1f08706e | -12.29008 | -52.48944 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dcd6a503-8efc-3519-8e53-a98969da39ed | -11.11812 | -54.66423 | 2025-05-22 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f0e28ec-338d-3cd2-be21-8e0f826db54b | -10.82939 | -56.95364 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c0a7f89-5770-3d62-a856-b36fee5f821d | -14.17098 | -58.32243 | 2025-05-22 04:46:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README18.md)
