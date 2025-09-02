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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b13ae2db-92ff-3665-a067-7e46d72767e2 | -14.58231 | -54.5566 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4604735f-c0a1-3d9a-ae03-721952846018 | -15.5743 | -48.3911 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b20edbad-4b9f-3ca0-a142-b25cc1020b6f | -15.57504 | -48.38681 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 47bd15f0-d62f-34fa-b496-a8dd73b4dd81 | -15.11669 | -48.18513 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6886c760-da97-344a-bf08-333b55a3c9ed | -23.50128 | -50.79539 | 2025-09-02 04:17:00 | NOAA-20 | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e1d78738-057b-30f1-b286-65caa11fdb48 | -14.19997 | -51.65792 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 84145a31-0560-385d-b3d5-176325b43c06 | -14.6154 | -48.03282 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43f7143c-b55d-34e6-98e8-9e3ca1cf7e50 | -14.1955 | -51.65724 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6c2f2440-ef73-31f4-b406-2c0c11ae8062 | -14.20271 | -51.66787 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0add4905-8238-371b-a907-e7d287c4aec6 | -14.79257 | -48.19411 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4caea28-f5a0-369a-bdd6-8031be0926b1 | -15.58864 | -48.37207 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0575b53-2bce-3c6b-8bcf-a75523d33b22 | -14.59351 | -48.04036 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd97759d-3da7-37a7-87f4-bc4cde71c1f3 | -14.78314 | -46.70686 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ca0101b-4ad9-314b-b269-387140ffd0df | -14.27354 | -45.25394 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36f8060f-0118-3cb0-bbcb-8de848a73176 | -17.14264 | -43.60817 | 2025-09-02 04:17:00 | NOAA-20 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47d889bb-18f8-36a8-b576-f1cb5d6a5eca | -12.91859 | -56.93639 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a81990ed-1894-3bfb-976a-d128d50e4737 | -14.61032 | -48.04094 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b350e904-2c9f-3168-a186-c4d57756f784 | -14.19912 | -51.66247 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1516fb22-6571-3fab-9707-f2a089ac89e5 | -23.50043 | -50.79999 | 2025-09-02 04:17:00 | NOAA-20 | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de8d5012-1cbc-3874-945d-7e0fe265675b | -15.97429 | -48.23956 | 2025-09-02 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24097e54-b16b-3cc3-8e6e-95073f33748a | -19.49956 | -48.04881 | 2025-09-02 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 536fc8c1-e6a0-3d44-9226-7800645cc7fd | -14.58516 | -54.55803 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54c02656-ec6d-3dd9-b96e-3e54a9449697 | -14.61968 | -48.94152 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd165920-beb5-309c-affa-06df3275792e | -14.73724 | -46.75258 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3979ec48-800a-3963-a237-89ac1059591c | -14.56917 | -48.96584 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb7bb631-ce96-30bb-875f-07a6111c9b46 | -14.22575 | -51.66779 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 083e83e9-2270-32d4-81fa-24123e073f08 | -14.9725 | -48.17724 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e627839-6526-329b-953a-18faaa1251ad | -14.49499 | -45.95193 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67d25743-ada8-3fd1-821f-4528d51abc74 | -17.23859 | -40.91853 | 2025-09-02 04:17:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36e856de-7f14-3db9-a068-59a2ceff75b3 | -16.28751 | -52.94147 | 2025-09-02 04:17:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aac67a98-8bbe-3e28-b77f-1ca8d57a2d75 | -14.7909 | -48.19218 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87bc8c9f-81ff-3105-9109-e7f8c6d74944 | -14.71686 | -46.74918 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7fbe591-e7d9-36a2-b167-744f6e15ee5e | -12.91679 | -56.93737 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14b2531c-08c5-31e1-b955-6069c6752b0c | -15.79906 | -43.56715 | 2025-09-02 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3752fc97-fe51-3f18-8394-f8ef2861dbc3 | -12.93323 | -56.96136 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 442dc96c-ddad-3946-a756-63ce858c11f1 | -16.28653 | -52.94658 | 2025-09-02 04:17:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b855c6d0-5edf-30bf-850d-c893f0ec3fba | -20.88478 | -49.03156 | 2025-09-02 04:17:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5a6ae7b2-068d-3dc6-96e9-9f44337defdd | -15.56936 | -48.35542 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f49214a6-9277-354c-983a-f18c98c49a6c | -24.14597 | -49.83421 | 2025-09-02 04:17:00 | NOAA-20 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e19f1eeb-6606-3a8f-8ba9-0837222c5d25 | -18.12322 | -44.99059 | 2025-09-02 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a56baa61-b744-333a-b12f-1e61aa47c751 | -14.215 | -51.65138 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fd14e3d9-f7e6-3876-8b22-c224f0fbe9c3 | -14.75523 | -48.15327 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa5946c-5855-362b-9fb2-aa117f3f780d | -14.20715 | -51.66877 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18fceee0-8b29-30d8-af30-d9fdd79f4780 | -20.11814 | -47.79321 | 2025-09-02 04:17:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7619341a-feb9-3340-9156-3ef6e1fc9d84 | -20.75835 | -45.20308 | 2025-09-02 04:17:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1329f820-a8c2-327a-b78e-b4e45bccd680 | -14.49224 | -45.94775 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d929ce15-1e3d-3ec7-bbc4-2035f367c40d | -14.79038 | -48.18523 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ad1c136-8d76-354d-8bc9-5a25eb8a586d | -14.77098 | -47.50014 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a50040d-79dd-34e5-83a6-8f94234ad659 | -16.04511 | -46.30421 | 2025-09-02 04:17:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c219407-3be7-3dee-b898-1f0dbef9b9ad | -18.12045 | -44.98637 | 2025-09-02 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae14191-aae5-3de0-9c0a-7c5383ed7c55 | -12.92312 | -56.9388 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db9e50fb-d8d6-3cc5-be68-fa5e6dabb8dc | -16.63095 | -44.59057 | 2025-09-02 04:17:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50c06984-35f8-3d45-960a-2b7fea83b48f | -15.80246 | -43.56769 | 2025-09-02 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20e29e1d-9e5b-3b07-999d-81d4dbfeb1a1 | -17.89366 | -47.1655 | 2025-09-02 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2af3669c-7c2d-37fc-9c66-c5b5967471ba | -14.57909 | -54.54475 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de6eff01-c02e-34fd-ac7d-77e9ecb4fef5 | -14.59287 | -48.06598 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b895b351-0ed7-35c7-8795-42badd12d59e | -14.20181 | -48.38281 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6af9991c-d9a5-3d86-b286-255cbcb1a328 | -14.5625 | -52.9994 | 2025-09-02 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add78615-6dec-3ff8-b598-8ebf34be2e5f | -13.32293 | -51.77108 | 2025-09-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94a84a7d-d3b8-399e-934e-ac59f217c208 | -14.78653 | -46.70745 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f20710f0-906f-392c-9fa6-bcc18e8a521c | -18.547 | -47.46584 | 2025-09-02 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82115fca-cc9b-3eec-962c-ff276d453164 | -15.1251 | -48.11339 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19d80c2c-ef24-318e-a56a-0a9529a3b001 | -20.12151 | -47.79382 | 2025-09-02 04:17:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2db1ce91-d900-34aa-b692-7fe4d2afd1ae | -14.49282 | -45.94413 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83b85360-33de-35f3-8db0-a4357959fa18 | -15.71599 | -49.02842 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da396df-5967-3a5c-a423-9071775d51b8 | -14.7887 | -46.7154 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fc19bfa-b3fe-39d4-97e4-d8a626f0467e | -15.69206 | -48.92545 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebd4448a-95a3-3a8a-94ee-d512d8f262af | -12.92524 | -56.99945 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dadbb151-4f91-3a28-8ede-859c9c218f2e | -13.89265 | -48.10604 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 072f8145-81f7-33dc-9bf3-4e3b05ec2bc2 | -14.62258 | -48.03379 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d24a64c4-b494-35c8-b4c1-b635ce496fe1 | -14.5816 | -54.56021 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2752378-56f7-3943-82fe-4064593b89b3 | -16.07848 | -43.61763 | 2025-09-02 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ed7f6b1-afe0-3812-93e6-1709ca1db8b7 | -14.79445 | -48.193 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af6a825d-1b24-348f-ae50-be7d20f11b3f | -15.72594 | -48.92672 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2ceb561-064d-32b3-95fa-dcb5cd6f57fb | -15.56588 | -48.33283 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52e3fa1e-7701-336e-8a16-3c6c4e3536d3 | -18.85307 | -47.33783 | 2025-09-02 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ee1e713-369c-3fbd-a48c-b04e5714a4c0 | -16.85828 | -49.57131 | 2025-09-02 04:17:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79a338f5-a715-3d4e-9536-06514415d94b | -18.38637 | -44.71138 | 2025-09-02 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2c876c6-6a6f-36ac-a57b-5055734d2f2f | -14.58129 | -54.54981 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66da27c8-6229-3b23-865b-45b9ae1c3c35 | -14.35319 | -47.09776 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85d5eaba-55b9-3fd3-b376-fc59c1b47047 | -14.59076 | -48.05664 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05604dd6-5261-3dc1-8302-d8f2a7a648f5 | -14.79426 | -46.72401 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d411769-4c4b-3480-b0dd-2a3620b0ded2 | -18.99868 | -46.65644 | 2025-09-02 04:17:00 | NOAA-20 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c91939af-88df-3376-8ff4-b3912197e6df | -15.56076 | -48.36254 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 864505c7-4c6d-3851-8c41-e9c198d5ddee | -16.2969 | -52.94295 | 2025-09-02 04:17:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 49462df6-ef38-3f87-abe9-6fb83c16ec35 | -16.41113 | -45.65185 | 2025-09-02 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69ce6961-9aab-3f2e-8884-93de6a4e9916 | -14.99042 | -48.31863 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 882c7f98-fa77-3b31-a02d-975cc57ad7aa | -12.91818 | -56.96979 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e6157ee-7746-3497-8d3a-2e2db66c7dfb | -14.00477 | -46.31508 | 2025-09-02 04:17:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7813df83-4926-3d8f-87b3-8db5541c9302 | -12.91411 | -56.95759 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85f06811-5e00-3150-ac0e-a33d0081dff9 | -14.75886 | -48.15358 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b542bf10-e635-39a6-966e-35d1ba8b7c8f | -17.17068 | -46.08691 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c67777d-682a-3d6c-a6b4-773415ac3393 | -14.55657 | -53.00428 | 2025-09-02 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c9810fb-332a-3615-8935-f759b4e9b4d2 | -20.29323 | -45.54565 | 2025-09-02 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 632fc62f-b3a5-3818-8382-bb9466b4f18b | -21.11456 | -46.85028 | 2025-09-02 04:17:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b72a6467-ff14-3c80-be98-92c94959a798 | -14.60674 | -48.04039 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef81fc11-56d6-3d93-81dc-d3b9ea487653 | -18.07068 | -45.95867 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a803fbbb-5bd7-34f8-81fe-7f27568ead63 | -14.7916 | -48.18815 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 480097bf-b7fc-3fbc-b080-f2e22cab8aee | -14.77316 | -48.15623 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c734ce4-10d1-388e-ad96-0edb770c71ba | -12.92457 | -56.97102 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README50.md)
