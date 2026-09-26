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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9453cb98-7c84-3dc4-85d3-951ea62a3726 | -3.00532 | -50.47328 | 2026-09-26 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 74a39794-a93f-35cb-9921-1b3b67081071 | -11.03048 | -54.04199 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f006fcdc-6ea6-3522-9c51-79b44e93ebba | -10.419 | -53.80972 | 2026-09-26 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 1ff481fc-ea7a-321c-b3c0-6bdb92ff0144 | -3.79876 | -51.01621 | 2026-09-26 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 7c05e1e5-c2bc-3dba-81c0-4a45d1849752 | -12.60304 | -51.95155 | 2026-09-26 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c7e357fa-e3aa-347b-94f3-2adc5e2822ef | -3.68816 | -54.25922 | 2026-09-26 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 01e98281-9056-39be-9720-65b6b0136fe6 | -11.99559 | -57.58937 | 2026-09-26 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f81ea269-55b4-3174-98a9-650f55818a39 | -11.03171 | -54.05101 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 0eeecce4-e65c-362d-aced-ddaa21fcf604 | -10.89845 | -53.948 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ece4ff9a-7a08-3992-afab-0c2f2cb3b1b8 | -3.42469 | -50.42533 | 2026-09-26 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 08d6d5c9-ade6-33e3-a778-f5aa8a9c0bd0 | -2.89614 | -54.19147 | 2026-09-26 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0c7d1ca-284e-3fa1-a075-183c41fe8841 | -2.99421 | -50.47482 | 2026-09-26 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 50a4f226-d563-315d-bb2b-f5d17c7da2c4 | -3.42383 | -50.43197 | 2026-09-26 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 5fa26ff9-3662-3545-be84-7da605c47233 | -11.04155 | -54.04379 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8746c483-c78d-33b1-9ffe-4fa30e1531c1 | -9.51172 | -54.65473 | 2026-09-26 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4a84267d-5830-36fb-b7af-c4f0dfc9c2c9 | -2.83959 | -51.38851 | 2026-09-26 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9e786707-7163-3ae2-891e-ea26ab4a1ef0 | -3.40037 | -51.87162 | 2026-09-26 00:20:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2dd9f37-0767-322f-9bde-93f908ba611b | -2.15737 | -51.98241 | 2026-09-26 00:20:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 0efdb263-ff2d-3750-a7db-487dfb11ccd0 | -2.9015 | -54.09884 | 2026-09-26 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e2427ab4-e32a-34a9-9870-9102862beb26 | -9.6412 | -55.13745 | 2026-09-26 00:20:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f594a840-23e9-3410-aeb3-e4011bac3f56 | -3.9863 | -52.03477 | 2026-09-26 00:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d15ad68f-7e78-3567-8576-5a487ba29f12 | -3.23648 | -54.32616 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b3daccca-af9c-364c-856e-4e6adfe4d8fc | -3.20404 | -53.4196 | 2026-09-26 00:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 843f4cc7-a181-302e-8b6a-7ebcd4b4c85c | -3.9803 | -48.43443 | 2026-09-26 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| efd676fa-e6e8-35c0-8388-232d61b5ff29 | -3.98783 | -52.0456 | 2026-09-26 00:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9974fbd9-4627-315f-b4f9-e77f459e1022 | -10.89967 | -53.95697 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57bd87b0-b9a4-34ce-b3f7-54188c07dc38 | -3.20142 | -53.40055 | 2026-09-26 00:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f789e28f-8843-3bc3-840c-708f09533792 | -2.97428 | -54.15619 | 2026-09-26 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de9261d0-a16f-33e7-ae0f-1cf5476f5d6f | -2.57762 | -54.74974 | 2026-09-26 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c446e31f-fba6-3a69-8608-fc6c084ef612 | -2.836 | -51.36363 | 2026-09-26 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 42021dba-9ecd-3bb0-88d8-05628a36ee47 | -3.80388 | -49.18419 | 2026-09-26 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a2b8128c-3228-3a6d-a77d-fd081c6e3111 | -3.21143 | -53.41267 | 2026-09-26 00:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a6bbf806-68aa-3b55-933a-7eb30afaf096 | -3.97892 | -48.42892 | 2026-09-26 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 83ec8e5a-19e2-38a3-a9b8-1ef4ff3786be | -10.41019 | -53.81098 | 2026-09-26 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c49daca-fdfa-36dd-b966-bd214db6a6e4 | -3.22638 | -54.31849 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 65463149-4024-3d3a-a209-829cbb91d899 | -5.6815 | -45.88013 | 2026-09-26 00:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 04e9b943-c230-3d85-aa35-887889f76935 | -2.15576 | -51.97076 | 2026-09-26 00:20:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1192563b-dd01-3396-b7f1-32e594d033ef | -3.87612 | -52.28203 | 2026-09-26 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| c259d65d-aabe-3a65-a44d-a606393e2f24 | -3.75967 | -51.80706 | 2026-09-26 00:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 50bec75b-4de3-3e9d-89fc-3409fb573cad | -11.27796 | -54.43384 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d58e27ff-2784-37c3-b992-3e6ab5e9fccf | -3.14326 | -54.57999 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48ae58b5-25d3-384f-8948-a05777847b5b | -3.73021 | -49.05531 | 2026-09-26 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dbcd1704-f86a-33cb-9026-4cd667b77742 | -12.59274 | -51.94357 | 2026-09-26 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 85dcd0e4-6bcd-3aa4-a0be-96490d581be6 | -10.61978 | -53.99664 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9b5c62e3-51f8-3466-9954-7d14a0493c3a | -3.22334 | -48.81694 | 2026-09-26 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| dfb83bb9-83f3-36b9-971f-f7bacde63ca1 | -3.42181 | -50.41762 | 2026-09-26 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8fbfda05-3afb-35e2-b695-89dd340e2216 | -3.8665 | -52.28342 | 2026-09-26 00:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b59194da-0f24-3601-8ffa-d62fb5033f8f | -10.89722 | -53.93903 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ad7b557-edeb-3dba-ba37-81e108ed964f | -3.30665 | -54.68863 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d1d204c5-61d9-3e73-96f6-2fcd227be07e | -3.07452 | -54.4091 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01c78f70-504f-34e1-8b61-affeede2a37d | -5.67786 | -45.87396 | 2026-09-26 00:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| af29f5fd-541c-3c6f-ab82-ce416248630d | -12.77045 | -52.82017 | 2026-09-26 00:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 66b4ddfe-51de-3ec1-8b10-aab27ccd1bb2 | -11.02285 | -54.05225 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 02b1dc25-bf01-37d1-b528-ebc6b1b5ac80 | -2.97392 | -51.0444 | 2026-09-26 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| acf714ba-e141-3768-b6cd-ad830dd937f0 | -3.71522 | -54.65179 | 2026-09-26 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d7dedc2d-edcb-36d7-b31b-f2e1831d42d4 | -3.50384 | -53.45827 | 2026-09-26 00:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fac42891-7cd3-30fc-9db2-214c48ad0eaa | -11.27918 | -54.44303 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1077145b-d514-3e1d-9a39-e955bab002b8 | -2.97303 | -54.14716 | 2026-09-26 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cba6de44-fc70-3d1f-9fc3-3aed512b6153 | -11.04033 | -54.03477 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 86be44ed-7c1d-3f4f-93d1-50939ad31adf | -3.07328 | -54.4002 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f3b2e872-11ac-327a-b687-518f4711d226 | -11.28812 | -54.44178 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 306d7a51-1797-3244-81b4-ea091f99c367 | -2.9696 | -51.05147 | 2026-09-26 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1fc5da06-7f7c-3487-bd04-0a2550b6d8b5 | -11.98479 | -57.59073 | 2026-09-26 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 45262012-5fab-3e7d-a33b-36f025e25565 | -12.76163 | -52.82148 | 2026-09-26 00:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| feef12b5-cd78-3f8e-ae82-06b6f79a67c9 | -3.20273 | -53.41008 | 2026-09-26 00:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9c2c4ac7-3759-35ca-8524-e961f7d18adb | -9.51295 | -54.66381 | 2026-09-26 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ac38b635-32a8-32bd-bd23-5defb445b730 | -3.26862 | -50.14478 | 2026-09-26 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 39b6c766-bb3f-3e6f-85bd-620f1611a64c | -3.09936 | -54.52307 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 434842b3-0a0e-3134-83f3-a0007b722191 | -3.22761 | -54.32739 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 124c2b12-cdfb-3e73-b529-0c3caccc6434 | -10.70732 | -52.50115 | 2026-09-26 00:20:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 71b0adef-9d09-37d5-b81a-f56f78a06499 | -2.91914 | -54.16074 | 2026-09-26 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 979a27d2-59e9-38fc-b64f-28bbbc11ac6b | -2.14727 | -53.71273 | 2026-09-26 00:22:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| f2e6ec89-b56e-36ef-883b-18ebf3169834 | -2.06638 | -56.87297 | 2026-09-26 00:22:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2e60ad66-794f-3580-ac6e-14371dc52b60 | 1.63365 | -56.04043 | 2026-09-26 00:22:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 839db620-fbca-38c9-8227-1eb27947c04c | 2.04806 | -50.97313 | 2026-09-26 00:22:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 49a04080-c376-3be4-b2e1-3f78759c8182 | -1.48403 | -55.85412 | 2026-09-26 00:22:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3d3a8777-4cd2-3f03-aa0b-396e3b63a3e6 | -1.13984 | -54.08973 | 2026-09-26 00:22:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 38dcaf96-fd8e-39f9-aa43-47c76d2454bb | -0.4927 | -49.15413 | 2026-09-26 00:22:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 176bd3d1-84bc-3ea9-9bf9-a5b5939850bd | -1.69392 | -55.56553 | 2026-09-26 00:22:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a700c1f1-f66c-3117-93f6-a965acfc83ab | 1.63245 | -56.04917 | 2026-09-26 00:22:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 137793a9-2549-3598-bfca-58802dc1a4db | -1.68512 | -55.56676 | 2026-09-26 00:22:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b36793dc-1800-3977-81d6-5ca17ab72a60 | -0.49406 | -49.16036 | 2026-09-26 00:22:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 10483e59-3ad0-3387-9192-dadfa511e694 | -2.15637 | -53.71146 | 2026-09-26 00:22:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 96cc4af0-9949-3594-86f9-cc58a871b123 | -1.34015 | -55.47869 | 2026-09-26 00:22:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 17db8257-fe1b-33e5-b345-12e7b3c9ae0e | -1.11706 | -57.0711 | 2026-09-26 00:22:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6bea3fbd-c34c-3b09-8acc-ff63603fdfe8 | -2.14859 | -53.72211 | 2026-09-26 00:22:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9f84518-b58f-3639-953b-fbc06cd4b199 | -1.33895 | -55.46994 | 2026-09-26 00:22:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 20744e44-5a74-3fe6-8d70-c78fc6eebcb2 | 1.1343 | -51.19265 | 2026-09-26 00:22:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c9d9b8e3-72d8-35aa-9acb-79ca361e8cef | 2.89512 | -60.28107 | 2026-09-26 00:22:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 70208c95-d97f-3cb2-aa01-0a053d2e41f4 | -1.48282 | -55.84532 | 2026-09-26 00:22:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d063fbe-2960-3baf-b0ad-93824577bc4d | -2.21684 | -55.41152 | 2026-09-26 00:22:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58a396b3-6404-32ce-936f-d8b343a237ae | 2.88282 | -60.29231 | 2026-09-26 00:22:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f603ee2d-da21-3d59-9b16-69bf70406414 | -1.19719 | -49.13301 | 2026-09-26 00:22:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ffb4a562-a975-3583-a0e0-ee220c24495e | -5.6943 | -45.8547 | 2026-09-26 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b8aa91e7-8f7f-35f6-a000-7ebd10a53d12 | -3.984 | -48.4297 | 2026-09-26 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 486e26f9-61f4-3577-ae5f-a853d2949269 | -14.7986 | -45.957 | 2026-09-26 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d4589ac8-fb86-327c-aafc-4245bab95f4d | -7.3656 | -42.0819 | 2026-09-26 00:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 0e7da7e9-53fe-3c5c-a4b5-d21d60883e3b | -5.6754 | -45.8784 | 2026-09-26 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 89d571c3-0662-36b3-a873-d6f4e6f6640f | -9.7612 | -36.0738 | 2026-09-26 00:30:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 138.1 |
| 94def00d-69ae-310d-b377-e8067391dc17 | -16.5732 | -43.9798 | 2026-09-26 00:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 84.4 |


[Clique aqui para ver as próximas entradas](README3.md)
