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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2253e4e5-702f-3bba-a11a-2bc4f6969d17 | -20.33634 | -41.4436 | 2025-08-07 03:42:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 458094eb-013a-33a7-b028-10223aebe340 | -20.09265 | -41.38873 | 2025-08-07 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 80bd320f-40db-32bf-a02b-7bb80985a681 | -18.8426 | -47.05132 | 2025-08-07 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a13ed8c3-c2c0-3ef7-88e8-74c7cb3fd496 | -19.64273 | -45.45016 | 2025-08-07 03:42:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7721273f-0e96-3b1d-a450-58625243a216 | -19.84312 | -49.078 | 2025-08-07 03:42:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fddb07e-1448-3e80-8dd2-594c4426a065 | -19.68449 | -44.90292 | 2025-08-07 03:42:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72e318e6-939d-3ff0-8cc5-5fca64d6a5d4 | -19.8493 | -49.0797 | 2025-08-07 03:42:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3a0b81f-e22b-3a63-80ae-dcba6b0937ee | -19.34687 | -44.30698 | 2025-08-07 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb7aa7ee-5378-3bbf-b2fd-a2859d1f4010 | -18.84363 | -47.05372 | 2025-08-07 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d8e0003-cad8-3d3f-94de-914dfdc9e9d5 | -19.84808 | -49.08496 | 2025-08-07 03:42:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc899a65-5a82-3a8c-b7c9-d26446ac2b11 | -23.6428 | -51.62951 | 2025-08-07 03:45:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 2a4a8bc5-cc71-38f5-90e1-c809ddc29f1f | -23.64047 | -51.62951 | 2025-08-07 03:45:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 3d73b4ed-496b-3687-9946-9fd4d593368b | -23.64196 | -51.62362 | 2025-08-07 03:45:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2bcdf6a0-fe5b-3024-83d8-e2893cfed6c2 | -23.64433 | -51.62357 | 2025-08-07 03:45:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 71ee0225-69bb-300c-b072-d9fdf622b10e | -23.64694 | -51.6319 | 2025-08-07 03:45:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| f0a6d992-5971-3f5b-a839-3be81f4fa801 | -23.64841 | -51.62604 | 2025-08-07 03:45:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 73ce4e7e-c43a-3318-a94c-ca3a8c0a9236 | -23.7202 | -51.7411 | 2025-08-07 03:50:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 0fea9e1c-ef4b-329f-a923-92e889dbbb1d | -7.4074 | -60.0108 | 2025-08-07 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 529d185e-b2d8-338a-a308-7928a2edea62 | -8.9041 | -60.5577 | 2025-08-07 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 702797dc-4cf7-37a6-ad34-7c8a0c603071 | -8.9212 | -60.7681 | 2025-08-07 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 1db6f96e-86be-36b2-9af2-6fe433994caa | -6.5382 | -45.5675 | 2025-08-07 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| dda9dcd6-4ff3-325d-a2a2-a0e95de65620 | -10.625 | -44.7439 | 2025-08-07 03:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| e09853a4-4233-373b-acf4-3ffdee2f16bd | -10.6441 | -44.7413 | 2025-08-07 03:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 53af07c9-6a81-30a4-83c1-fa42c2d0ca78 | -8.9213 | -60.7489 | 2025-08-07 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 341d0b0f-065b-3a70-9429-c580c576be9b | -6.5194 | -45.569 | 2025-08-07 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4aafae07-9cb7-396b-bf1d-31d12145ee2d | -23.7209 | -51.7182 | 2025-08-07 03:50:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.4 |
| 20c9ef9d-5557-3eb0-adeb-ee6ba88e4345 | -8.9215 | -60.7297 | 2025-08-07 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 6799df81-9cfa-3d45-929e-2c6edf98f6ad | -6.5192 | -45.5915 | 2025-08-07 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 4bce9cb4-c8d4-371a-ad91-a48622129055 | -6.5194 | -45.569 | 2025-08-07 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 0bdf1c08-aef9-3c64-85f6-00c714d21240 | -8.9213 | -60.7489 | 2025-08-07 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 57125dbe-3e09-340a-9480-b4ea3d637417 | -8.9215 | -60.7297 | 2025-08-07 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| bf8af3de-2286-3f6b-a777-e6f3945c2eff | -7.4074 | -60.0108 | 2025-08-07 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5068cea5-17df-329d-9342-5226ae6ac41e | -8.9399 | -60.7481 | 2025-08-07 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c05248d4-53f5-332f-9a43-4e98516e0f67 | -6.52854 | -45.57396 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 5fc3e360-fcba-30cd-8156-32c1c69413ba | -3.51755 | -47.21452 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4acdc7bf-7057-3d84-84e4-20a1d9262702 | -7.81232 | -45.11833 | 2025-08-07 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fe742e6-d91e-3b35-9afe-d09807a1e709 | -7.32786 | -44.69719 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25d5d927-f0e1-36e1-95b5-94e36a77ee2b | -3.82149 | -41.55241 | 2025-08-07 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a2c0bfe-03a2-30d2-8596-08599ff93d29 | -7.18331 | -45.47882 | 2025-08-07 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a68c8c5-f577-3509-be5f-16742b832ed4 | -7.80751 | -45.12275 | 2025-08-07 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 309ba0e4-abbb-3467-b384-3a8868736543 | -5.17003 | -38.11422 | 2025-08-07 04:00:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52dfe1cd-f6f6-3910-9c2a-f9b8527cf869 | -7.18614 | -45.48686 | 2025-08-07 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6dd591f1-c71b-386d-8921-0f348adc042f | -6.83589 | -46.3964 | 2025-08-07 04:00:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dfa1a9e-04c2-3150-9479-041c8114b348 | -4.29993 | -48.07953 | 2025-08-07 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3985c649-1bb1-3e08-9dd5-49c4b264af55 | -6.41099 | -53.37505 | 2025-08-07 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6311347-c86f-3e49-b32b-afa44be9ca08 | -4.02824 | -48.06851 | 2025-08-07 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d2d5f5c-23d3-33b7-825d-e102708203b3 | -7.5845 | -44.89463 | 2025-08-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5403198-3c5f-3bf0-b9de-a5d8bda7cea4 | -6.51675 | -45.56799 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a3454a6-a2f0-3a1b-ae8c-17f4a55413cc | -4.77772 | -45.32758 | 2025-08-07 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33bacf6d-f9b0-3e52-82e3-72271323c82b | -4.65041 | -42.5019 | 2025-08-07 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 58f7ec99-06f5-37dc-b574-0321e436f78c | -6.49687 | -45.21775 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7c9a8e2e-9571-37ed-8609-99a990eb3c86 | -4.31524 | -48.0822 | 2025-08-07 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 50fc9bba-1ef9-395f-9491-34f5b14c3d1d | -7.36403 | -44.62341 | 2025-08-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34772b06-c675-3aba-9dc1-41e3f6b41daf | -3.51601 | -47.21089 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1a24b87d-1436-368f-a0e0-924e3d3f206e | -6.52374 | -45.57708 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9c26d1bc-7f22-3bc7-89b5-0bdcde43a8f9 | -6.52308 | -45.58096 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7fc35eaa-36b0-3b51-ac03-1d98de246b21 | -6.52026 | -45.57244 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd363a19-0224-3229-a289-2fab1b2f968a | -3.84515 | -47.75512 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f1f9c78-2a90-3ee7-8c01-f58817920c0a | -3.6505 | -48.32386 | 2025-08-07 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13c9261b-a1ba-3d9c-a318-a13dd4fee29c | -7.32707 | -44.7019 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce057aa6-49c7-3887-8b78-f6a5cba816b9 | -7.10929 | -47.83931 | 2025-08-07 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc484f5b-1fd2-3dc2-96ed-fc15b46a9460 | -6.37775 | -39.25101 | 2025-08-07 04:00:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 58d093d3-1319-3386-a250-878a1bc5e5e8 | -3.84606 | -47.75344 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73086cec-73a4-3034-bf95-689dca5cfd6d | -3.43119 | -39.04522 | 2025-08-07 04:00:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73111a20-825a-30e3-bada-7f63934a99fb | -6.44261 | -46.10658 | 2025-08-07 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c967cff-03e5-31a3-9c59-94251385e14b | -7.19083 | -45.48396 | 2025-08-07 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f36f02b4-d6bd-3028-bd0d-07f0705c33b1 | -7.75884 | -43.595 | 2025-08-07 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83f48ebd-df8e-30b9-8474-d9d36f5c8651 | -7.11322 | -47.84507 | 2025-08-07 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64184108-d766-31ad-b8fb-26e1543a105f | -3.6502 | -48.32407 | 2025-08-07 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b72b0e6-a24c-34d2-bf49-7f9ef51cde22 | -6.44188 | -46.11083 | 2025-08-07 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b856110b-490e-3d7d-b900-8e7f8d99ae27 | -5.72593 | -49.10473 | 2025-08-07 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77f1d143-02aa-3a75-82c9-487354bd8929 | -3.84558 | -47.75637 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4fffcbb-95d3-38e6-a635-203305233dfb | -7.18676 | -45.48318 | 2025-08-07 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 90c01ba3-5919-3e41-931b-1c14dbc51849 | -7.89156 | -45.07618 | 2025-08-07 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2831a71a-6b84-30f7-b87a-cb445c086193 | -6.5196 | -45.57634 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a4706bf-c4dd-3e85-861e-36e7de1583b9 | -7.85417 | -43.86039 | 2025-08-07 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f428d4-0c33-3794-9f7a-4c377388dad7 | -7.94216 | -43.89402 | 2025-08-07 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f80f4471-2cdc-301e-a0a6-f1093a4792a4 | -8.32967 | -38.09058 | 2025-08-07 04:00:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d4e04674-a3ae-3fe0-8f9e-661d40cd633e | -7.36901 | -44.15211 | 2025-08-07 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 001a9abf-52a1-3422-a54c-ea6db864b1f7 | -7.1141 | -47.84002 | 2025-08-07 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0137770c-8ac2-3de7-8d46-84f6958eb314 | -6.5205 | -45.59621 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49926c5f-6c9e-3ab7-a98b-2acc1ff7003e | -5.7265 | -49.1014 | 2025-08-07 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ca3bd60-2313-333e-96c1-43fed01e9f2e | -7.23375 | -44.63483 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78838a4b-6da6-322b-ba06-0ad39bec9faf | -3.82089 | -41.55615 | 2025-08-07 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09a16775-cfd8-3bf0-833c-b204b3a1304d | -6.51894 | -45.5802 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 666c9093-90ad-34d6-8f68-a7c5ad17013f | -7.36421 | -44.15358 | 2025-08-07 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0df702df-5250-329a-9983-557933d01586 | -6.52114 | -45.5924 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f56f78b0-9f95-3229-a2fe-b33cfaa25d70 | -7.23682 | -44.64021 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64c113fb-5a4b-3420-aba4-d00c8b99fe18 | -3.42792 | -43.15342 | 2025-08-07 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faf0484e-aff2-3fc5-bdbf-d2da3d912f5a | -7.14665 | -44.08501 | 2025-08-07 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78380499-7182-3de2-bea3-67e948ed42b9 | -7.18739 | -45.4795 | 2025-08-07 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 449f4e4d-0d23-30fa-b0bc-4c22809a724a | -7.36346 | -44.15818 | 2025-08-07 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6835cb1-cac1-350b-a346-44fef3758ed1 | -8.38562 | -42.26608 | 2025-08-07 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 42b0b668-ce33-3177-ab0a-7b367fe7b00b | -3.82132 | -41.57548 | 2025-08-07 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5394b22d-a328-38f8-a49c-785d5341941e | -6.83237 | -44.74956 | 2025-08-07 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b606f8b2-cb16-3c4a-8d38-a83bb58c12ba | -6.49745 | -45.21425 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18d1e0b1-5c32-3008-9542-694296bf6800 | -6.83276 | -44.74641 | 2025-08-07 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a564b60d-d41f-349c-b7ee-4534dda30901 | -6.53267 | -45.57473 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97010a6b-5d6b-304a-a243-714176f1a783 | -4.99279 | -37.33123 | 2025-08-07 04:00:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1cbedfe-e0ca-3622-9947-066881d40aea | -6.52788 | -45.57786 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |


[Clique aqui para ver as próximas entradas](README9.md)
