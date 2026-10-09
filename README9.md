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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a70950de-be78-3268-90cc-7ec722d504cd | -16.914 | -40.900002 | 2026-10-09 00:06:00 | METOP-B | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83e2d811-7108-306b-a942-9debdbc16437 | -4.284 | -49.088402 | 2026-10-09 00:06:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acbecd4a-f1af-3117-9926-977afac306cd | -8.2994 | -45.719501 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afeadeb8-b001-34d9-917e-d154d3ca598e | -4.7447 | -55.661598 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61e9d66b-e613-31ae-b638-15a0a8b5b3d2 | -12.0384 | -43.4412 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96bccd92-790e-331d-a16a-bd6f7a4318bf | -3.0771 | -54.2743 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad77492f-5eef-368b-896f-6517d5177f6a | -2.3609 | -48.882198 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35730223-ebc2-3e53-bf56-ef5e43809763 | -3.7291 | -59.425999 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7724674-e93e-3692-8d48-539dcc778dc0 | -0.6575 | -52.519501 | 2026-10-09 00:06:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2678c0f-1059-3ebc-b4b5-880121fa2676 | -5.4958 | -43.051399 | 2026-10-09 00:06:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8811d105-80d3-35b7-bd2b-e1946c829c5a | -2.7741 | -54.066299 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b35fe40-2c97-3079-9994-967d60c9157e | -11.3054 | -46.674 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 846179c3-c6cc-31a0-b2f2-0af995b04b93 | -2.8845 | -54.193199 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbc60742-8263-32ae-898f-e6b14ee5042e | -8.2482 | -54.710602 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d02b40e-192c-3950-96d2-ec51b8cea574 | -16.125799 | -43.7579 | 2026-10-09 00:06:00 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f8b69f2-db2f-39eb-9c78-1935dd9e3845 | -1.4709 | -54.761002 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4844a482-1edf-36bf-a3b7-1c89c25a26ed | -2.9433 | -54.180401 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 180f4437-30b3-31d7-8b6e-e07df73f4e73 | -9.3064 | -47.454498 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7209d1f4-3f32-35e2-9f51-4b55f4ab3beb | -18.081301 | -42.277802 | 2026-10-09 00:06:00 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b1fb78c-7628-3839-9ecd-4172f0eee475 | -2.9455 | -54.190102 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c98ff3bc-2d2a-3c77-97dc-930e503cd982 | -3.0284 | -54.101101 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af9c8a52-eb1e-3507-895b-e173eb251a88 | -14.3902 | -43.809101 | 2026-10-09 00:06:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9352fa80-caa0-3447-a1d3-4fd30f664acb | -11.7215 | -43.628899 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cae00053-8558-381b-8a25-ce39cf87efcd | -11.6225 | -43.603699 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ef3b4e8-d3e3-397f-8952-0c59842f330b | -9.075 | -45.106098 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ffe4ebc8-8316-3435-9b29-39cf89d0c8e3 | -3.0254 | -54.041401 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edd01de6-4ea6-3655-8860-11e7e3833911 | -5.7413 | -43.261398 | 2026-10-09 00:06:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81850c10-1bdd-3344-b16d-7a8ae3f02bb0 | -11.074 | -44.077702 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccb67faa-086f-3bb6-8caa-1612819f5dfc | -6.4808 | -55.280102 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1036e19-e217-3293-91f5-b0b88500d738 | -4.5695 | -54.9515 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c736f99d-3c10-31cd-b4fd-691c2344658f | -18.3857 | -43.471401 | 2026-10-09 00:06:00 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e12776aa-e339-3241-a4e2-cc1e0897d20a | -2.9981 | -54.750702 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0884c4e7-20f4-3732-b7a1-71432e5e4559 | -3.2274 | -54.303902 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71f70e85-1c18-3917-8642-e19aab234104 | -9.8561 | -47.4683 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c384dbf7-68df-37b0-a627-c3ac97e94657 | -2.9883 | -54.059502 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1013882-0f96-3762-af2d-469492e0c239 | -3.0186 | -54.103199 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed18399-ec17-3f93-b812-563e4f6c8f16 | -3.4558 | -50.580502 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb6829fd-625f-3a83-9a2c-dc3148ccd83c | -2.4658 | -56.045799 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c03b85bf-b9ee-322f-8106-1a4ae692c9b9 | -12.0346 | -43.381802 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 740b583c-234b-3ba5-8208-a6af3d81d1a0 | -13.5254 | -44.394402 | 2026-10-09 00:06:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea6169bb-fb31-3cad-93c9-03aeb70abfe1 | -8.9731 | -45.910099 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af9a714a-0751-303e-b849-e1bc00cf118f | -4.0899 | -48.959202 | 2026-10-09 00:06:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce6aae46-2ce2-372c-af90-2b8d5e25561f | -7.2627 | -45.3447 | 2026-10-09 00:06:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77e9dd8e-ed50-30a4-b861-c91bbca29dbb | -10.7071 | -44.492298 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 266bb753-663f-341f-9beb-7deaa1d4a44a | -2.5223 | -58.050598 | 2026-10-09 00:06:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85105206-0bdf-342d-92b6-584c7a51e3da | -5.8346 | -44.9272 | 2026-10-09 00:06:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfbb7757-5fe0-3833-94ac-cd35fd51e3cb | -13.595 | -48.584301 | 2026-10-09 00:06:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 98e2c953-207d-3825-9467-d41e932e1700 | -6.8059 | -46.444901 | 2026-10-09 00:06:00 | METOP-B | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06eb7560-fad9-3a2d-9b23-e88057f25ea0 | -3.5215 | -54.659302 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61e289e-0cfd-3c86-99a3-4c096429604d | -6.117 | -44.812 | 2026-10-09 00:06:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f683f937-fdf8-3a61-bb86-19c41dd5a6e7 | -2.9836 | -54.131001 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc035a38-8e4c-3459-8449-9a74c0f4f917 | -8.9283 | -45.140701 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d26ab27b-3934-3807-8f07-dfa1bffd681c | -14.5243 | -48.034401 | 2026-10-09 00:06:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13f3c1fd-4783-369e-90e3-7a50da97f545 | -10.8419 | -48.1404 | 2026-10-09 00:06:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2277f79a-16b5-3835-857e-c27b28df96ea | -4.532 | -47.052502 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8326785-957a-3bd1-a089-f35bc7589802 | -13.4101 | -43.730701 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4173b08-7d61-3c72-926c-4d769cc08bd3 | -2.8442 | -59.092999 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79b54d45-b544-3054-93fc-eb20386a9c1d | -3.0924 | -53.927502 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9c17ee-f5c3-3c8e-ac99-a35fde877965 | -3.2588 | -50.391899 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9343cfa-210a-3aa4-80f1-9732c7d3eae7 | -12.0159 | -43.476799 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0ab67e0-abc5-3dfb-ad66-18df54943861 | -8.7444 | -45.148701 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 656ce94b-18ea-3f53-9421-1b625e3b4098 | -2.9674 | -54.104198 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8363e348-18d7-3486-9c1a-f03f75c0e74a | -4.6568 | -56.197601 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01b4eb18-1b0c-3ab1-9c7e-a770905c9092 | -4.5793 | -54.949402 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd9dbbd4-20f5-3e80-b806-2316dcadf9c5 | -3.31 | -53.704498 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8522529-f72b-3ce4-83c5-197382548aa2 | -3.5924 | -54.654999 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8dfdfdb-582c-3b1f-9cc5-888745369e87 | -7.2022 | -55.168999 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf834934-4efc-3b40-8625-d2f5175f6eaa | -3.1145 | -53.795502 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d35a7bda-ea10-3619-a738-287c1fc4efb2 | -10.7747 | -46.6092 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e33c8860-914e-3fd1-844c-a7c35b6248ce | -3.5001 | -54.608799 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6650d3b0-8c60-3f77-98c3-dd5fd35bca91 | -11.8417 | -43.569599 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cf9f5bf-9195-3e2e-8d79-101bce243c05 | -13.2029 | -54.362 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c120bc7-4a95-3a4c-b498-530d768becde | -14.2546 | -52.7915 | 2026-10-09 00:06:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| facddc69-a225-3db2-b337-f6a476ab744d | -12.0137 | -43.4674 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d89925d9-8e79-340a-9aee-426655a229f4 | -1.4021 | -57.924 | 2026-10-09 00:06:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5d80742-a011-3a39-8980-a84d43d93015 | -14.4379 | -43.923199 | 2026-10-09 00:06:00 | METOP-B | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8446ea2f-caab-3ea1-87cc-8e7864826c42 | -17.6131 | -42.311699 | 2026-10-09 00:06:00 | METOP-B | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a7d5cc5-4a47-3667-a54c-2ef90d24ea9b | -9.0008 | -47.744099 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d595980a-acbf-3508-ad88-683f070ea175 | -3.3492 | -50.473202 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2609eb2e-b6d9-3706-bec2-ecd2b273a404 | -2.8824 | -54.183498 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 931fab71-33fd-310a-861c-5248a7624f52 | -4.2625 | -46.2836 | 2026-10-09 00:06:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9429fa83-09cb-3e30-9f25-c91bdba2424e | -11.8569 | -48.026699 | 2026-10-09 00:06:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 869aa6fb-5986-3f8a-ad2e-b6453f1e4860 | -11.7807 | -45.596199 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3522846b-07f5-33fd-9499-c072a00827f3 | -15.7879 | -50.1259 | 2026-10-09 00:06:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db7d5d03-62bf-38cd-9453-7f9ae3cf1248 | -3.4903 | -54.610901 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6b7e25-d4b4-3b51-977f-abba431e567a | -4.9012 | -48.763401 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e66cec86-23a2-3989-b9e6-f6f90e558307 | -5.3366 | -45.179001 | 2026-10-09 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fffdb94a-6eef-3d92-9380-d75f86a8e49b | -3.5602 | -54.6954 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1869ec92-d396-3903-8b93-3927c92ce297 | -3.0825 | -54.252499 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db1b1500-3c41-36da-8f19-35fc3819bad2 | -5.3464 | -45.176701 | 2026-10-09 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33d07d6f-fffc-3724-b8e9-b0cd280843dc | -5.0902 | -46.2066 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f940f49-fea3-3da0-b753-5dda071e8f22 | -16.521 | -42.507 | 2026-10-09 00:06:00 | METOP-B | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9255461c-6130-368f-913d-ba595d93f447 | -2.7549 | -49.529301 | 2026-10-09 00:06:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9a3ef51-2ac7-34c0-961b-3e12b026c892 | -9.6047 | -42.134399 | 2026-10-09 00:06:00 | METOP-B | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4b25208b-7d25-3ab4-8c67-083b8ceb51d1 | -8.1347 | -49.441101 | 2026-10-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3393090-bb38-3222-b858-abf109cec15e | -11.3968 | -46.667801 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce06f201-27ff-39a1-8be6-50542258e142 | -15.4441 | -45.681301 | 2026-10-09 00:06:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5101d214-9f88-3b07-8403-d87a783b1aba | -4.6403 | -50.948002 | 2026-10-09 00:06:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4723a4f4-2567-34a0-849c-d005e082c738 | -2.8403 | -57.459301 | 2026-10-09 00:06:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b3ebb97-8e93-3e77-b3e2-8675dd2b4481 | -6.9327 | -46.592201 | 2026-10-09 00:06:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
