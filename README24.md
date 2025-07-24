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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e9001d-17e9-3675-b365-bd91a6664f6f | -14.76958 | -48.27453 | 2025-07-24 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88e6826f-7ad6-391b-9fbf-2de6a8b3f4cc | -19.05814 | -48.33673 | 2025-07-24 05:06:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7802231-a453-3d43-a669-7fa77091c993 | -12.27082 | -63.80082 | 2025-07-24 05:06:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dc2f584-8ff4-3fa3-918d-f439abd9d3b4 | -12.5778 | -56.96974 | 2025-07-24 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43d4c092-5067-3dd0-9bbc-53278125efb2 | -12.49539 | -57.77264 | 2025-07-24 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8055cc1c-c10d-3849-b9b1-3275c10b1e73 | -17.81065 | -52.66615 | 2025-07-24 05:06:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b46c4ed5-8ac1-3d24-b9f4-b86924d1f44f | -18.40411 | -53.32808 | 2025-07-24 05:06:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cea01aaf-805f-3ec0-929b-fbcd4bdd3fbf | -11.94881 | -58.762 | 2025-07-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c48a38ef-7515-34e0-9bd7-5a6f4e088ec8 | -13.74564 | -45.92214 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e6f4aef-7868-3f63-8a17-5cd04940b788 | -15.63002 | -58.18645 | 2025-07-24 05:06:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8966be6-8d1c-3c75-9e03-c28765140267 | -13.21944 | -51.08252 | 2025-07-24 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 495b3509-cc98-3360-b405-860b0b76f392 | -14.37396 | -50.33104 | 2025-07-24 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee5c52d2-a624-3a15-98ae-739d2f3d3c59 | -11.9476 | -58.76945 | 2025-07-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad009564-b8d9-3356-a457-a18038706964 | -13.70291 | -45.69499 | 2025-07-24 05:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c485e6f9-85e7-3b26-b96e-99eebe305afa | -23.91884 | -49.10134 | 2025-07-24 05:08:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33ce6ebc-2b5f-3ebb-8169-f7cacbf62212 | -21.75612 | -52.75012 | 2025-07-24 05:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b0505f4-2004-3756-bd62-9636ad087d85 | -21.49772 | -57.06428 | 2025-07-24 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51532d37-b95d-3f45-b24a-19a8df17284d | -23.00883 | -48.91049 | 2025-07-24 05:08:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6e02c488-242b-3c12-b1aa-2576d873a0a3 | -22.87153 | -47.09852 | 2025-07-24 05:08:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cc67775b-bddf-35c7-b62b-13185d00870d | -20.40314 | -54.63333 | 2025-07-24 05:08:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6526ac4-6029-3b9f-a1a8-7fc6d2b0a37f | -23.29814 | -46.12666 | 2025-07-24 05:08:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2aeb6498-6f40-31d6-8a9c-c770b471aad9 | -22.39881 | -49.79227 | 2025-07-24 05:08:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3daadc28-195f-3947-8235-ab46f9913ce9 | -20.47747 | -53.67668 | 2025-07-24 05:08:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dde99d65-4de2-3ab8-8801-df8d45da600c | -24.1097 | -48.57114 | 2025-07-24 05:08:00 | NOAA-20 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5fc86afe-b9d2-3676-8059-a65acb415ab4 | -21.49714 | -57.06835 | 2025-07-24 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f968b93-4680-3503-b78e-21e67d5171d2 | -23.0146 | -48.91084 | 2025-07-24 05:08:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0caa957-77cb-3755-bcca-718f36cb1c4d | -21.48097 | -57.10732 | 2025-07-24 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ac3d469-e642-3e4b-aa89-1f39965501ed | -21.30881 | -48.57101 | 2025-07-24 05:08:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9cab328-e221-384f-ba27-f0ad17eabc7a | -20.28825 | -55.49268 | 2025-07-24 05:08:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10c528ff-003d-3a60-bd0c-a1c09e85440d | -20.2869 | -55.4948 | 2025-07-24 05:08:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e31c17bb-6e6c-3fe4-882b-7b195a7cc317 | -23.29765 | -46.13329 | 2025-07-24 05:08:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9270c27c-53b3-3618-bab4-61724718c8d2 | -21.30923 | -48.56679 | 2025-07-24 05:08:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2da761c8-6bae-35dd-88af-25113ca3761f | -19.36755 | -52.03869 | 2025-07-24 05:08:00 | NOAA-20 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad8ec3bd-0934-38b9-a3b7-62b02a2cd2fa | -23.00845 | -48.91482 | 2025-07-24 05:08:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2cefae8-84d4-30e7-9207-1f95a81772b8 | -21.76443 | -52.75591 | 2025-07-24 05:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d28ffd3a-33ef-3cee-bdee-d65d7b1e6736 | -22.87112 | -47.10411 | 2025-07-24 05:08:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2b00d39d-2767-3f05-9036-96466ab03907 | -24.1093 | -48.57586 | 2025-07-24 05:08:00 | NOAA-20 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3a1d458f-88bd-3623-9830-971d8dc0f2ae | -20.28762 | -55.49725 | 2025-07-24 05:08:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f0b7af1-7a96-3fca-a630-7a7a9618a07c | -20.29471 | -54.07625 | 2025-07-24 05:08:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 628d3587-5ca8-33ed-97e1-381c297c5cb2 | -21.76885 | -52.75657 | 2025-07-24 05:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cba43419-19bf-3b8d-a87e-c8deafbb9ee1 | -21.36552 | -48.53273 | 2025-07-24 05:08:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fd65779-f904-358b-92ac-7aff7e1f4a7c | -21.36589 | -48.52884 | 2025-07-24 05:08:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fd938b4-02c4-3cb3-9de5-f255ddeb457f | -18.44625 | -54.67348 | 2025-07-24 05:08:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc9718ba-11bc-323a-894e-ced20532f08c | -22.25802 | -49.5773 | 2025-07-24 05:08:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6af2bec2-82a9-3ef2-b624-d89e7751e8d9 | -20.40205 | -54.63138 | 2025-07-24 05:08:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3344f46e-f764-39f1-b979-1789ad66c30b | -22.39845 | -49.79597 | 2025-07-24 05:08:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fdd21147-f9e9-31dd-acf6-16f8483056d1 | -23.30013 | -46.12833 | 2025-07-24 05:08:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5bc670b3-8da9-3017-b6e6-e170947946be | -21.30972 | -48.56926 | 2025-07-24 05:08:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b588cb5-4253-39cc-9141-6a225be861cb | -7.2597 | -43.0645 | 2025-07-24 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 7e1de4ce-2c2c-3a04-90ee-eaf9c1998a76 | -3.1649 | -49.4435 | 2025-07-24 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3693e113-a467-322f-a61b-f0d8518651cb | -7.2408 | -43.0664 | 2025-07-24 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 52b6c4df-03ca-30c9-849b-fdeb3986f0a0 | -3.1648 | -49.4648 | 2025-07-24 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3c855b1c-5e6b-3a8a-875f-0c6667b6b0e4 | -3.1833 | -49.4429 | 2025-07-24 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 85f483b3-5c0e-331d-8553-612191f627eb | -4.0569 | -42.5118 | 2025-07-24 05:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 2f8b04e7-2323-3818-a7f0-1e4fb778a167 | -3.1832 | -49.4642 | 2025-07-24 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 845692e8-a882-3763-9630-7874529909c8 | -3.1648 | -49.4648 | 2025-07-24 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1230653f-67fe-3f4d-ae01-5d0d356f40ed | -7.2594 | -43.0881 | 2025-07-24 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 8a62e6d8-594c-3a1e-8ac3-ee6865454542 | -7.2597 | -43.0645 | 2025-07-24 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 2af7fa9e-2d5d-30c6-844f-ff066434423e | -3.1832 | -49.4642 | 2025-07-24 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2a8e1148-fb84-3f7f-bda8-2ad6bfe933cf | -3.1833 | -49.4429 | 2025-07-24 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4b862549-5986-36a7-b646-db65c1e4da77 | -3.1832 | -49.4642 | 2025-07-24 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 153a0ae0-6212-301f-b27c-81c7b77ac939 | -8.569 | -63.8967 | 2025-07-24 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c2ce1391-11c2-3935-9fe0-406a5673c85c | -3.1648 | -49.4648 | 2025-07-24 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 0dbc2f6d-0e29-36fa-905c-80a6337259ba | -8.5691 | -63.8779 | 2025-07-24 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 223ce810-38fa-391e-b295-170ae02bd946 | -3.1833 | -49.4429 | 2025-07-24 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 07749154-8323-3beb-8c48-9dbb229e1d8f | -7.2594 | -43.0881 | 2025-07-24 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 0284a05e-3f54-379c-87d3-a1589e4713be | -7.2597 | -43.0645 | 2025-07-24 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| cb66ff64-d073-3efd-b68a-b3a77bd4fc64 | -3.1832 | -49.4642 | 2025-07-24 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 9e7f9ea8-a378-3abe-bdc5-6b6dc49e4990 | -7.2597 | -43.0645 | 2025-07-24 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| d1f2e9ae-5d32-3161-9e07-9b59c5451e07 | -3.1833 | -49.4429 | 2025-07-24 05:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8fd0b650-7b39-3aed-8e57-e9ac139d16a0 | -3.1832 | -49.4642 | 2025-07-24 05:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 4b51b59b-b358-3393-86c7-b473d93bdfd0 | -7.2597 | -43.0645 | 2025-07-24 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 5d2047e2-7712-3f9f-8e12-82a2dc22fc4a | -3.1833 | -49.4429 | 2025-07-24 05:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 091262f7-bfcd-327a-a7aa-52d2cdb17b0f | -7.25458 | -60.18733 | 2025-07-24 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96e4a2c2-e33b-39aa-b96d-1b7fc6d162d8 | -9.89105 | -68.36803 | 2025-07-24 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 178db9da-ee3b-3d70-9bb3-c820d83b8dbb | -8.61405 | -64.03658 | 2025-07-24 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 419a1806-69c9-3ee9-9d73-87f1946972a4 | -9.76116 | -65.09091 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9785eea-12e5-34ab-a28e-db17ea8b171a | -12.02227 | -62.80778 | 2025-07-24 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 333c97b1-bded-3d64-9bb0-4f0528eb6437 | -9.37582 | -66.57761 | 2025-07-24 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83f3058d-f4d4-3d4d-bdab-fcf73240a012 | -8.77044 | -63.78269 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d11e64fb-a6c6-3596-af91-077912bd9da2 | -9.025 | -61.23177 | 2025-07-24 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f25ffb80-1afe-32bf-a812-37eeac79eb16 | -7.45682 | -57.6678 | 2025-07-24 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce73310d-bd48-3c77-b3a0-6e6687b972d6 | -12.43719 | -63.69824 | 2025-07-24 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc342d5-d56d-369a-8651-fd51cad8e7db | -8.56519 | -63.88552 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 273cbee8-7214-3a9a-9dbe-424ae4284241 | -9.37936 | -66.57816 | 2025-07-24 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f5d807a-4d35-3958-87a2-1f752b8c40bb | -7.97882 | -70.9936 | 2025-07-24 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20618805-556f-3277-8e8f-a92364228ec9 | -7.27733 | -60.17479 | 2025-07-24 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7654666d-686f-3da7-ac12-08c3a5941f6c | -9.7626 | -65.0934 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63b6a8ab-161e-3b87-9cbc-0ed3dcac1566 | -10.29688 | -60.54342 | 2025-07-24 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b54757cc-ebc7-3db6-a4d9-7cb5e804f7be | -10.85069 | -61.96743 | 2025-07-24 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbf2d26a-f4d2-3622-8e5a-aa10c8f13814 | -7.255 | -60.1843 | 2025-07-24 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e915167b-2625-32a5-922c-b3b08c20fc7e | -8.92526 | -63.80841 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac86b585-885b-3f29-93eb-c0d4b67155c8 | -9.20793 | -59.67933 | 2025-07-24 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c1f05ee-f2e5-398e-879c-7f4de7d31bc6 | -10.12197 | -57.77236 | 2025-07-24 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bc859a2-5167-34c7-a9da-151e1dcbbaee | -10.09435 | -63.32259 | 2025-07-24 05:55:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68ef1b0b-dbad-3a75-8d41-ee33e51dc32c | -8.99253 | -63.85967 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e326670-3c25-3d9d-b20b-915f16db8295 | -10.04976 | -59.0964 | 2025-07-24 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8e3eba9-e686-35b5-a1ce-f97b5fcdadee | -10.85073 | -61.97059 | 2025-07-24 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5375e1a5-1e74-379e-9f92-e377abad63b4 | -9.37464 | -66.58566 | 2025-07-24 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 721e31d5-7448-3d71-84a0-9e7d806eac47 | -8.74913 | -71.0287 | 2025-07-24 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
