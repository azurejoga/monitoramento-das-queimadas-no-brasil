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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32e37d72-566f-3429-b334-a1e65c76858f | -19.04687 | -42.73388 | 2024-09-26 03:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b8714921-d318-3983-96bb-f9ac7477b35f | -19.62924 | -40.21444 | 2024-09-26 03:19:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7108937d-8e04-3c90-9e8e-8a0d612600f6 | -11.84523 | -43.8287 | 2024-09-26 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d22af190-d7f8-3aeb-87e6-13bdcaca6055 | -11.84666 | -43.82193 | 2024-09-26 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41be0c9b-658b-347a-b1c7-39b8c7bd8686 | -13.26465 | -43.56905 | 2024-09-26 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22a78528-ec75-396c-a755-1e71691c89bc | -13.26729 | -41.49912 | 2024-09-26 03:19:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 21d35b78-f4ac-327b-98bc-10e7930a219f | -13.44296 | -43.77499 | 2024-09-26 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6314ecbf-fd84-3c2f-81a9-dfa1e31c926b | -13.53135 | -42.56273 | 2024-09-26 03:19:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87baaf8e-529c-35ce-bcf9-717600779ad0 | -15.91104 | -45.0056 | 2024-09-26 03:19:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e164d67-d3e9-3d61-a56a-63ec4878cd20 | -15.91258 | -45.00175 | 2024-09-26 03:19:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76f43fcb-9850-3f2c-9ffc-4dc917a4c239 | -16.03769 | -43.6184 | 2024-09-26 03:19:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bd75e0e-f8ba-333a-8523-b43dfbbcfc3c | -16.03858 | -43.62055 | 2024-09-26 03:19:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c33651db-60ea-31a1-ac22-87fb2ae13864 | -19.04754 | -42.73506 | 2024-09-26 03:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e03b6f49-6068-3a27-ba9d-9863ea844203 | -16.32044 | -45.67569 | 2024-09-26 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1cd7201-e0b1-315b-a1e5-83303b0c1fb8 | -19.04767 | -42.73018 | 2024-09-26 03:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| e1d1dbb7-fa1f-3b2c-88bb-7bde8d37b966 | -16.32392 | -45.67608 | 2024-09-26 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56e7c2bd-fdd0-376b-99ae-fb87c88c0e21 | -20.10101 | -43.84776 | 2024-09-26 03:21:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 41a2c700-9959-3fd2-b20e-55b5fd09eddd | -19.98588 | -42.34449 | 2024-09-26 03:21:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5143432d-ee27-39f3-a336-632c950fd8ae | -19.954 | -44.96608 | 2024-09-26 03:21:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03a0bde3-ec9f-3373-b309-714e1b25ddc7 | -19.95271 | -44.96725 | 2024-09-26 03:21:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35dbf947-61e1-3f3c-a03a-0327509a49a9 | -19.95262 | -44.97184 | 2024-09-26 03:21:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bb85f09-f04b-3e00-8658-961159d36765 | -19.93463 | -43.79535 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 05925bfd-bcf5-3f1d-9166-2e78740264c2 | -19.93338 | -43.80076 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8b86ec61-7f87-31bf-8d77-98470b1105d8 | -19.93239 | -43.77773 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0969932b-880c-3667-a55d-647d13c7e3b1 | -19.93063 | -43.77671 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a870e687-7afd-345c-bdff-a95cece83865 | -19.93001 | -43.78808 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5c650371-87ad-3152-a065-a6077e607cd5 | -19.92872 | -43.79368 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 98cda42f-409a-3408-b380-eb5889f0832e | -19.92826 | -43.78733 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9d849f3b-9f1b-3cac-82fc-b25da4d6e909 | -19.92745 | -43.79917 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b7d73b20-407e-35cc-b2e8-5b02763c32ba | -19.92701 | -43.79294 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e5fc0942-8c06-3907-a803-91993d81067f | -19.9258 | -43.79835 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 698d00dc-c67f-30e4-85c1-588ecbf083f9 | -19.92534 | -43.78101 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 161ed8e4-0686-32ff-ac05-59d40163ba85 | -19.92359 | -43.78011 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2fcb6fd1-fbb8-38df-98c3-452dfbf20658 | -19.91544 | -43.79659 | 2024-09-26 03:21:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 274c2043-dd9c-3465-9db4-79f38b7691f5 | -19.82673 | -41.94008 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6a973f69-1957-3748-8e20-18bee92dc965 | -19.82597 | -41.94356 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61a2519a-3f38-3497-95d2-65a4c30d4ebe | -19.82133 | -41.93902 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a35de4b5-83a8-3e03-a0b4-f93126dbf33b | -19.82047 | -41.94298 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e23d3002-a1e4-3ca7-8172-16e8e9c995af | -19.81959 | -41.94702 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1a0a02d-7a63-3ee9-8686-a2701023f7d1 | -19.81589 | -41.93814 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 32473b0c-c6da-35b3-81ff-f9f4a5f661a5 | -19.81502 | -41.94216 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2b6bd10c-970c-37d1-97cf-d28525834d04 | -19.81415 | -41.94617 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| ae984ac2-ee01-398d-8e21-9611acbe7b6a | -19.81326 | -41.95024 | 2024-09-26 03:21:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3ee47fdb-f7cf-37d9-b095-d024b57cb2e6 | -19.80927 | -44.06094 | 2024-09-26 03:21:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eab4e737-5409-3406-af2a-0f276ef4a23f | -19.75242 | -43.97452 | 2024-09-26 03:21:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f73febff-0487-3fa0-9e99-f0eba00e3439 | -19.75127 | -43.97944 | 2024-09-26 03:21:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73c1cab2-4e9c-3940-ad9c-d47dd64c02fe | -19.75124 | -43.97729 | 2024-09-26 03:21:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4290af7c-af8b-3254-a9cb-581890d82825 | -19.73407 | -44.77052 | 2024-09-26 03:21:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f2d0f130-a94a-3016-86f7-217f80cb19f3 | -19.67797 | -42.43582 | 2024-09-26 03:21:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c36e5552-4fd1-354e-8601-9260507ed129 | -19.6771 | -42.43975 | 2024-09-26 03:21:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ef94f7f5-5409-39a3-860e-9348e3b8f211 | -19.67157 | -42.43841 | 2024-09-26 03:21:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 09c8466a-529c-3429-82af-3f8ff16fc29e | -19.64781 | -43.81295 | 2024-09-26 03:21:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7271325c-6413-3c07-a2a7-93c478cec6cc | -19.64299 | -44.16957 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbb8a8c8-8de3-39f7-96ee-cba3d9043726 | -19.64187 | -44.17441 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5267e78e-14d0-3028-afa2-f72fe810a771 | -19.51473 | -43.75138 | 2024-09-26 03:21:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9da632af-b521-3a6a-a90e-9d579e1fffc1 | -19.51889 | -44.50434 | 2024-09-26 03:21:00 | NOAA-21 | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7c74fdd-0b39-3862-8acd-5dcb1b34da86 | -19.52516 | -44.50584 | 2024-09-26 03:21:00 | NOAA-21 | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9e5fda1-69c2-3525-afd7-dc2767f56ec1 | -19.57493 | -43.5423 | 2024-09-26 03:21:00 | NOAA-21 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 691c8c47-264d-3f40-a36c-617c64ff3ec6 | -19.576 | -43.53757 | 2024-09-26 03:21:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| dde032a8-7cc7-3ba2-98f5-437d5f8d2c19 | -19.61315 | -42.80647 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d3059949-29e1-3ca3-8089-4ac40af8f7d4 | -19.61384 | -42.80334 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c338c803-b74f-3f44-9a3e-9fee69987384 | -19.61454 | -42.80021 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 3057ee45-89a0-395c-8aa4-bb63137b772e | -19.61472 | -43.59971 | 2024-09-26 03:21:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32235228-dff0-3843-8f38-1a2c5613be91 | -19.61527 | -42.79696 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 28392c31-c929-3387-85b3-70a3a3557627 | -19.61608 | -42.79331 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| cf0a4e83-565f-3e2b-a8dc-bd3aea24d5ea | -19.61726 | -44.16882 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eba70a1-b765-3e3b-aa32-0129df2e5a0a | -19.61862 | -42.94343 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| afd859b4-1ba9-378c-8807-8670c456fab3 | -19.61892 | -44.16685 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e94a4221-a880-3aca-a09c-6cec42204805 | -19.61968 | -42.93869 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 241cbd34-45f2-3802-88fd-3277b79bcc29 | -19.62005 | -42.80225 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f8623d60-80a9-381b-84e1-d93852f913ad | -19.62091 | -42.79839 | 2024-09-26 03:21:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 781bae31-c602-3d12-a779-39fe8be8efb8 | -19.621 | -44.1806 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 152489c1-698f-3ba4-848a-737c08bb5d1d | -19.62155 | -44.18385 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 937b811e-fadd-3595-a2e7-bf6e7ff3a2de | -19.62277 | -44.17846 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21fddf74-c78e-38d2-b038-dad3c2a7c712 | -19.62349 | -44.16988 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7659d1f6-36d5-31b7-8f13-6c3e7f33ffdc | -19.62603 | -44.18683 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 150db215-de04-3367-86fb-f868e196249a | -19.6273 | -44.18135 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14465f62-0bf2-3ee8-81f2-ad7dabb21a72 | -19.64177 | -43.81165 | 2024-09-26 03:21:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d600fa7-2bcf-323e-b84d-a186fd7800c9 | -21.18831 | -45.75072 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e4c2beb-16e3-3f1e-a0e6-b743a4cbf8d6 | -19.87549 | -46.88377 | 2024-09-26 03:21:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36deafef-d5f4-3172-ae0d-c616d93317e0 | -23.52934 | -45.92426 | 2024-09-26 03:21:00 | NOAA-21 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9303d2ce-13fa-36d5-b5d9-003acd62b89c | -23.3569 | -46.28988 | 2024-09-26 03:21:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3bb153ec-55a2-37f9-967d-0231dcd67d1b | -23.25485 | -46.77407 | 2024-09-26 03:21:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1809ea31-d93c-3c73-901f-c7a159a289e5 | -22.54969 | -45.8503 | 2024-09-26 03:21:00 | NOAA-21 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9a9f32ca-434b-30ee-b869-a23888b96f6d | -22.36872 | -47.63625 | 2024-09-26 03:21:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c35c379-0d4a-3361-9510-cee6dc4f331e | -22.36685 | -47.64339 | 2024-09-26 03:21:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 64a00a4f-a6ef-3493-931b-ce44d10a6c95 | -22.36442 | -47.63538 | 2024-09-26 03:21:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee2c2b21-7946-310a-b27e-0f2a7b940402 | -22.36252 | -47.64281 | 2024-09-26 03:21:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7c85a55-04a2-3325-87cb-8ca2de51ea5b | -22.35127 | -47.76046 | 2024-09-26 03:21:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6600466f-d62b-340d-9796-83bb24d507f8 | -22.34883 | -47.75524 | 2024-09-26 03:21:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e5c8dd6d-a4f9-3c2c-93e7-6b6bdad32019 | -22.3475 | -47.76044 | 2024-09-26 03:21:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 66b06d50-6619-3e4a-bfa1-556726bacc9c | -22.34586 | -47.76687 | 2024-09-26 03:21:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 892747fe-d5be-36c7-8075-144c3a151dd4 | -22.3441 | -47.75906 | 2024-09-26 03:21:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bfbf6c7f-8fe1-3181-94ed-59a362c400fd | -22.34237 | -47.76569 | 2024-09-26 03:21:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e1c9825-80a9-36cd-abb1-50ceb05c42f8 | -22.21478 | -47.56123 | 2024-09-26 03:21:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 546bbb78-41c7-3539-9f08-2138587e7033 | -22.21285 | -47.56871 | 2024-09-26 03:21:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a2297de1-55be-373f-99a7-9bca42880166 | -22.20795 | -47.55873 | 2024-09-26 03:21:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 87339a5f-c425-335a-a3b1-d289a8442f6f | -22.20593 | -47.56655 | 2024-09-26 03:21:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 30cbaf5d-6612-3fc2-bc61-6e7eab60ee00 | -22.19408 | -45.71013 | 2024-09-26 03:21:00 | NOAA-21 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a7799f8f-f292-3f83-819a-4d57c0e592d5 | -22.19293 | -45.71494 | 2024-09-26 03:21:00 | NOAA-21 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README52.md)
