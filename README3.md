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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ab8bb09-0b9a-3010-af3f-014529544e60 | -5.64165 | -45.76728 | 2025-01-01 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c8e2377-4ea1-393f-ac21-6bfc98b7e702 | -12.30767 | -37.88132 | 2025-01-01 04:40:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2d260af2-389c-3a12-aca3-e44d9a6115e3 | -5.43002 | -39.465 | 2025-01-01 04:40:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ca6c547-13f9-388e-be31-076ec57cf22c | -8.84051 | -49.9044 | 2025-01-01 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d270e67e-719e-37b6-bcc8-75ec2e0dde9b | -5.43056 | -39.46117 | 2025-01-01 04:40:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30219caa-649b-3f54-9afa-fc7c0db15ad4 | -6.95337 | -43.0057 | 2025-01-01 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9a9bc99d-ae3f-3c6f-8b21-89d238b03889 | -5.1389 | -38.15454 | 2025-01-01 04:40:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 11ed8e31-b0cc-399e-b1ef-5471b91bb47f | -10.75313 | -44.9353 | 2025-01-01 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19c517de-0b1b-34db-83ad-11ce98d31dd9 | -5.10724 | -38.02109 | 2025-01-01 04:40:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 44047192-5495-3dbb-99ff-242d6fe7db60 | -5.21494 | -44.90371 | 2025-01-01 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5fba696-1a37-3211-b935-49a2c6495032 | -10.50686 | -49.12682 | 2025-01-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3486dd91-1a36-3372-bbb8-872caf372a25 | -11.24549 | -44.48195 | 2025-01-01 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9ae56bb-9732-372c-8fd2-1f36b8013bcf | -22.48221 | -47.42073 | 2025-01-01 04:42:00 | AQUA_M-M | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.8 |
| 9cc9b282-2772-387c-9442-d975c22d1029 | -22.4742 | -47.42347 | 2025-01-01 04:42:00 | AQUA_M-M | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| cb5c17ad-64a6-3822-aa7a-b2efd6ec65f5 | -11.81149 | -49.33039 | 2025-01-01 04:42:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0e7a640-de37-3f14-84ce-f4444750e397 | -15.26509 | -60.21465 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f01c86dc-3ae6-38b0-bdc2-7e1c63f73988 | -12.25507 | -49.32674 | 2025-01-01 04:42:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e653e19f-fe40-3476-be23-6e741f2e3d25 | -15.26566 | -60.21171 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa9d24b3-f302-3f87-8f62-a23a14ec44e2 | -15.26008 | -60.21372 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| efe22d91-93e0-3048-865e-f29b39c7e667 | -15.21805 | -51.57958 | 2025-01-01 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2545084d-f13a-3d16-9b72-25885d901be4 | -12.2601 | -49.31618 | 2025-01-01 04:42:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afb273d5-f49f-3f3b-8b42-ed8288ac91ca | -15.26121 | -60.2079 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 61d43fba-cc1b-3d6c-b575-a1c4dc57b643 | -14.70716 | -56.81297 | 2025-01-01 04:42:00 | NOAA-21 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7c3600e-8f29-3ce6-bebe-fcf4f64d7f4f | -15.25563 | -60.20992 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c7ecadce-14b5-3104-a846-9af8d0eaf41c | -14.7065 | -56.81669 | 2025-01-01 04:42:00 | NOAA-21 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3b595e0-5752-3422-9a39-3d79e5f0ac97 | -15.27236 | -60.2039 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd72c7c5-a08e-3700-9bc8-ac1bab65c77d | -15.2153 | -51.57547 | 2025-01-01 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea6f2b20-76da-3d3a-8e3d-21a6c8428837 | -15.26679 | -60.2059 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b8d1bd95-49c5-3c9c-a3b9-09f753b2e469 | -15.26623 | -60.2088 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d999330-4423-37da-b394-9421a1618b12 | -11.81431 | -49.33455 | 2025-01-01 04:42:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cfd9730-a201-3ca4-85a1-f0e555b08b0c | -15.26065 | -60.2108 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ce74279-55b4-3c97-a90d-54758b71c81d | -15.26735 | -60.20298 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1985de56-3149-382b-aedb-619b839252b4 | -15.27124 | -60.20972 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9da8242a-4ede-372d-bdbe-76909ec22463 | -12.26348 | -49.31671 | 2025-01-01 04:42:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10dbfa1e-7007-3634-8030-b0928d81c410 | -15.2718 | -60.2068 | 2025-01-01 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a0622dd-7fc2-3e8d-964f-c6f644892a80 | -11.81094 | -49.33404 | 2025-01-01 04:42:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3398a09d-a96f-36a9-8193-4cd734b5a7de | -20.4763 | -55.8409 | 2025-01-01 04:44:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b773d37-1961-3974-beb7-08843bc61c88 | -23.59331 | -47.43732 | 2025-01-01 04:44:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63b26771-7e72-33a7-84d6-ed834ab71595 | -19.76899 | -55.40648 | 2025-01-01 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 301076e7-2d07-3998-8cd3-37c36dfc5422 | -19.84202 | -57.46386 | 2025-01-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fb9ed8d4-d7df-3b31-a140-63231b6527d0 | -22.54161 | -48.8138 | 2025-01-01 04:44:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2c36948-022b-3bf1-abbc-eae4d1825a67 | -19.18315 | -52.32055 | 2025-01-01 04:44:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2edec2d4-f266-3ccf-bdce-ddd658c43d77 | -18.01173 | -54.42966 | 2025-01-01 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84b1a0b9-7f5f-3f8b-b03c-d6407f36bdca | -19.84341 | -57.46098 | 2025-01-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0164c6d4-1c5e-3509-b3d8-57ea81e84b0c | -21.50506 | -50.6997 | 2025-01-01 04:44:00 | NOAA-21 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f8f6e46-e676-3ce2-bd7c-31b17eb5f168 | -23.35445 | -47.34789 | 2025-01-01 04:44:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 795d94d7-693d-3040-bd6a-4bd33ea8d8e2 | -19.83815 | -57.46307 | 2025-01-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8a4d1f63-7005-3ff8-bce7-d7b5e093f8cb | -22.47998 | -47.44718 | 2025-01-01 04:44:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| cf4ee7a8-9f38-39d9-bd9f-94153d9a19ca | -20.99629 | -51.79291 | 2025-01-01 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f5798a92-b470-32d3-a6d6-fa4117d38194 | -23.70886 | -46.89497 | 2025-01-01 04:44:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 33302380-1261-348f-909e-a201909ee4a0 | -20.76404 | -46.76868 | 2025-01-01 04:44:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8410319-d857-319e-b3d7-39c9f7a93d08 | -22.11996 | -51.46664 | 2025-01-01 04:44:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 499cfe3c-cb73-3fee-ae26-79a3ec159ec3 | -22.47628 | -47.44258 | 2025-01-01 04:44:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| b3d8c641-5fd9-3831-8461-57823473dff8 | -22.96955 | -49.91011 | 2025-01-01 04:44:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 626d25ba-57f7-35d2-9a81-2641e32a1541 | -23.33827 | -46.77472 | 2025-01-01 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 438b06a0-1aab-3c5a-9e77-a2fcbd3c0bd9 | -18.05081 | -52.27751 | 2025-01-01 04:44:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11ebffd2-161c-3178-a350-1da9ce1e05c6 | -19.71868 | -55.36276 | 2025-01-01 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8506aa07-182c-328f-a725-8703425ecac3 | -20.9225 | -54.77927 | 2025-01-01 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b53ead15-ee01-3c89-a757-037d3b69b720 | -17.65431 | -52.95648 | 2025-01-01 04:44:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 781b4cf2-994d-3ab1-ad03-b08030dd0157 | -23.14304 | -46.95686 | 2025-01-01 04:44:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ae2e3193-e465-3e03-b674-134e3381408a | -19.83954 | -57.4602 | 2025-01-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3dba9d19-d60e-3c1e-9b93-804a9649a1e7 | -20.75634 | -51.69192 | 2025-01-01 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62916a78-bb79-34ec-ab35-20cd988aa70d | -19.76969 | -55.4023 | 2025-01-01 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 385fa002-4bdc-3da8-af1c-cfd0209e7cd0 | -19.76549 | -55.40582 | 2025-01-01 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 87d77b08-81ee-3905-9851-119c952f3d09 | -22.48876 | -55.71634 | 2025-01-01 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4ea1d8f-c415-38ba-b5bf-4d60e32406ba | -26.73458 | -52.4665 | 2025-01-01 04:46:00 | NOAA-21 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 98355678-fdbf-3098-aedd-0ee840acf37b | -25.33045 | -52.74446 | 2025-01-01 04:46:00 | NOAA-21 | ESPIGÃO ALTO DO IGUAÇU | PARANÁ | Brasil | 4107546 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bbd811c9-9332-39e3-817a-24c5c846f8a5 | -30.0777 | -51.72417 | 2025-01-01 04:46:00 | NOAA-21 | ARROIO DOS RATOS | RIO GRANDE DO SUL | Brasil | 4301107 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 6a3b87af-9e29-393e-99b8-85c295e67311 | -29.16318 | -51.24889 | 2025-01-01 04:46:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f5d66643-2824-399a-84b3-3f47df5a42ad | -8.83813 | -49.90374 | 2025-01-01 05:03:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8020a228-c159-34b3-82f4-b4ee6156367f | -8.84263 | -49.90434 | 2025-01-01 05:03:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60647121-8d8f-3e9d-88f6-fd18985939a0 | -1.80484 | -53.22208 | 2025-01-01 05:03:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be73f8cc-658f-33e5-9f94-66258b0d5b7b | -12.26252 | -49.31539 | 2025-01-01 05:05:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41dd6339-beb6-3440-8ad2-ca9ac2b6d45b | -12.25613 | -49.32591 | 2025-01-01 05:05:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c167a56-5aaf-37e1-8fb6-d1f06dcb3366 | -12.25867 | -49.31546 | 2025-01-01 05:05:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28629688-7157-3052-a48e-87ee651a1c4d | -12.26359 | -49.31612 | 2025-01-01 05:05:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4fd14b8-7477-3850-8da9-7edc823b6795 | -13.48581 | -60.66522 | 2025-01-01 05:05:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85f735aa-53b6-317a-bc4a-76428f6b3e8d | -16.22062 | -59.93754 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2be84d33-1d47-351a-a227-fb15813c70ba | -15.266 | -60.21181 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3769ef2c-781d-3df8-a7f6-8e9685876291 | -19.84214 | -57.46264 | 2025-01-01 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db8936fe-8bc2-36f3-a295-44f219c19e23 | -22.47402 | -47.4429 | 2025-01-01 05:08:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| cd823d89-cc02-3bf6-bce1-f8040dd071ff | -14.70665 | -56.81556 | 2025-01-01 05:08:00 | NPP-375D | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ad6df2a-7828-38c5-b89f-1e0f0fc7d963 | -22.47777 | -47.44102 | 2025-01-01 05:08:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| dcb8f618-4462-3f33-ae11-8876eadf4993 | -22.48032 | -47.44337 | 2025-01-01 05:08:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| db36a5c6-8479-3395-9c7b-0bf9c89cc514 | -15.5527 | -59.45197 | 2025-01-01 05:08:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efb0b476-9974-3182-b22b-a8011abfdb3e | -19.71998 | -55.36103 | 2025-01-01 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46c80014-7f13-3616-81d4-9ea0938ba060 | -16.22404 | -59.93815 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5af81c2b-a4e6-38ec-b879-c4509feb4e8c | -15.26666 | -60.2079 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e21050e-f39f-3d1d-95d5-c58bf1eb5ef8 | -15.27013 | -60.20851 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 50b636dc-3407-3be7-93a0-a7cb071ffe3d | -15.57176 | -59.42081 | 2025-01-01 05:08:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cff30d30-cacb-3b75-adaf-330db7921d30 | -19.76688 | -55.40551 | 2025-01-01 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fb1a3b9b-a472-30cf-9d35-40466708fdbd | -19.77057 | -55.40609 | 2025-01-01 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5f8ef781-6447-33f8-91dd-b14bb92c5580 | -22.12128 | -51.46547 | 2025-01-01 05:08:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 452fbefb-d015-351a-94f7-ec45fd71aeba | -19.71628 | -55.36043 | 2025-01-01 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 275c4c17-d34f-365e-8118-089ff8e166c8 | -22.47989 | -47.4485 | 2025-01-01 05:08:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| ac7665d6-bd77-3ace-9adb-852259a8e600 | -15.26318 | -60.20731 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b92ad505-37cd-3923-bd08-dbf066ed5c03 | -22.47737 | -47.4462 | 2025-01-01 05:08:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| a2692ad9-1d49-3a97-8157-1e1daa28b4f1 | -15.25971 | -60.20672 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a74fb1c5-953f-3043-b2b1-9f46c6a4f8d7 | -19.83873 | -57.46207 | 2025-01-01 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 10425238-14b9-3a94-9a73-b8c7cf3e8874 | -15.25906 | -60.21061 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README4.md)
