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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fe231e8-2824-3cb6-a4c7-7ff792f768b0 | -10.73787 | -45.37358 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbb1212e-2f99-3fad-a98c-2851ff63c063 | -14.76921 | -48.10622 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c081b034-9711-3a5c-a8b5-f3b5c5fba572 | -15.13882 | -48.01429 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a6d4074-1066-3702-99bf-015165d2f8b3 | -12.8365 | -47.04372 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7aa273e-70b4-3eeb-bb56-d3da82871420 | -10.06359 | -48.18763 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab47fe89-fe80-3015-b94a-1fb6b1e7beea | -10.91824 | -46.47716 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1f0ae6a-7cdb-3e81-a269-a4dcaab6ac51 | -15.39107 | -49.19206 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| daae11c2-6f43-344c-bc81-7e0957061659 | -15.2498 | -56.81232 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6575e5b-1cf1-3002-9b68-f950e374b91f | -12.24197 | -47.81564 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| da6179e3-8920-3215-8e1f-c1f1bb18f239 | -11.46451 | -45.09327 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 238a755d-a092-3509-91b5-75be820688bb | -13.46231 | -44.37806 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38e41a35-5ec2-3624-96f5-6cdee4cb5089 | -10.04699 | -52.09393 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a9a7af7-8d54-3771-8224-e68c889726da | -11.44459 | -43.5063 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb107bcf-3fe3-382c-9cc5-d214e2b91697 | -11.38357 | -45.0663 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4441b8d9-4dca-3f51-b6b6-3a3d9fbb1e99 | -15.63372 | -49.17273 | 2025-10-01 04:21:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7e38a58-5d9b-3b05-abf2-34ac8a1e07e0 | -12.83011 | -46.97697 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61a9d1f8-868d-30dc-a24a-fcbc1f3754ba | -11.82701 | -44.99022 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 794b55f0-ef03-3a91-a028-5bbab6e9d1ea | -17.20835 | -46.9838 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae2a6a4-4786-3b20-a0da-661f571ee4aa | -13.98593 | -45.04981 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53480c4b-2bb6-3b53-9b3c-3315e56ddbfb | -13.37123 | -47.29735 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d91bcb6-5603-3c76-8003-3437265d9f26 | -10.90653 | -46.52942 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f4362ffc-2216-3015-b5e6-5ca8e460c190 | -12.83158 | -47.03189 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 955ffe53-2d40-3ed1-bc5e-2f1f2101c69f | -11.69677 | -44.30175 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32add555-8e2b-38af-a7ff-b8da7ea412ca | -13.21515 | -47.33769 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9861d6b8-0460-3049-a05d-9b5547d40815 | -14.60833 | -48.30777 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbe39219-2456-3030-aa09-86732b8a28ed | -14.98693 | -50.75704 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 215f1d2e-b0e9-36bd-9714-5aa3b02a7263 | -11.09959 | -40.95765 | 2025-10-01 04:21:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 67d42a45-594e-381c-8478-e08cd9783b6c | -10.82557 | -47.96487 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bdcb429-6daf-3cad-9a73-71511cd798ab | -13.67511 | -48.06597 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42ceee60-c481-355d-8793-d361710e33ce | -11.98172 | -41.83484 | 2025-10-01 04:21:00 | NOAA-21 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f306f8e-ad81-3db4-ae88-d854c5a76319 | -12.64273 | -44.16286 | 2025-10-01 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec1fca38-c327-3232-84d9-6a8fbe2b626c | -15.53037 | -44.34475 | 2025-10-01 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e005270b-e9d9-381d-aba3-28e1f45cf3d2 | -15.3367 | -46.2675 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b712ae6f-743a-3ea9-bfbb-63d54fcda56a | -16.76132 | -51.34718 | 2025-10-01 04:21:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 980175d8-65ec-3811-a2be-7bc9ef38e040 | -16.37296 | -47.04263 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ca32279-7fa1-34be-811f-b5459d1f0274 | -15.25894 | -49.26535 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c97f7da3-d2a4-37e1-801d-579ad4c6a7fa | -17.63584 | -46.14461 | 2025-10-01 04:21:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5af03a6b-128b-3f5b-922e-dbb033a41f00 | -9.43229 | -54.57156 | 2025-10-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8aadf3b1-01ad-32ed-ba6b-988cd4e6ff2f | -13.77816 | -47.96526 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b61b5a69-7453-3710-878e-45c0d003b51a | -14.35643 | -45.90021 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32ba277a-f103-3cce-9d77-861317717700 | -12.24892 | -47.79428 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bbdc031-97e7-370a-8a30-f39e201a23a7 | -9.95214 | -51.38084 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32692a4b-e95d-3f8c-86dd-c312e200e8ca | -13.81852 | -48.02595 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6f48000-0f00-3dca-b2c5-5e9c9fec7261 | -15.40975 | -45.65486 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aceefa31-a933-3738-979c-4d444ba04e1e | -10.84462 | -45.40845 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04f8aaf2-6698-396f-9601-6a8eb8f16c27 | -11.46729 | -45.09732 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7fc55e15-2889-388b-acfb-a243f0ffdb96 | -13.94417 | -48.11474 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8fef7f6-a9d2-306c-8644-30cee9e8a62c | -11.50993 | -43.53511 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aadb4cb-163f-3ed0-8c0e-dbbb9691ebe4 | -14.63415 | -46.97861 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64b9996-1b28-387b-89fb-b413111d1352 | -11.81209 | -48.24953 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f6df922-49e0-3e36-a553-1fec21713361 | -9.73291 | -48.02748 | 2025-10-01 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bd6e051-6eec-3cb8-a6aa-2e5094df028d | -11.83917 | -44.97759 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f27a92e8-d166-3d50-b842-aacc479b9e7a | -15.4839 | -48.54907 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 846ee053-a716-3757-82f4-105a1e919b55 | -12.05737 | -44.86128 | 2025-10-01 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7fbcb4f-15ac-3b0f-989e-63ae09812cd8 | -11.65371 | -45.32216 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c9b5a8b-fe5b-3b47-a0d5-e45f83651837 | -15.77716 | -43.6787 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9456b10b-21b8-36d1-a168-f4024a547ac3 | -15.40502 | -47.05246 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63de6f94-1798-33e4-9f88-3ea7998822b5 | -14.78687 | -45.79693 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37c00208-efde-35d0-94f2-d5710623daa9 | -13.78253 | -47.98095 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4089d2af-a214-3565-a084-bdbe7dc5b42f | -16.64459 | -41.12501 | 2025-10-01 04:21:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 40e2cc71-d9d5-3e17-9691-2ae64317963f | -10.91407 | -44.33214 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19d39f1a-7be0-3e66-a070-78004a7c477f | -14.98447 | -50.771 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f52a5d3-083d-3d78-9ece-5385afc9181b | -11.8198 | -44.99279 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f67c1c5a-7672-3ca1-bb74-7599682ce2b1 | -13.09228 | -47.02047 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8b18ab2-d6c2-3ea3-a16c-db7f78947224 | -14.7902 | -45.79747 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d276b8ba-b3e9-3901-b7f5-179a6b320c7e | -14.09749 | -49.74684 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0630fb0b-e431-3f18-b429-966b0b481c0c | -16.25777 | -50.93457 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| bc9f5c62-fea4-3fc6-91cb-015346c5b94b | -12.69783 | -48.55417 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb21ed46-876c-37a1-8046-1b1fdaf2e183 | -14.89797 | -48.11235 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1c744f4c-6d6c-33f0-8f8d-9ea502f7ea6e | -16.58029 | -45.1124 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6441db5-2497-3e21-96f1-40fbe68e99d0 | -14.02614 | -46.31905 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6114d6e3-b408-3bde-a6ce-2f1935291e71 | -10.90759 | -46.54409 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2945b939-0a81-320c-9e49-10bab0bd72bc | -14.95503 | -46.8864 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e349a442-dc05-3b8f-b9ae-a3c21fa78145 | -14.02174 | -46.32557 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 981a58c5-d29b-3bbb-a8fd-805d6016bb77 | -10.81428 | -45.3606 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c5e214a-b3a4-3070-b787-c49a6caf4027 | -11.92393 | -47.88988 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c9bf6dc1-900f-398a-a33b-5370f15c1030 | -11.79783 | -46.61793 | 2025-10-01 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6db64cdb-632b-3062-8da7-5ea6f130a367 | -10.0374 | -52.09668 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1af8a08-b311-3070-ba5d-6c177a915688 | -14.76704 | -48.0984 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83b4a202-8842-357d-8e3c-12c3d061f500 | -14.50583 | -48.48686 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed48daec-91cf-35f8-ad25-87070f1de82c | -14.44298 | -46.35146 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d17cac87-acd3-359e-929f-8cfc8b73a12a | -14.01721 | -44.97935 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e31f8ee5-876d-3dec-ba41-2de7e5df0888 | -14.51326 | -48.48419 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0df8d323-9136-3341-a53a-011fbab151b7 | -13.33081 | -47.33878 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6660b96d-a9c3-37bf-aa50-f8b1e39fbfac | -13.80392 | -47.48697 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c219029-6f3b-3c3c-b07d-121d96193086 | -16.38119 | -47.05501 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af69ecec-318e-3852-83e6-2d50413aada3 | -14.1928 | -46.1217 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a89a44b7-672e-3d49-8c23-7fe6b70befe8 | -10.93088 | -46.50447 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2220fac0-3d36-3d9f-944a-ee165192b78d | -14.21688 | -46.10003 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f274f038-4dcc-3679-ab5a-0d735e28c8a8 | -16.39993 | -47.04348 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 837bd3db-f6af-332a-93ff-1ea7fd972426 | -15.14034 | -46.43999 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29b84a58-1964-32c8-a753-66959f26b783 | -11.81617 | -48.24626 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d64c5f40-2b19-36c2-b1c1-23167f613c7d | -13.6472 | -47.21175 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55a6a303-effc-33f5-9192-853c6ee9dcaa | -12.82955 | -46.98053 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cba2d962-a167-382c-a495-d33398ac5362 | -10.06843 | -50.26478 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28fc54e5-c35a-35af-b9f1-5d2aa51c4109 | -15.30641 | -46.39784 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64020d13-cf75-3a71-8dd1-d31d8f071440 | -15.17336 | -46.40165 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88cb062f-4b55-3aee-b6af-3885b29d77df | -15.78136 | -43.70124 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 548a5454-5935-3443-b0b4-5c131f67b065 | -15.38282 | -49.19879 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59cb89de-fa15-34a6-9b50-97f5fb1ff366 | -13.92138 | -48.08447 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README64.md)
