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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| deed55c8-09ea-3b00-bebe-988e05265936 | 2.8885 | -61.581 | 2025-02-03 00:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b25325ba-9f15-3cf4-981c-88db6032cda4 | 1.9419 | -60.3827 | 2025-02-03 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 70088393-cb79-374f-a34e-27af1422f031 | 1.9419 | -60.3827 | 2025-02-03 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2fb8305f-67a5-3ab2-b1c9-8a4b961767db | -11.4959 | -37.431198 | 2025-02-03 00:10:00 | METOP-C | INDIAROBA | SERGIPE | Brasil | 2802809 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab43df31-de08-313b-9387-2d34d1cbfcb9 | -6.8329 | -35.005001 | 2025-02-03 00:10:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 008cadb9-96c9-3ede-a425-08f19bed54a9 | -7.9273 | -35.264999 | 2025-02-03 00:10:00 | METOP-C | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a15b8585-232c-3114-a6dc-1eefbbdb44c5 | -7.7031 | -35.191898 | 2025-02-03 00:10:00 | METOP-C | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 56d51424-dc79-3e20-b196-55b396238f52 | -6.8266 | -34.979099 | 2025-02-03 00:10:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1616fe32-ad50-306a-860b-f1ef8ee8422c | -7.7157 | -35.0322 | 2025-02-03 00:10:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a440caf6-b856-35a5-8a27-30f8dc23a36f | -6.8395 | -34.9897 | 2025-02-03 00:10:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d60a269e-9b4f-33f2-a302-cf29f134b72a | -6.9781 | -35.0513 | 2025-02-03 00:10:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 665bda1a-d336-371e-b6b4-2ea44a39673b | -9.5095 | -35.9562 | 2025-02-03 00:10:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 52d3d9ad-0148-31eb-8095-05d5b7d55ac6 | -6.8298 | -34.9921 | 2025-02-03 00:10:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38d3ad1e-e6ab-39ee-9122-d9e7360e80a6 | -7.0445 | -44.390999 | 2025-02-03 00:10:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84d6bdb3-1382-3f6f-ac5c-16bae88dbf5d | -7.6885 | -42.990299 | 2025-02-03 00:10:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ed74c6c-fda6-31cf-ba8b-c78d3cf5e34b | -7.7188 | -35.044601 | 2025-02-03 00:10:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e4d02832-5aef-3275-85b7-a112d07bb791 | -7.9243 | -35.253101 | 2025-02-03 00:10:00 | METOP-C | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1240c39c-db54-34d5-bb3a-684c11c6229b | -9.512 | -35.966499 | 2025-02-03 00:10:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c711fea-8c33-3cca-bd92-b6c5dafaa30d | -9.507 | -35.945999 | 2025-02-03 00:10:00 | METOP-C | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad5913b4-1b0c-38f7-8470-d5b2bb37a602 | -7.709 | -35.047001 | 2025-02-03 00:10:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7aa53c40-f9f0-3d63-ad40-32588c9b7617 | -7.7128 | -35.189499 | 2025-02-03 00:10:00 | METOP-C | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9d50711-6979-3673-8f6d-ab6538e6f159 | -7.9214 | -35.2411 | 2025-02-03 00:10:00 | METOP-C | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6c4dcd3-a10c-3a78-8c5e-293acf774683 | -17.8433 | -40.0812 | 2025-02-03 00:14:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe6662e5-9ba6-368d-98ed-5ff08072dc4f | -17.8531 | -40.078999 | 2025-02-03 00:14:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30b91ed4-2c48-31dc-8c05-28d4c1962acc | -17.884399 | -40.462799 | 2025-02-03 00:14:00 | METOP-C | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23132e24-9573-35a4-b973-8b4d3e29825d | -17.8449 | -40.0886 | 2025-02-03 00:14:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 13d5bf5f-cb2e-392a-826f-487ab4c3b20f | -17.882799 | -40.4552 | 2025-02-03 00:14:00 | METOP-C | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 741b518a-4808-39f0-b15e-470d981ed00b | 1.9419 | -60.3827 | 2025-02-03 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ac9856fd-a0f5-33b0-a4ca-5d83c0394961 | -17.84122 | -40.09065 | 2025-02-03 00:22:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 44.0 |
| 6fb0fc28-86a5-3a59-9024-f89547993a82 | -17.83994 | -40.08141 | 2025-02-03 00:22:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 41.1 |
| cbeccf77-9e8c-304d-ae17-3c12108ca307 | -17.88341 | -40.46264 | 2025-02-03 00:22:00 | TERRA_M-M | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 82c4c0fd-6b30-330b-80a5-e379ad80ffaa | -17.85096 | -40.08332 | 2025-02-03 00:22:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 51bb78f1-b6d9-3e80-985d-fd809c818b27 | -17.87453 | -40.46399 | 2025-02-03 00:22:00 | TERRA_M-M | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d21bb80a-f76d-381d-ab79-212bb44780ef | -6.82909 | -34.99454 | 2025-02-03 00:24:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 274.6 |
| b85b4a49-d0dd-3e22-a9c6-d6b4c56f8e81 | -6.82302 | -35.00212 | 2025-02-03 00:24:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 173.1 |
| cdecd23d-72f7-33e2-9e04-348124fac27e | -6.82532 | -34.97127 | 2025-02-03 00:24:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| f59f5839-41ea-3ba8-a467-a542e111c42a | -7.04691 | -44.39719 | 2025-02-03 00:24:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0c0083b0-64a7-3ecc-9022-209aaf801aca | -9.38937 | -35.97808 | 2025-02-03 00:24:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| c2e50409-8a3a-3eed-9005-f1a12c105085 | -9.38147 | -35.97285 | 2025-02-03 00:24:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| c386bc4e-2088-3772-8bbe-bf74b53acde9 | -9.39356 | -35.97085 | 2025-02-03 00:24:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| ae653bb8-0767-315d-97e7-9ef95781bcda | -9.38664 | -35.96029 | 2025-02-03 00:24:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 81224ffd-3f5c-3562-97d6-1ed892c56df9 | -7.70242 | -35.19077 | 2025-02-03 00:24:00 | TERRA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| d1853dcc-57bf-3f62-8f2e-aea5bfade814 | -7.70684 | -35.19561 | 2025-02-03 00:24:00 | TERRA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 1fe5d6af-eedd-30ba-ab4c-a2eaa1d77214 | -6.8194 | -34.97875 | 2025-02-03 00:24:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 182.8 |
| 12313b3b-9360-3c8b-a0ab-a85aad9e8f62 | -9.50926 | -35.96391 | 2025-02-03 00:24:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 6731782e-0431-3814-8514-b832a9455323 | 1.9419 | -60.3827 | 2025-02-03 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d94e5719-4615-3101-ada9-cd292cc3d1df | 1.9419 | -60.3827 | 2025-02-03 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 660669af-0fa6-3652-a885-8b6b81763a49 | -6.8292 | -34.9913 | 2025-02-03 00:50:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 72.5 |
| 84ff3fb0-14c0-3112-80d7-bc092551697f | 1.9419 | -60.3827 | 2025-02-03 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 89197933-2fd3-32c7-a062-dd0366c54b33 | 2.8747 | -61.571499 | 2025-02-03 00:58:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 34e0c539-00a7-350c-9fa0-e8599cd76091 | 2.8862 | -61.566299 | 2025-02-03 00:58:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 103d7444-1d49-3847-9f91-bc7deb3a4cc9 | 2.8764 | -61.564098 | 2025-02-03 00:58:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5e7a91-6f0d-3b20-b260-c42e0329398a | 1.9395 | -60.376099 | 2025-02-03 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dbed8554-848a-38c3-b441-105d6c9ee9f8 | 4.4458 | -60.780899 | 2025-02-03 00:58:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9b374901-c508-373d-8485-27ce5ee8185d | 1.9379 | -60.382999 | 2025-02-03 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 441168f6-c1c9-3064-b6bc-5ca4807a1fd5 | 4.4256 | -60.733002 | 2025-02-03 00:58:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 53b8121d-9082-3aa7-acc5-aef804815d0e | 1.9297 | -60.374001 | 2025-02-03 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7748de17-d896-3de6-9b6a-460d545b801f | 1.9363 | -60.389999 | 2025-02-03 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 27568eb6-691a-3e3c-a921-0d798e163610 | 4.4442 | -60.7878 | 2025-02-03 00:58:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 52ef0f7f-19e2-3c54-b8f5-856ba21be309 | 4.1 | -59.891602 | 2025-02-03 00:58:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a9cc05a1-1e51-35e1-8a92-7104b0cf27f1 | -22.214701 | -53.438301 | 2025-02-03 00:58:00 | METOP-B | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 387308c3-a92c-3f4a-ab38-b03dc6802258 | 4.4272 | -60.726101 | 2025-02-03 00:58:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6b02f010-4bc7-3094-ab4b-00e21fb82ffc | 1.941 | -60.369202 | 2025-02-03 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce5b132-1238-3dda-8fa0-7def3b4800f1 | 4.4288 | -60.7192 | 2025-02-03 00:58:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d39ff92a-9cfe-3044-816e-6d4cdd200967 | 2.8845 | -61.5737 | 2025-02-03 00:58:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68c01a0e-5c82-3f55-b92c-41c6a732773f | -22.2131 | -53.430901 | 2025-02-03 00:58:00 | METOP-B | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9e97d1c-2b47-3904-af39-be38ce0287f0 | 1.2 | -60.0453 | 2025-02-03 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 44999350-1569-345f-ba88-e39d7b4d150f | 0.7139 | -59.413101 | 2025-02-03 00:58:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c1e97e85-a4bf-3fdc-b8ba-822f6e350adf | 1.7798 | -60.626598 | 2025-02-03 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cc921ab9-08b6-3d44-8b77-6c783914bd34 | 2.8829 | -61.581001 | 2025-02-03 00:58:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ac778991-3177-3af8-ac51-da9e70f41240 | 1.3112 | -60.419701 | 2025-02-03 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d2886c0f-b3d0-3b02-a310-a593999e202c | 1.9281 | -60.380901 | 2025-02-03 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9e80bd89-7be2-31b1-b4d3-779a2e8759c3 | 3.0177 | -60.850101 | 2025-02-03 00:58:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 74e72ed3-bece-306a-8899-a000b2059db3 | 0.7294 | -59.847198 | 2025-02-03 00:58:00 | METOP-B | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7903f81c-27a5-3abc-829e-27a5d2f3017c | 1.0188 | -59.523499 | 2025-02-03 00:58:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cfb60adf-4d2c-303d-97ca-8ff5606cae0a | 1.7814 | -60.619598 | 2025-02-03 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fff18403-bca4-3a08-b800-5e14736b237b | 2.8731 | -61.5788 | 2025-02-03 00:58:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c1e2fb5-af27-34dd-8323-42b4fcffe761 | 1.0173 | -59.5303 | 2025-02-03 00:58:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dce2c780-57a0-3ec9-ab2b-c3f81cd10798 | -6.8296 | -34.9638 | 2025-02-03 01:00:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 182.5 |
| d70ee7da-8958-3260-88e3-bddb239e5bfb | -6.8292 | -34.9913 | 2025-02-03 01:00:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 325.7 |
| 416350cb-3c47-3e97-b833-659fb17503b0 | -6.8487 | -34.9614 | 2025-02-03 01:00:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| e09d8a20-c483-3fe8-b368-5432a2fe0401 | -6.8101 | -34.9938 | 2025-02-03 01:00:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 113.4 |
| 62934f23-667e-3e78-b07b-a243fd68d9c6 | -6.8483 | -34.9889 | 2025-02-03 01:00:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 129.2 |
| a9457bfb-998c-3691-8088-f7f6704a01c0 | 1.9419 | -60.3827 | 2025-02-03 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 208894c4-5ff9-3869-b888-60d17ae1cf7e | -6.83 | -35.0 | 2025-02-03 01:00:00 | MSG-03 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1901385-da73-30b0-8b84-3f1dbd53c4b8 | -6.83 | -34.96 | 2025-02-03 01:00:00 | MSG-03 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 18d4dddd-fa24-30c1-b051-fcfe2a1c6136 | -6.8292 | -34.9913 | 2025-02-03 01:10:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| caf81a1a-50e1-3163-8262-42132f3e0b68 | 1.9419 | -60.3827 | 2025-02-03 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 52c3419d-6f98-3ab2-8172-6b2a680300c8 | 1.9419 | -60.3827 | 2025-02-03 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ddea8ce9-3b20-3d5f-80ec-3c6a07aa7002 | 1.9419 | -60.3827 | 2025-02-03 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 936eea14-a1b1-3042-a5cc-19440b67044d | 1.9419 | -60.3827 | 2025-02-03 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 91aef221-78f3-3558-b122-53068ba22e3a | 1.9365 | -60.374001 | 2025-02-03 01:53:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ca7e5878-36c4-31df-9085-99600307a686 | 2.8837 | -61.559799 | 2025-02-03 01:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0c3f384c-fd58-320f-9603-ae9e747e66ce | 1.9325 | -60.391701 | 2025-02-03 01:53:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 13279a10-ed5c-39f7-9a0d-a1d723530cd9 | 2.8803 | -61.574902 | 2025-02-03 01:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 834453f3-51e4-3985-a881-dd3cab34f4d4 | 1.9462 | -60.376099 | 2025-02-03 01:53:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 11cf6f20-ca90-3ab6-81e7-30d84a484506 | 1.9419 | -60.3827 | 2025-02-03 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7db9ae34-2a06-34cc-b643-bf6980998ca6 | -12.28142 | -64.40972 | 2025-02-03 02:02:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f0d09a1-c7af-3123-928d-80a1571129ed | 1.94062 | -60.3876 | 2025-02-03 02:04:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| c8955ae8-851d-33e6-88c8-7862da62404c | 2.88773 | -61.58248 | 2025-02-03 02:06:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 34.2 |


[Clique aqui para ver as próximas entradas](README2.md)
