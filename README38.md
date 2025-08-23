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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7637359b-5957-371e-a21e-2fdf0917ee70 | -6.67125 | -58.81464 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aff85d98-4957-337f-b790-8b30e5cc9a79 | -7.55738 | -63.85486 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64b936f3-c331-3a33-b60e-d732c2bda5dc | -7.43155 | -60.62854 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e7c4e8e1-7e6d-3e27-9e44-7758384f33d5 | -9.60262 | -55.34903 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4a11c75-7396-3b3d-a557-def8a6450da2 | -9.20548 | -59.61351 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a331bddd-9dd6-358c-b8bd-f5cc2c76fdb8 | -6.44136 | -53.3933 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62571848-6d7b-3f24-986a-7856b0daa384 | -6.26812 | -53.71346 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d01ce200-791b-3ef4-b058-29c1652ebe6d | -9.19242 | -59.63695 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3357564-f5f8-3779-b4ba-2a213f124a59 | -7.81388 | -63.5634 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab4e7f78-1c53-3fd4-a55b-c882b2fe8f66 | -6.38363 | -45.53294 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8725575d-f579-363a-ba13-1664e46e70b0 | -8.30142 | -47.2671 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f286c4c9-d5cd-3ed6-ba69-dc21820fbabf | -5.87604 | -53.63319 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26c96be4-41e6-3237-b8b0-3d6aa8a41ef8 | -9.20907 | -59.61845 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7ec6664-cfa1-32db-96ab-ccdef29376f5 | -10.64129 | -50.12922 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f63b781-6239-36b3-8a82-4b8fad435eaf | -7.13675 | -44.16768 | 2025-08-23 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13eefafe-b166-3601-bf3d-cc8e09d5fe8a | -7.81314 | -63.564 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba5695f7-f9a0-3bb3-9c7a-d074cd7d8ad0 | -7.6144 | -46.24765 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 51bbb41c-686f-3cb9-a01f-37dfe0dfd537 | -7.61118 | -46.27084 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c075fcab-ad60-3cfe-82ac-2bbb2227982c | -9.17643 | -59.6174 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed568a37-c9ce-321c-8f3f-b4705bc35784 | -7.03135 | -44.6453 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3354645d-5b15-3535-8ad8-2bc13f4d8153 | -9.18071 | -59.59227 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1a2a8af-b14c-3fc8-84e6-e19c80557f5e | -6.39038 | -45.51862 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 039cd137-16db-3011-ba33-317066a93674 | -7.30266 | -59.62604 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3d90d16-41c6-36ce-a52f-b59f1bffa935 | -9.16702 | -59.59428 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83e0e104-da0d-3038-b379-3db7ca850bd8 | -2.83299 | -54.56036 | 2025-08-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a18680c-1b56-3133-89e1-8faa2f4509e5 | -6.25982 | -53.67976 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08b78ca9-0edb-37ec-9936-d20088842a00 | -9.17728 | -59.66476 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88af218e-250e-362e-a723-b0af461ef672 | -9.2268 | -59.74739 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 024d6773-e15a-3955-9611-b2e7a382ce57 | -6.46179 | -53.39294 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c25bd8d7-a872-3e4e-a5a5-16fd2d2cad7f | -4.31342 | -48.09358 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88209715-0e45-398c-a6c2-4df5c98352db | -8.6624 | -51.27867 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bb394ea-4487-3d7b-8501-e99528360e11 | -8.44031 | -48.25715 | 2025-08-23 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b53d9ad-ecf1-3a83-a20d-df0e2e15b095 | -9.23042 | -59.75241 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ea9488a-379e-3f5a-9339-8a95965aa0c0 | -9.19753 | -59.46776 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b26cad2b-a5ae-3760-8305-1cf48b2edb6a | -8.2924 | -47.2597 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ac7fe90-5620-3577-b18a-80fc13cb5e9c | -7.80812 | -63.55888 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4544265a-8688-37d4-b1a2-970a51787c22 | -5.95084 | -44.13789 | 2025-08-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f60133be-b2ad-385f-b64f-641f4d184881 | -6.26868 | -53.70993 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 155ee2d8-6513-377e-8cf0-829c90c0d207 | -9.16269 | -59.59356 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76bc96da-57eb-3a33-94e1-474fdaf4aeda | -2.9334 | -53.69727 | 2025-08-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f47edd54-a58b-3468-baab-0b9ed86455fa | -9.16984 | -59.66338 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3ce5dd7-2239-3b11-81bc-a9214456e0d7 | -7.8706 | -46.28793 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1738fab1-ed87-32ec-8764-2a8f134226a2 | -9.23332 | -59.76164 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2513a8b0-c393-3887-9863-c42bce4b6b6d | -7.61636 | -46.26686 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79624fa2-4083-3779-a318-76784036279c | -7.2937 | -59.62463 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f08dd8f-3de9-3435-8f49-2106c8791a62 | -5.22704 | -56.02061 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 021d762f-95a8-3045-9e6a-7bd2f82f8fad | -8.29346 | -47.26173 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f0c5b8a-6a4f-3ace-9532-0fc5040efc10 | -4.30959 | -48.09301 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dcf5e85-319a-3bb0-93a8-bf242c1402d0 | -7.05642 | -59.826 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6e6b374-4f89-3970-a34d-31083c833c11 | -4.56162 | -55.96432 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9db792d-1bd6-3407-895b-2d6758d5dfb2 | -11.12161 | -44.751 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62be2c4a-0d98-33d2-99d1-db0877872670 | -7.82113 | -63.5565 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf39f19f-c579-3401-a920-7b234b444393 | -9.15765 | -59.59701 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58bdd6e0-e2b6-3e9a-a1e1-90cbaad224f8 | -9.20401 | -59.48155 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4436ad55-8fed-305c-ab6f-77b3aa3a339e | -10.68624 | -50.13144 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0d76fdf-8d34-3e3a-a0ef-bcc5f6921791 | -6.47747 | -55.87984 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9aad954-34ca-3145-98c4-a8f542ae9a8d | -9.61104 | -55.36179 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bb98347-a048-35d7-abac-2f11ff243861 | -9.19114 | -59.5939 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05c9af85-0368-36dc-b25d-1e0f1c40dc80 | -8.29666 | -47.26047 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f48bf5d-6cf5-3c0b-98eb-2e8885a62df9 | -9.60823 | -55.35754 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fed5005a-4d64-3abd-aca1-f444544cdd77 | -5.49058 | -42.15538 | 2025-08-23 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ada67d7-b28a-3fb7-8838-29ae9d808e9e | -5.92967 | -47.2936 | 2025-08-23 04:51:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31f1701e-9bcb-33ad-a342-f21cb0428961 | -9.87796 | -47.81264 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54291e4d-1caf-360c-adac-edec1adf7d0b | -7.10205 | -59.77691 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a12249f9-b5b4-3d86-855a-f8e3917fbb1c | -3.13607 | -58.04358 | 2025-08-23 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d04b8f7-7ea4-380e-bd24-226c94b6ffd4 | -3.28113 | -48.88238 | 2025-08-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a723690-999d-3b85-b670-41c2ff7adacd | -8.16107 | -47.30931 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 219f7ed3-bdbd-386a-b8e1-f6619d870ebd | -6.75679 | -56.8509 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f50b452e-4724-3819-902b-1c6319013914 | -5.83165 | -52.07165 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4fd89f57-975f-3e82-bde5-66ca8b7d3579 | -8.28861 | -47.26508 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f017a9af-cfc1-330c-8d1d-ed542ece245d | -8.62787 | -51.57378 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8483346e-2364-3b6f-9211-caafed7f78db | -6.63034 | -58.53935 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5b69000-7c52-3b7b-82d1-80e25e353347 | -5.82888 | -52.06769 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7101b97c-fa87-35cc-8702-64ce195faff7 | -7.79103 | -61.57346 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bc42be4-f56f-38c8-a881-e2fd748231d4 | -6.87831 | -59.81909 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4fb22d02-1187-3cfd-b5fc-9bd023b7b035 | -9.19676 | -59.63763 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6598f652-17d8-37ad-a690-07b00867c43e | -7.82034 | -63.55708 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8d29207-86a9-36a6-910e-2faeb4f8e100 | -5.75075 | -57.59662 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 307115c1-26c2-3542-b7f1-8fa73569b5b3 | -9.20881 | -59.44466 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b9f8509-d08e-3232-90f9-ab8caaabbcc3 | -6.37266 | -45.55907 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 03a9f689-705d-3e74-bc3b-0a1b5175a773 | -6.14883 | -57.71795 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aceb99a-6d4b-3d35-b20a-cc8005a4a797 | -5.8606 | -43.89052 | 2025-08-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e1ef1814-20ce-38ab-804b-5a091ee0498a | -5.9938 | -53.29748 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 165a496c-3d73-3242-be0e-9395b3d5034b | -9.19007 | -59.58956 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9d6fd3b-22d6-3552-b7dc-f7135e57d575 | -5.85625 | -43.89201 | 2025-08-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0a78e9ad-f585-3eb3-80da-81f6a8189ec9 | -9.59982 | -55.34478 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30e6f61e-f896-3c61-b5d4-0f7d96b1988f | -6.25649 | -53.67923 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70d862f3-9a64-3bff-8536-81aa646f7cfd | -9.19023 | -59.64929 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e75a3fd3-be40-348c-a9eb-567286f95553 | -9.18086 | -59.62658 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a24292b-ab5a-3ccd-81c4-fd896488a752 | -6.69015 | -58.85951 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e7fed37-e50b-3033-9f10-520e305c9dab | -7.81539 | -63.55537 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6d8d08b-9ccd-3afe-9343-cd79a8f80940 | -8.52588 | -48.83383 | 2025-08-23 04:51:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c70a076-873b-3af2-99f1-a72c151d0c01 | -9.07423 | -49.51577 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 960e9374-5fa0-3ba3-b322-dcf2c2ed34ec | -11.13541 | -44.76987 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1e62ea2-68a8-3da3-9f11-c6e1570ea6d2 | -8.68028 | -62.88101 | 2025-08-23 04:51:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53f0ef29-1c87-3e22-9879-c00f67321ad4 | -3.65802 | -54.75661 | 2025-08-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 914d7458-eac4-3a95-b906-86f878f25ba7 | -6.43968 | -53.38236 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3afc9d0-35ee-3c35-a5f7-90c55f76f2a8 | -9.8111 | -46.40003 | 2025-08-23 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b3161dee-31f2-3d3c-a029-58dc1444af1b | -6.4419 | -53.38982 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41c8a008-bfcf-385b-b127-7e3e06bdb5c0 | -9.20688 | -59.6309 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README39.md)
