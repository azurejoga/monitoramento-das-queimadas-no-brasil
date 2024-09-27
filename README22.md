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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb541c4-4b37-3b64-975a-6a64d806a5fd | -14.7109 | -45.5096 | 2024-09-27 01:16:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f4736676-f01b-3864-b05b-6a70beef3a09 | -14.7114 | -45.4863 | 2024-09-27 01:16:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 29f10598-9325-3f73-a271-6f4192e12c71 | -14.7305 | -45.5061 | 2024-09-27 01:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 0fd5d184-fb15-37e0-8598-aeacd81b4533 | -14.731 | -45.4827 | 2024-09-27 01:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e3c62112-30d3-30e8-b0ba-84556df9ec91 | -16.7133 | -55.8262 | 2024-09-27 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| bc88e301-a270-3be2-a1dc-d2e9392c49e3 | -16.7325 | -55.8445 | 2024-09-27 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 07041a8d-cab2-3556-82be-08a19a522159 | -16.7329 | -55.8237 | 2024-09-27 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 80fef031-08fa-341e-919e-0fc25ab95022 | -17.0988 | -56.1919 | 2024-09-27 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| c2c9f5fe-f610-3107-9667-24a38a4712c7 | -17.0991 | -56.1711 | 2024-09-27 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| daf233a1-a3e8-3f55-b199-95506f5fb80c | -17.1184 | -56.1894 | 2024-09-27 01:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| deb6a678-1236-3597-9f35-162e6b099bf4 | -17.1188 | -56.1686 | 2024-09-27 01:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 79161cf7-294c-3d0c-bedc-f44e2700711c | -18.7036 | -42.1119 | 2024-09-27 01:16:49 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| 181ab817-3a9f-3863-8610-685b56aeff58 | -18.7044 | -42.0865 | 2024-09-27 01:16:49 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 162.6 |
| 35c7f560-3a73-3196-93bb-4af29d2ba53b | -19.3773 | -42.5809 | 2024-09-27 01:16:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 77f2cfb4-19db-3840-a877-d9542ef42f20 | -19.6136 | -42.8159 | 2024-09-27 01:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| 2d96e2b2-fb3c-3ce3-b1a1-5f3ef304cb01 | -19.5266 | -47.8952 | 2024-09-27 01:16:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5e64ace2-e307-3892-acd5-98e0f8c733f1 | -19.5272 | -47.872 | 2024-09-27 01:16:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d666a21c-e861-34fe-b7cd-c92010252413 | -19.5469 | -47.8907 | 2024-09-27 01:16:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a71ecf69-88f9-3d34-9c0c-ee9a012e0f90 | -21.4123 | -42.9778 | 2024-09-27 01:17:03 | GOES-16 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| a5f8cd14-9774-3c81-8252-a868d5d06dc5 | -21.4132 | -42.9523 | 2024-09-27 01:17:03 | GOES-16 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| a5ca7fc1-22ea-37df-9ae5-26c8fd1b20c0 | -22.7433 | -44.8035 | 2024-09-27 01:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.9 |
| 1f2e0ed6-4ccf-3bd8-af4a-d90f70e0971c | -22.7442 | -44.7785 | 2024-09-27 01:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| d434f90d-34a8-389a-bf7a-496b103eb1bd | -22.7645 | -44.7973 | 2024-09-27 01:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.8 |
| 350d59ec-78ac-3811-acc0-77685ecbfdfa | -22.7653 | -44.7723 | 2024-09-27 01:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| 4c88bdd9-8e92-34f5-9fb4-cf4fe64508dd | -23.5816 | -47.3408 | 2024-09-27 01:17:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.3 |
| a967ea9f-0971-3f56-8e26-67756db1a2eb | -20.33747 | -42.72527 | 2024-09-27 01:20:00 | TERRA_M-M | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| b1197beb-a572-3d90-a259-12ee693adc47 | -20.33214 | -42.72107 | 2024-09-27 01:20:00 | TERRA_M-M | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| b2120c3a-4ae8-3cf1-88ea-c021d472548f | -20.32203 | -42.72862 | 2024-09-27 01:20:00 | TERRA_M-M | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.1 |
| 18bcdc8f-1a33-31b6-a278-4304117617fd | -21.40599 | -42.99492 | 2024-09-27 01:20:00 | TERRA_M-M | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| 33ba643f-8601-3480-94b8-3554d951342f | -21.40491 | -42.98902 | 2024-09-27 01:20:00 | TERRA_M-M | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 138.9 |
| bcb010d6-aaf0-3959-a5d6-b962e0978bfe | -21.40093 | -42.96907 | 2024-09-27 01:20:00 | TERRA_M-M | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.9 |
| e878dd70-ea29-35f0-87c2-61e53ff5c69a | -21.39982 | -42.96383 | 2024-09-27 01:20:00 | TERRA_M-M | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 4a22ced4-d41d-3452-ab89-f1060e309c20 | -22.67755 | -42.86967 | 2024-09-27 01:20:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 33.8 |
| 0d9f24ea-e882-3414-998a-e23629d7d2de | -22.67152 | -42.84795 | 2024-09-27 01:20:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| dfb4cb4c-66df-3bde-9107-d9d797fd8bc0 | -22.39688 | -43.96706 | 2024-09-27 01:20:00 | TERRA_M-M | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 1c5990b5-5e41-30ba-b2a3-7c27b5ac870b | -22.90088 | -44.7457 | 2024-09-27 01:20:00 | TERRA_M-M | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 0291a816-6f61-343e-a892-0a37c236ea44 | -22.74119 | -44.81222 | 2024-09-27 01:20:00 | TERRA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 184.8 |
| a6a8b53e-ce16-3f47-b18d-3bb46ecfc219 | -22.73756 | -44.79265 | 2024-09-27 01:20:00 | TERRA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.2 |
| e89da64f-6b24-33dc-92ed-ec54d60ab286 | -22.6473 | -44.87685 | 2024-09-27 01:20:00 | TERRA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 2c369351-a11f-3310-af0f-82dbfd95dabc | -22.64342 | -44.856 | 2024-09-27 01:20:00 | TERRA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 69b1e866-a0c0-38d0-be9c-0ad10bc25db4 | -21.96245 | -45.82038 | 2024-09-27 01:20:00 | TERRA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| d542d149-bca9-3d6b-b618-f7638cd8ed2d | -21.95736 | -45.82784 | 2024-09-27 01:20:00 | TERRA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.5 |
| d176a451-1a85-3c84-880b-f1f7cae81100 | -21.95417 | -45.80963 | 2024-09-27 01:20:00 | TERRA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| e2ec1c9c-377a-3268-b726-6f56d991693f | -21.95052 | -45.82261 | 2024-09-27 01:20:00 | TERRA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 73388239-28d5-3a05-938b-6f4633f9375d | -21.94545 | -45.83025 | 2024-09-27 01:20:00 | TERRA_M-M | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 41da9a91-a8d0-35b4-b443-10934d680bd9 | -23.58109 | -47.35272 | 2024-09-27 01:20:00 | TERRA_M-M | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 9612d57c-77ed-3643-b708-346272af2ba0 | -23.57292 | -47.36779 | 2024-09-27 01:20:00 | TERRA_M-M | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| c0fb893a-91c1-31c5-a488-332ae82aa1d0 | -23.57073 | -47.35468 | 2024-09-27 01:20:00 | TERRA_M-M | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 53552b86-89b3-31d3-ba51-07ccd420126c | -23.5685 | -47.34132 | 2024-09-27 01:20:00 | TERRA_M-M | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| a1f67ccb-f1da-3b06-b730-cb9d4bee3af4 | -23.44302 | -47.01501 | 2024-09-27 01:20:00 | TERRA_M-M | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 8c6cf57c-5ea4-34ff-b6f7-9230627d2042 | -23.4407 | -47.00115 | 2024-09-27 01:20:00 | TERRA_M-M | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| b5d9d172-eefe-35f0-853c-bd3cece92663 | -23.43583 | -47.35813 | 2024-09-27 01:20:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 543f2afb-9869-32c7-9ce3-0020470f442d | -22.96239 | -45.96555 | 2024-09-27 01:20:00 | TERRA_M-M | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| 7cae20a3-70cd-3cc2-af5d-81d1bfc78441 | -22.95899 | -45.94623 | 2024-09-27 01:20:00 | TERRA_M-M | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| 29a3a013-8e54-3b06-8a67-718b762c05e2 | -22.95102 | -45.96885 | 2024-09-27 01:20:00 | TERRA_M-M | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 003be610-e903-320a-a4c2-0323cce9f736 | -22.94773 | -45.95028 | 2024-09-27 01:20:00 | TERRA_M-M | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 9714334e-e2a7-3298-8c5f-f9a13ef20587 | -22.34486 | -47.76597 | 2024-09-27 01:20:00 | TERRA_M-M | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2e82576e-5828-35f6-86ab-9de5535b3a84 | -23.16916 | -47.72193 | 2024-09-27 01:20:00 | TERRA_M-M | CERQUILHO | SÃO PAULO | Brasil | 3511508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d252621e-c151-391c-a7d7-f88ffe752811 | -22.51183 | -47.78687 | 2024-09-27 01:20:00 | TERRA_M-M | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3de3f63a-6631-3a19-96ee-e894d156881f | -16.59097 | -54.03418 | 2024-09-27 01:22:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24564604-255d-35a6-a5e2-71fd2c3391a1 | -13.97953 | -54.5901 | 2024-09-27 01:22:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29eb3604-cce5-3bee-bd4c-bf399dccfb68 | -16.54048 | -56.0355 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| a6312e6d-4c02-3e83-8113-0b67efa9039e | -16.12423 | -55.42898 | 2024-09-27 01:22:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 384f6338-d391-3551-acf8-33294f191a06 | -15.33048 | -55.64141 | 2024-09-27 01:22:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a331d34-de3c-3b38-babd-1c314a037df3 | -17.11902 | -56.18031 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 83498475-5b2e-3146-84e3-0264d445a876 | -17.11201 | -56.20542 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 5cc1ef9e-d7cb-33a3-aaa0-f592bf606de4 | -17.11052 | -56.19355 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 240ffe27-3d1c-3955-aaed-6bbdc51498a8 | -17.10904 | -56.18168 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| d90fa4e9-fd16-39ac-aefd-a9029c8d9d81 | -17.10756 | -56.16985 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| ba7d236b-e44d-3cbb-a4d0-d45bbcd03a28 | -17.10052 | -56.1949 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 05ffac70-3636-363b-a537-8b7271d4def4 | -17.09905 | -56.18304 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 911c837c-33be-3af6-b3df-f6e72d027543 | -17.09757 | -56.1712 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 30beeaea-9da9-3c75-bf1f-3f41cfe409f2 | -17.09253 | -56.37931 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 7798eb3b-9752-34fd-9f7d-5b2884216268 | -17.08613 | -56.16073 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| dc86a41a-08bb-3356-8d5f-bf9d99ae3d64 | -17.08467 | -56.14894 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| f43417f6-7275-3c38-b7a6-e3ee9fe9d271 | -17.07471 | -56.15031 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| 56b91fcb-ed0a-3197-968e-35f720f2f650 | -17.06619 | -56.16346 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.0 |
| f5a2395b-2db7-378b-947d-b18497f36f02 | -17.06474 | -56.15167 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 1daa7c9e-a22a-3ab0-9f3d-b8b52395f7e5 | -17.0633 | -56.13989 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.8 |
| 2a9a2195-3940-3c69-95c2-43608846847c | -17.05766 | -56.17665 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.1 |
| b0198456-38df-38a5-a03c-84861e611d0a | -17.05478 | -56.15303 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 5875409e-7e0b-3703-8911-3d38b82e3bec | -17.05334 | -56.14125 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 146.4 |
| d685ae1f-9112-35a5-acf9-42405fb5e64a | -17.05191 | -56.12949 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 78e4e2f4-55cc-32c6-abf1-02bae1ec949b | -17.03664 | -56.17376 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 5f1098dd-1317-31a4-8be7-10f454e7c181 | -17.03514 | -56.16195 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.1 |
| e16bb9ae-c22d-337b-ab4d-df6a0551d4c8 | -17.02667 | -56.17512 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| b105b5c3-6ded-3ff2-8a8d-23fd249afc86 | -17.02518 | -56.1633 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 0928a98e-9102-3fc7-83a6-a7c479fa1f68 | -17.02073 | -56.12806 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 0d5b1bf4-0847-32a6-adab-58ef34b9388b | -17.01925 | -56.11634 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.9 |
| 8e24cefc-6172-3594-85e2-b6b492b3069e | -17.01778 | -56.10464 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 863ab607-9084-3830-b460-2ff5402a034f | -17.00932 | -56.11769 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.5 |
| bbb07632-2898-337b-a394-77efb795b83b | -17.00785 | -56.106 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| d02edc65-71b6-3764-a988-86b76940f62c | -16.73429 | -55.55061 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 073a920a-8182-376b-a366-a019fcca9998 | -16.73292 | -55.53982 | 2024-09-27 01:22:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0cfd19fe-c053-3df6-93cb-fe07d545aeb1 | -15.61604 | -56.95546 | 2024-09-27 01:22:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b8e5593d-4254-37c4-a6af-2e883c14ef5a | -15.60561 | -56.95584 | 2024-09-27 01:22:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a4525fff-9e7a-351e-b396-6ed0c1f7aed1 | -16.49074 | -57.37711 | 2024-09-27 01:22:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f668f88e-6246-3063-9945-76d7f6e23901 | -15.63316 | -57.49289 | 2024-09-27 01:22:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bfa62d19-34b1-30d8-88d7-577991820f47 | -15.62245 | -57.4943 | 2024-09-27 01:22:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e56d0bba-cb5b-33d3-b81e-094e2040c977 | -15.61756 | -56.96791 | 2024-09-27 01:22:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |


[Clique aqui para ver as próximas entradas](README23.md)
