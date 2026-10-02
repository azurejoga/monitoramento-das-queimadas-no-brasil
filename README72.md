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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d1e49a-2e61-3447-81f5-46f63e31e2a8 | -3.00672 | -53.88094 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65635909-5556-3131-bffc-a9b659fddc4c | -4.26313 | -50.76116 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd4513b5-4846-3d44-810f-00365327b95e | -4.29813 | -49.09073 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce0b7f71-0823-393c-8c78-c0998bc8e18a | -3.26435 | -57.91525 | 2026-10-02 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b191efa-5147-39a9-8a40-32a1bb0db40c | -3.29887 | -53.85257 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54010dc8-b619-3e1c-9fdc-39ac954080ea | -4.89298 | -48.37598 | 2026-10-02 05:33:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12b82259-42a6-33fb-8348-447ec4e557b0 | -3.1382 | -53.75512 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7ae857dd-c14a-3a64-8ecd-291912c49953 | -4.27552 | -50.75228 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52bb3a66-f650-3493-9e77-9e7e96488047 | -2.57516 | -50.0007 | 2026-10-02 05:33:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43c61365-d72b-32dc-b690-228bcab2a2c0 | -4.69009 | -55.79463 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d6e4dd-4489-384b-9f34-fba3f068b76b | -4.30619 | -50.77746 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f104883-7481-3301-bcf2-415a535683b6 | -3.13388 | -53.75446 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b0063a44-7fec-32b3-83cb-5571f4413dbd | -2.90546 | -54.09521 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9253e56b-35bc-3582-b60d-2111f5441f35 | -2.84364 | -53.99054 | 2026-10-02 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f377c01-1219-34b6-8341-49320c007626 | -3.16142 | -54.0793 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ece6e812-f227-3018-b655-2bd87313a13a | -4.27184 | -50.78593 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e232fae0-1735-320f-b945-6771aa9a5a19 | -2.93384 | -54.16111 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47e54ace-83d2-3c73-99e2-581fc0a6e88b | -2.89822 | -54.08625 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ae9cfe3-d751-3c16-aaa7-da2f170f75ea | -0.40585 | -51.83971 | 2026-10-02 05:33:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8b2c8d3-8a62-3d7a-b3af-478ab1e03427 | -1.65528 | -55.21281 | 2026-10-02 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5611b9c-f18e-3a20-9561-a4f28da7e43e | -3.85144 | -55.80293 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcc82f15-944a-39a6-ba59-a9bfe970b225 | -1.46055 | -48.9081 | 2026-10-02 05:33:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 515ec6eb-ca3b-371a-b8fb-a510eef52216 | -1.083 | -54.11143 | 2026-10-02 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 931f2c41-dade-3ded-8baf-4ea336e5a3d5 | -3.28905 | -53.85931 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0dda112-9415-3581-b5ce-8e812fff78ad | -3.04221 | -53.87811 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 450afc53-739e-39e6-bdd7-c9ed95e77bcb | -3.13141 | -53.74154 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0168eeec-171b-32a4-8f1a-d272d345c166 | -4.28372 | -50.77127 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e08979bb-d0a8-3bae-a2cf-eb0a583e20e0 | -4.2603 | -50.74302 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2861580a-e85f-35af-b241-d2679e8c784f | -3.12955 | -53.75381 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f596e340-581d-3080-a890-705c6d07eda3 | -1.26961 | -54.56241 | 2026-10-02 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa7784a3-f24c-34b1-87f6-bea0a403f8b7 | -1.86632 | -54.88647 | 2026-10-02 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc3acc9c-b69e-3179-affa-e42e2d98d62d | -4.30028 | -50.78011 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8689904-9bd7-30f6-9965-ec29191f0b4a | -4.25875 | -50.75343 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 690a1075-b2f2-35f3-a80d-fc52049e4996 | -4.27779 | -50.77396 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86bedbdc-dbd8-315d-8624-6908e0aa564c | -2.92811 | -54.19907 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f0728fe-2219-331f-85d0-0d3f6fee2974 | -5.86394 | -53.48177 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2623731-610d-3b46-b563-5e976b83e766 | -3.49035 | -54.72638 | 2026-10-02 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8cb62ec-0806-3a26-91a2-b868e605a288 | -4.28112 | -50.75961 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e44e1dd-20b8-32ee-8d05-89c6c461784b | -3.2894 | -53.84341 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e2bebcd2-b125-3ddf-b4dc-b807edbb6a74 | -6.1505 | -47.46886 | 2026-10-02 05:33:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d5baa17e-672d-33ee-869b-84b4ac3ee007 | -4.28996 | -50.77504 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95660cc5-0b1e-3be5-bc86-69cfc5d997cc | 0.62811 | -54.40528 | 2026-10-02 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3836743e-bcd1-327c-a0b5-04cb3f5439d5 | -4.25384 | -50.7492 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74872f0e-6d32-381b-acb1-2a7edb2b0160 | -3.68682 | -55.48994 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0a0817e-1d86-37d2-a32e-fe79adbea89c | -1.26562 | -54.56183 | 2026-10-02 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| effa85e3-c764-372a-902b-110b2d262f73 | -4.27629 | -50.78391 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c77a16d-ce53-3c4b-846d-274ffc5f6432 | -1.63565 | -55.13676 | 2026-10-02 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db67b287-579d-389f-bd75-b66d61c83b24 | -5.27012 | -56.05163 | 2026-10-02 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c113f23-10c3-3032-8e04-d064b644baa7 | -1.48628 | -55.87229 | 2026-10-02 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b16065f-f8b9-325f-b397-d23fe01d6a93 | -4.19714 | -54.57431 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20e8e9b1-dbde-3c4f-ba76-7d104d9bb704 | -4.38721 | -54.82415 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d46c5e67-9628-3445-aec4-390e66d578cf | -2.39313 | -56.99054 | 2026-10-02 05:33:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22f36af7-f1cd-3fcf-af86-2c8d20f337e4 | -3.29577 | -53.8438 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a6bd2625-2ea1-3cb1-896b-59d520168543 | -5.87108 | -53.49714 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a2179f2-cafe-329c-8fe9-ede05eb46296 | -4.88662 | -48.37495 | 2026-10-02 05:33:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b12aa6-f7f2-30d1-930e-569be5464f70 | -4.27571 | -50.7588 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f262578-c047-3cf0-b1d9-6db3fdb47000 | -4.0144 | -48.9446 | 2026-10-02 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d331105e-ed6f-3eea-a5bc-5d5f4296731c | -5.92534 | -53.47975 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8c22f3c-35d6-31fa-ada8-31a39c0052b9 | -3.13883 | -53.75103 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 31f3db6d-7f77-3ae3-b05c-27d1c0ac6ee9 | -4.0426 | -54.23029 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50b76f11-63d5-3641-a95c-38a2666ff15e | -4.14045 | -53.94529 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1629884-024a-353d-aec3-14cf92c4c93e | -3.17233 | -54.09307 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 616b0dc1-6187-36bd-824f-c9693b137deb | -3.00733 | -53.87692 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fcd0bff-a2a0-3563-81d5-a5cc2baddd49 | -3.29026 | -53.85122 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe99d820-3602-384c-8abc-e004a3c2fd82 | -4.27231 | -50.78265 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99fcf0b5-537c-3cc2-812e-eb1c0b88ad88 | -1.34563 | -55.24432 | 2026-10-02 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21a4ee0f-0d1a-38a4-ac42-0f3c639e8141 | -4.4286 | -54.84829 | 2026-10-02 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1933dfa-254d-373d-9c4f-9404c87df76e | -4.61162 | -50.91799 | 2026-10-02 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c00698a9-a565-3c67-bb7d-0b8fcb98619c | -3.87843 | -51.89758 | 2026-10-02 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6a12b4b-0694-3ff4-8cdf-584a98bc029a | -2.9007 | -54.15328 | 2026-10-02 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede9a624-fe15-36d7-8aaa-8670a7b03a14 | -4.17282 | -56.34683 | 2026-10-02 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20be1e54-4508-3a04-9049-c47e30dee9e1 | -3.03854 | -53.87352 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92efc7cb-d98f-3dfe-9cc4-b232fe90a747 | -1.44482 | -60.26205 | 2026-10-02 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 493aa6cf-4de5-3153-92e1-aa0abe41d2f6 | -3.00774 | -53.23095 | 2026-10-02 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22926835-e6a9-312a-afe1-a467b5234b8d | -4.26081 | -50.73955 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5970d1e-fa13-38fd-b2e4-09d51d0a17d6 | -4.29637 | -50.76892 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 847acbf0-f845-3e2f-9c10-be0e01862f06 | -4.29391 | -50.78603 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e17f79a-9e7c-3a62-9078-ba0c5b7960ef | -4.28967 | -50.76852 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd272978-e6e3-3bfd-8209-8013009032b7 | -4.29507 | -50.76932 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d7da8be-063c-3375-b826-b2ea5e4b0328 | -5.8988 | -53.50011 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c54dcb2e-1189-3c7f-9b0e-d013acbf84dd | -4.35834 | -47.77468 | 2026-10-02 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1338818e-2731-3ada-ae48-2de37d43cfc6 | -3.85073 | -55.80763 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2f78b9e-64a6-39ad-8d9d-819a1ea7ffc7 | -3.29244 | -53.85214 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a03ab6b0-2357-3a07-928b-6e250f66a7db | -2.57572 | -49.99709 | 2026-10-02 05:33:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f59cd873-7003-324f-b7c3-652431ceff06 | -4.2714 | -50.77974 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a03ccc3-386a-3b50-9b2a-2f0c0f55e56e | -4.24796 | -50.75158 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2676dc8-a58d-349f-a400-2c84c8b40d47 | -4.25335 | -50.75253 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53c2e981-5f78-394b-bf57-f386ff523f2e | -4.2876 | -50.7822 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ba74da7-d3da-308d-b28d-f8192195997c | -4.26621 | -50.74047 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c440f5d0-b939-3d1a-9156-2ea6b03df0f2 | -3.57405 | -54.61681 | 2026-10-02 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9716651f-83ca-3c65-80ff-6e691fcf3a1a | -4.29455 | -50.77278 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 813bccae-392d-33c7-b7a2-e965e68dec02 | 2.16344 | -55.80324 | 2026-10-02 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e5f4c41-6a83-3a2b-ba5a-8167f6cc8630 | -3.84807 | -55.80905 | 2026-10-02 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e04d4314-383d-3214-9910-2abc4058245d | -3.73056 | -51.17815 | 2026-10-02 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 429e0e4c-f0d1-3eaa-b031-0bf801c69dd0 | -4.30568 | -50.78093 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6566f8ee-3752-3ed7-bb36-7a937fc984c0 | -1.26642 | -54.55667 | 2026-10-02 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 7bbd78c7-2478-31ca-809e-fcd5c34fb90b | -4.25285 | -50.75588 | 2026-10-02 05:33:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c4c5cc2-ea8c-37dd-99b4-caa4c174d0e3 | -3.1681 | -54.0924 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e414533-7918-38b4-bb57-baa6e004a9ef | -3.28715 | -53.84245 | 2026-10-02 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 07055431-3673-346f-b6ff-2b6254b68d0b | -5.89951 | -53.4953 | 2026-10-02 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README73.md)
