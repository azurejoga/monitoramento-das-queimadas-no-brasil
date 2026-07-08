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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61d296a3-d805-36f6-9fb2-df66a9cede1d | -13.29524 | -54.41299 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 227f2d4b-d0a4-3e5a-a5aa-87b8a7110243 | -9.56862 | -49.10811 | 2026-07-08 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bca5fdfd-3002-3166-b253-a488879a87e6 | -13.29646 | -54.34778 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc359e1d-a4f4-33bb-be37-642272df38cc | -13.33692 | -54.38018 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 631f2690-3beb-3d04-af73-5c74690e71b3 | -12.49803 | -48.25713 | 2026-07-08 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a95f8cd5-96e0-3797-8eb0-4889009a84a1 | -9.23589 | -50.14557 | 2026-07-08 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff3a0aee-75da-399f-8971-257037ece109 | -13.95182 | -45.22787 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d39be7ab-0918-325e-bab1-8fdad2fa8a51 | -12.36614 | -47.42292 | 2026-07-08 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8818e94d-9486-397c-8269-bf5692e3c7c4 | -8.59817 | -48.00653 | 2026-07-08 05:12:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5efac327-201f-3e3a-8ac5-984afe08463d | -13.4791 | -49.91159 | 2026-07-08 05:12:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5262bb1-b3d3-3a74-8ced-98dc3d22fef8 | -13.76996 | -46.29065 | 2026-07-08 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a6371871-4764-3a9b-aafc-83fe13009b78 | -13.29456 | -54.41788 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 659f400e-9da8-38a7-ab25-67a6daccf7db | -13.29343 | -54.39776 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97c78ca2-e896-303a-82ab-7ea84f8be5a0 | -13.30049 | -54.4037 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 002f334b-99f0-3af5-ab7f-2b891828af82 | -8.59865 | -48.00284 | 2026-07-08 05:12:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2aa8092-1314-31b0-9a39-a728f40fd263 | -9.21958 | -48.58809 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cd639c03-c39c-385e-9356-96e2a4247dc3 | -12.36135 | -47.42284 | 2026-07-08 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41dfea26-b034-30c1-b30c-0df879b8103b | -13.28414 | -45.18642 | 2026-07-08 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2639c64b-f312-354f-928c-457a6c70e512 | -13.33304 | -54.37963 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d8720b3-7aab-39aa-8938-efb94317a35e | -13.95899 | -45.20825 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 881ac5df-9dce-376a-b3f7-ad8ee5b6c245 | -13.95253 | -45.22089 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 07f828df-b513-31de-8ee5-0cd2c221dcac | -13.32917 | -54.37906 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82b420e3-2685-3cf8-b461-f9122b4861d6 | -13.29275 | -54.40266 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22b3480a-f0c2-301e-91b6-abe2036d803b | -13.96025 | -45.21497 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7751cd46-2ace-3a4b-ad5c-5a3fb8bdbf93 | -9.22544 | -48.58524 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9bc6242b-9b29-3edc-aa2b-97812f847fe5 | -13.28751 | -54.41189 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13def73a-28ad-3ac2-97fa-e6c808d5f1f9 | -13.2998 | -54.40862 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c2dd0e8-111c-3899-af95-e64020cf75f7 | -11.91346 | -55.90883 | 2026-07-08 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1f762e9-89d9-37df-8382-3098c4c64b94 | -13.27783 | -45.17876 | 2026-07-08 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27eeb7f2-c18e-3d2e-9caf-301a1cbf2a6d | -13.95065 | -45.22116 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 107652a3-85b0-3485-9fe5-cb2065751583 | -13.95954 | -45.22195 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| db8739dd-5d9e-35fc-aa8c-7f7067a016ce | -9.22637 | -48.57816 | 2026-07-08 05:12:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5377aebf-78d0-387a-8819-05f569d3b5cb | -11.97213 | -46.95287 | 2026-07-08 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3a9e13e-c7c0-3ec9-8fdc-6db2a7095f18 | -13.95833 | -45.21515 | 2026-07-08 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a54e9d6-5d54-3f6d-9270-b5f18c3925fc | -11.91289 | -55.91284 | 2026-07-08 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aabc2535-4bfa-3163-bd7b-6c51fb434140 | -13.47873 | -49.91483 | 2026-07-08 05:12:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf234466-b28e-3b1c-873f-1080112fb222 | -13.29138 | -54.41244 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b61921b-4a4b-33a4-ae7c-1bc67cea5d96 | -11.96538 | -46.95668 | 2026-07-08 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8fe27d3-7399-3492-b192-5f97057b72d6 | -11.55402 | -52.79298 | 2026-07-08 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e419a801-a829-3d29-a4fb-9e7cd94712df | -11.32187 | -54.47806 | 2026-07-08 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5183e4c-82d0-3f13-a2a6-988b438c188f | -13.29662 | -54.40319 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18ec21e1-aed5-3e8c-8c3d-7082afc9c688 | -13.29206 | -54.40755 | 2026-07-08 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66824ef0-53b6-33f5-8277-e8dc589cf416 | -9.36682 | -48.80724 | 2026-07-08 05:12:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c21a318-103d-34a0-984f-8315ec7be83d | -9.60185 | -56.91967 | 2026-07-08 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9d9384e-79ec-3136-bed9-322b22598316 | -8.5977 | -48.01024 | 2026-07-08 05:12:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7c310d6-2e51-37d8-a08a-5d0ea0b91627 | -14.14647 | -52.88782 | 2026-07-08 05:14:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7dc21ce6-931c-32ff-8142-e3b0997b46f1 | -16.48189 | -50.90739 | 2026-07-08 05:14:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98328cf9-2f18-3f5e-b7af-b326e3a7bcd0 | -21.36592 | -49.16747 | 2026-07-08 05:14:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b04aa0e5-42c2-3434-b841-418eeee655a4 | -19.44208 | -54.66381 | 2026-07-08 05:14:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a539b091-a5d6-32be-bf87-28fbfbbf90eb | -17.53771 | -54.01189 | 2026-07-08 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9aed0a4-ff5e-30d8-90da-658889b3ca37 | -14.86261 | -48.31535 | 2026-07-08 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25812267-90dd-3ebd-9736-aeed349ee4fc | -14.14272 | -52.88297 | 2026-07-08 05:14:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7c12fc56-9dfc-38e5-84f8-1d31ee6bd941 | -17.28396 | -50.0233 | 2026-07-08 05:14:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bae769a6-2cd6-3b4b-ada4-2587f2d27896 | -19.63506 | -47.58308 | 2026-07-08 05:14:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a58fd9f-93f9-3383-8a5b-76e743643ad7 | -16.16169 | -59.32032 | 2026-07-08 05:14:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b56eac22-d30b-35c2-8922-627cc6a6e20e | -17.57287 | -54.04451 | 2026-07-08 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b34618ce-30f9-3393-a52d-6250489ade7b | -21.36636 | -49.16248 | 2026-07-08 05:14:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 595b3998-1e67-365a-93b4-4d0341296fe6 | -18.08222 | -54.02896 | 2026-07-08 05:14:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 265bf2bf-716b-3159-b33f-edda66c7f1bf | -19.63539 | -47.57874 | 2026-07-08 05:14:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e00daa3-0f37-3ec4-ad21-0ac25a6ca580 | -21.37197 | -49.16792 | 2026-07-08 05:14:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 876d2f32-d3fd-3a72-9e0d-32658117ee6e | -13.6014 | -56.6084 | 2026-07-08 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e20d2739-e5ff-3a68-ab9a-45cde28eb8d1 | -17.28022 | -50.0207 | 2026-07-08 05:14:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5d9124-6946-3000-adac-b36cf52a2359 | -17.5419 | -54.01252 | 2026-07-08 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4c79384-be17-3753-9079-39c329fbc267 | -21.3724 | -49.16299 | 2026-07-08 05:14:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 256f4d0e-1af5-332b-b85c-75f905d6722b | -21.06279 | -47.25745 | 2026-07-08 05:14:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71a5145a-ea2f-38d4-993d-0913d710ce96 | -17.53721 | -54.01581 | 2026-07-08 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c1a5a8d-a9a6-3a4d-9516-7478cec6df54 | -20.47507 | -56.73079 | 2026-07-08 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4b286a3-3873-3387-8212-1d8c18b7a3c0 | -19.63488 | -47.5845 | 2026-07-08 05:14:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a775471-bbba-3ad7-8d70-e334b390f02c | -17.27984 | -50.02439 | 2026-07-08 05:14:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 031c4da8-49cb-3fab-b95b-5365ecd3137b | -14.86308 | -48.311 | 2026-07-08 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90893996-8a89-3c53-bac4-32952a19d0c7 | -18.08696 | -54.02549 | 2026-07-08 05:14:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f229668-f38b-3d19-85b9-520628b56a80 | -16.48223 | -50.90436 | 2026-07-08 05:14:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b14fdcb-1f46-3b08-acec-e160dcdf778a | -18.24131 | -54.60197 | 2026-07-08 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e118ee7-788b-3926-a4b8-5e4585bd99c7 | -19.62159 | -47.58728 | 2026-07-08 05:14:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dbbf6d1-7c7f-3ce9-b85c-b4eb01c79f5e | -18.2418 | -54.59819 | 2026-07-08 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a81d698-fa73-3f18-b54c-24a687f9058a | -19.62204 | -47.5817 | 2026-07-08 05:14:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe9e8bb9-4e26-312a-84bc-1598e220afd5 | -17.27852 | -50.02245 | 2026-07-08 05:14:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b9fd301-6e76-3822-a61e-a83c57ca1d40 | -19.62138 | -47.58875 | 2026-07-08 05:14:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c04a6c81-37e4-3f49-a1e1-37984c484842 | -18.078 | -54.02834 | 2026-07-08 05:14:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1358036b-8321-3fa7-8ebd-405c04a037ec | -21.1564 | -50.18523 | 2026-07-08 05:14:00 | NOAA-21 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7a97adb-8890-3585-9624-617b53ded2ec | -19.64108 | -47.5899 | 2026-07-08 05:14:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfb0f3c2-1c01-35d0-93a6-98d9ca5215fc | -17.5382 | -54.00801 | 2026-07-08 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 875b28e3-60e9-3c7a-b8e8-28d85005e465 | -16.71756 | -50.70826 | 2026-07-08 05:14:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 250ea433-fb55-3740-8a79-62629be210dd | -21.41835 | -47.06378 | 2026-07-08 05:14:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7af717fe-f838-325a-8aec-be10a649c189 | -21.06321 | -47.25184 | 2026-07-08 05:14:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f74a5a49-b967-3be9-b129-89cc88644ada | -19.64086 | -47.59127 | 2026-07-08 05:14:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75d94da6-f51d-3868-9332-0beb0e59f5e0 | -16.73744 | -49.43006 | 2026-07-08 05:14:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0848e9c4-2799-35db-83fc-95351ee1ea9d | -17.5424 | -54.00862 | 2026-07-08 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd141140-c586-3d99-a778-d6e1dab6d045 | -16.73785 | -49.42613 | 2026-07-08 05:14:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f833b73-91f8-3a79-8b57-949a492bbd9d | -14.14704 | -52.88356 | 2026-07-08 05:14:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7cafcc34-ec98-301f-a57a-922f2819c60f | -19.62187 | -47.58311 | 2026-07-08 05:14:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49def671-df72-3d5e-9289-573784ef5391 | -18.08274 | -54.02486 | 2026-07-08 05:14:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5383d827-642a-3ced-81c4-af921a1b630c | -21.32692 | -57.74823 | 2026-07-08 05:16:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f170da9e-c5f0-3579-9130-6e9a69392c0b | -21.80545 | -56.26778 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68d86544-46f3-3b62-a92a-f71c0bbcde8a | -21.80359 | -56.27144 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| fd64e189-570e-3e1d-9522-098924890076 | -21.80038 | -56.2658 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| dd529db0-70e0-31ae-aedc-6a868283dd29 | -21.77774 | -56.28876 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8b3c521-218c-31ea-bab8-7748b87b9841 | -21.77322 | -56.29331 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32d88ae8-29c4-3ab3-9802-9e80dee1e97d | -21.79519 | -56.27553 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| abf7ba4c-adb1-3dd0-97dc-552087457723 | -21.80426 | -56.2663 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |


[Clique aqui para ver as próximas entradas](README22.md)
