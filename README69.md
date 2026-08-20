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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a021684c-a7e5-3e6c-a45f-847310a68c98 | -9.39369 | -60.56226 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0dbe51d-45d4-3ea0-87d4-80a3ad600130 | -9.15739 | -59.55241 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06c9c9c4-dc9b-3e8a-94ae-d77eb1bb7951 | -11.82602 | -58.84496 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 959c474d-161b-3a65-88b4-62e102b53ac0 | -9.417 | -60.42879 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eab71ff8-38a7-3f75-87f0-24718178fe48 | -10.39294 | -61.20654 | 2026-08-20 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36d762f9-fcc8-3ebc-b4a2-46794a6d57bf | -8.64494 | -62.83121 | 2026-08-20 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d4c2e5-b174-343e-9f14-f5d6b5204649 | -10.39214 | -61.21247 | 2026-08-20 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d65411c2-bbf2-3c0c-8447-20e77422b393 | -13.43435 | -57.06937 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c62a00e6-fb03-3262-a542-d45cf757b8ce | -9.32045 | -68.66872 | 2026-08-20 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8264e4f-6c7c-3cd3-b476-2b64cbba295b | -17.3372 | -43.6139 | 2026-08-20 06:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 967db843-78de-3585-9fb5-c9c18c987602 | -17.3372 | -43.6139 | 2026-08-20 06:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ea79d3c7-5617-3c0d-b9e7-f06a2d1249a1 | -6.34004 | -44.08158 | 2026-08-20 06:25:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6ae7f92b-c84a-35a3-91e6-626036565cd1 | -8.35719 | -46.33969 | 2026-08-20 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c1dde75d-b487-3835-aaf6-01a845fcb2e1 | -7.34826 | -45.82088 | 2026-08-20 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 2441d5b4-07ba-3123-9aa3-3f510954ef79 | -3.96116 | -43.11391 | 2026-08-20 06:25:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2742590-72d8-33cf-a651-febb3cb320f9 | -7.35779 | -45.82238 | 2026-08-20 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 31f450e2-e322-3d3d-a58f-e2f0138ab39a | -7.9714 | -44.65654 | 2026-08-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f6f2589f-fc90-36d5-82c3-4a79a13a202c | -7.34988 | -45.8104 | 2026-08-20 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ff06dd93-6535-310e-84bd-f5c75a346d78 | -6.42232 | -41.7659 | 2026-08-20 06:25:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fd6d2c84-f12a-3a5c-bc0a-2514f3e974cd | -8.71367 | -49.61321 | 2026-08-20 06:25:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 095a3bdd-f953-3081-a366-624208423340 | -3.9625 | -43.1051 | 2026-08-20 06:25:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 26cf2d0b-a93f-3763-ad9e-aec8710eb0f8 | -6.78076 | -42.8773 | 2026-08-20 06:25:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e094e1e2-dca1-38b5-adc2-b712a34da8a7 | -6.42187 | -43.06437 | 2026-08-20 06:25:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3123280a-8582-337e-8321-d968d343826b | -7.34663 | -45.83139 | 2026-08-20 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 25edabc8-8ee7-351d-b3c9-cb92c72837a4 | -7.96102 | -44.66438 | 2026-08-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 4087dfef-9b01-35bd-a617-fb1c9027e992 | -6.26697 | -43.27945 | 2026-08-20 06:25:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2bf555b8-e713-3761-9b21-8f0d012d9df7 | -7.96998 | -44.66573 | 2026-08-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a6babb3d-c162-3bb6-9a93-bf3aec2ed9c5 | -6.2683 | -43.27068 | 2026-08-20 06:25:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 496d4c95-4ab5-344b-8152-f8accd49fbe3 | -6.77944 | -42.88605 | 2026-08-20 06:25:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 16830346-5ed2-3a38-8c07-7efdaec82392 | -17.32965 | -43.62591 | 2026-08-20 06:27:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 141.6 |
| a3d8b3f8-0e2a-32e8-8a77-789653143db0 | -13.43994 | -43.84548 | 2026-08-20 06:27:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4f55db89-c1e3-3083-afb0-f59a0f4e43b2 | -11.31896 | -45.2074 | 2026-08-20 06:27:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 54e176ae-7afa-3769-be38-31a5b2bc2289 | -12.79783 | -48.43226 | 2026-08-20 06:27:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a48aeda3-5bcb-3131-83b7-99f262bf8331 | -12.25704 | -43.16045 | 2026-08-20 06:27:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ea4df11e-0146-3657-a3b0-33422752568a | -11.38546 | -46.3707 | 2026-08-20 06:27:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ee343808-0d6a-3e45-9cf8-68ef808f9ed0 | -14.4467 | -45.6219 | 2026-08-20 06:27:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0d2834ef-36b4-3e83-b45e-34d840c7eb51 | -11.80681 | -44.80454 | 2026-08-20 06:27:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 09e355cf-a1da-39bf-b88b-67a0925f3b9c | -14.44812 | -45.61275 | 2026-08-20 06:27:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9f91bf83-da92-343d-85ee-fe45bf1e4b41 | -11.37615 | -46.36906 | 2026-08-20 06:27:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d554b57c-45cd-35cd-8c0b-1bd46a54899e | -11.81562 | -44.8059 | 2026-08-20 06:27:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97409119-0da3-39a1-bc90-248ae77f3958 | -12.79989 | -48.41999 | 2026-08-20 06:27:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ca0d656f-d395-30b0-979c-3f06fb611fe9 | -13.44128 | -43.83642 | 2026-08-20 06:27:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3d9633fa-429f-34c4-8c16-c0cd0960d95f | -17.33104 | -43.61608 | 2026-08-20 06:27:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 93cdd88f-dba5-3a1d-a769-143b2ebbdec3 | -19.65676 | -45.90497 | 2026-08-20 06:29:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8af42d8f-321f-3e92-a800-b4968c44df9c | -18.03809 | -44.60694 | 2026-08-20 06:29:00 | AQUA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ca0c9b0b-e3ab-3a0b-8a69-4999d757e436 | -20.56009 | -47.35571 | 2026-08-20 06:29:00 | AQUA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7a664b06-3314-364b-838d-dddf781e71cb | -19.65815 | -45.89572 | 2026-08-20 06:29:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b6da1a27-37df-3bfa-afbe-95c586274706 | -18.03672 | -44.61633 | 2026-08-20 06:29:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6e72815f-68cc-390f-b57d-1c83d758702f | -22.76622 | -47.74094 | 2026-08-20 06:29:00 | AQUA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e2631f04-9ef6-348e-a400-a9d2221f6052 | -21.35451 | -48.73133 | 2026-08-20 06:29:00 | AQUA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 84760b8d-0764-3dd6-9fa2-57c740616184 | -21.86512 | -46.57573 | 2026-08-20 06:29:00 | AQUA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f6710f43-86dd-3674-8127-b26c5c4d6553 | -18.02784 | -44.61492 | 2026-08-20 06:29:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eeb5c8a0-084b-306d-84d4-4ddb7a5d300c | -21.86654 | -46.56634 | 2026-08-20 06:29:00 | AQUA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 4d165be2-e707-357e-bdf8-f107908dccc6 | -21.87531 | -46.56784 | 2026-08-20 06:29:00 | AQUA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 1d661746-84df-3b41-89ee-8e9e536a9122 | -17.93847 | -44.40271 | 2026-08-20 06:29:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| da23a391-c542-386d-9e46-df01f5513165 | -17.3372 | -43.6139 | 2026-08-20 06:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a702fb28-fd23-3f71-a997-f82b2523728e | -17.3365 | -43.6383 | 2026-08-20 06:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 4960e4a4-6b06-307b-9a45-014f108b054b | -21.3561 | -48.7298 | 2026-08-20 06:40:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 21340442-f7ab-3d95-887d-c35804242dc9 | -17.3372 | -43.6139 | 2026-08-20 06:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2f7e18e2-da8d-3840-8ca9-25b9a1129204 | -21.3767 | -48.7249 | 2026-08-20 06:40:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1d1e4893-f06c-3af0-9a82-2c022ab29220 | -17.3372 | -43.6139 | 2026-08-20 06:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4b038ee6-0b49-3d29-a4f2-3ce0c3dc134e | -17.3365 | -43.6383 | 2026-08-20 06:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 17c254d1-5261-3d7b-9a57-0dbe14cac849 | -9.4257 | -60.416 | 2026-08-20 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f96b9301-2030-3b4d-813c-191096501c5f | -17.3372 | -43.6139 | 2026-08-20 07:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e7bc40fb-a369-3997-96fb-783b8a1a1a71 | -17.3372 | -43.6139 | 2026-08-20 07:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 59475790-4a93-3350-8b43-b486ecace2bf | -17.3372 | -43.6139 | 2026-08-20 07:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d2f4d9d7-b1d2-3de8-b0da-b21af22af74c | -9.4257 | -60.416 | 2026-08-20 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ddaab2a9-5ae7-3181-9f9e-f30ecf2fe472 | -17.3372 | -43.6139 | 2026-08-20 07:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| cc60fa3e-82a3-3859-9eaa-03768d3b8f8c | -17.3372 | -43.6139 | 2026-08-20 07:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8750c331-9d86-3e8c-b321-64f3dbbd40f9 | -17.3372 | -43.6139 | 2026-08-20 07:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| da4295e2-4abb-3d54-aa99-f70e7fedd605 | -17.3372 | -43.6139 | 2026-08-20 08:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5373d92a-acbc-35af-89f3-c3a589ac0772 | -9.1053 | -60.9241 | 2026-08-20 08:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 56bae62c-18ed-3849-bbd3-76daf6d43227 | -9.38458 | -60.55935 | 2026-08-20 08:03:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| b876bae9-8af4-35bf-bd13-750a7f3c467b | -7.86916 | -63.76238 | 2026-08-20 08:03:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b2dbe9be-a911-323c-a6dd-bbf936d410e4 | -9.2087 | -59.78024 | 2026-08-20 08:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 64e70918-40cd-3dd9-afb8-786b35242216 | -9.21066 | -59.77352 | 2026-08-20 08:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9137e86d-2df1-3004-be09-d91cc9dd74bd | -9.10796 | -61.59615 | 2026-08-20 08:03:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| cf0c6faf-9138-3201-b123-006f3140723a | -17.3372 | -43.6139 | 2026-08-20 08:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f4b38064-2e84-3031-97ea-4567b4f7a1e9 | -17.3372 | -43.6139 | 2026-08-20 08:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 70755800-8a69-36cb-aa9d-3c3812f1c93b | -17.3372 | -43.6139 | 2026-08-20 08:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 623d032d-dda5-3ae6-96b0-cdf2f3f4bd08 | -6.167 | -45.235 | 2026-08-20 09:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 41dab278-4741-395d-adb7-848474b3559f | -6.2353 | -55.4118 | 2026-08-20 11:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7e325be4-57e5-3144-a154-0147206b9e68 | -7.2628 | -49.8853 | 2026-08-20 11:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| c70c9ad9-a30d-3c02-a5a4-1e0084776257 | -7.12221 | -47.49621 | 2026-08-20 11:34:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| facbd419-4da9-3315-9eac-87a37fdeb232 | -7.35408 | -45.82041 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b9f85932-1697-3aee-aa33-7a6ec61a4998 | -4.72227 | -42.76911 | 2026-08-20 11:34:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7510c5f2-ad1d-3789-a658-98b69c3a0561 | -8.02044 | -44.15058 | 2026-08-20 11:34:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ff174945-84a3-3e1d-a5f6-48ab1b258e32 | -7.71127 | -46.15559 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76aaec18-0b24-339f-aa3a-75da442837a6 | -7.35266 | -45.83002 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 88bf1927-4e77-340e-a1c2-21909f42bdad | -8.01162 | -44.14934 | 2026-08-20 11:34:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 88e8a287-2876-34c2-b23f-7a78efe6f71b | -6.29657 | -43.638 | 2026-08-20 11:34:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 703ec595-10aa-314d-8310-cdd0da5fa424 | -7.71911 | -46.16678 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| deeddc48-bc28-3a38-95af-e9e3f6b38ba8 | -5.83942 | -42.62982 | 2026-08-20 11:34:00 | TERRA_M-M | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bf15ab0c-5d6f-34f6-9d53-0fcac0dc6d03 | -7.158 | -44.06342 | 2026-08-20 11:34:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 70fc3731-09cf-313c-81af-e3ab046a45ce | -6.7824 | -42.87387 | 2026-08-20 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1d6f9495-aa9f-3ae9-9ba8-c858298cae74 | -6.78113 | -42.88295 | 2026-08-20 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 50c7cfa9-23c2-3541-a080-7c8fc1a376d2 | -7.7098 | -46.16552 | 2026-08-20 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1fb3bc78-6a00-3a74-9a7e-83ec9232a563 | -7.60678 | -45.16649 | 2026-08-20 11:34:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6e829296-998d-3f69-96ce-47048c74f828 | -5.80593 | -43.64015 | 2026-08-20 11:34:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 40e8c16a-ac32-3458-9c96-0b6af1ebd185 | -5.73888 | -43.27399 | 2026-08-20 11:34:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README70.md)
