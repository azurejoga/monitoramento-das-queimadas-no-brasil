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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf7779b8-05f5-377b-be0b-9281df0b225c | -11.142 | -44.6261 | 2026-10-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 810abc62-e54d-3c2e-a42a-a2b48a03b281 | -13.8763 | -43.6396 | 2026-10-02 12:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 89853da0-1d33-3948-a0b8-b633c2f4ed67 | -11.2278 | -45.1913 | 2026-10-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 9f717148-ed12-30e5-9de0-e18004cabc3e | -11.1424 | -44.6029 | 2026-10-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 486.6 |
| cc6d5d1b-3c0d-3a17-b731-b1c0e47952d1 | -11.2242 | -44.2888 | 2026-10-02 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 16ba42ae-288a-36c2-9078-1f3dd5296e65 | -12.5527 | -43.0637 | 2026-10-02 12:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 125.9 |
| d9f417c8-2670-342c-b5b7-830b5eff66d2 | -11.7567 | -43.4325 | 2026-10-02 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 0113fba9-614c-3ee4-89fa-d682f4043f82 | -11.1615 | -44.6002 | 2026-10-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 263.7 |
| 69655e37-d729-374b-a785-f3bf29291252 | -12.5329 | -43.091 | 2026-10-02 12:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 151.8 |
| 1e0b5f0d-937b-3892-a8ea-0e7279275fae | -12.5522 | -43.0877 | 2026-10-02 12:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 155.2 |
| 68802891-daad-3574-ab42-e222dfea56bb | -11.1427 | -44.5796 | 2026-10-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 418.4 |
| d7843060-75c1-39a8-9cd3-57ea6f41ebd4 | -12.5334 | -43.067 | 2026-10-02 12:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 7efa98ff-3101-32d1-9846-7fc1b04032a1 | -11.1236 | -44.5823 | 2026-10-02 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e8065f86-be3e-3602-94ed-8e2586c59b67 | -11.2282 | -45.1682 | 2026-10-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7a318a8d-6ff8-3ae9-a5ee-87d796a3447b | -11.7169 | -43.5098 | 2026-10-02 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| c32527e5-7b7c-3700-af65-5af00d30386f | -11.2466 | -45.2116 | 2026-10-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d8491243-532b-39ca-840b-fd386e335ad2 | -11.7182 | -43.4386 | 2026-10-02 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 6266fafc-9fb4-3829-9865-71a67edd3f4f | -11.2753 | -43.5539 | 2026-10-02 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e85d68c0-ccd5-357c-a39f-a49643ca2df9 | -10.303 | -44.648 | 2026-10-02 12:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| cd0bccac-68e3-38e4-baba-4b4772971f36 | -13.8763 | -43.6396 | 2026-10-02 12:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| c5b7fdec-9abe-37df-8dd7-7939abdaa7fb | -12.5334 | -43.067 | 2026-10-02 12:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 154.5 |
| 6a5a4f0d-b069-3c0a-be9f-aae867450201 | -11.1611 | -44.6234 | 2026-10-02 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 6f6f088b-f6a2-328e-8c08-d982507c0892 | -11.247 | -45.1886 | 2026-10-02 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 38e3ccb9-57d2-3da3-815e-0395b4203517 | -11.1615 | -44.6002 | 2026-10-02 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 7ed77499-087d-37ce-9bf6-ddebda787ba7 | -12.5329 | -43.091 | 2026-10-02 12:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 254.7 |
| f2e77504-3fea-3075-b2c2-ef36c1ce8a81 | -12.5527 | -43.0637 | 2026-10-02 12:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 181.9 |
| 4f5d5b47-9065-3e1c-8f12-1d7774cb0c2d | -9.0844 | -44.9811 | 2026-10-02 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 8abe9b19-0e22-3678-9f63-496ecdb76b1e | -13.3287 | -43.8573 | 2026-10-02 12:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e6371ede-392c-34a8-9b8f-b9b89811d22c | -13.8037 | -45.2287 | 2026-10-02 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 1734b8ce-8c76-3655-a354-56d88a760877 | -10.303 | -44.648 | 2026-10-02 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 481.4 |
| 8ff65d3e-bf70-39b4-95c2-482368e1613e | -11.2278 | -45.1913 | 2026-10-02 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7bb3ec56-8dc3-388f-b3b7-d1bcb853d506 | -12.5522 | -43.0877 | 2026-10-02 12:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 290.9 |
| 26392e0c-addc-3862-8b3b-1a4fe42f7541 | -10.9262 | -43.8406 | 2026-10-02 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| bcddc462-988c-3bf7-9636-9192c8bcb87e | -11.7169 | -43.5098 | 2026-10-02 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9e791e43-1778-35a7-b102-3f320c94a32f | -12.4544 | -44.1466 | 2026-10-02 12:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a2d7646b-7ad2-3375-b0c4-bee1f9931207 | -12.4737 | -44.1435 | 2026-10-02 12:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 443.9 |
| 326cabc7-4ad1-30fe-8f9f-d949839ca210 | -12.7808 | -45.1897 | 2026-10-02 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 60ec9756-9883-3239-a23f-ae62710c733c | -11.7921 | -43.5926 | 2026-10-02 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 674de4ba-bfe0-30d6-82cf-0a7e3473b8f8 | -9.8444 | -44.8218 | 2026-10-02 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 1122bef8-2811-325f-9539-1f14fb6330f5 | -11.1424 | -44.6029 | 2026-10-02 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 5f833ee1-26a0-31de-8619-cf25b04b3855 | -9.7877 | -44.8058 | 2026-10-02 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 166.3 |
| b62e9dc9-ead7-3796-b1e9-ade81a00a623 | -9.8257 | -44.8011 | 2026-10-02 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 247.0 |
| a3b7bc8f-efdd-392b-9c8e-6c787d2f19a9 | -12.7812 | -45.1665 | 2026-10-02 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1bb80cd2-4486-3e6d-812a-5fcebb711e4e | -11.1427 | -44.5796 | 2026-10-02 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 205.9 |
| f1e7d41a-ff59-3d5f-9d7d-f20d1f571acb | -12.4732 | -44.167 | 2026-10-02 12:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 62b65c51-5189-3327-8459-856609b4ad1d | -13.3481 | -43.8538 | 2026-10-02 12:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1307a1e2-d92f-32f9-83ba-b5c487ca4bbc | -11.2466 | -45.2116 | 2026-10-02 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 05dcd795-f271-33f4-997b-15c9642f6a40 | -9.0655 | -44.9832 | 2026-10-02 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| cc9c90bb-ec61-3c66-860b-f52254b8d806 | -10.3034 | -44.6249 | 2026-10-02 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 369.8 |
| 92391d18-3044-3046-9ab6-da7a4f38e824 | -9.8254 | -44.8242 | 2026-10-02 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 247.9 |
| 6467e56d-becf-3b58-8d33-4f5787f5d97c | -13.8032 | -45.2521 | 2026-10-02 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 341.2 |
| 30f7e241-e955-3195-8016-c2ad2a7ca4a5 | -10.3034 | -44.6249 | 2026-10-02 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 234.7 |
| ed1bc966-d047-3453-ab64-d01a45192506 | -11.7537 | -43.5987 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| b7cd7bbd-ba2d-3807-a221-4b941c840a70 | -11.716 | -43.5573 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 528bbf48-f299-3f4e-9126-9bb7baa6ff1f | -11.1427 | -44.5796 | 2026-10-02 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 26023bda-2c9b-3784-8f49-226aa54568cc | -13.3287 | -43.8573 | 2026-10-02 12:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 256.6 |
| afa46983-5b67-3cf4-9f7c-b216684ed75d | -13.3486 | -43.8301 | 2026-10-02 12:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 7f55a201-b80f-3362-bb57-65b5485c10e2 | -9.7877 | -44.8058 | 2026-10-02 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 0bc44a09-69e9-3d61-a218-b39c9aacba7b | -11.2466 | -45.2116 | 2026-10-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e33fce8d-10bd-3214-91c1-6b90e7556388 | -9.8444 | -44.8218 | 2026-10-02 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 9816f212-295b-3cf8-aa14-012a1ca9df30 | -12.5334 | -43.067 | 2026-10-02 12:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 262.8 |
| 1684c98c-5316-30cb-a600-8b13fb3d8125 | -13.7843 | -45.2321 | 2026-10-02 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 1cd75c5e-8192-39c9-9138-3957f6d1c81b | -13.8032 | -45.2521 | 2026-10-02 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 2164f233-1b9f-30de-8c25-f27ce74672ca | -12.7619 | -45.1696 | 2026-10-02 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 021df54b-4d65-324b-b194-c2938cd3e53c | -11.7738 | -43.5482 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 082a3a5f-f416-3e71-b24c-8a45c5fc12e3 | -11.2753 | -43.5539 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| c8b5957a-7b42-3112-b4a4-8026ddc6f042 | -12.4737 | -44.1435 | 2026-10-02 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 931.7 |
| 49f4f9ce-3990-3b2e-ba00-f47f655484ae | -13.3476 | -43.8776 | 2026-10-02 12:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| f4375dae-71d9-3191-9cd3-bae8ee382c88 | -10.303 | -44.648 | 2026-10-02 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 298.1 |
| 32e36864-0ee4-39c3-9a23-31087f0b2ce0 | -13.8037 | -45.2287 | 2026-10-02 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 8785ca4c-6e83-331d-906d-9a4640c1b774 | -12.7808 | -45.1897 | 2026-10-02 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 5397dca0-f121-3715-bc7e-ec76b9349cc8 | -11.7353 | -43.5542 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 7c3a53db-2f52-3d2d-a6bd-15bf79b2895b | -12.4544 | -44.1466 | 2026-10-02 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 627ecde2-5c90-3fe8-8b94-33c3d3940fd5 | -13.3481 | -43.8538 | 2026-10-02 12:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 360.9 |
| b32ec2d0-5d6b-3256-9f79-384c078e5d1a | -12.5329 | -43.091 | 2026-10-02 12:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 457.9 |
| 7f4377af-5cd3-3b26-8554-0df73a11060c | -12.4548 | -44.123 | 2026-10-02 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 7dd8d850-fcf0-3753-a607-5da844cef945 | -11.247 | -45.1886 | 2026-10-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f4f8e581-dacf-3e39-a518-c3efce40dfee | -12.9229 | -44.8186 | 2026-10-02 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1cd85eaf-01d9-3605-9262-f2cafcfcc9e9 | -11.793 | -43.5452 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 419.2 |
| 14a3d0f8-3e0d-3bd7-aba1-234c6613bcc2 | -11.1615 | -44.6002 | 2026-10-02 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 4ddfb922-6548-37e5-a70a-88104e83deca | -11.7545 | -43.5512 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| c530843d-971b-3928-8514-a11091c93325 | -11.2749 | -43.5776 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| ea3cc111-6eb0-3c10-99b1-9159603be1e1 | -11.7169 | -43.5098 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 540913fb-4187-33e6-8bca-e7d8edd6823c | -9.8254 | -44.8242 | 2026-10-02 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 186.2 |
| ac6d815d-c200-3793-80d5-3ebe22bfd6fc | -11.1424 | -44.6029 | 2026-10-02 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| da4bf744-b3d2-359e-bd1a-851e2d067b24 | -12.7812 | -45.1665 | 2026-10-02 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 0245d789-5c4e-3bb2-92ef-5578d1979a93 | -9.8067 | -44.8035 | 2026-10-02 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7a516a37-d956-306e-a052-0ff9fe2819cd | -12.5522 | -43.0877 | 2026-10-02 12:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 326.8 |
| 34fed173-0e1a-343f-b197-f6b97ce0ac81 | -11.755 | -43.5275 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e00e8259-1daa-3138-b21f-e2f3112e42fb | -11.1611 | -44.6234 | 2026-10-02 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| e95329eb-78e0-3afb-9e0f-5ae8e2d72aca | -10.9262 | -43.8406 | 2026-10-02 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 122f4035-6e18-38e4-8994-84700bd4c294 | -12.4732 | -44.167 | 2026-10-02 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| b1122e87-1276-3332-bd0c-8b8d1e665d82 | -13.8763 | -43.6396 | 2026-10-02 12:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| b0a1d20f-9a4b-3c31-bed9-b94cc34e3318 | -11.1611 | -44.6234 | 2026-10-02 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 221.6 |
| c4e15728-4226-3548-8da0-853e6a39232d | -11.2749 | -43.5776 | 2026-10-02 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 9e85b876-baa5-3559-b54e-a092367a2f2b | -10.303 | -44.648 | 2026-10-02 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 222.1 |
| c94059f3-1e37-3fc3-b24f-57ee9f3af88e | -12.9229 | -44.8186 | 2026-10-02 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 19387737-1ca6-3da6-9051-60750d61cd3c | -12.7804 | -45.2129 | 2026-10-02 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 7cf8cc33-9d25-39ac-a0ea-a02699ec1278 | -13.8037 | -45.2287 | 2026-10-02 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 335.0 |
| 3319ba6c-a029-3c85-8c77-0b84f076836d | -11.142 | -44.6261 | 2026-10-02 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |


[Clique aqui para ver as próximas entradas](README86.md)
