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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa3c534-3b93-337f-b392-c75ea9598944 | -18.31755 | -39.92327 | 2024-09-28 00:24:00 | TERRA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7d43fb07-e0e0-3ec1-a367-fca03f17e35a | -18.29449 | -42.53779 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| c2dd5201-106a-3d71-b174-40961c75592f | -18.29193 | -42.54459 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 5155c4d2-c07a-37bc-9168-55539cea8a15 | -18.28304 | -42.16034 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.3 |
| 10f769d5-3aa1-34e6-a23a-c3789c3604ad | -18.28154 | -42.14775 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.4 |
| ecad0db0-5a13-3456-88b7-91817d8fafa5 | -18.26042 | -42.15004 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 05725f7e-3e9f-3953-9c8b-cd04bdbf11c3 | -18.14095 | -42.41356 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| 54325edb-dce2-3e58-9792-def9ca014ef2 | -18.13929 | -42.3996 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 2f64003a-49e6-3e65-b2a2-75b4f59bbf35 | -18.05559 | -44.39835 | 2024-09-28 00:24:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 93248169-1457-3e3d-96b7-b89a890678c0 | -18.05363 | -44.37992 | 2024-09-28 00:24:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 733e1718-a3b3-3d21-b74b-d195dee2d091 | -18.0515 | -44.38541 | 2024-09-28 00:24:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 150.1 |
| a2894be3-4b3c-3256-aad0-1e566ae89545 | -18.0494 | -44.36693 | 2024-09-28 00:24:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 4888d14e-3fd3-30e1-b8aa-a0efce307be0 | -18.02013 | -44.33062 | 2024-09-28 00:24:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1c4e9b68-4e2d-3a3f-b062-21639d6c6cf0 | -17.98221 | -42.30113 | 2024-09-28 00:24:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 5cceb8fa-ff41-3368-aeed-51da9fc4bf77 | -17.94813 | -44.24445 | 2024-09-28 00:24:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f97b3e31-6de8-3aa5-91d1-53862e7b0010 | -17.94493 | -44.25061 | 2024-09-28 00:24:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5628ec10-27ef-37b5-85d8-a2c143e05a80 | -17.91464 | -42.13969 | 2024-09-28 00:24:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 6e4c67c9-2312-3ade-ad42-b2a7698164f5 | -17.88313 | -42.14304 | 2024-09-28 00:24:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.8 |
| fc584985-0029-30da-a252-27d4d73588cf | -17.84592 | -45.89022 | 2024-09-28 00:24:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 33.0 |
| cef54d8d-3716-310f-b93f-6324fc14ed30 | -17.84222 | -44.48204 | 2024-09-28 00:24:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d0c656c6-2468-3e42-8d12-48480ad45fab | -17.84077 | -45.89603 | 2024-09-28 00:24:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 38.6 |
| fb66755b-9413-391b-a184-034df76d2830 | -17.80407 | -43.34164 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c3dd029e-9a86-342f-ae5c-85bd11664f13 | -17.80047 | -43.31065 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 741.2 |
| 43d40b6d-f165-3d21-af45-f71afd7bb498 | -17.79863 | -43.29478 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1938.5 |
| 44c610b1-160a-3269-8498-f50893434e2a | -17.79681 | -43.27913 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1046.9 |
| 3dad55ff-8a34-33ab-a151-09c70cd80294 | -17.79497 | -43.26329 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 57cf79f8-93f9-3840-a072-1b0c92eeea7c | -17.79266 | -43.34329 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9a625ce8-ba70-34f4-a748-9e73afb7e0f2 | -17.78908 | -43.31212 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 988fd19a-9503-3b9d-a623-960eb8ee08ac | -17.78726 | -43.29638 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1343.6 |
| 57cffaf9-3d4d-342a-9b6f-f82c97e277c5 | -17.78543 | -43.28053 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 3165a02b-06fd-3414-9f46-5dca13887218 | -17.78362 | -43.26487 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 40.8 |
| c6887804-b327-35d5-8eee-42e08b3f5422 | -17.7818 | -43.2491 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6bcbd35d-ccba-37d5-b2f7-8c0c4200c586 | -17.77766 | -43.31345 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 723a1aba-5b01-3f46-8aa8-e80b3b3d0cee | -17.77586 | -43.2977 | 2024-09-28 00:24:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 84103ad2-9e10-3348-b622-044da567bbe5 | -17.76325 | -44.33476 | 2024-09-28 00:24:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 73389808-fc89-3f0b-85e1-fb63c38004b6 | -17.76048 | -44.34134 | 2024-09-28 00:24:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a4bffecd-2b22-35aa-aece-2b1c1faba7e3 | -17.71655 | -42.33059 | 2024-09-28 00:24:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e533363c-91c2-37d0-8e32-e03d6f9cdfbf | -17.7123 | -42.33865 | 2024-09-28 00:24:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| cf088dce-f5d2-3050-87eb-e8e901d880b5 | -17.71075 | -42.32521 | 2024-09-28 00:24:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 1824b9d3-342b-3fa2-9c51-76ede60489c1 | -17.44482 | -42.62069 | 2024-09-28 00:24:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 99.9 |
| a1b7fdaf-9673-309c-96a7-c49ef0922094 | -17.44319 | -42.6071 | 2024-09-28 00:24:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 72d149e1-ba0b-30d4-b20b-d8a113c30d3a | -17.43406 | -42.6221 | 2024-09-28 00:24:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 46cdfc3f-9423-3fdb-b167-8994e800868f | -17.03797 | -43.23519 | 2024-09-28 00:24:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 26729354-8145-31a9-ba99-3bbaebadfe5a | -16.88118 | -45.33242 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7a4adf7f-f250-387e-9800-35c9a3cf2da6 | -16.82881 | -47.69284 | 2024-09-28 00:24:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 3ee5260e-c6ad-33cc-83c2-f3c7589c887f | -16.04301 | -43.61705 | 2024-09-28 00:24:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a384e36e-2656-3d4d-a3b1-b085263e8cd7 | -15.92847 | -47.37809 | 2024-09-28 00:24:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 365dd7e2-83e1-33ae-ab4d-b2d71976db30 | -15.92587 | -47.37172 | 2024-09-28 00:24:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 76bb7858-4471-38b7-a458-043dd547128d | -15.51181 | -43.56489 | 2024-09-28 00:24:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e990e7d9-3c38-3d7e-9cfd-d7f1ce66329f | -15.1912 | -43.84899 | 2024-09-28 00:24:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4a79194a-6d13-336b-86cd-ecd2e22e967f | -13.44633 | -43.78742 | 2024-09-28 00:24:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f069654e-8f6b-3a94-a15f-f3d09ecc3cbd | -13.44469 | -44.43196 | 2024-09-28 00:24:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 19a1f727-5195-3a65-989c-43e72117ed76 | -13.44456 | -43.77295 | 2024-09-28 00:24:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 979ffb0d-6945-3121-a960-a19386d9fe03 | -13.3821 | -42.04747 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cf302105-1f0c-3c40-a3bd-6c0e168c58b5 | -13.38067 | -42.03615 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5cd94420-6a5d-3402-812b-300af5ad647c | -13.37232 | -42.04858 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 6930a1f3-4c11-3ce6-92e9-723346c6b99a | -13.37086 | -42.03696 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 8439af75-6fb8-3eb9-9174-eec55aaeea8a | -13.37077 | -42.05497 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 24.5 |
| be5e3b54-b7ab-3395-bad6-1d674e7f5c21 | -13.36918 | -42.04304 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 8a99de77-3ed5-3b63-9a39-2bf4b64bebd5 | -13.35116 | -42.05705 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9f6938fb-a3b2-390f-8003-17d40784c0f3 | -13.34967 | -42.04561 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1cd26486-2f9f-3a4f-9051-c091e18e9701 | -13.34142 | -42.05846 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 64c80128-855d-3f71-bf18-8fd9f41410c4 | -13.33993 | -42.04702 | 2024-09-28 00:24:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2398ecce-2e3d-3155-b8d7-816ce62a0383 | -13.27577 | -46.33373 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4032dc07-65ad-3332-8ced-652918a6a497 | -13.27299 | -46.30897 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c1611421-f91f-34b4-844a-8d4ecbccb4ea | -13.26764 | -46.34109 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 80b4fe0d-4915-33d4-96fc-a59416de8af0 | -13.26482 | -46.3175 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 67656d03-7f52-3ec1-923f-4de62cdd6aa0 | -13.26473 | -46.35777 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| c82d2acb-807c-3472-980e-401df8ee6bb3 | -13.26216 | -46.33459 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 328.3 |
| 4b944a20-e760-334b-92ab-b409f5f6d0ba | -13.25945 | -46.31022 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 145.7 |
| af33d2d1-68f1-3d67-944a-cd8dada21d65 | -13.25101 | -46.31657 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| eb1b3edb-1b43-38fb-b863-61224e576e39 | -13.01537 | -42.22188 | 2024-09-28 00:24:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 56c62612-83a1-3e25-90fd-9c98a227f9f0 | -12.9902 | -44.75388 | 2024-09-28 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d93de27d-8765-3ad9-a4d0-4640886156d6 | -12.74588 | -43.48005 | 2024-09-28 00:24:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a5f842ec-110e-3c81-b514-8b7fa59c762e | -12.74423 | -43.46661 | 2024-09-28 00:24:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a4ba3a19-aea7-3b04-bf07-b70cb86b04c5 | -11.32733 | -46.23953 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 0b5ed330-7244-3c6d-afb7-87dc89b457a1 | -11.32546 | -46.23443 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 88b67d90-7bc1-3b34-a364-929af4a4de22 | -11.32473 | -46.21846 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4850e460-6dba-32b8-a107-aef584f8c42a | -11.27594 | -46.14153 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 321ee806-0da6-3e0a-9314-161cd638eb9c | -11.11702 | -45.58387 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9dc21f6f-6e4e-318b-941e-af8fc8d23349 | -11.04338 | -45.72849 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5a9928e9-5cb6-34cb-b19d-e903724233e8 | -11.04111 | -45.70989 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 8f19f316-8c8f-3398-8413-046aec3eb1ce | -11.02867 | -45.71125 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| fc0f6ff4-e8e8-3c72-bc4e-50fc1f0228d2 | -11.01626 | -45.7128 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6459038d-46bf-313f-b86f-c9debe6997b1 | -10.99751 | -44.43653 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 41d89889-0e0f-3efd-91c0-485b4907bf3b | -10.99563 | -44.42175 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7484ec43-e5eb-37ed-8d55-c260554a76c8 | -10.98631 | -44.43789 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 37fadc35-c539-3dd6-b615-0aa4115b25a4 | -10.87631 | -45.51533 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6b665a87-ba03-3875-b96d-42eb077e257f | -10.27408 | -43.58621 | 2024-09-28 00:24:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ab7e4895-f0bc-359a-a1fe-5bbf91addda1 | -10.87247 | -45.52164 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| cbad13b1-b836-3b5d-a2e0-0a7f8afba7c6 | -10.86495 | -45.56043 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 11813c5f-221a-3c44-bd31-897fc1b1e74e | -10.86264 | -45.54197 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 50541e8d-2f2d-341b-9c50-b30b6102082c | -10.86114 | -44.80484 | 2024-09-28 00:24:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ee46537e-004c-3347-9745-ef3c3893bfb1 | -10.85271 | -45.56186 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 336bbba9-8857-3503-abe4-44595b1bbdc2 | -10.69572 | -45.87302 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f35994a1-651d-35ba-875f-cd0bb547de18 | -10.69333 | -45.85354 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 66d2c7ba-f406-309d-9efd-4e2d4959f7c1 | -10.67287 | -45.89417 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 60382ab9-0e7f-3286-82f0-4cbd05009b21 | -10.67169 | -45.99109 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a8dac223-2f63-311f-8b51-3a4f8353e74e | -10.67062 | -45.8755 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 43762b5c-c820-32f1-9910-5f01bd8c8dad | -10.66944 | -45.97216 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |


[Clique aqui para ver as próximas entradas](README13.md)
