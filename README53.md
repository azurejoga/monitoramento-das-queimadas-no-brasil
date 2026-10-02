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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99002ec2-072f-3a72-a8c1-7302447c7e85 | -3.16509 | -54.10043 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3abf6fb-fd71-3e0b-8ede-81ebe42b150b | -4.26745 | -50.78029 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4bfb614-b45d-3bc9-bb6b-edaee308bd7a | -6.13828 | -53.29254 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8f291da-385f-316a-863a-0507a17a5dc4 | -3.00579 | -54.74809 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbdb24c5-c97a-3c1b-8e2f-88c9ea5a2b27 | -8.08156 | -54.88905 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fc90516-2051-3ca0-8727-d7d06a7cf557 | -5.98183 | -56.13793 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 469f7c8b-d771-31e9-a4a1-810f650031c8 | -1.60955 | -54.75574 | 2026-10-02 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7af5ba3c-e46e-3dd5-900c-3257d876800f | -7.33332 | -55.23141 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44e21edf-0b73-3a0c-8d7c-0039b5add293 | -7.56792 | -55.01667 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 628c35ef-cffe-32d4-b5b1-93a605a6c8b8 | -6.7042 | -55.5731 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f641ece5-3573-3049-949e-798f4e91543c | -6.89969 | -43.69957 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1344eb21-484f-3978-8b73-9756242b7198 | -3.01509 | -53.23326 | 2026-10-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebcd71df-0c6d-3112-9902-8b119352f1f1 | -6.14655 | -47.47264 | 2026-10-02 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dd97f1f-b3b3-3138-9e48-8c5e2e4ca8cc | -7.49193 | -55.00053 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64fc367b-bc45-3e73-9c2f-8e71e101c5d9 | -7.49804 | -55.02633 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1df285d9-aa1f-3d47-8c76-b8d3e2ced014 | -1.60711 | -55.13266 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df8e74da-e70b-32da-9236-94118e621896 | -6.83719 | -55.27071 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24137e74-fc41-36cf-b44d-14884be0716f | -7.57013 | -55.02412 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a839589-e8f6-34b0-aedd-fe6df1f3fe84 | -7.74553 | -54.79311 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23339962-e3fa-330b-960f-c940accbacdb | -2.95212 | -54.09143 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b420703a-c267-3790-9c84-36242e43c651 | -7.49302 | -54.9936 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5418ee2-ce85-3453-a7e5-3e0f799d8bf1 | -3.16225 | -54.07534 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 852e8de4-f2ac-314b-b9dc-f272d9c81d7d | -2.96917 | -54.09418 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adab64c4-83ab-3851-8955-e7c35d183c59 | -6.87557 | -55.56437 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01f1755a-b441-30b8-b032-e05a7c00cd28 | -3.16617 | -54.09355 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f5bdf6-0fce-3a01-a9c2-7ed7a8cf5cf5 | -6.24955 | -53.14667 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82b7175b-6be9-3715-a721-9782f1e38dbe | -6.90854 | -43.6785 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 80ab8427-656b-3b85-b7d4-0f346426f95b | -4.06027 | -51.12064 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7669116f-6200-349c-ba50-d82937ec296c | -6.23947 | -53.12325 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7039bc8a-ac57-3f36-a895-5e60c3aae1c4 | -3.81805 | -52.32932 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 081c7813-17d1-3075-9d6c-3e94ce883202 | -3.28568 | -53.85205 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a69665d3-ff84-3e23-8f3c-5dc904f044b6 | -6.08167 | -53.30851 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a3971cf-0508-3cc5-ac0d-321633b537db | -7.55362 | -55.02154 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01c7a1a6-4a21-3033-8232-ec035682f810 | -3.11689 | -48.59497 | 2026-10-02 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aff91035-6d37-3348-9fdc-b12b630a8c0e | -3.16117 | -54.08221 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a94d681-6c83-3144-b501-2c25a35d92a4 | -7.70203 | -54.76859 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eda59884-5b30-3b29-8bc7-0abe01a838bf | -7.25037 | -48.0624 | 2026-10-02 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 386fbb0a-255c-32f8-bbe1-369e94a665e2 | -4.63144 | -50.59929 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9500be0-ae93-3a34-9818-a21d45c04528 | -3.15841 | -54.07827 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b6e7b8d-3804-3024-9ceb-33cf0e78901e | -7.05072 | -55.64273 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c13dda-f989-333a-91ad-cb29767e54f9 | -7.41577 | -55.59294 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a9ca657-e990-318b-8cde-b54452959cc7 | -7.46665 | -55.01073 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4420eac-689b-3e58-baa0-a4d5fdf60f18 | -8.74307 | -47.58723 | 2026-10-02 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 783c2e42-94a6-37be-a660-e21a4a83b354 | -6.39764 | -56.41634 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4aad5690-b0e4-33dc-809e-d397905699d0 | -8.16387 | -54.83821 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc1c755d-150f-3da7-a682-dba8ee70677e | -8.01071 | -47.43593 | 2026-10-02 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e04e8fa-8d61-367e-90ea-d3e7da9a9f54 | -2.03288 | -54.29147 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11fb1b5e-8c25-3930-a575-4e6396283c9a | -4.30404 | -50.78174 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5913707d-da61-314a-bc13-963f6e3f419f | -8.23115 | -54.69349 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d00a6e27-565d-34a8-9712-f6bd59f29436 | -6.58933 | -53.01595 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a74fda73-1aaa-343f-9c3a-b0db5f33fced | -6.47388 | -55.52241 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cec12381-a026-3c57-89a9-05a7ce4cd515 | -8.06543 | -54.83685 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de6b27a0-c30d-3c40-ae87-977730734a92 | -7.41812 | -47.52099 | 2026-10-02 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bebc5ef5-184d-3ae7-bdfe-868d4967a65a | -7.33277 | -55.23491 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fcdbe8f7-1789-3be9-a0af-19855051a748 | -3.04428 | -53.8736 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65a9dbe8-3d34-3a5b-a546-32b3355fd581 | -3.0059 | -54.22694 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ebcf663-aa81-3da7-80ba-40d306541943 | -5.97739 | -55.37059 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42234f70-18fc-3cfd-b084-60c80e2aec32 | -7.8735 | -44.17278 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f719131-3086-3101-887e-c1de0c0abc20 | -3.11382 | -50.28574 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34c7623c-35d0-30e9-bfaf-8e1729bf7e51 | -7.39481 | -55.20914 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| fb5572f9-a6e6-38e5-b5cf-a193bcf16f70 | -3.14116 | -53.73471 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e52b133-7460-3a6e-b885-656f384cad3d | -5.99849 | -53.53932 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7a41a5a6-9a53-353f-b4ca-99628dbf9462 | -6.87613 | -55.56085 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e612ac44-6338-3f9c-b2e2-dbef0536f679 | -7.87914 | -44.18061 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cb6d6cce-98b8-3acf-8c76-1ef88893fa4c | -3.17554 | -54.09852 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fba04ce7-8131-366b-8cfd-1daf576af1bb | -3.01681 | -53.8764 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf694fbd-4855-3ae1-90e9-98e37fc7cfcc | -6.79381 | -55.54433 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 810a3025-520c-3add-8eba-0e6f2f1bd682 | -4.4511 | -54.90644 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30a7be3a-c358-3d61-a970-ac5b0b138007 | -6.1979 | -52.90108 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e2c749a-80b2-3b9e-b23a-283c1ecb5a35 | -8.25767 | -54.74017 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b597beed-f8cd-320f-9d93-c281777a48f4 | -3.1181 | -50.28208 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7f8f7bf-d13b-3796-a8df-688476d2c614 | -3.16893 | -54.09749 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 706927ac-e042-35c1-8209-007b2449e732 | -4.32406 | -48.63113 | 2026-10-02 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eaf1347-b170-3be5-8dcd-70c0f077c4be | -4.30045 | -50.78118 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 31c82909-1519-3a42-b8a7-e0bb5241f97e | -7.34613 | -55.58135 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6a9dd4f-ac55-3d89-adcc-edff365294b8 | -8.08924 | -54.88317 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d874c40-ac59-3453-bfe1-38fb14f181ed | -3.17438 | -54.08425 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 669c7cf7-d865-348d-bc63-9fcd4fe369b5 | -4.2765 | -50.76908 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc9b8d0-d900-3af5-beae-b17692f1224e | -3.28729 | -53.84175 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 21bf773f-4b48-3be6-b967-80f1feffa66f | -4.45164 | -54.90294 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4046676-c560-3ffd-b66c-46c92d0b3832 | -7.68554 | -54.766 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bca44489-a601-3bd2-87ac-954b21dfb96c | -3.29451 | -53.86043 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e6a702-0da3-35a8-b010-2a960d90fd7b | -3.42884 | -54.54581 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75067f31-7622-3358-9526-909b7682777f | -7.88463 | -44.17882 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f5fdb038-abfd-3b69-ac73-27795d006fbe | -7.03571 | -55.6295 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bedc85af-fcd1-3479-861f-126e2af73a1a | -8.1808 | -54.79476 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fdc3853-dbb5-3228-aaca-5c1aa94950ef | -7.0435 | -55.62347 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed5aebb9-f9f0-3486-b5f7-d6eaeae6a68f | -6.83775 | -55.26721 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b06c699d-d25e-3e9d-ad58-1102ed222e67 | -3.26923 | -54.00056 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b7b945f-5ada-391f-88a1-6c4912a40afa | -2.92936 | -54.19381 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f01fa20f-386d-37c0-8a6f-ad3fc5717385 | -2.90756 | -54.09513 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8541438-a45d-3afe-8741-41d6322412d2 | -4.26646 | -50.73773 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8ac1cb5e-8b67-3eed-a236-ea2f9aef67cf | -5.85812 | -53.4786 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2f4a458e-5515-37db-a984-29cdcdd59afb | -6.08222 | -53.30497 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e07b241-2ec4-3cca-b81b-78c77d31e3ca | -3.84929 | -55.80971 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1265c439-a65d-3f3d-86e9-be243fd48698 | -2.90277 | -54.14731 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c86f9671-8db3-3703-8c01-c7fd12d8cb07 | -6.84992 | -55.53511 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9bfc0bd-ef8c-36a0-a477-d7a06d485ab3 | -5.87242 | -43.59229 | 2026-10-02 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 66f24f35-ecd4-3eba-a3f0-1ab59c450e37 | -8.0114 | -47.43082 | 2026-10-02 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45b1acbf-d607-3e44-89e6-fc56f0a380f6 | -3.92519 | -55.37263 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
