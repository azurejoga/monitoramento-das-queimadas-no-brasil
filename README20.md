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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55c5af3c-603d-3d0f-9b2a-f5794c8b9ad9 | -16.01216 | -43.27532 | 2025-08-12 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6228100e-d609-3649-8156-0d9697dd11aa | -17.6345 | -46.67205 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c7a8105-ea94-3bd0-8302-d0f759306715 | -18.47701 | -48.5147 | 2025-08-12 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b781a887-73b1-3ce8-813d-3f794d4950ba | -16.28804 | -52.91052 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 34b14677-edee-3a46-9b0a-c92e5744e171 | -17.64077 | -46.67734 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 3b20c565-92f8-36cb-960e-152d895b8a13 | -17.64008 | -46.68135 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| add0acb7-0777-3923-b715-34c87f70d5cf | -14.73552 | -46.30088 | 2025-08-12 04:10:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b86e53af-f5b4-32c4-b43d-a3ef85cb6790 | -17.64908 | -46.67061 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 94693483-a51b-3897-a446-046bd0d6386c | -17.5671 | -45.33245 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2a4aa079-70e0-3c0b-bdc9-edad48f68513 | -17.65187 | -46.67525 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c2965e85-e713-3d88-afe1-db6a65b70394 | -17.65603 | -46.67188 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b3f41238-8856-36b3-9451-3785939c06f2 | -17.6533 | -46.68792 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4c983b10-93f9-3942-8ecf-4097bec4e9e7 | -17.64771 | -46.67863 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e6911b05-1cfb-3074-bfc0-b8855e2cc4f7 | -18.89582 | -46.96092 | 2025-08-12 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e3003c0-4ef0-33fa-8f60-8612b01d5d2d | -21.30884 | -44.26173 | 2025-08-12 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2cf6c2e3-002f-32f9-a189-888308ef1dac | -17.64287 | -46.68601 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 358e2c1f-4df7-338e-9c08-bb8d678a200c | -17.65051 | -46.68327 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 635a6501-bec2-361e-942a-0f164515ea5b | -18.37957 | -44.4845 | 2025-08-12 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0c902e4d-470e-3554-84e2-9852225ce879 | -16.29612 | -52.92342 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9a79e29-0b3f-3e35-8427-6dc721571288 | -15.44879 | -47.01307 | 2025-08-12 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dae4c571-2f5b-33d6-b015-d8bf297c6f51 | -19.38937 | -48.89895 | 2025-08-12 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e355f751-87e9-37e7-81ff-1cd6d5afc596 | -15.45774 | -49.63801 | 2025-08-12 04:10:00 | NOAA-20 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8db530d0-4de0-300d-8796-b92376624855 | -19.33362 | -44.4192 | 2025-08-12 04:10:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efcc2bc8-fabd-382b-859f-12cfbba33423 | -16.29758 | -52.91614 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e18ed7ac-98f4-3edd-948e-436825f8e7b9 | -14.73985 | -48.3927 | 2025-08-12 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8795b93d-0b10-33f3-a6c2-4d7acf83438b | -17.96405 | -44.29874 | 2025-08-12 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 917b3090-227e-3dff-9ccc-06d67bd3f059 | -17.65256 | -46.67125 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 42754126-ecdf-3d04-89ae-79e3611d5137 | -14.68857 | -53.72479 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f3818a0-5e33-3c29-b154-0e85deaa9135 | -15.76839 | -47.77085 | 2025-08-12 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44404c23-94ee-3632-a85a-a1ee6d8303e0 | -20.48532 | -42.24577 | 2025-08-12 04:10:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0462edc9-fdf8-356f-892c-e54fc6b25100 | -17.87287 | -44.4239 | 2025-08-12 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4a6862f-c247-371f-a135-db450d8eb04b | -15.45447 | -49.55995 | 2025-08-12 04:10:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 843009f1-c15a-3eba-9e6e-290c2f33d78f | -19.29847 | -48.43146 | 2025-08-12 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6625117b-2afa-3d39-81e0-9dfa5880e9f0 | -16.30267 | -52.91739 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ec690f3-85e4-3a66-9b14-9cf3458cfc51 | -16.18652 | -43.6385 | 2025-08-12 04:10:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0683c439-4614-3a36-9e83-5dd0c8fbd4fc | -16.28739 | -52.91372 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 579b61d6-8983-3288-9d4d-6dbb0de10e4c | -14.68381 | -53.71981 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7944dbd8-2b66-33b5-9b84-8e2da4d45836 | -14.50924 | -47.85472 | 2025-08-12 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71f73cdb-7c8b-3e04-997d-15332a107e27 | -17.65467 | -46.67989 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| cc3623df-3e83-3c37-abc6-f48e73a3a400 | -16.00664 | -43.267 | 2025-08-12 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d7fec9e-a77f-3722-9b6a-b6fda85a7cc5 | -17.64214 | -46.66933 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| da75b6cd-fdc9-306d-b09c-a2c7a3ca886d | -19.45434 | -45.30733 | 2025-08-12 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81dcd64e-0fa6-38e6-bd99-194c7f7ad774 | -13.07047 | -56.85016 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 136bf78f-1dbf-3060-af88-0f1637922161 | -17.66509 | -46.6818 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9fd191a1-cd3c-3636-b909-c35f7f2c1b94 | -20.99251 | -46.78349 | 2025-08-12 04:10:00 | NOAA-20 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0658dc84-5fa4-3976-8686-d20d6aa43770 | -22.97933 | -49.02956 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7586ea6c-03c6-3ef5-a276-8ed043f7101f | -22.98294 | -49.02735 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 37e24458-bd8b-3c04-955f-8fb8927a0e01 | -22.98213 | -49.0319 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0253690b-654e-3660-a7a6-c2b077440240 | -22.98739 | -49.02649 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 0c494cdc-329a-3a3d-8d2c-f11cd9770399 | -22.8768 | -47.23534 | 2025-08-12 04:12:00 | NOAA-20 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2565c0e2-9cac-33ee-93f4-9f255bc6a038 | -22.98573 | -49.03556 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f4216c4-68b5-3258-b5c7-a664f0e57416 | -22.65653 | -47.80029 | 2025-08-12 04:12:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b532650-2851-3269-8d17-7878ce5d6aef | -22.65582 | -47.80437 | 2025-08-12 04:12:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a45d1fd5-279c-3bb2-a2a7-9fc7bd0a9b6d | -22.98656 | -49.03102 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 8c131631-2025-39fe-99ac-f90dfc7a9cdc | -22.97852 | -49.03117 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 83715e68-1d77-383d-b42a-79909b1c416c | -22.991 | -49.02721 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 73ec58aa-a21f-3614-8355-1de03f971dd4 | -22.19196 | -54.76592 | 2025-08-12 04:12:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8f91074f-7444-3e8f-95fd-dc0aabdc65cd | -22.99018 | -49.03175 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 56e43eba-4504-3396-b0cf-8728f10e2594 | -22.99748 | -50.42135 | 2025-08-12 04:12:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ec8ae6f3-a5e4-3cce-94b1-d01a4dc3dd92 | -22.98377 | -49.02575 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 23e69ac9-a6f3-39ab-842c-c6b6b676552e | -23.27041 | -51.99142 | 2025-08-12 04:12:00 | NOAA-20 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| a196751b-a1f1-36d8-b4d7-11d1fe7c2e3c | -23.7207 | -51.29764 | 2025-08-12 04:12:00 | NOAA-20 | MARILÂNDIA DO SUL | PARANÁ | Brasil | 4114906 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a25f2f3f-7b6e-3bc7-ac77-80d289f9213d | -22.99359 | -50.42055 | 2025-08-12 04:12:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 518c6d92-c8fc-320a-bb5e-ce900ffd579d | -23.97977 | -49.65255 | 2025-08-12 04:12:00 | NOAA-20 | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9982cda-de41-36fc-9182-b47da887d1a3 | -22.98294 | -49.03029 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 927fdb49-1cef-3800-89fe-db55556c005d | -23.07675 | -46.983 | 2025-08-12 04:12:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8b2da837-d549-3deb-8afc-1c3c3e54c6b1 | -23.2033 | -46.01942 | 2025-08-12 04:12:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 31b8887a-5511-35e6-af7a-d073b896f13e | -23.26956 | -51.99572 | 2025-08-12 04:12:00 | NOAA-20 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e93eb89b-6960-389f-97f3-dfb763e2d4ae | -22.97932 | -49.02662 | 2025-08-12 04:12:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 88ac7186-51d4-329f-994d-d05d9617091d | -23.20271 | -46.02317 | 2025-08-12 04:12:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a52c756b-569a-3349-89fa-cc1e77ba54fd | -29.22205 | -55.63885 | 2025-08-12 04:14:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 93c2ba6c-c8c5-3c7a-bf41-ea90aeab0382 | -29.22419 | -55.63466 | 2025-08-12 04:14:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| b18beec8-5ea2-314a-97df-4e2717653f3b | -7.1299 | -60.1182 | 2025-08-12 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 2501cdd1-4aa9-3d8c-b490-ccd3e3d1ab7e | -16.2957 | -52.923 | 2025-08-12 04:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 17455ac3-8095-3531-b0ea-1b618906776d | -17.6544 | -46.699 | 2025-08-12 04:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9c634fca-9811-324b-abde-bc6fa86b67eb | -3.9686 | -47.8684 | 2025-08-12 04:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5fc38e11-4a45-3562-a1e3-58d7dcef6527 | -12.5742 | -47.0006 | 2025-08-12 04:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1f2d4faf-bb4c-3698-9b59-02f365c4e974 | -16.2961 | -52.9016 | 2025-08-12 04:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bb3bffed-c663-381a-a103-48c8964f38c5 | -17.6555 | -46.6523 | 2025-08-12 04:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 77a5353b-189e-3891-b967-7171ad0ec112 | -17.6549 | -46.6757 | 2025-08-12 04:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 344.1 |
| 030d1f3c-f30e-3c8b-8d32-5f49e7d2a90a | -8.9401 | -60.7288 | 2025-08-12 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 37ef3645-d70b-3ba0-86ee-2d9969be5800 | -17.6355 | -46.6565 | 2025-08-12 04:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| bd7db54f-5a3a-305c-bfb8-037c6deea0d5 | -13.3619 | -50.2423 | 2025-08-12 04:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 56427e0a-d700-37a0-a734-34b0fcd05606 | -7.1483 | -60.1174 | 2025-08-12 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| b7f349a4-e4a4-32ff-a122-d21f67c2a21c | -17.6349 | -46.6799 | 2025-08-12 04:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 136.0 |
| c47a4633-6664-3d65-9ac9-3a6926767785 | -17.6749 | -46.6715 | 2025-08-12 04:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 49fdebbc-deef-3923-bee9-4ead590421c4 | -3.9684 | -47.8901 | 2025-08-12 04:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 1e6d2fd4-b089-36e8-9c30-174eaa7c3884 | -9.723 | -49.4806 | 2025-08-12 04:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| abf9622d-a283-34e7-8228-04888e784b1f | -9.7041 | -49.4825 | 2025-08-12 04:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 952b9625-5bee-3b02-9dbd-0d7bfdc72a20 | -7.1298 | -60.1374 | 2025-08-12 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| bfe1cacf-c51c-30ba-9418-a835b95a3387 | -12.555 | -47.0034 | 2025-08-12 04:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2c33a4c8-f8f7-323c-9ae7-48bc3bda8f21 | -6.5856 | -44.564 | 2025-08-12 04:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 16cf22f5-8b82-304c-abe6-f44b97281094 | -13.3427 | -50.2448 | 2025-08-12 04:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 16cd7280-5548-3edb-9e73-e763ef336e65 | -17.6549 | -46.6757 | 2025-08-12 04:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 273.3 |
| 376e9c5e-f186-340a-9782-d2268d791129 | -17.6355 | -46.6565 | 2025-08-12 04:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c6d217b0-c8be-3537-aaec-4f449243c24f | -16.3157 | -52.8988 | 2025-08-12 04:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4be113e2-ef8e-3caf-bd52-17464b175894 | -16.2957 | -52.923 | 2025-08-12 04:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| fb32d73e-ccd0-3fca-ac0b-bf0ea01c8ea9 | -17.6349 | -46.6799 | 2025-08-12 04:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 8f393025-5f5a-3b2e-bf57-980239ee2e78 | -8.9401 | -60.7288 | 2025-08-12 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1f16d6c9-8c71-32d8-9380-104d9539f37e | -7.1298 | -60.1374 | 2025-08-12 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |


[Clique aqui para ver as próximas entradas](README21.md)
