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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c09e538-abf6-30a4-a194-a3b8f95a6a00 | -12.74318 | -44.56388 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e24a8d4-f740-3a0d-82f3-da255f9c49bd | -11.911 | -43.38475 | 2026-07-04 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1519a9f7-0d42-31be-b01c-930e18689b72 | -8.081 | -46.70566 | 2026-07-04 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a31a7adc-0681-322c-991c-bf034a6b220c | -12.74937 | -44.5286 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 627e785d-7e55-3bcf-950d-7f456507c0f1 | -8.03434 | -46.71452 | 2026-07-04 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bb5e99a-3b59-3ffe-8708-b99b3eb20e27 | -7.00977 | -42.78112 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a47d8c4-44c2-37df-99cf-563bf058a4c5 | -12.76356 | -44.56234 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e204646-6194-38d7-9a5f-143d10c830ed | -11.4349 | -46.56675 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b450c5eb-9d46-33da-ae4a-7a5cab8bfef3 | -12.74636 | -44.52287 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3c0d9be4-828e-3f74-a1f6-bb1682a2baa2 | -12.74548 | -44.52788 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 11aba6bb-d6a0-3aee-a0da-61cd2db55433 | -12.75099 | -44.56526 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 131c5069-ca50-3093-803e-1fb8d995d160 | -11.45545 | -46.55672 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06395995-046c-3919-8898-075e1e257ad2 | -12.74673 | -44.54366 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ac244e9-b3cb-36dc-a84c-09e88971f1c5 | -7.00596 | -42.7805 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b14d1dbe-2aa7-3e57-8fd3-508091aef134 | -11.92282 | -43.38237 | 2026-07-04 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96d110df-8896-3116-a874-615977d5bac4 | -6.90642 | -43.71759 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edd2a961-ccbd-3bb1-bdd0-bc43c4627129 | -6.93596 | -43.71531 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d46d01c-afa7-3345-badb-86ae6a34da31 | -12.75414 | -44.5243 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9c96a80-517d-39a1-9258-05745aaa898e | -12.73716 | -44.55237 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b501e6c6-94f4-3c3b-b7ce-6b2e7d350f46 | -10.92661 | -43.04345 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 435da473-cf7c-3fdf-84f4-fb4c390dc136 | -10.98038 | -43.70782 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcb12054-1301-3840-8ab4-be3a4d4701b7 | -9.43658 | -40.32032 | 2026-07-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| acc5016e-527a-3773-9c3e-6cc221dac7e2 | -8.4434 | -51.5686 | 2026-07-04 04:00:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcde420b-7c27-39f4-ac42-332544bfe0ad | -11.91199 | -43.38661 | 2026-07-04 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 032756d8-b33f-38e8-ac38-5de4298f6a2a | -8.02876 | -46.24076 | 2026-07-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4264699-4c02-3393-b1b0-43752ad4dc52 | -12.74886 | -44.55445 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d79c585-5f4f-3fc9-81c6-f504e4b1291e | -6.90917 | -43.65213 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68cd3302-52de-3890-912f-492aef44f78e | -12.75714 | -44.53005 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 04190e26-0887-3f53-94b4-3a6a2a0d2f92 | -6.90237 | -43.71692 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db58032b-f3c6-3fd0-8b16-5d4d47e3b476 | -7.0091 | -42.77888 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7075f641-d829-3945-bf59-0f10089727cd | -7.0037 | -42.77035 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ceeedd21-d04d-319e-adf5-df56bc478499 | -12.74407 | -44.55881 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1daebd94-54a7-3eae-b2d2-99edddee846d | -7.90283 | -48.24908 | 2026-07-04 04:00:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afc1274d-e50e-30cb-a919-ebece791db3f | -7.00673 | -42.77574 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 478f70c1-1fda-3761-83ba-a3f04783b1c1 | -8.72162 | -47.83865 | 2026-07-04 04:00:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de2a185c-5415-39a3-87b5-80644bde165a | -11.453 | -46.5486 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6deaab84-a888-378f-9b44-d3c06be2dc1a | -7.23018 | -43.20404 | 2026-07-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74b9b488-c42c-3953-bbad-1cadeae49702 | -10.98418 | -43.7085 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657a57f8-249e-39cb-940b-f9205cfcb806 | -12.75802 | -44.52503 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4ae5902-9fb8-3228-8a74-34bdf9529f8d | -12.35348 | -47.90382 | 2026-07-04 04:00:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b713e78-aab0-3034-8b81-eac4ff0336c4 | -6.93192 | -43.71459 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4a47b69-f139-3c5c-93d8-c9bc37a5b2af | -12.75363 | -44.55011 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 016b35b1-b1e0-3a1c-961b-f71c956cab17 | -12.7515 | -44.53935 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 244888a0-3edd-3d28-8890-fe50cf0a2c3d | -12.74247 | -44.52214 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d61f0d9e-a678-3bf4-b069-818cdc5db8bd | -7.73127 | -44.17515 | 2026-07-04 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79173ba5-fb00-33ed-b79e-12da430de6f7 | -9.4405 | -40.3173 | 2026-07-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 4b94b2dd-cf19-3015-a107-e224ea60f70e | -12.7584 | -44.54581 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 32ce3f7b-11f7-314b-b6eb-bee6140a8bf9 | -10.98382 | -43.70548 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b39609c5-78f9-3cb2-9581-6367dadddd00 | -10.93245 | -43.05354 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3303d1d6-9318-3bcc-b674-3a39e9439a35 | -12.74159 | -44.52715 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ba23c50-3fbf-3658-b98a-b25864266f70 | -8.02973 | -46.24289 | 2026-07-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3e59fb23-60ac-3b8f-aa0d-c8463c260afe | -12.75577 | -44.56091 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 428f28c3-efe2-380d-9085-4504d8bfeef6 | -12.75966 | -44.56162 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b39ac4d3-c1dd-3fe1-875d-f2754bd2f031 | -7.8968 | -48.25162 | 2026-07-04 04:00:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d92cf8ce-93f8-327f-b0c8-579a62417ed5 | -12.76531 | -44.55229 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d11efb81-2c6b-3aed-9d8f-6b4c691a93e5 | -9.44154 | -40.33215 | 2026-07-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| bb06773a-2fe3-30c6-bcdf-b127aa0ddf6e | -6.92847 | -43.71031 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a6b6d79-73e1-32f8-8c97-1b0585b1d294 | -10.92953 | -43.0485 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 92e13956-9142-33ce-be82-1db25bc11add | -11.44022 | -46.56326 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 823d5d24-68e8-3b13-8c6f-985ae6676f77 | -8.03538 | -46.23855 | 2026-07-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 557a15c9-3fea-39a8-832c-a23582247663 | -8.03073 | -46.23741 | 2026-07-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ad8c456b-41a4-3654-bf8e-bd46d2810d9b | -14.2061 | -45.42681 | 2026-07-04 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9da0a90-9aac-3fb9-a481-d0f784ea1673 | -13.24807 | -54.3457 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 03545b81-70a1-3443-89f1-8b4c58701c6f | -18.77111 | -47.62294 | 2026-07-04 04:02:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e0fd3bf-3aee-3217-9b97-eb4a496e69da | -14.16383 | -47.78609 | 2026-07-04 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c09e44c7-e2ec-36fd-ac81-93ea85417ba7 | -13.22748 | -54.37125 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b23bb27-2f57-310c-977c-961fde9333f9 | -21.29578 | -41.44184 | 2026-07-04 04:02:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3e37e3a5-7c07-3382-ac1f-fa5c8660a39b | -18.71661 | -47.53777 | 2026-07-04 04:02:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ee78f7f-b5ad-303e-bf12-67f54829a470 | -19.74298 | -44.07396 | 2026-07-04 04:02:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c15c967-066f-3b23-8027-fd7bb356ed63 | -13.24253 | -54.3372 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d4bfe713-8fc6-3e5b-ae99-38f6265adc4e | -18.52032 | -42.7266 | 2026-07-04 04:02:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e937665-e4bd-3260-9f68-8af4bc31ce11 | -13.24508 | -54.34375 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b3ce859f-77d2-3a05-afde-1dd650c25672 | -13.22041 | -54.36954 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5a5115a-886c-38df-be04-c97f638b4b62 | -12.5235 | -48.28933 | 2026-07-04 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e65771a-09b4-34af-a171-49e4342f4f89 | -19.57889 | -44.05273 | 2026-07-04 04:02:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c781a5ac-efe7-3c03-adce-5eef61ba6b77 | -18.13183 | -46.46381 | 2026-07-04 04:02:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ce3be9d-c077-3bbc-96a3-e49a4e6b92ba | -16.11501 | -42.30166 | 2026-07-04 04:02:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4510ff84-211d-387e-b685-3baaae769d1f | -18.77316 | -47.6268 | 2026-07-04 04:02:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 793f8283-d182-367d-a7e8-9c2bd6c127db | -13.2221 | -54.362 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23fe2aab-deae-31ce-ad6d-d4512d6598a3 | -14.20675 | -45.42321 | 2026-07-04 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed80f933-65c4-3a8d-896a-b08c60ea7881 | -20.39354 | -46.56218 | 2026-07-04 04:02:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 177278f4-8700-3f29-82a5-7d2729fb6aac | -13.24597 | -54.37405 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7949326-18bc-37af-8b13-4a3e2c734f39 | -20.44521 | -43.52762 | 2026-07-04 04:02:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6fe7e38a-d412-351d-9c42-62b8c52e8c14 | -13.23457 | -54.37289 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7fd1e82-6f59-38dd-ae80-95db2e7b4ce7 | -13.25068 | -54.35225 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 04e82a38-a73b-38be-87bd-afd35372b3e9 | -13.25519 | -54.34716 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8e999304-0199-3881-af8e-c1290dfc753a | -12.67579 | -48.22063 | 2026-07-04 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd2efeaa-2c77-38f2-9f70-f8d7aa63ffdf | -13.23133 | -54.38739 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 414fcb4d-e66f-38a5-aef1-5c67444b121f | -13.24357 | -54.35075 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0022c893-3dc7-3857-a45f-f0e92fa53614 | -20.08583 | -43.69926 | 2026-07-04 04:02:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ad37da2-7199-3078-91ef-fe782c862c41 | -17.54677 | -46.94612 | 2026-07-04 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18d5977b-3edc-385c-943e-f2f4b94420d1 | -13.25364 | -54.35413 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 778eefea-cf0e-3e04-b955-2333ab46df1b | -12.52405 | -48.28641 | 2026-07-04 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1874438a-695e-3ab4-8e01-7fb5ba229039 | -13.23886 | -54.3725 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b35ac168-9b59-3eb3-911b-d20abc9eeb26 | -13.22542 | -54.40018 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a12b57e-4553-38ed-8876-fe807e8e311f | -12.50963 | -48.2532 | 2026-07-04 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe9964fa-2b00-3a4d-8ae0-b64cfbd63bbc | -13.23731 | -54.3797 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 701f8d6b-e6a3-369b-b684-41a43fb69d14 | -20.55693 | -42.10037 | 2026-07-04 04:02:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1877811b-5649-3caf-8093-ed8ba44dc800 | -13.22703 | -54.39273 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e414220-bbfe-3390-8166-823d8754d807 | -13.24652 | -54.3527 | 2026-07-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |


[Clique aqui para ver as próximas entradas](README11.md)
