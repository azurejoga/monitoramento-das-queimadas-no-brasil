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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3182b82-1c18-39de-a5c1-10fe04398d98 | -10.71986 | -48.82925 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b44726d1-a0af-302b-ad1b-776fd00ddff7 | -12.09461 | -40.59343 | 2025-05-23 04:04:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0faf1ed-a780-3401-b266-997d23412fbe | -12.29154 | -52.50291 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6f1ae08-3d19-3c93-82d6-4130d226315c | -12.33051 | -49.98672 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ca419c9-215c-3614-bedf-25aa452c52dd | -12.42387 | -49.9786 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9feebdd5-d67f-3f52-af2e-bff02c359c44 | -14.03524 | -53.37922 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bce885c-db33-32c4-9bc8-c20f43337080 | -10.64715 | -49.48038 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82da834b-41c0-3475-99a3-2ab0fbb3f09f | -10.66349 | -49.47728 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f86ec18f-9d20-38e8-8af4-620758d7b786 | -14.03622 | -53.37441 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16a29e78-6fe4-3525-a000-bbe8ad3632b3 | -10.71499 | -48.82843 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebb6443a-b82f-3725-9220-d7eae36ec08c | -14.67747 | -45.10844 | 2025-05-23 04:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 580dc722-9f7e-373b-afe2-be4c4feb2784 | -12.33505 | -49.99072 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfd03da2-7cfb-3c99-8d0d-fb57d4ab8a69 | -11.30516 | -54.02955 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29709ffd-0614-3f86-a439-5fdd65fa2b89 | -11.31052 | -54.02466 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8924c579-0cde-3b26-9796-d95ed130423b | -12.32542 | -49.98574 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52c7e4b5-85c3-3471-ac91-ca1dba60f55f | -11.79006 | -44.28855 | 2025-05-23 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4811cb99-e778-3166-99ac-54529a550f7b | -10.71736 | -48.83048 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e680768-9a8e-31eb-9245-fd8d2dab9312 | -10.6646 | -49.47132 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5610b25-c56f-3cb7-af9a-fd54180702bc | -14.04761 | -53.37567 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d0f331c-1048-3acc-98d7-dddcf19a0479 | -10.64207 | -49.47946 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cafc23f-002f-33e5-9b4a-7629b90daba8 | -14.02594 | -55.13551 | 2025-05-23 04:04:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98efd99d-eb57-3779-9084-e51162d99d6a | -10.71836 | -48.82513 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52fd2926-1ca0-3205-b0e2-28af5a6c94e2 | -11.79468 | -42.63881 | 2025-05-23 04:04:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4da7208-98ca-3f34-8f02-d31a75c2a9db | -12.33159 | -49.99183 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 650926b5-0d6f-390e-bdbc-3e1a24de6976 | -11.30928 | -54.03078 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5270a0ec-8f94-35f3-bc30-080923e5114f | -10.6528 | -49.47826 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57e51fb5-b0ad-3508-a261-03d33e70c679 | -13.77985 | -54.31776 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aafc5461-9e81-3741-961a-645a2ad42524 | -12.07201 | -47.338 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d92ba0c2-2aac-3392-87c1-54d5038a13b6 | -11.79394 | -42.63908 | 2025-05-23 04:04:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c722bfd-8a06-318d-bd74-4156261a2c95 | -12.33619 | -49.9846 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 541f5791-fab6-3cd4-96ba-2434e06dbac6 | -8.71874 | -50.25545 | 2025-05-23 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06a80d7c-b7d2-38e2-b801-5503b81661ee | -12.72421 | -54.97926 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7f49a9c-429f-30b2-af04-6a77a4c418de | -12.3367 | -49.99275 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34fe7fd6-411e-35a4-a885-8a61a669afa1 | -12.27883 | -44.60064 | 2025-05-23 04:04:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb85feb4-9a21-382c-931c-90738d46b5b3 | -12.29094 | -52.49858 | 2025-05-23 04:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 248f2118-333a-35b4-97ee-0e789516229c | -12.8472 | -47.38762 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 100e8eed-7dc7-341d-9b2f-41a4084387ab | -9.01982 | -47.7523 | 2025-05-23 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d709a9a-ef79-3b4f-beee-110974785267 | -12.33729 | -49.98967 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4601acc-1bab-3f5a-aa29-795c4c53567b | -10.49346 | -42.41145 | 2025-05-23 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fc3a8fae-c580-39cb-973c-0ea30d989df5 | -12.13435 | -54.66423 | 2025-05-23 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba04db0-4c46-3b13-839e-460cb79f6f23 | -13.98996 | -56.02048 | 2025-05-23 04:04:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4c958e33-2239-3545-8f3e-b609ec00b90b | -12.84647 | -47.39163 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d33225f0-4c79-3afd-9537-d971c40de972 | -12.84222 | -47.39081 | 2025-05-23 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7541792d-ff86-3d38-952e-c0e90fa208de | -12.07555 | -47.34285 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 975c3877-3b79-365c-af08-7799749c5a4d | -11.55979 | -47.44735 | 2025-05-23 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3471adc9-b9cc-3a04-bf95-8d8ebb01b3a4 | -10.64771 | -49.47739 | 2025-05-23 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81fb87cb-d136-3850-80c0-57f2e274aa07 | -14.04744 | -53.38194 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6f80f51-ac9e-3602-9c74-32476823dbcf | -12.41822 | -49.98063 | 2025-05-23 04:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d0ee708-fc49-3616-bc13-fd0534c91a16 | -20.57931 | -44.57421 | 2025-05-23 04:06:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0c20578-ced3-30c9-9149-7deb49b2c33e | -20.85324 | -53.75059 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb4792a9-4332-3793-8401-2813ef5dc499 | -17.3339 | -51.90357 | 2025-05-23 04:06:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dcdd559-5745-3cb1-be79-65696b673dea | -20.8541 | -53.74665 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27387867-9f94-3bae-925d-eae88ec34e01 | -22.69725 | -43.34721 | 2025-05-23 04:06:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d9c0dbc-b1c0-3f6d-8823-13a0e889119b | -17.68242 | -46.82454 | 2025-05-23 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 044a4e1b-36bd-3602-b2e0-9b29c862abf5 | -19.71666 | -40.35322 | 2025-05-23 04:06:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58e68ba2-883e-38f3-83ef-a94b9a4f17e0 | -17.59132 | -43.19651 | 2025-05-23 04:06:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9720cf5-dda6-344c-9b95-95e110de69d4 | -17.75207 | -42.89561 | 2025-05-23 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cde1f5dc-2659-3262-bdf8-da84889b9c8a | -19.9675 | -44.21465 | 2025-05-23 04:06:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4dfe6c2a-460e-3add-8b5b-b0957825b005 | -21.63099 | -45.27634 | 2025-05-23 04:06:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2061bbf-baeb-3cee-bcb2-e72ed2ec8ae5 | -16.68121 | -43.88576 | 2025-05-23 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9ba0848-6e90-3933-9940-21de4618605f | -19.51078 | -44.27668 | 2025-05-23 04:06:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f12a9f72-1dd0-31aa-b538-e29bfad3034b | -17.59466 | -43.19708 | 2025-05-23 04:06:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24d93f46-da51-3f12-b815-f3fc5c15e0bd | -22.78015 | -43.04259 | 2025-05-23 04:06:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1e64d71f-094a-3419-acb3-590fc52c4ae7 | -19.45139 | -45.30452 | 2025-05-23 04:06:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4489960-e546-3aad-9f95-0f7d89646362 | -15.26348 | -51.48229 | 2025-05-23 04:06:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74a26a3c-020c-3104-b029-7077b0f5d5fd | -17.9149 | -45.52895 | 2025-05-23 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb4281ac-d363-3ecf-b208-e64e0e7fe0d4 | -17.57662 | -47.48617 | 2025-05-23 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac759bda-dbb5-305e-9c9a-24c2f5a9f2e4 | -22.33395 | -41.77057 | 2025-05-23 04:06:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 62f35995-d9eb-3a8e-9d59-0916c907f78a | -17.67169 | -47.53182 | 2025-05-23 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 113f00d4-8ff5-3871-937c-4247ae01a460 | -22.49471 | -43.51195 | 2025-05-23 04:06:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99369812-c32d-3a37-8aaf-6bc2531ed6dd | -17.67563 | -47.53266 | 2025-05-23 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfee9b68-2066-3511-a522-486f658f6608 | -20.85788 | -53.75577 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c645f067-fa6a-3fe5-90d1-3cd62b8f5a31 | -21.63089 | -48.33993 | 2025-05-23 04:06:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21fcaa62-1005-3623-b260-13543c226522 | -17.59913 | -42.83596 | 2025-05-23 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 500cd051-f0a9-3be2-8229-3cba398c954c | -19.05236 | -53.4567 | 2025-05-23 04:06:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc38c856-757d-3815-a879-90a3dfc014b9 | -17.91419 | -45.53312 | 2025-05-23 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd34ed70-083c-376a-9e62-b747609f898c | -22.55727 | -42.21965 | 2025-05-23 04:06:00 | NPP-375D | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 241ed79f-1acf-37ee-b613-821300dafdce | -15.2688 | -51.48344 | 2025-05-23 04:06:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 975784c8-279e-3aea-aff7-b87c84ab9f04 | -17.77983 | -42.80714 | 2025-05-23 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ad75849-7feb-3231-b3af-11787e970cd8 | -20.85238 | -53.75453 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b87ab8fd-e23f-3c4d-b53b-dbdd17d70114 | -16.68123 | -43.88492 | 2025-05-23 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6af7e088-6d41-3c50-8327-407c1df9dff7 | -18.5497 | -40.06384 | 2025-05-23 04:06:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e42e2642-b3fe-3ccb-813b-fd329f1a9f86 | -16.01485 | -53.19765 | 2025-05-23 04:06:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d9e1212-a0a2-33dd-a259-b855c6a13bf5 | -19.94509 | -44.71384 | 2025-05-23 04:06:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7058fde-b50e-3561-a455-6936d730d36b | -20.84772 | -53.74938 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86cf2d44-1dd4-3981-881a-501fd87a17eb | -17.67663 | -47.5273 | 2025-05-23 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f700cd2-aed3-3067-a9f0-0a176b2e3ae0 | -20.84859 | -53.74542 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f444668-a80b-33ea-9fb6-21467362bc7e | -19.79074 | -53.83735 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 693556f3-3d4c-383f-a603-77758fec3b19 | -21.6262 | -43.46794 | 2025-05-23 04:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b05435f0-b531-3f14-affa-7296b78b9824 | -20.85873 | -53.75186 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a91c23fc-c8b5-3c7f-9be9-e8e8a90787be | -17.57958 | -47.48409 | 2025-05-23 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec5e6f5d-9f81-3b5e-b91d-108a9a62dc2c | -20.41669 | -43.55295 | 2025-05-23 04:06:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 07f4c4b2-1531-325c-baeb-dc7be526677d | -19.71725 | -40.34903 | 2025-05-23 04:06:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 121a31b1-ca5e-3d12-956e-f11d8f394753 | -18.33853 | -45.5911 | 2025-05-23 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13b97376-5ab6-3a73-8e9f-3c7a34203d4b | -16.70107 | -48.17263 | 2025-05-23 04:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c152067f-2265-39d1-9e71-2ab01c2faa13 | -17.77764 | -49.06488 | 2025-05-23 04:06:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b7f9414-7710-3168-9f34-cfa85437ebee | -19.79722 | -53.83489 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63ec7769-d085-3c69-8852-0180591941aa | -20.06635 | -42.24377 | 2025-05-23 04:06:00 | NPP-375D | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ca2bd476-7ee8-3d8d-8f1b-7d14aed0230a | -19.73251 | -54.50877 | 2025-05-23 04:06:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1efb5e5f-264c-348c-b056-b637b3a5a4ef | -15.26949 | -51.47995 | 2025-05-23 04:06:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README11.md)
