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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efe31321-cee8-31b9-a092-eeee81218c87 | -18.15032 | -40.13823 | 2025-08-25 12:17:00 | TERRA_M-T | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| f2da26f3-4ffc-3ee0-9c4a-842877d951c6 | -14.77583 | -45.38133 | 2025-08-25 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e82b61d1-6413-3b65-9eb9-82a76746c909 | -18.65643 | -46.34941 | 2025-08-25 12:17:00 | TERRA_M-T | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e0844728-9771-3ed3-a02d-919941488d59 | -13.65257 | -47.97954 | 2025-08-25 12:17:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e45690a0-6070-3625-99b0-5add44d60cae | -13.61621 | -48.16417 | 2025-08-25 12:17:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2171771b-061c-3094-8cf3-7d5b5c1e288f | -14.25365 | -45.23067 | 2025-08-25 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 897c6462-4706-37ca-a43e-46d6b22f359a | -11.61265 | -46.34648 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 70467640-1cf8-3616-8e7f-85813242a81a | -12.75247 | -48.13979 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5f0e7635-2bb4-3e07-800c-76508d1a21ea | -11.61764 | -46.37464 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 95f10440-bab1-3f1a-8434-30710beaa5ca | -18.73282 | -45.14556 | 2025-08-25 12:17:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6023ac4d-71b9-3a25-90ac-9707ee0d61bb | -11.59997 | -46.37207 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f680520a-7820-3719-a9ce-72861c64b823 | -13.51325 | -46.90921 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| feebf623-0045-3adb-818f-8a831becfb22 | -13.21422 | -46.03436 | 2025-08-25 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a6356812-5f40-3e88-8818-ee874f31d79c | -13.12201 | -41.046 | 2025-08-25 12:17:00 | TERRA_M-T | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 5e79c0c5-a8b0-3954-94d1-22b864134a39 | -14.25232 | -45.24062 | 2025-08-25 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 675dd27e-78c8-309c-b5d5-af4ba296a2c5 | -12.31409 | -49.14227 | 2025-08-25 12:17:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 068b3b34-f6e2-3ef3-a47c-d717d34ea0e7 | -14.79297 | -45.39383 | 2025-08-25 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4085a11a-41a0-3031-a2bb-82f9d9095a8e | -12.74207 | -48.14769 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 17be31bf-3098-3fe2-a59b-3e40a5df29f9 | -13.44418 | -46.87418 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7a0a6869-bc23-3665-8245-2c5f94dd7664 | -19.1806 | -44.50707 | 2025-08-25 12:17:00 | TERRA_M-T | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1fe08fa4-6d54-311d-b8f9-9562a7991598 | -14.26205 | -48.04012 | 2025-08-25 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4c44b93-e702-3762-aae6-0ba674605fd4 | -13.8153 | -45.8824 | 2025-08-25 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2b9dd779-56ee-3a99-ac43-998310ff6c0a | -16.85017 | -46.3062 | 2025-08-25 12:17:00 | TERRA_M-T | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6d6f0ea6-d56e-3cb9-8974-e1c509472ffa | -13.46412 | -46.87439 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9ccd4d6e-5673-3eef-be27-86f1ffd0d07b | -11.90482 | -47.12825 | 2025-08-25 12:17:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0a939765-bbc9-359f-a462-5eb51302df55 | -15.57076 | -43.5529 | 2025-08-25 12:17:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 6a623c32-e047-3f91-b9a5-ca964706aaa7 | -11.64068 | -46.21316 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2a5986cb-5410-3847-b102-becce75d80ca | -14.63706 | -45.11349 | 2025-08-25 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cdbe925d-1b82-3535-86f2-ee56d0ecf9a1 | -13.6176 | -48.15472 | 2025-08-25 12:17:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1f22bbd5-e6f7-33a3-97ec-fb6ceba2c25e | -18.52442 | -46.84589 | 2025-08-25 12:17:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0be064c9-3f50-3182-83f6-7a37b109bb93 | -19.17904 | -44.51959 | 2025-08-25 12:17:00 | TERRA_M-T | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f2b5533b-3c3a-3e62-bfc2-a5c0a0640568 | -15.03864 | -48.15778 | 2025-08-25 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e0c0c532-b1b3-339e-b631-6ede09eee70c | -15.06732 | -48.70616 | 2025-08-25 12:17:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3dc94f2d-3f2e-3021-b51f-98a42735614f | -15.20488 | -48.28116 | 2025-08-25 12:17:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2f6610b2-a417-3cf1-bcdc-0179b39420af | -11.6088 | -46.37334 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 684078e5-f1e2-352d-b0ee-e45e7d6d9fac | -15.13863 | -43.92026 | 2025-08-25 12:17:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 814a2fc3-a596-3864-851b-03e52c5397bf | -13.48885 | -47.0162 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b4328ac-bf89-3df5-b495-f8511a0f3c69 | -15.09584 | -48.70101 | 2025-08-25 12:17:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d971f10e-e197-3b43-b038-a0b584fec932 | -12.67193 | -45.29291 | 2025-08-25 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 43c9b85f-043b-3e4d-a53a-b8d5a9832162 | -12.74347 | -48.13828 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5430f6ee-50bd-3a09-a57e-aa877d585555 | -15.08111 | -48.55294 | 2025-08-25 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 136a2c6b-e812-3884-83a0-973a1ce433b0 | -13.40757 | -45.89802 | 2025-08-25 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e5516a05-6a96-399d-9409-1f1a003514df | -13.65121 | -47.98883 | 2025-08-25 12:17:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d38cc8e7-2454-3e89-a545-46394bc3dfee | -11.61009 | -46.36439 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 95091de5-887a-3ac4-b3ae-693588c82542 | -13.23454 | -46.54544 | 2025-08-25 12:17:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a8cbfe42-5492-3517-bdcf-5fe5448f308e | -11.6394 | -46.22216 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c98bccb7-a346-3270-ab4d-ca8dd1447055 | -12.69573 | -47.83939 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 562b5bfa-fad5-328f-8892-271e05895e4f | -13.49817 | -46.88858 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 18e5a332-2c71-3665-b776-d679a855fa4b | -18.76449 | -48.02735 | 2025-08-25 12:17:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| cc855aec-f0f6-37b4-81e0-0dc034455902 | -14.373 | -51.93299 | 2025-08-25 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3070ba2c-1ce0-3780-bb82-96901f6f32dc | -13.45069 | -42.26118 | 2025-08-25 12:17:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| e7c3cdb3-a62b-37c6-8947-65e6424391a1 | -16.08461 | -45.35982 | 2025-08-25 12:17:00 | TERRA_M-T | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1170cd78-2e53-3edc-a6ef-455223346338 | -11.86647 | -45.12449 | 2025-08-25 12:17:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| bc42c41d-3802-358f-a830-7bd0b3aa9a3e | -11.54111 | -50.47181 | 2025-08-25 12:17:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 2f894b37-6b62-38c8-87bf-dc1c029f99d1 | -13.83815 | -46.6981 | 2025-08-25 12:17:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cb45bf18-69f0-3073-88b8-f18fa5b64ff4 | -18.5231 | -46.85546 | 2025-08-25 12:17:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 867119ae-4a0a-3ff6-8cc4-d1f57d67373c | -11.61892 | -46.3657 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4690e134-2164-3303-9fc8-6f5188087070 | -12.30623 | -49.13038 | 2025-08-25 12:17:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ed0e67f7-0921-39aa-9aa9-a3e0eca28dac | -11.56982 | -46.31608 | 2025-08-25 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3eeb2346-dc02-3100-86fa-0c19ed46d496 | -12.30462 | -49.14083 | 2025-08-25 12:17:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5da7fcaf-4cbf-3795-a2a8-4610aa64ebbe | -11.92675 | -46.72771 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e1c519e4-0cd7-3c01-ac19-920971f6dc17 | -15.10488 | -48.70237 | 2025-08-25 12:17:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e3872048-2b75-330a-9add-d8c624d00fb9 | -12.68678 | -47.83806 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bb14c00b-fbda-3460-b8d8-37b66e80e85c | -17.89801 | -45.13664 | 2025-08-25 12:17:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3e7a0cfa-c962-3a2c-9942-e5f3c5fb68a4 | -13.43275 | -46.89093 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |
| e8d6776c-69f7-30f0-88bc-79ccd9dac528 | -18.72158 | -45.15554 | 2025-08-25 12:17:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| dda37513-c058-38df-9ce0-699214d023a3 | -17.57488 | -44.23789 | 2025-08-25 12:17:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 960c21b7-a193-3afa-9ca6-dbeaee9f60a0 | -12.24232 | -44.66782 | 2025-08-25 12:17:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c5e5b89a-3fca-30c0-bd5a-a665c37d8adc | -13.44289 | -46.88319 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 09df25a7-3ecd-3187-84bc-ebb74698f2dc | -11.62928 | -46.22985 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f5e11927-a656-35d2-9d59-f4ed89dc7c2e | -19.87717 | -43.2833 | 2025-08-25 12:17:00 | TERRA_M-T | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 80e8504e-59ca-3c06-b58c-a3268a1dd9a1 | -11.86778 | -45.11492 | 2025-08-25 12:17:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7360ee54-b51b-3282-9f81-b90fcdb79cc1 | -14.82445 | -47.91789 | 2025-08-25 12:17:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fdeaf22c-3121-34f8-8f8b-56d436285ba4 | -14.79379 | -47.94134 | 2025-08-25 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0adb03d0-62a4-3f48-a5bd-dd1f7383dd52 | -13.40407 | -51.7886 | 2025-08-25 12:17:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 5b80d176-c09b-385e-9c6a-1eea47ab4c55 | -15.57239 | -43.53963 | 2025-08-25 12:17:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 8bf72b31-e04d-306c-a932-d4e9ae43172c | -11.60752 | -46.3823 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 2b0551f1-c49b-35b8-8a01-ccaf70ca42f9 | -15.07968 | -48.56245 | 2025-08-25 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d136b8a7-ad53-3aab-a87c-c251a823f73e | -18.14619 | -40.13082 | 2025-08-25 12:17:00 | TERRA_M-T | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 66fc4ddd-3907-349c-bc59-f9d740e120ca | -12.7643 | -48.1223 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7aaa9b13-d9a4-3a1c-bd29-f0b6b4f6b4fa | -17.79807 | -44.48467 | 2025-08-25 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9030c6e0-be6d-3ce9-b652-e051b3a62875 | -14.09977 | -43.90751 | 2025-08-25 12:17:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| eddd9086-8cce-3a00-8315-7f4f3731450e | -18.19591 | -48.38514 | 2025-08-25 12:17:00 | TERRA_M-T | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 151b9a44-a9b5-3f49-be55-c62942d5de70 | -13.06142 | -46.32624 | 2025-08-25 12:17:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 503db5fe-ddde-34f4-9be3-c9171d0eda79 | -11.61137 | -46.35543 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 409ddac8-ff46-3430-a897-514866c584c6 | -15.13706 | -43.93229 | 2025-08-25 12:17:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 994d92b0-c846-3abc-859b-8ec8f3c2ce2f | -14.49984 | -51.93055 | 2025-08-25 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 74a50767-e0c5-336a-9204-a2925d64d5ad | -12.94413 | -46.31241 | 2025-08-25 12:17:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 96589db7-d429-3256-802a-13c6c14f1530 | -13.40626 | -45.90731 | 2025-08-25 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a3f7fb8f-eaf7-32b4-9bbc-40bbbbc751e4 | -13.73838 | -44.70095 | 2025-08-25 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| aaa3a95f-9b47-32c8-97da-a6bda03a6bd7 | -12.94287 | -46.32135 | 2025-08-25 12:17:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 51c86eaa-315a-3712-a30d-20094aaf1f5c | -19.07059 | -44.3158 | 2025-08-25 12:17:00 | TERRA_M-T | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7760e71b-c102-371d-84a3-a6aad4b3b719 | -15.66422 | -43.4855 | 2025-08-25 12:17:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d0742785-e2f5-3e0f-8be0-f082cfefc5f3 | -13.23582 | -46.53638 | 2025-08-25 12:17:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e26c8afc-a925-3745-9b09-35afe6da26cd | -12.67972 | -45.30375 | 2025-08-25 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4b7f88f9-5932-3240-867c-01b059521e28 | -12.68815 | -47.82882 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 399b1619-d341-3eb0-87a4-bf9888898444 | -15.17997 | -48.19534 | 2025-08-25 12:17:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3f0eda2e-f015-3d5c-b139-c76dbb9643bc | -14.26156 | -45.24194 | 2025-08-25 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3727da2e-a814-3774-a914-d1a677abe1b1 | -12.68103 | -45.29418 | 2025-08-25 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 3eb63c4f-b7f2-3387-bff5-8e07e356ff7c | -19.73464 | -46.46621 | 2025-08-25 12:19:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README95.md)
