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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7dd53de-6c31-315f-8096-904fccc70f97 | -17.70732 | -53.2762 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b44d2c-8a96-3aeb-9970-3d06880a14ca | -19.64389 | -57.28143 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5bc9e767-633e-37f2-b506-eeed8d10a27e | -21.07907 | -50.17587 | 2026-01-25 04:50:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73466b27-0cd5-3b76-a55b-63532f09ed98 | -19.63607 | -57.28431 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 28eb2fd6-5e31-38f3-9fe8-638e9b21d806 | -19.60773 | -57.27887 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 14c5acb4-fb09-3b1f-a01b-9702b049e0ab | -19.62824 | -57.28718 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b5e9a419-b7ee-3336-ac7e-a049ba3dfac2 | -18.81122 | -51.60799 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be349dbc-a9e3-3a61-8b1c-b14723149e19 | -21.07352 | -49.52994 | 2026-01-25 04:50:00 | NOAA-21 | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7294a153-3f5f-3268-ac15-6dabf396b348 | -21.07451 | -49.53455 | 2026-01-25 04:50:00 | NOAA-21 | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 74a18e71-2ed1-303a-a6a5-ab04b68c3f48 | -18.81527 | -51.60454 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0d13ba6c-123f-3f3b-9243-fbde24c74e37 | -19.63622 | -57.26245 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c2ce382e-d437-37fa-ab03-d72c9232ebe6 | -19.64256 | -57.26804 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 19e23d6a-d7ba-35a9-af88-df43310d1010 | -19.66281 | -57.19348 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6af34ae2-c21c-334f-8cff-b4b2931980a8 | -21.07054 | -49.53399 | 2026-01-25 04:50:00 | NOAA-21 | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 99a5ffc3-164a-3e31-9059-f2f7799d9a0c | -16.18652 | -59.33537 | 2026-01-25 04:50:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06d7b4b0-9ce1-3141-9da1-a3d74762689e | -19.63342 | -57.25754 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b4af70c1-15fd-35f7-8b82-ebf7352adf66 | -21.94819 | -47.42168 | 2026-01-25 04:50:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 470f195c-799e-353a-8f95-27975436db2d | -19.63459 | -57.29279 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 336d982d-ae4a-396d-afdd-da939a643d69 | -17.70126 | -53.27148 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c85140fa-77aa-39da-a802-b1bf4e3d06a9 | -19.99563 | -54.37265 | 2026-01-25 04:50:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f539815d-37f7-3bfb-9f73-5446ed7e8113 | -19.6219 | -57.28158 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b5a2b379-2656-3576-8308-5aa28ca28030 | -19.63046 | -57.27447 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e2e88153-6e03-382b-9fea-5953586e12b9 | -19.62544 | -57.28226 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 4d7e026a-be1f-3292-a1c3-cefc726de0cd | -19.63961 | -57.28498 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a242375f-922f-36d3-9d32-c161ea298b01 | -20.31909 | -57.83313 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2c049610-e734-3467-adae-30d2e41d26ef | -19.3431 | -54.17382 | 2026-01-25 04:50:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dc5c9ad-ae56-3935-b556-16417fc79731 | -19.62206 | -57.25974 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f4e9d756-7598-3bd8-9ab4-f2d26f69c168 | -19.64182 | -57.27228 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c11c2554-9d48-3cc3-ba5b-77f0379b0488 | -19.64123 | -57.25467 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6c6d4ca4-82cf-3326-b589-b606515d3659 | -20.32269 | -57.83384 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 33be3bd1-1f53-3c85-bd56-89a610867dca | -18.79442 | -57.65913 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1fb70539-d896-3deb-abc7-c1132ab0f4a1 | -19.61333 | -57.28871 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f13498fc-fa85-3c8b-88b1-24ab0bff26e9 | -19.61145 | -57.2577 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4132f27b-192f-3b76-93e3-ee189710860f | -17.58534 | -53.07409 | 2026-01-25 04:50:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8113915e-db71-35cd-bb20-70bcb39856a2 | -17.7007 | -53.27509 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42bf83a4-9a3a-3fee-a491-5a876eae7fc8 | -20.34866 | -57.83439 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d958d77e-60c0-3c49-a36e-f208d403b283 | -19.6163 | -57.27176 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 80f0a773-9edb-3ef1-8210-d90fe84d4ffe | -19.62058 | -57.2682 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 8eefbd6a-c0c5-3e28-b351-d37711a10d80 | -19.62956 | -57.30059 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| da3c839a-eed4-3386-bcca-9ea99b164416 | -19.6483 | -57.25603 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b90674ed-bd7d-336c-a4bc-163fd50111ff | -19.63194 | -57.266 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 99bee084-0859-3ff3-a342-bd35a718ea44 | -19.64049 | -57.2589 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b1bd4dca-427b-3a6e-92fb-1348284fc90d | -19.62149 | -57.24215 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c931f80d-158d-3686-92eb-7756bf4c8bcc | -17.70015 | -53.2787 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 188d6f9a-dd74-3123-ae53-e6ffa8f4c6d9 | -19.62338 | -57.27311 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| f8f698b9-0cf6-3e17-97d9-48184bd76e10 | -16.02305 | -59.90886 | 2026-01-25 04:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e24b483-2b5c-37ee-b3ed-a45f40edfc5c | -19.6247 | -57.2865 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b83cca02-b545-3a99-b1b8-129b1399de76 | -20.63676 | -51.67731 | 2026-01-25 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8df7dbb1-0f99-3e45-8619-9ec336f6222a | -20.34506 | -57.83368 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 166192bb-66c6-37b2-bd7b-3b11fcbdcb2f | -19.64743 | -57.28211 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 856bcb3a-712a-3fcc-b580-634690df9b0f | -19.61778 | -57.26329 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c8e8372b-cbda-31f7-913e-2a00daca5ca2 | -19.63326 | -57.27938 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cbae46eb-3b1b-3813-b321-74e4acb8f5f7 | -19.62766 | -57.26956 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1ff12355-aa8d-33ac-a3aa-7223868a09cb | -18.81644 | -51.59641 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fef730cb-5178-3b24-af7e-2bc781549d58 | -19.62898 | -57.28294 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| fcb97c36-1225-312d-801c-460aa49e7db9 | -18.78873 | -57.64878 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 97681f51-5a90-333f-ba6a-cabfa3840442 | -19.6511 | -57.26094 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 46dab30d-ad39-3d85-ac3e-34a7960df67f | -19.65244 | -57.27431 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b43b537e-d986-3105-9e53-1ab3563bf6a4 | -19.64403 | -57.25958 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| abfd7ef6-26d2-3dbf-8147-19815f492e55 | -19.64683 | -57.26449 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| c8c3d93b-a303-36b0-b4e3-bc67a287f578 | -19.63887 | -57.28922 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9891fc22-ec80-3dc9-98ea-e733be61a1ac | -19.66353 | -57.18928 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ecf14f93-b936-36e3-853b-be6a67cc6c8e | -21.35643 | -56.8665 | 2026-01-25 04:50:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5579c53-55a1-3957-aa34-d3ade55aa4a3 | -19.63104 | -57.29211 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6c90e82e-1f90-3cc7-99fc-e2173729cea4 | -19.65317 | -57.27008 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c6901ec9-6fb6-3741-8f96-2f5acd13a34a | -19.66698 | -56.85654 | 2026-01-25 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 655438cf-8e3a-3048-8c33-5091848188ac | -19.634 | -57.27515 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| a984f0c6-a8ba-3fea-80af-e0cb6df08503 | -19.63681 | -57.28006 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 02331c09-1a8b-300e-bbe3-f3641e24d361 | -19.63533 | -57.28854 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 792835eb-35a7-3dff-8cb2-2da8aa2b20c6 | -19.62075 | -57.24637 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f5cd1d93-caa0-320c-8e99-5663957660f7 | -18.8118 | -51.60396 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4356795c-1df4-3c72-90e1-236e05ac5fbf | -19.62396 | -57.29074 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 51797251-9b08-3500-b2ef-a77b1c3a2c12 | -19.62634 | -57.25618 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d0366876-12ce-36f2-b64d-2e56ee1e9da4 | -19.61853 | -57.25906 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a218fe9b-9ff8-3214-97f6-68e37eea307b | -18.79078 | -57.65843 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 85e91e59-2939-3616-a404-f4d41e2817c8 | -20.33066 | -57.83084 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 12dd387f-8b7d-3f49-8267-e146c31e1531 | -19.63696 | -57.25822 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6d2b9dcb-2c24-3eab-813d-959cf8282a34 | -19.62502 | -57.24283 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9e615ac6-0263-32e1-9e6d-eda4b6f4bd0c | -19.6284 | -57.26532 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3b156109-8958-3d86-aa7b-54c2924ed144 | -18.81586 | -51.60048 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 64730366-6d02-384d-8de2-c521045323e4 | -20.91805 | -56.37618 | 2026-01-25 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0bd1a4f-43c0-39df-8538-df9374570818 | -19.62988 | -57.25686 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d10540c6-2b23-33a5-919b-b9d64fe2586b | -19.66541 | -56.85739 | 2026-01-25 04:50:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 84f8d0e9-cd0d-327f-8cac-50d3e2a9f210 | -17.70457 | -53.27203 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73fcc034-37ee-340c-b349-ef68549d7dba | -17.58866 | -53.07464 | 2026-01-25 04:50:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52b5a81a-91f8-38c9-a030-d82894b59134 | -19.64757 | -57.26026 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 81be4bb6-b3de-323e-a654-f2f579387ad6 | -19.63548 | -57.26668 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3424ae1e-031e-3203-89d2-c629e90c948f | -19.63077 | -57.23085 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 02f79e25-ad95-3796-81bf-bcecf1f27440 | -18.78713 | -57.65774 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| ee11d2cd-d91b-3cd2-93e8-c55542b84bd6 | -18.81238 | -51.5999 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d0a6465-5aec-3c4a-a4a7-07b119b46222 | -19.62116 | -57.28583 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0d63cb4b-49a9-3aea-84a2-15f52cc65eb1 | -17.59197 | -53.0752 | 2026-01-25 04:50:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52afaa91-920e-3de1-ad0a-779e3f9c64da | -19.64108 | -57.27651 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4c2630cb-3d74-3809-a96d-391dc20155ba | -19.64964 | -57.2694 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 83bf0993-8925-3f01-8310-061e31a706d1 | -20.56396 | -54.65242 | 2026-01-25 04:50:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e0ae41d-d550-3716-b396-833f56a57105 | -17.70182 | -53.26786 | 2026-01-25 04:50:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19537ab1-4213-3e91-b444-37651ee8409b | -19.67909 | -57.18358 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 532a146c-fe64-3993-8ebe-06093324b265 | -19.61556 | -57.27599 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a9332e7f-5dd2-3c4f-99be-0ed057e48564 | -18.81874 | -51.60512 | 2026-01-25 04:50:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 816459cc-9070-3c82-bc3f-5b20335e2d2f | -19.62708 | -57.25196 | 2026-01-25 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
