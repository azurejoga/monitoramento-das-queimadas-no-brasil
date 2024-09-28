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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6bf3d4a-3a34-319d-82bb-fdd35ab20113 | -9.11497 | -67.89936 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 767b79ee-d672-3675-a6a6-f37d1e243b5e | -9.11282 | -67.89101 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11bf586b-4de1-3559-b3bd-bdb1e47d33a1 | -9.11213 | -67.89483 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2e8ff4-8b5c-3fcb-974c-70295b13790e | -9.11144 | -67.89864 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd746a39-9611-3fd2-9650-10db7131d42f | -9.11082 | -67.89068 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d1c5f6a-5322-3622-99ad-81d1037a3d95 | -9.1101 | -67.89449 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1252e153-8550-3302-9b95-6debb5c55eb1 | -9.10937 | -67.8983 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 713f4689-0d04-3d77-a5d8-c8e93532563a | -9.10654 | -67.89374 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53c4d559-5b45-33e6-a032-050959e1a7a3 | -9.10584 | -67.89756 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6f217ff-545c-332b-bdf0-297cf35091bc | -9.10515 | -67.90139 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e4e4e68-26ed-3195-a912-624c40685a55 | -9.1045 | -67.89342 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6746933c-db1a-3710-a4d3-af07b5067b1f | -9.10378 | -67.89724 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45ae37c2-ec30-39e1-af47-8b820db4386a | -9.10306 | -67.90105 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a1cafae-4462-3fe0-8f1f-1b7fd4efc8dd | -9.10025 | -67.89648 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 427b9e1d-a5a4-34bb-9fca-601be614a37b | -9.03653 | -67.89617 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df7647c8-77b5-3f9b-a681-7a542cffd520 | -9.03582 | -67.89999 | 2024-09-28 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc431915-aefc-3e54-b0a3-e059e031d112 | -10.99312 | -44.42909 | 2024-09-28 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef35d294-41e2-3c00-8199-19f2dcf10140 | -10.9923 | -44.43616 | 2024-09-28 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17fd94e9-7be7-3e4b-b387-269d16b9c611 | -10.98947 | -44.42857 | 2024-09-28 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4cdacbda-fcba-3d18-96b0-f98f73d40561 | -10.98871 | -44.43562 | 2024-09-28 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2e69478a-f375-36f2-bf1a-981850675204 | -12.99586 | -44.73832 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2bb8aeb-e198-3bd3-b335-47c699271a9b | -12.99512 | -44.74543 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b1f4e9e-e374-3f16-8788-e6037a518df2 | -16.87839 | -45.32227 | 2024-09-28 05:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 475ce7f0-4579-3126-958c-ca537854ddef | -16.87776 | -45.32965 | 2024-09-28 05:10:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5086ea82-ed1c-333f-a98c-10c8aed64297 | -16.87504 | -45.32853 | 2024-09-28 05:10:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20e77842-5f51-353e-bee5-c4347e304cad | -10.85862 | -44.80375 | 2024-09-28 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f89ffcaa-5695-36dd-b99f-30ee79b17e5d | -10.85855 | -44.79853 | 2024-09-28 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b9abc3a-8ce3-3a24-a696-e79a9114714c | -10.85781 | -44.80517 | 2024-09-28 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36f3d9d0-6e6f-31f5-a775-5b0edd3966d7 | -10.69249 | -45.86204 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8ea60a1-ea4c-378b-862a-07226ac49f1a | -10.69186 | -45.86739 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 720c6b06-b822-323c-a932-a3ba218d6521 | -10.68656 | -45.85623 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23ffd557-3b6b-3026-b302-7905700a5a06 | -11.25236 | -45.40498 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79c6d354-c407-3ebb-8554-0c84fff3de5f | -11.24566 | -45.40369 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 007e3059-f68a-39fd-9be6-98020e26bb15 | -11.21837 | -45.58445 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5193a18b-c072-3c51-a925-a929d4369878 | -11.21381 | -45.58945 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f6c98c1-c78e-319b-8ebb-36c553ec22a9 | -11.21308 | -45.59549 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2bc0df9-5e6a-39c1-88c7-f849dccc4528 | -11.21121 | -45.58787 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 355c7f92-523d-37bf-ab5f-03d220b1ae94 | -11.21052 | -45.59396 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7225965f-3a96-329a-a0b8-07c47bdfad7d | -11.10801 | -45.59436 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15464152-afe4-353c-af66-559d5f5b5156 | -11.10566 | -45.58862 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b164d9e-4810-3b30-b574-1a57666d9e58 | -11.10486 | -45.59569 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f3d645b-407d-3df6-9a42-55733762dda5 | -11.10121 | -45.59468 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b07001e1-70c4-3dae-8caa-50a9bdf08fa3 | -11.05003 | -45.74165 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3228417d-24e4-3fcf-a57b-028071f8271c | -11.04933 | -45.74754 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 96b05c09-e119-355d-a6e7-9c2f72a2c07c | -11.04865 | -45.73645 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 234bf126-ef17-3510-8a8e-dcbdd6139472 | -11.04799 | -45.74241 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 53ceb2db-e7ec-376f-b78b-6bd11bbd4b02 | -11.04733 | -45.74829 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 80fc0d5e-8abd-3d50-a3eb-9b1f20114636 | -11.04548 | -45.72348 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a801bdf4-e52f-3381-af4b-6a2bcf89cf31 | -11.04479 | -45.7293 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f37e7324-ea01-3266-984e-aa7ae41aa02f | -11.0441 | -45.73521 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ea1753d1-5086-395b-93bf-8ff9c2b7339a | -11.0434 | -45.7411 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 2cdb0f1d-9080-39fa-9256-8ac2c19be33d | -11.04271 | -45.74694 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e9af971d-abdf-324d-aa96-6527051cf863 | -11.02693 | -45.71018 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2d7c3219-29bd-38be-a00f-d64bca157030 | -11.02625 | -45.71597 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9c680dfe-9dc8-39d6-8ddc-1dad32b8aa70 | -11.02558 | -45.72173 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1be3c568-cb13-37b3-8755-232690576659 | -11.02031 | -45.7094 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77853da8-9ab0-326a-873a-3c5008599b50 | -11.01964 | -45.71517 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa39681c-36a0-382e-a65e-24d4529a87ca | -10.87554 | -45.5228 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3905691b-213e-3c8b-bd7a-7b32b3ebf352 | -10.87207 | -45.52203 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 30fde57b-46ca-323e-9db1-d10f2b313b67 | -10.86879 | -45.52264 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d4ab7e6-7d80-343c-8756-7a9041ba7dc2 | -10.84881 | -45.54695 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a352f907-c6db-3e9f-8987-f970f4f99b74 | -10.84822 | -45.55195 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b80e38b5-47a1-3970-89b6-0930c5c834d2 | -10.84759 | -45.55732 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 930dd748-d960-37cf-ad58-8d583c7225e2 | -10.84156 | -45.55118 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02c566ec-ea7d-3bc0-bd73-55a7eface277 | -10.83105 | -45.9732 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b4ed4fd8-eeff-3192-b340-d6d05814e67d | -10.83064 | -45.9772 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 170e8ef4-2262-3bfc-a37b-533a4529676c | -10.83044 | -45.97852 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0bc83127-6a4a-3e42-b197-75c699ef9cc5 | -13.35101 | -46.2986 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44b23164-8f1d-3346-93d6-b29051ac65be | -13.35043 | -46.30376 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f13d944c-ce66-3931-86a7-d90c38dd43d8 | -13.34981 | -46.29912 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c96cedc-7fdf-3786-bf9f-05140d085b02 | -13.34928 | -46.30413 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83748e0d-6893-37f9-aa73-16bfcab88f4b | -13.34442 | -46.29811 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acf3b4e5-e1f6-315a-8847-513a403e94dd | -13.3439 | -46.30273 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dbef66c-c6f6-354d-9249-6bc7000a3832 | -13.34332 | -46.30789 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d41fe237-beec-383c-b839-cf95f3315b26 | -13.34325 | -46.29837 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e3c97bf-c9f6-36e7-851f-918767ab297e | -13.34275 | -46.30312 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87d139f9-0bea-3787-a18f-e507a66db3c2 | -13.34219 | -46.30836 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1c9dfb2-1e55-39ab-9e9c-89df3a2e9fcf | -13.27477 | -46.32803 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3da6c3f9-725c-3d54-9b46-83c2cc74ea5b | -13.27418 | -46.33349 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b1a35f5c-d2de-32f2-b10b-5f1c287e4d0c | -13.26931 | -46.31731 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| da9ece16-af13-3111-82b3-adaa5193d8e0 | -13.26879 | -46.32217 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc25661c-d88b-331d-8d34-4fc468cbfd07 | -13.2682 | -46.32755 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be7b7ea-aee2-3087-a1c4-d2d0036c1aaf | -13.2676 | -46.33312 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6a6725c-aa8f-3725-a4fd-bf0e257b35fa | -13.26156 | -46.32775 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ea50ecf-82d1-3199-9b68-42eed389e144 | -13.26092 | -46.33361 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54b0e383-e486-3610-b28c-a29c57b555cc | -13.26033 | -46.33907 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8c9bdae-d7c0-3f50-9819-a240eb87e760 | -13.25524 | -46.32497 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c86c16d-323a-3e48-8f22-6c2334bd8b6b | -13.25462 | -46.33072 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d6a540b-28a2-3d95-b6c5-831b21bb55eb | -13.2541 | -46.33547 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa325848-9fe3-306c-93b6-7d3caaa126dd | -13.25365 | -46.33968 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 434cbb5e-3db7-3a24-a92c-4268d47afc68 | -13.24759 | -46.33446 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12696507-8457-3826-b37b-bcddd5c0d882 | -13.24716 | -46.33848 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c0b65a9-a8bc-33a4-8bfb-6a5b9a94c515 | -13.24196 | -46.32923 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| beeb809e-2f8d-3472-bbe9-1c2087308f4a | -13.24158 | -46.3288 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fc12cfe-3740-3f7a-8e6f-2a65d51f8243 | -13.2415 | -46.33332 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6454fad2-c619-397b-a9b2-6dad14c45749 | -12.74002 | -45.57069 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 653dc38a-413b-3f99-9404-c0dfda817c73 | -12.7339 | -45.5637 | 2024-09-28 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8e618a5-a148-3673-84ae-e89762f02f9f | -14.17053 | -46.44652 | 2024-09-28 05:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdddfdb2-7ca6-3968-9fca-23f46f4484f2 | -14.16994 | -46.45182 | 2024-09-28 05:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1c21f68-4f87-37f7-a9d2-849a076a7e03 | -16.57107 | -46.9362 | 2024-09-28 05:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README76.md)
