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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa9be589-bac7-3212-a876-67bfacac895d | -21.31492 | -47.60904 | 2024-10-09 04:42:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e8a60c1-5610-3376-9f12-117bd5702dc4 | -21.08086 | -47.57172 | 2024-10-09 04:42:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77900f99-657b-33ff-894b-54bf8fcb998a | -21.08015 | -47.57737 | 2024-10-09 04:42:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e32585c5-9609-3788-9bd8-bbd116fb5151 | -21.07685 | -47.57108 | 2024-10-09 04:42:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1629a78e-f67a-3746-b926-99392af41e33 | -21.02951 | -47.5811 | 2024-10-09 04:42:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce17447-44ac-3497-beb1-cb8527d094f4 | -21.02549 | -47.5806 | 2024-10-09 04:42:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17e30b63-e263-3efd-b74d-1dd52c1212cc | -21.02147 | -47.58009 | 2024-10-09 04:42:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 235baf12-8e33-3aa0-97c5-b90d91a0022f | -20.88673 | -48.18948 | 2024-10-09 04:42:00 | NPP-375D | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe8114e3-8cf7-3d92-aa26-d7b2679d5913 | -20.43404 | -47.97395 | 2024-10-09 04:42:00 | NPP-375D | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13de33d2-d46b-38fa-bd9a-ffe6d2678e8f | -20.01993 | -48.22395 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51802fb0-aa80-300c-9ac0-48cd92023cb7 | -20.01611 | -48.2234 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ed1a909-4798-3fae-883d-7bad5c5a26b9 | -20.01229 | -48.22286 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b7086ac-6db1-30a8-a649-6b3301f13b9e | -19.77753 | -48.26796 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2b49b5f8-e3b8-36e9-aa5d-5f785c9b8977 | -19.77607 | -48.26954 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f5960182-e196-3261-b825-c55ee43143e7 | -19.77373 | -48.26745 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6610c334-77ee-3d38-850b-70a1c748073c | -19.77227 | -48.269 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 38f567af-0106-376c-8f86-183d2dc4105d | -19.76993 | -48.26693 | 2024-10-09 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee549197-0158-37dc-868d-1608c0fc5555 | -19.76481 | -48.27612 | 2024-10-09 04:42:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e73e1b8-22cd-3272-a150-21f61230e05a | -18.93092 | -54.56118 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5cb149d0-ff33-3b45-9cde-783965be4549 | -18.93023 | -54.5652 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e57a8e45-da42-3034-b910-52d0e3b13655 | -18.92884 | -54.55242 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2794cc2-f5b7-3a86-ae83-c1c89ccc7237 | -18.92815 | -54.55642 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 50a73040-ddc1-3034-8f08-a3296a0d69ac | -18.92746 | -54.56046 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 78fdcbdc-14c0-30ee-9ea2-8070e2d4c8db | -18.92676 | -54.56449 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e1eb6f17-dfaa-3188-b3de-e8511f9288e0 | -18.92538 | -54.55171 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 43f39429-d179-3f91-b30f-b153c1c4efb2 | -18.92482 | -54.54863 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da701547-eb0e-344e-9bfc-4c1e81f6859e | -18.92415 | -54.55258 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8611b881-484a-372e-821c-44228328be19 | -18.924 | -54.55973 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16e965da-ec70-3577-bf27-1dc0f9db8c07 | -18.9228 | -54.56064 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7b6ce74-fbb1-32f4-b787-72a2c1060ddc | -18.92192 | -54.55099 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d51b21e5-2778-374d-869d-a358b7ef65f3 | -18.92123 | -54.55496 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a63b711f-8d92-3868-a9be-fbd874cc1101 | -18.92069 | -54.55187 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3d597d6-12c3-3c68-aabb-f67fbad171ad | -18.92053 | -54.57988 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b537d1d-b4fe-355c-9953-3b58975a9616 | -18.92001 | -54.55588 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8299fdc-3e97-3f35-a6f9-6bc17aa0273b | -18.91941 | -54.58083 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ceb7f8f4-4bcf-331f-94f2-0afca12f3e40 | -18.91705 | -54.5792 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6612fc2-b15c-3cb9-89c2-57a102b019bc | -18.91635 | -54.58328 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 783a63b0-fa1d-353c-84b6-d7458e7fec6c | -18.91593 | -54.58016 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4019388c-21c9-38a5-95a7-4b473960ddda | -18.91314 | -54.57541 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c88b22c-9b92-3c97-b59d-47fc77b1bf53 | -18.91176 | -54.5836 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4d84f4f-e24e-34e5-a85d-37eb5a241c1d | -18.90828 | -54.583 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e62e54c-1506-3516-ba26-8ce3b5a7c35e | -18.90411 | -54.58646 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fa3c845-c52c-36ab-9168-7a3c51557516 | -18.90062 | -54.58585 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb78b6c1-849a-3fb0-9f95-3158284008e6 | -18.89725 | -54.45743 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35b7cc90-9bf3-38fa-9571-fb3863036e48 | -18.89713 | -54.58525 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1869af9-4e9b-3de1-9bdd-8d2d3edc682a | -18.89378 | -54.45683 | 2024-10-09 04:42:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 596491c4-739a-3cb6-b590-ac5a3109ad22 | -18.89311 | -54.46078 | 2024-10-09 04:42:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8c3adce-30d7-305b-b496-3f834ee456d9 | -18.8797 | -54.58219 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbddade0-1359-343f-a43c-22e70b0ce261 | -18.87621 | -54.58163 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19d21229-0017-3ba7-bc60-cd6db2f4dc84 | -18.87552 | -54.58565 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e8e79de-8f2e-33d5-b563-d4a51ab80a19 | -18.87202 | -54.58514 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c4d1db7-5173-3888-a175-2ae5854a3462 | -18.86991 | -54.57643 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb615472-332f-37e7-9959-b1d042264857 | -18.86922 | -54.5805 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b83afb6b-8e0b-3106-9ba3-44ebaaaf534a | -18.86853 | -54.58455 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 916cc2ca-d3a1-3957-918b-18827953dc6a | -18.86642 | -54.57583 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e9e0ebe-8fde-36e9-b04d-d4ab2a2ec0e7 | -18.86293 | -54.57523 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db512bd6-bb0e-3b9d-9a84-8f3a67e91bdc | -18.85946 | -54.57456 | 2024-10-09 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2edbec83-2cce-35d4-a49e-d31008461809 | -20.6583 | -45.9146 | 2024-10-09 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df9b6e26-39a8-3c50-952a-850713bb4335 | -21.11536 | -47.22721 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19dbe120-4164-3836-884e-d044c57cdfe9 | -21.11489 | -47.23103 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 274615bd-58ef-36bc-8737-a50285aff557 | -21.11121 | -47.22696 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6f53b61-ce4c-325c-8673-9f6c7f4a1e6f | -21.11074 | -47.23084 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f6ab3b6-4e9e-3e8b-9260-6f6d802df649 | -21.10985 | -47.23806 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6f2ed85-f60b-3b79-b71f-286e2b19ad86 | -21.10706 | -47.22678 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17410f65-cd19-3c7b-955f-de086954df1f | -21.10658 | -47.23072 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fc0aecb-540b-3029-9a8a-4427062a449e | -21.10615 | -47.23425 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 100e0206-cc26-3b48-ac0c-cd27a5a13c02 | -21.10571 | -47.23776 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae70a691-54e6-397e-a84f-eb43a2a44143 | -21.10527 | -47.24136 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 515ef278-b03c-3611-8a12-d303b47db0f2 | -21.10245 | -47.23039 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9ca1d1d-8d33-317e-ae0d-13e17537c937 | -21.10202 | -47.23388 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81fce692-902a-3518-851e-2dcc35dcb5b6 | -21.1016 | -47.23731 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83aa8406-dee9-3b11-95bc-f75ca0a5f4b0 | -21.09883 | -47.22575 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 089e4312-e513-304b-8065-1cb0a1b7e67d | -21.09791 | -47.23335 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f98a9111-554d-3bb0-bdf0-55ea4f348c73 | -21.09749 | -47.23676 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c56c7d76-7c4b-3570-a7d7-79c471d46288 | -21.09473 | -47.22514 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf7c847c-f72c-363d-8bdc-20f3dfe07fd4 | -21.09424 | -47.22921 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 08799b9b-796b-32ca-b599-8271b892e3b2 | -21.0906 | -47.22477 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d7103d0-0cf2-3b62-b1de-a7e74ed377e7 | -21.08862 | -47.2177 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cc18d9f-a472-3e8a-aa03-4b1288810644 | -21.08743 | -47.21648 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c3382b6-78f2-37ee-b39d-d176db387b97 | -21.08385 | -47.21146 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f521ad5-6cdc-37a4-b3e5-1e2d7c1d80a5 | -21.08335 | -47.21566 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 684cb39d-82bb-3bf3-8bf7-13fb01f1a201 | -21.08101 | -47.21192 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c73d90a-c8bf-3c49-9239-e0318b9f923d | -21.08046 | -47.21617 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d56e0aa-fe0d-3107-9f9c-96fc662a1c05 | -21.07641 | -47.21518 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7095d3bf-725d-3395-9031-e0eb28b806dc | -21.07588 | -47.21936 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4b34075f-9616-3455-a012-cad2f4dbea93 | -21.07184 | -47.21827 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3082f122-4bb7-344b-91c5-c41d2973ada0 | -21.05145 | -47.24746 | 2024-10-09 04:42:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ddfa6a4-701e-3753-85d5-53468b7f7e3f | -21.05099 | -47.25111 | 2024-10-09 04:42:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fc8ef3d-ceb5-30e4-8ffb-315f5075f50f | -20.98719 | -47.15878 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6dc4d77-527c-3a8e-b1c7-a67b007905d4 | -20.98552 | -47.15617 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28193e2b-799e-3cbd-9b47-b146d6326cf8 | -20.98505 | -47.15988 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 617e3765-cf57-3acb-836a-78119b1c8df7 | -20.98305 | -47.15836 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18aa7703-de4e-3ef2-abee-c969ca1c57fa | -20.79996 | -47.2141 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d14964d9-f82c-3c7c-bd1a-943d79e131ed | -20.79944 | -47.21828 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e427207-3c0b-30ab-b7c6-3044127ebf86 | -20.79731 | -47.20182 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4542abe7-bbde-308f-9776-38625e7a262d | -20.7968 | -47.20591 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb407d6d-250b-3bb1-ac51-7dada0479378 | -20.79632 | -47.20986 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c51be77-e617-3a85-b098-ef7588b825cc | -20.79583 | -47.21382 | 2024-10-09 04:42:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb3fceef-409e-3eb9-ac0b-960a8e9474ba | -20.7944 | -47.22538 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3173f090-7aad-3626-872d-7aa0355e9c54 | -20.79394 | -47.22911 | 2024-10-09 04:42:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README154.md)
