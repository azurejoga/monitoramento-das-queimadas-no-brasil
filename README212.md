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

## Dados Diários - Página 212

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15f4dd95-7be5-3adf-a8e7-fe000029cd41 | -9.90818 | -60.17623 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 569dad95-6f71-3d3d-bb6a-10591e24b6ba | -9.87434 | -60.1031 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 278ff1e7-dffd-39be-a4a6-cda5aa061f84 | -9.87391 | -60.10648 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 851788be-d93d-3b72-a01c-54a1e1a93849 | -9.87348 | -60.10985 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d16a2245-5faa-3c65-8a97-17c1bbca233b | -9.87022 | -60.10329 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a42fa2a1-11e4-30ae-9c33-70aa50fdf837 | -9.86977 | -60.10667 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9d38025-c4ad-3f60-a600-c105e32ac8e8 | -9.86932 | -60.11006 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5ac4803-c23a-32b8-b5b3-8447c0744f6e | -9.86178 | -59.83585 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a80acfe7-79ac-307f-8672-40834594c66f | -9.86132 | -59.83935 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b49f46-4b62-3a60-a0d7-209c05e5a001 | -9.81776 | -60.466 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f51dfaa-75d0-3224-8aa3-aa3f064d9c52 | -9.81256 | -60.46535 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78606cd3-1174-356f-9616-68c74d9e88d9 | -9.81216 | -60.46852 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47c9da2c-2c32-3e1f-aa35-58da31f15951 | -9.81094 | -60.43638 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a340ebcd-5943-3c45-9803-15f76a42dc31 | -9.81054 | -60.43955 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6618f445-6416-3534-8c1e-06013397a0b3 | -9.81014 | -60.44273 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f7b8d79-b95d-353e-81aa-c578d020ab54 | -9.80965 | -60.43663 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0d4865a-ff6b-3128-b437-f7b7c683604f | -9.80923 | -60.43979 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea2fd52d-1e42-349e-861b-84288213fad0 | -9.80881 | -60.44294 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee53f0e7-d9f9-3bac-a37f-2433bc5322f5 | -12.0587 | -61.05899 | 2024-10-09 05:55:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c147c12d-80b1-3f3e-b4a2-8e4bf904ff4b | -10.98395 | -61.12706 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f728d11-9597-3c0d-8c89-aeb4b2b03348 | -10.95981 | -61.11543 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 989cbe2e-d7e6-3c60-a815-014437c034a3 | -10.95942 | -61.1185 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 417b8b10-762f-3f41-8e3f-1dc905516cf6 | -10.92895 | -60.95165 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b554a8bf-d4c7-381e-bb00-88cd29a6b73e | -11.44133 | -60.4369 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4613e7d5-64e0-3dc4-b8bd-80c3c88e38a7 | -11.42858 | -60.453 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94c35ca7-4b82-382d-9a6d-50dcd51e0456 | -11.39689 | -60.41243 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79ebbf22-4c64-3fe4-a866-8601b2e0e7c6 | -11.39157 | -60.41172 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a37c759-2fd8-3d7b-9fb3-6a4af63ba8e4 | -11.35083 | -60.5645 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b5923a-1b03-3cc8-96fb-9c032974115e | -11.35041 | -60.56786 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f1f862-f241-30fd-a102-bdaeb506abb4 | -11.34999 | -60.5712 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b5ee121-c72a-3b47-8799-139adf704a26 | -11.29716 | -60.56635 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afccb8cc-deec-3195-941f-a2f3324ea141 | -11.29704 | -60.56707 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb18f89c-b318-3268-9e6a-db48bdd49f44 | -11.29219 | -60.56295 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aed36ca1-954f-3cad-8603-d3119f4c3c9e | -11.29192 | -60.56549 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bd279dc-8326-3a8c-95c6-4e95a7fdf45a | -11.29179 | -60.56623 | 2024-10-09 05:55:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a0564f3-53ee-358e-9b14-19b170ddbfe2 | -11.27103 | -60.39175 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a39d8ed9-f0a1-39d5-b6b9-8cd476a84533 | -11.2706 | -60.39518 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 767eacd5-7c37-32fc-a135-6bf2d5154477 | -11.27019 | -60.39845 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cb9beb90-d3bd-3c8a-b772-e4f163e9acfd | -11.26693 | -60.38131 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 403e92c2-93ef-3cc5-80b2-318a5114b402 | -11.2657 | -60.39113 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0da72aa4-821a-3ccd-b7b1-d67f7eb23a33 | -11.26531 | -60.39425 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 820ab117-7d9c-3789-a432-1fbbe3cf5003 | -11.26492 | -60.39735 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bda82b46-22d8-3dfa-a200-3d638c8d37fa | -11.26453 | -60.40044 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d7309459-20e8-325a-9fa6-d0736bcdbb5f | -11.26422 | -60.48865 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df2d92b3-239e-351b-8ad9-faa825a89bbd | -11.26379 | -60.49207 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f1c451d-5802-3954-8f6e-ee9540540929 | -11.2624 | -60.37424 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 825af31d-6ac2-310a-9f32-30735494ad34 | -11.26198 | -60.37764 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1414bdb-5ba3-3bba-9f87-f126fed87c69 | -11.25848 | -60.49157 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de7690e3-9a27-3916-a19f-087bddeabfc6 | -11.25805 | -60.495 | 2024-10-09 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a454e4-7a5c-370d-ab7a-a177e3be781b | -9.2852 | -62.32818 | 2024-10-09 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012f8e85-ca83-35b7-8bc1-65adf1e58742 | -9.26867 | -62.382 | 2024-10-09 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3f84362-dfac-3119-9fe5-de4f83bffcd6 | -9.26328 | -62.45523 | 2024-10-09 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f971f6a2-0225-322c-b58b-4d41613acba9 | -9.1628 | -61.57128 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| af5736a0-f793-392e-a377-596d5a8ea674 | -9.16211 | -61.57642 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4b46735-4087-320a-8e12-c90a3799cb2b | -9.15805 | -61.57056 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a15121c3-5dd7-3f48-b8eb-bf1161630275 | -9.15736 | -61.57573 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ddb3800-211e-354b-8717-8a20f7ccaf27 | -9.12297 | -61.43061 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a799d77-9197-3501-b25c-b14be9e3c1fd | -9.10325 | -61.13626 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71b86aaa-a60a-3447-bba1-4459f3ff31c5 | -9.10252 | -61.14173 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9875240-ece8-3d22-ba90-6835802d847f | -9.09835 | -61.13556 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9beb412-5075-30fc-98c5-ca43893030ca | -9.09595 | -61.13477 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d08dc35-70c0-36ef-9aba-2468079bcba1 | -9.09345 | -61.13483 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1214aa0a-7946-39be-81a6-ce427fec668b | -9.09273 | -61.14034 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0c80f56-055f-3b5f-899e-6183fe5ad5de | -9.09106 | -61.13402 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31d776ba-916c-3388-aedd-4d3b1bb70f76 | -9.08856 | -61.13407 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33593518-0ae7-346d-9ccc-accbf2e70785 | -9.08617 | -61.13327 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d9a5199-c5c9-3753-9424-9ba6cb32d1f0 | -9.08473 | -61.38719 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d68d922-6fe7-35ae-b564-34a49f5c612a | -9.08402 | -61.39255 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f6beaf8-a594-38e8-b1cb-90cd631af5c0 | -9.08366 | -61.13332 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dce009f-cc7b-394d-b564-e839d5140691 | -9.08128 | -61.13254 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9afb606b-8e62-3c09-afb5-27f011603c2b | -9.06689 | -61.37378 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3551811-d0bc-318a-85fd-d896fa922d0b | -9.06336 | -61.4004 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21c94494-9fd0-3fb7-b923-51b093a187d0 | -9.06274 | -61.37254 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2805968-8810-362b-b691-a003e20c8fc3 | -9.06206 | -61.37315 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fac9e78-1a8e-368b-9d45-f4dc2ec67f17 | -9.01263 | -61.55704 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 872e092f-613b-37dd-ab3a-573b133a6c4b | -8.84608 | -61.49069 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c495f9a-7c9a-3d16-9a5a-273122391ecd | -8.84131 | -61.49001 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a522cdf-7e08-3233-afa8-af0e8d2a064d | -9.18414 | -62.27885 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0237c83e-f920-3102-9c9f-6e65138bcbc5 | -9.17961 | -62.27818 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a351cff4-590a-32cf-9459-5cd04a843edc | -9.17898 | -62.28279 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d89ea703-33a5-3fc1-8c23-2145931d6c96 | -9.1599 | -62.21835 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5264fd12-467f-3863-bbed-2b484cb2b791 | -9.15931 | -62.21645 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b53c9722-ead3-377a-b896-d04c11e80727 | -9.15865 | -62.2211 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc89052-2ead-31fa-8084-b3c04f2b00e8 | -9.15535 | -62.21766 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2658a36-645c-3338-bce5-19181845318e | -8.90314 | -62.17484 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 060b0877-6747-398c-a407-5d2530acb159 | -9.75639 | -62.37145 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 83278a6f-03ad-30d1-9615-3aba827ff330 | -9.74726 | -62.33675 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eba47f8-ec3e-3e9d-8c64-c7b604a64522 | -9.74661 | -62.34151 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa784f0f-2600-357b-a31f-b80c92a60256 | -9.712 | -61.96837 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55b4166e-4ee8-3ab2-8e6b-7b57bc9c55cd | -9.68664 | -62.30414 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dca8c2e0-aa10-3918-8f12-3cfb3e4733dd | -9.65512 | -62.43732 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75ac84a3-aadd-3fe3-9788-8978d2f58760 | -9.65451 | -62.44195 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e27d72f-174c-3733-8331-b3952f3ccb19 | -9.65302 | -62.43904 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d68d4f42-92a1-3a48-bc86-7d89a37c1dbb | -9.40007 | -62.34273 | 2024-10-09 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02231b70-4f47-3e51-95b7-e2ae75d157c9 | -10.86093 | -62.0234 | 2024-10-09 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a6e12b3-0524-38eb-8f3e-7851ed2b5059 | -10.86026 | -62.02846 | 2024-10-09 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39b728aa-1aec-363b-8b94-3fb86c58d17d | -10.65343 | -61.74662 | 2024-10-09 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 448d7ae7-0920-34b3-9464-e3d69eb2909e | -10.478 | -62.89803 | 2024-10-09 05:55:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f7d0f36-f9a3-32ec-b2a9-75f0a0b73ca1 | -10.4736 | -62.89715 | 2024-10-09 05:55:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bee64af7-43aa-336f-b3b0-e9c79f32efae | -10.20067 | -61.95787 | 2024-10-09 05:55:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README213.md)
