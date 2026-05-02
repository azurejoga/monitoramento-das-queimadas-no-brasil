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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98638328-6611-3bd3-a8b4-06c1fd6e4a50 | -12.37756 | -50.04221 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b2607dda-45f8-34b5-b5e7-d86964d24f7f | -11.4453 | -55.10629 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4eb34d1-e539-3f42-ad71-c86af91bd915 | -11.44179 | -55.10215 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88a3c7c6-35b0-364f-b216-81715a5d88a0 | -12.28693 | -57.39506 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20a7fb5d-eab7-3e89-8c1b-604b50226efa | -11.43427 | -55.09743 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c95600a-98c7-35c6-91a6-f9b5f3f9aa47 | -11.55778 | -48.26671 | 2026-05-02 05:21:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70cbaba7-9234-3036-ba1f-29459b41469c | -12.2976 | -57.39666 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53813817-63bf-38d7-a79b-5c6ee683624e | -11.4413 | -55.10569 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be44bbdc-a439-339c-b4d7-6822b5e60ae1 | -12.29464 | -57.39203 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71050fa3-a2b7-3b7d-8a5d-db8e464a8e38 | -7.86627 | -61.49151 | 2026-05-02 05:21:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c742224-dd17-3b30-be82-3537287cf2f8 | -14.2066 | -57.42606 | 2026-05-02 05:23:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78d0c325-c578-395b-b667-5daa399ef7ed | -16.15497 | -58.48932 | 2026-05-02 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9c7cb4f3-dfb2-3c81-931b-87f9b9d6afdf | -14.20296 | -57.42555 | 2026-05-02 05:23:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fdc3cc2-e2a6-34a0-81dc-8ea8992ea03e | -14.20597 | -57.43037 | 2026-05-02 05:23:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c874c6ef-4395-38d2-8421-ce7b105c89f4 | -17.93201 | -52.89439 | 2026-05-02 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2453661-0101-30c0-b21d-41c1eecbdaf4 | -20.71488 | -55.17788 | 2026-05-02 05:23:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a07cab8d-0a35-3337-ada1-5f716fb76710 | -17.93059 | -52.89137 | 2026-05-02 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d36958c-fa54-3bcc-a235-90b5bff36c0b | -13.99637 | -56.63649 | 2026-05-02 05:23:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 437902c8-21e2-3bf8-977d-d8d70a6e955f | -13.99326 | -56.63128 | 2026-05-02 05:23:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5181b71c-e75b-32c8-95d2-5510fab69ed6 | -18.32612 | -54.52565 | 2026-05-02 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f5cb676-f905-3aee-b98e-152ac3f119be | -16.15438 | -58.4934 | 2026-05-02 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1ef1b982-4e7e-3685-9e41-fd51444609a0 | -14.21748 | -59.00018 | 2026-05-02 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c886148-3f81-3ab1-8151-37f64bac0959 | -18.49298 | -51.69048 | 2026-05-02 05:23:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 468914ec-957f-3559-9f32-328e8f04e143 | -17.93238 | -52.89121 | 2026-05-02 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bbed807b-53cf-322f-b6f3-aa1b58149aa1 | -17.93564 | -52.89228 | 2026-05-02 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d41ac8a5-d4a2-3d56-a6e3-7440b5ab57b9 | -18.31098 | -54.6515 | 2026-05-02 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d84d9030-73fd-3b21-bfc8-b815dc1ee5e0 | -13.99704 | -56.63183 | 2026-05-02 05:23:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6193bb16-e6c2-3f1b-a9bc-bd54cb3fbac7 | -21.95432 | -57.59628 | 2026-05-02 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de050f4e-c102-3a4a-99d0-a3086492adb4 | -21.95827 | -57.5969 | 2026-05-02 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5babe7e5-e5ec-358f-b9eb-6f30178b76a9 | -21.23324 | -56.92875 | 2026-05-02 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da0d4491-69e5-38fb-9b91-23d6ba10c54d | -21.66889 | -56.31271 | 2026-05-02 05:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ba5e79f-c74f-3256-8e32-3e9ec001e89c | -21.66838 | -56.31693 | 2026-05-02 05:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b050395-43e6-33db-b983-60999601f105 | -12.3887 | -50.0435 | 2026-05-02 05:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d9bb237e-2dc1-3c11-b756-4ecd807ac56c | -10.9815 | -45.0874 | 2026-05-02 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| be17593d-caca-3184-8fb4-cc859f28b18f | -12.3696 | -50.0459 | 2026-05-02 05:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 506ab832-b196-3cc2-bcae-627b8e983927 | -10.9815 | -45.0874 | 2026-05-02 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 362e9ed3-ce62-3e3b-a14b-8fca93d3a708 | -12.3696 | -50.0459 | 2026-05-02 05:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9df1bed1-17af-38c2-81b6-ef34f25c25b9 | -12.3887 | -50.0435 | 2026-05-02 05:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 89748846-8ba8-384d-9181-ebb7eca478dd | -12.3887 | -50.0435 | 2026-05-02 05:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| edfe47a5-6923-3f7d-9ac1-699b6ddd09f1 | -10.9815 | -45.0874 | 2026-05-02 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 55b5cc40-9560-3d17-b9e4-a54383bbfdc4 | -12.3696 | -50.0459 | 2026-05-02 05:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a5b95c2e-f708-3a49-b9fb-6e115ad7022a | -12.3696 | -50.0459 | 2026-05-02 06:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| eed99f4e-a0db-3c48-b7e5-b6d97677b952 | -10.9815 | -45.0874 | 2026-05-02 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a91fe2e9-d680-3610-b73a-4201b97b4db1 | -8.63726 | -63.99209 | 2026-05-02 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2f81b67-2c1e-35db-8f7e-ba9806f1f211 | -12.3696 | -50.0459 | 2026-05-02 06:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6514eb81-88a3-3c6e-a9ea-d902fe48a21e | -12.37 | -50.0242 | 2026-05-02 06:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 26c0b331-e026-3e33-9c98-5d230e4c8cf7 | -10.9815 | -45.0874 | 2026-05-02 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 88d26523-8506-3589-b21c-a6d8c30a2fe7 | -12.3696 | -50.0459 | 2026-05-02 06:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8a22949f-ccc1-3e7d-bbd1-2ab2e2a2ec46 | -12.3887 | -50.0435 | 2026-05-02 06:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| a591433c-81ee-313a-8dcb-5b15ba762e1d | -10.9815 | -45.0874 | 2026-05-02 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 66290a58-4cc6-39a5-aacc-6d914026ad0c | -12.3696 | -50.0459 | 2026-05-02 06:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c9603d58-6785-3399-a110-66559691f89a | -10.9815 | -45.0874 | 2026-05-02 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 06d80768-18de-3a18-b91b-ade31e9dcf87 | -10.9815 | -45.0874 | 2026-05-02 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 73d80f0e-0924-3e1a-b424-5e4144be575b | -10.9815 | -45.0874 | 2026-05-02 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 9083ddcf-cc8c-3d7d-a8b6-df5b11f3d15d | -12.3696 | -50.0459 | 2026-05-02 07:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 882e1bff-95e8-344d-bee3-a28694f088b7 | -12.3887 | -50.0435 | 2026-05-02 07:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c6ffc435-9c77-3a04-856e-8d7bd38434f9 | -14.20387 | -57.42627 | 2026-05-02 07:07:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 934fd0c8-c9e8-391a-873f-d1501a1691a0 | -12.37883 | -50.0186 | 2026-05-02 07:07:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 5d102d88-17c0-3261-adeb-056836dd09ce | -11.4447 | -55.10665 | 2026-05-02 07:07:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 04a7c2fa-ca5b-34ed-9fc1-3ff2a880cdcd | -12.37952 | -50.02602 | 2026-05-02 07:07:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| dba0fda0-50ae-31dc-b9fc-ca1cddc5cac7 | -12.37546 | -50.04567 | 2026-05-02 07:07:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 1808d471-09bb-3d72-9427-25213048d436 | -10.9815 | -45.0874 | 2026-05-02 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 4e15c11e-ef9c-3fb1-891d-0a93e234102b | -12.3696 | -50.0459 | 2026-05-02 07:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 6b1986f8-a6e8-384e-9a30-a94049c78ecd | -12.3696 | -50.0459 | 2026-05-02 07:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 52cb67cb-c761-3802-a5e8-d7ed03ab4a30 | -10.9815 | -45.0874 | 2026-05-02 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f291d1a0-feb4-35f6-b05d-b6389ea8fe52 | -12.3696 | -50.0459 | 2026-05-02 07:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7436bfdc-9846-344c-9438-f75abb22b036 | -10.9815 | -45.0874 | 2026-05-02 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 7cd5b89b-a9c3-3e6b-b0ee-1c88ab2d5f40 | -10.9815 | -45.0874 | 2026-05-02 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 74117384-55f9-3a8c-b7eb-57d13b51273a | -12.3696 | -50.0459 | 2026-05-02 07:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| dc461566-6c49-3521-86e1-930ce3586a04 | -10.9815 | -45.0874 | 2026-05-02 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 15576b90-7c14-3348-b0e6-83aba9f62df6 | -12.3696 | -50.0459 | 2026-05-02 07:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d97a940d-189a-3d83-abae-2dae78a8615b | -10.9815 | -45.0874 | 2026-05-02 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| fa17cccd-c660-3a42-bdf6-b24d44d67372 | -10.9815 | -45.0874 | 2026-05-02 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| baa2debc-dbc4-3df7-ade0-c425b4a333de | -10.9815 | -45.0874 | 2026-05-02 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 6b8d517a-414d-31da-b49a-7bf05b6922ed | -12.3696 | -50.0459 | 2026-05-02 08:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 0125d8a9-3ec3-3e4d-bd74-f2ed935ec9d7 | -10.97964 | -45.0901 | 2026-05-02 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1931e882-8ba7-3efa-831a-5a98d0977608 | -10.96961 | -45.08865 | 2026-05-02 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1a2f8ad2-51f3-3cc8-b9fd-2637dfeb6c0a | -10.71559 | -46.35838 | 2026-05-02 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2d698659-e5b5-3b9e-92b3-6f7fe34f7304 | -10.98967 | -45.09148 | 2026-05-02 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 97c3d3fa-9997-3740-a67b-fe4d3c5b9d38 | -11.04964 | -44.69955 | 2026-05-02 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5a68698f-b43f-3057-8a18-aab4d6e7eafc | -10.71695 | -46.34844 | 2026-05-02 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 5e0d0e0d-a5ed-3db3-ad67-78053379eb93 | -10.7183 | -46.33864 | 2026-05-02 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 32bd2e1e-d59e-3a0d-af6a-5344f8e8f6c3 | -10.98121 | -45.0783 | 2026-05-02 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 12a2a0d1-8104-360f-8408-5b4cfe3538c9 | -11.30984 | -48.55827 | 2026-05-02 12:02:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f34d0d3-d7fb-3bf9-a63e-3d853322d1e7 | -12.77346 | -47.11832 | 2026-05-02 12:02:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7272fbc5-1303-3b87-866a-27be0590741e | -14.26 | -52.08946 | 2026-05-02 12:02:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 8bd224fd-06ea-33ad-9fd0-47d4b64e7bc7 | -12.37743 | -50.03165 | 2026-05-02 12:02:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2bb0a233-d1ec-3919-88cc-5945a868c629 | -12.28269 | -44.62743 | 2026-05-02 12:02:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2a5915b9-6ea6-3a6a-b4e1-ea249575c40e | -13.39368 | -43.01951 | 2026-05-02 12:02:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 35.3 |
| c1be989a-8d75-376d-ab5f-02ecfa8c6aee | -14.68781 | -46.14603 | 2026-05-02 12:02:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6a99650e-9c14-30d5-b325-03a6e294e44f | -13.86694 | -48.72596 | 2026-05-02 12:02:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8f974439-dca3-38cb-aa39-e18279b9fec9 | -14.06365 | -53.3848 | 2026-05-02 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 67711952-f075-3cfc-ad83-d5b493e73ba7 | -13.47254 | -43.98664 | 2026-05-02 12:02:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 9b9cdd15-53f9-353b-9ef1-665d1b53edb9 | -13.47065 | -44.00216 | 2026-05-02 12:02:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c8030833-1007-30a3-84bd-541c9a78b460 | -14.26176 | -52.07825 | 2026-05-02 12:02:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3bea39a9-ba44-39eb-b7b7-bbcde115128a | -12.37604 | -50.04107 | 2026-05-02 12:02:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ad0ae9af-3378-3bf1-bb2e-a09c250cb5f6 | -11.55378 | -48.2676 | 2026-05-02 12:02:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 057da1b7-56e5-38d0-9ba7-d121fd4c25b8 | -18.00588 | -52.99578 | 2026-05-02 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 31bc9b7b-e712-3489-994e-21853048e773 | -20.20049 | -46.44208 | 2026-05-02 12:04:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| dd20fd54-3ae1-338c-bf3f-f74a334ad3de | -23.14382 | -47.34874 | 2026-05-02 12:04:00 | TERRA_M-T | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |


[Clique aqui para ver as próximas entradas](README8.md)
