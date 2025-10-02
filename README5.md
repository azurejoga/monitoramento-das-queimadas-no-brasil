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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f96b519-05b6-34d9-a30c-e681d49c286c | -15.00714 | -40.15472 | 2025-10-02 00:11:00 | TERRA_M-M | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0f1a1894-5c15-3330-a852-8742c5d00778 | -12.11811 | -43.42916 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e84df31c-830a-31ef-b2cf-1a48af77f6f3 | -13.32453 | -43.10048 | 2025-10-02 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 1085f483-ce8d-306c-adeb-b07f37f3f605 | -15.60344 | -46.90893 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a368be78-e136-3293-aa42-9a9469c28d8c | -14.41735 | -46.104 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 333443ce-277d-31dc-90cf-55320aad6cef | -13.94961 | -48.09948 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 755751a6-c4a4-3ac9-ad65-2c2e862e5120 | -15.17287 | -43.61843 | 2025-10-02 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f7560304-621a-38f0-8cb4-86df77d67f75 | -14.48174 | -48.42291 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 47da852a-efad-399e-bbcd-94b84df98898 | -14.40552 | -44.90656 | 2025-10-02 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a524d949-69f9-3841-bebb-0f945ecb8859 | -12.84027 | -41.55348 | 2025-10-02 00:11:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| fd2efbef-8c90-3809-9664-12d7278ac82b | -14.49241 | -48.47161 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dc99527e-0393-3f75-b3bf-9f17fa55dc65 | -13.46991 | -47.25562 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 10672953-c960-3c07-86b9-8671b4fba0f4 | -15.24098 | -48.09724 | 2025-10-02 00:11:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2bff9e0b-6011-3854-a7a7-1f9e127c2977 | -13.37129 | -47.28886 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 13e43f26-077b-3fe5-98cd-14d458676cd5 | -13.78421 | -48.04882 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 0ff73244-a060-398e-9d49-35cef9369f08 | -11.1242 | -47.73158 | 2025-10-02 00:11:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e894a2ae-1678-371e-8b0c-9c440053d373 | -13.31293 | -47.20148 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 788af6eb-ba28-30af-9e52-420e485ef717 | -14.21512 | -46.11884 | 2025-10-02 00:11:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 04a304ee-09f0-3396-a72d-097bf8ce68af | -9.93612 | -43.70862 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| a28921e4-2521-369c-a4ec-94dac42fa2ec | -13.80561 | -48.0558 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5416e6a7-f76a-32d3-905d-16b5b0f82e08 | -11.86867 | -49.91155 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0745eeac-c9be-3fe4-b592-f017cd497feb | -11.13539 | -43.39264 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5006bf10-035c-341f-ae90-ec825f7f299c | -11.80741 | -47.59562 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ad776011-367f-3422-938d-044b07001b4c | -15.24781 | -49.2967 | 2025-10-02 00:11:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7b81f93d-ffd9-304b-9bb5-29a48e1ff710 | -10.95012 | -46.66951 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 00849113-c7d6-3749-8135-861f73cd63b7 | -12.21555 | -43.74612 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e1bbda8e-b25a-330d-b5ce-a6d856785747 | -12.14519 | -46.67659 | 2025-10-02 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| db0d5cae-fc94-3168-9b92-95701fa6d591 | -11.50175 | -43.50652 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b9caea4-6f4e-3657-b22b-010f9eddf99b | -11.60652 | -42.86775 | 2025-10-02 00:11:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a144700c-fab4-3f96-aa93-f85f7f89a42d | -13.39794 | -44.38752 | 2025-10-02 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fe83a85d-c70a-367f-bd4e-3c209d28a246 | -14.31144 | -45.98962 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e60200b4-e7b3-3bff-9480-41736dd12ebb | -12.12693 | -43.42786 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4726c79c-5d6c-321b-b20c-de2d3bcaa7a4 | -11.34915 | -48.34369 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2bdd8279-dc45-3e76-93f8-ff6eec08e99e | -17.17227 | -47.03381 | 2025-10-02 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 4f3e9337-d65a-3c66-9aa8-58c5f1b8168f | -13.82377 | -47.5261 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 38c2889f-e6ae-3a9a-9c4a-481aaea79373 | -16.87254 | -40.60759 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| cc7f3880-2fed-33d0-85e9-823b39cba6b4 | -9.95106 | -43.75182 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 85e54ab1-ae32-323f-ae4d-f2fe7e54f6ac | -11.58973 | -47.22294 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7f37d0e9-0265-35ea-845c-48ea451e7fc4 | -11.79489 | -44.99759 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4c0f111e-3da9-3eaa-9109-9a96303d220c | -15.24539 | -49.27458 | 2025-10-02 00:11:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| d3c0234c-bdd2-3849-805b-53c9fd2808f8 | -13.17464 | -47.8382 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 94723e23-b4af-367b-a4e8-3a2bfe4040d5 | -15.17523 | -40.4275 | 2025-10-02 00:11:00 | TERRA_M-M | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 819dcb8d-0ecc-3d64-ac00-c4abcedc3fb3 | -13.79217 | -48.04158 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 13605545-e418-3f0d-803f-4db7bd948c81 | -13.80889 | -47.49559 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 1f3e768a-1481-30bd-8ba0-bd039e17514f | -13.40702 | -47.77495 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3c7ac88b-14b5-3f5c-8a43-7d836d870cb0 | -13.31317 | -47.84563 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 0b0a1c43-4721-3503-9a44-40e389fd2d38 | -9.93344 | -43.75436 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 342.1 |
| a3a3b442-8b45-3b87-96b7-8a1beb5b640f | -11.76727 | -46.83703 | 2025-10-02 00:11:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7b382311-7d42-358c-b0f5-c466e24d37ac | -11.81762 | -47.68069 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5995d0dd-3e03-3411-a1f1-5d5aa286a5b9 | -16.88314 | -49.68321 | 2025-10-02 00:11:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6a06865c-c651-30da-81b5-2cf1cbaacade | -14.22524 | -46.11757 | 2025-10-02 00:11:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d7ebb7a0-bc6e-3919-972c-670634157caa | -10.2384 | -50.348 | 2025-10-02 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 275.4 |
| 8510fce1-e8dd-3c0c-8c33-73ac949397ff | -10.9123 | -44.32148 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5b4b2e92-c21d-369f-a94c-8c72075aedda | -13.75773 | -48.68783 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e849a555-2af6-395c-b456-a6466dcec0c1 | -14.53417 | -42.97581 | 2025-10-02 00:11:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 56721bbb-3151-311b-9990-49b9481597f9 | -12.65547 | -46.9434 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 744aed75-49c9-32e1-a805-5c679c820b79 | -9.85438 | -46.87757 | 2025-10-02 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b07386a6-6c90-34d0-a8e7-4c6124483906 | -11.00762 | -49.57911 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| c9704201-703d-363a-8999-db27e88c502e | -13.82361 | -47.53184 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| f5b9a51b-a7bf-36de-8943-cd272f18493b | -14.70678 | -48.21629 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fb1ebfc2-ced0-3136-98b7-d050cb61f6e7 | -15.0497 | -42.10544 | 2025-10-02 00:11:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a0846685-c1d4-3687-aeb0-722d87a13327 | -13.19934 | -47.85196 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ae942288-7d71-3742-b99e-d261bb721cf7 | -13.38881 | -46.9471 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 96e55895-f4dd-3d61-a18e-46d7b68fd7eb | -14.9089 | -47.22593 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f1afde68-3453-39fc-9d98-fbb80f2486c3 | -13.81435 | -47.54262 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| daddfe5d-67b7-328c-b562-eb530e34e6fe | -13.17123 | -47.80994 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 0ed81e55-7dd7-3f36-a790-7d56b5003db3 | -11.48007 | -45.11582 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 79b6afb1-262e-352c-b1b2-5c2ccd0b19ef | -9.95128 | -43.68831 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6f5be3ae-a736-3a66-8e0f-030d9cd8b8ac | -11.46697 | -45.01809 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7c21535e-43dc-3222-bb83-c7ff0f508be9 | -9.89762 | -45.9563 | 2025-10-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c4012ddb-f730-3dee-9430-c71eb6453351 | -13.79579 | -48.04704 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 2093a673-d637-3686-90ac-0d084bb883e2 | -14.31995 | -45.97614 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7947ff0c-34c8-3706-a27d-ccdd2b0a6ca5 | -9.95005 | -43.67942 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1534c03b-512d-35bf-a7ca-db47ecb03ea8 | -15.15981 | -40.43613 | 2025-10-02 00:11:00 | TERRA_M-M | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| dce93c67-d713-3dbb-9a21-bc2c861d3b7c | -15.82023 | -41.89244 | 2025-10-02 00:11:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 58a4a25f-02df-39ed-892a-55786d19b2fb | -13.39922 | -44.39713 | 2025-10-02 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fc854289-02a2-363a-bb95-e2bc3229a95f | -11.9105 | -47.88958 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 52ed5e86-0ca8-3d3a-be69-a621b13daf9d | -13.06277 | -47.01371 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 28454381-ac17-347e-83d8-ee35f04ecf64 | -13.38413 | -46.95321 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 65dcce1d-d36e-3bcb-a76d-373829486a21 | -12.11933 | -43.43808 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 29fc987c-9e7f-3c29-863e-22ccd64a1338 | -10.95792 | -46.65075 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| aafab5d6-c241-36a8-a170-ac68a6f7794a | -12.41294 | -47.5101 | 2025-10-02 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 543c29a5-53b4-3d11-bc13-e88406759154 | -11.78872 | -47.56063 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9a723466-2ac1-3edd-a80c-7fa492639cc5 | -14.48433 | -48.40001 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ffd2a8d5-5b7b-35c0-acb8-7432d882c123 | -11.34686 | -48.33845 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 56875b99-6922-3b3f-8348-09be90b82911 | -11.59771 | -42.86905 | 2025-10-02 00:11:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e0d64fac-af46-3346-94cb-d80a630a95b0 | -13.24016 | -47.32743 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 69a27bae-de41-354b-bb66-a647008bc968 | -10.95939 | -46.66242 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a66be3dc-edde-3346-9ba7-94f78285a2ef | -10.90338 | -44.32274 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8e043af-a1a7-3e29-86c1-86b0bc8c2ff2 | -14.35929 | -45.96526 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 91c882e3-3c6c-309d-9379-5793755d7c78 | -10.83303 | -46.63243 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3c3261ea-4c7e-3149-89ad-897481cf8084 | -9.94347 | -43.76198 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| ca358182-ef4d-3564-99cb-aa93370f61ce | -16.27911 | -42.54392 | 2025-10-02 00:11:00 | TERRA_M-M | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8ee83d24-e554-3814-86a1-ee32ea597a0d | -13.78626 | -48.06564 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e209f32a-5153-33f8-b9d9-08cc462f3792 | -13.80861 | -47.50236 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| d4672ef5-5a21-386d-920f-aad86f5a6e99 | -10.24092 | -50.36956 | 2025-10-02 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 08473417-34b0-3672-8c02-864ccdac19bd | -10.84149 | -46.61944 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 5d872012-0836-3674-84e3-5f1e606399b1 | -10.22265 | -50.32809 | 2025-10-02 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| ae523423-a742-34a7-aaf3-f1b12d7ccddd | -14.21569 | -44.93431 | 2025-10-02 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 6dc44399-4096-306e-ae6d-aa36aeef4a94 | -13.44115 | -44.22937 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README6.md)
