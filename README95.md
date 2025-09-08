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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d38bff6-a566-33a5-9f25-280c2bcad82c | -13.82357 | -46.24133 | 2025-09-08 11:38:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 6ec4c844-d754-3f60-818e-61384ae2a9ac | -16.91531 | -45.8192 | 2025-09-08 11:38:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 314e66b2-3a7d-355c-a867-0841d146200d | -15.80248 | -42.32273 | 2025-09-08 11:38:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 40.8 |
| 68302d7d-33b7-31fc-98e3-fbe5067bb422 | -16.22323 | -39.13998 | 2025-09-08 11:38:00 | TERRA_M-M | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 13afa12f-d8ce-3a05-adac-b6e66510f546 | -13.83817 | -46.24479 | 2025-09-08 11:38:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9a07ddae-b77d-381c-a276-aa825f991d2a | -17.23739 | -46.56909 | 2025-09-08 11:38:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| a93ed5fc-d401-38cc-8db2-232ec868c526 | -15.18622 | -48.00434 | 2025-09-08 11:38:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 270dacdb-cce6-392f-88dc-3e29ca348fd1 | -15.11882 | -42.0489 | 2025-09-08 11:38:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 5c84f97b-7517-3417-be10-2c3fb3612906 | -17.23434 | -46.56145 | 2025-09-08 11:38:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 43.0 |
| e7231275-ba44-3dca-a3d5-b29c9a1f60ed | -11.27733 | -46.50757 | 2025-09-08 11:38:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| cc029eff-2f35-3eff-9ef0-ce8571d3a388 | -18.35409 | -43.91702 | 2025-09-08 11:38:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 36e62fbb-3cfb-338b-9f8f-8fd797266fd0 | -16.97844 | -39.76897 | 2025-09-08 11:38:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 231924d6-6437-3b45-ad57-6392246b05fc | -14.26699 | -44.93923 | 2025-09-08 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 965c48db-11b4-39dd-b29a-4440c260dfbe | -16.17264 | -40.63657 | 2025-09-08 11:38:00 | TERRA_M-M | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 14eed833-44be-35a4-838b-e7a5dd0e67f6 | -17.25914 | -39.43421 | 2025-09-08 11:38:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| a01a5cc8-240e-3b64-9b8e-1919fd57827b | -14.52754 | -48.77015 | 2025-09-08 11:38:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| dbcd4f45-2f39-37bd-9082-257f5f595dd0 | -14.46667 | -42.72472 | 2025-09-08 11:38:00 | TERRA_M-M | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| aca01879-684b-3709-8538-4614047be127 | -14.52704 | -48.76426 | 2025-09-08 11:38:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 1a8d2ca4-19e8-33e7-b128-b9d38aa5b088 | -15.80461 | -42.30969 | 2025-09-08 11:38:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| eeb31125-cd8c-3b8a-8762-0d40bf8352fc | -16.97702 | -39.77852 | 2025-09-08 11:38:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| fe75185b-2090-3d2d-b2bf-7ab557ff82ea | -15.57426 | -40.26299 | 2025-09-08 11:38:00 | TERRA_M-M | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8fc07ada-a4de-3c10-bcb0-eb709578657f | -18.35141 | -43.93236 | 2025-09-08 11:38:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 897a9a55-3cad-3f5d-92db-883a82380009 | -16.95131 | -45.85031 | 2025-09-08 11:38:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 4c308b9a-1406-3056-9db7-8c4fd86724ea | -13.81911 | -46.26305 | 2025-09-08 11:38:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| be454855-c145-3f8d-8989-7ef81db28931 | -16.9075 | -45.81145 | 2025-09-08 11:38:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f286df4a-c0f7-3a4f-b0f1-a85168d287d9 | -14.25379 | -44.93674 | 2025-09-08 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 56e42d76-1028-3a95-9314-5a59af0226f4 | -15.044 | -50.1118 | 2025-09-08 11:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 074874f7-282f-34cb-b163-f8668be0c98c | -14.2562 | -44.9393 | 2025-09-08 11:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| b83d2532-3e73-3d6b-9511-594cb4d84f57 | -11.282 | -46.5269 | 2025-09-08 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 94d2fa44-6124-3cfe-96dd-a884e5e703d0 | -7.4367 | -49.2747 | 2025-09-08 11:40:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 8e0456a5-540d-3ff4-aeb0-50e47296e270 | -7.6559 | -47.9593 | 2025-09-08 11:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 231.5 |
| b48d3118-bd5a-3e2f-a867-92f2d01bd1d2 | -11.2823 | -46.5043 | 2025-09-08 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5557dab9-e6ee-3d6d-89f9-82d9e9e78eba | -19.52959 | -42.38002 | 2025-09-08 11:40:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 9f82e93a-8311-3727-ac0a-b499479897cc | -20.95513 | -44.85179 | 2025-09-08 11:40:00 | TERRA_M-M | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| c786efa6-b78c-318f-8316-6b7422b47f4d | -21.22589 | -44.02629 | 2025-09-08 11:40:00 | TERRA_M-M | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2069475f-58e7-3c71-8b3b-964d4bcd719f | -20.95792 | -44.8357 | 2025-09-08 11:40:00 | TERRA_M-M | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 4e1774ca-cae7-3120-8bf1-fac472a3930e | -19.41607 | -43.66127 | 2025-09-08 11:40:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0414d3c9-ed56-3665-9f73-0f8fe6cf4927 | -18.0255 | -47.11184 | 2025-09-08 11:40:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| e6c5f910-ccf3-31f1-84d6-ce9d68a4d12e | -19.41195 | -43.66874 | 2025-09-08 11:40:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f33b21ab-3699-32e6-b4d6-0f756e1b783a | -14.2562 | -44.9393 | 2025-09-08 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| b6a43f4c-ef65-3bab-983f-b7a99c3ac910 | -12.2941 | -49.9904 | 2025-09-08 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| bb7da703-3858-3958-9a45-fd65a2c7cd4a | -10.4842 | -47.7196 | 2025-09-08 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 832eeaaa-f852-3d55-8afc-98305add6705 | -11.2827 | -46.4817 | 2025-09-08 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1c8cdfe4-f353-3169-8166-7545739e60b1 | -12.2938 | -50.0121 | 2025-09-08 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 64e3e4e7-dca8-38b1-aeac-ac6469f0e040 | -14.2757 | -44.9357 | 2025-09-08 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 2f167edb-6263-361c-90f8-4f3d9bcf73bd | -15.044 | -50.1118 | 2025-09-08 11:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4afb45df-1599-32b4-8584-882f471e41ab | -11.2823 | -46.5043 | 2025-09-08 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 2f0267eb-e538-399f-99d3-e00a103587b7 | -15.0635 | -50.1089 | 2025-09-08 11:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 46a49091-0e6d-36c8-8f69-80ca716fce56 | -7.6559 | -47.9593 | 2025-09-08 11:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 262.2 |
| 123cdcec-5b8e-3815-97c0-f87eed34df03 | -14.2752 | -44.9592 | 2025-09-08 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| fd14e813-7731-3cc7-a427-495691215a39 | -12.2938 | -50.0121 | 2025-09-08 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b64db3d5-e783-3ae6-b0a6-184b3830e06c | -11.2827 | -46.4817 | 2025-09-08 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| af4434dc-7b38-30d2-926d-2930551b5e36 | -15.044 | -50.1118 | 2025-09-08 12:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8b3bbf99-ef4e-3bd6-a193-273e0007769a | -12.2941 | -49.9904 | 2025-09-08 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d5605dd9-4f66-3c89-8c8e-d51d8b906810 | -9.5127 | -48.244 | 2025-09-08 12:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1950ca16-ab37-32e9-b9c9-95e3ae1a4b0a | -16.9223 | -45.8258 | 2025-09-08 12:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 235abec9-5076-356b-b2d1-568fbaa1cf0a | -15.0635 | -50.1089 | 2025-09-08 12:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 851ffc1a-b382-3f42-81d6-2babcba7c2b1 | -7.6559 | -47.9593 | 2025-09-08 12:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 300.1 |
| 2729b7f0-5e5b-3606-a258-fb1a86942e8d | -16.9024 | -45.83 | 2025-09-08 12:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 73c663e9-6387-382a-8a55-90d36275e083 | -11.2823 | -46.5043 | 2025-09-08 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 51348654-4977-341a-87cf-063092815abe | -7.6561 | -47.9375 | 2025-09-08 12:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0c77fb97-3a12-3e14-80f2-2fb6571bfc9d | -6.5453 | -44.8415 | 2025-09-08 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ff5a95ec-2110-3667-a351-cb0a7d3dbdb9 | -15.044 | -50.1118 | 2025-09-08 12:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a738f269-f513-3d9a-80d6-8c59349d7c8b | -15.0635 | -50.1089 | 2025-09-08 12:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ad586411-2da3-369e-b26c-6c4209870283 | -7.6559 | -47.9593 | 2025-09-08 12:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 32e98408-1b60-30c1-bdd0-f8c158b8e46d | -12.2941 | -49.9904 | 2025-09-08 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5fe85665-fc08-3e57-9e18-776e7f565bf0 | -11.2827 | -46.4817 | 2025-09-08 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 079b6b72-b0e4-3e34-a4ed-e73a49a946bf | -11.2823 | -46.5043 | 2025-09-08 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 281612e2-b625-300d-96ba-fa7b67e48a37 | -6.5453 | -44.8415 | 2025-09-08 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 99566ea2-e6e3-3af9-af38-ef2c1885b5cb | -6.2224 | -43.3693 | 2025-09-08 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 135564ef-da4a-3bf0-b33a-a56a43a8b702 | -8.3239 | -46.9533 | 2025-09-08 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 719384c5-3dc7-3dbc-a1fd-8983a0bd11f9 | -11.2831 | -46.4591 | 2025-09-08 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8fc27919-8705-3925-be59-208d981ac518 | -12.8411 | -52.8994 | 2025-09-08 12:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 54d362dd-2ea8-3e2f-b620-a42e3fcdcf09 | -15.044 | -50.1118 | 2025-09-08 12:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6468cadc-952a-3b87-8df4-b242d1e331d6 | -5.211 | -43.2833 | 2025-09-08 12:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 2c22695d-6584-3783-b58c-a856e7af5e4f | -14.4359 | -48.4644 | 2025-09-08 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1702d676-ca1b-383b-9ab7-dc4ce80eb9b4 | -11.2827 | -46.4817 | 2025-09-08 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 49d49b73-d040-34b7-a146-d6b4b34b3560 | -10.165 | -46.2176 | 2025-09-08 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a658b99e-62e0-34e4-945c-188273885125 | -7.6559 | -47.9593 | 2025-09-08 12:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 6aee27e8-a5d7-3e07-b075-ceb5ea90ca30 | -11.282 | -46.5269 | 2025-09-08 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e93d4b22-7a63-346a-ba0b-979512bd6702 | -6.1024 | -44.144 | 2025-09-08 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 30832ed6-f3a9-3947-92e4-a5cf6bd655f7 | -12.8223 | -52.8806 | 2025-09-08 12:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 23c77431-ef4d-3d20-aa15-39c2098a30ef | -11.2823 | -46.5043 | 2025-09-08 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 365.4 |
| 5f1512b7-6154-3f57-bf3d-a340f9227325 | -10.146 | -46.2199 | 2025-09-08 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9d8db45b-5929-3c0a-9a34-e35307d0812f | -10.1464 | -46.1973 | 2025-09-08 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 2b1b0fc3-e199-3292-9da8-13d05ad6a942 | -7.6559 | -47.9593 | 2025-09-08 12:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 301.3 |
| 11bb5e26-4f40-3817-ba76-3c7f3c503dfa | -11.2823 | -46.5043 | 2025-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 958489c7-753d-31cb-8485-7613fc5287f1 | -11.2827 | -46.4817 | 2025-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 76b2c974-ce87-31b6-9692-af3f67e06d56 | -12.2938 | -50.0121 | 2025-09-08 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 36232a2b-3677-3d5c-9923-1bc352f47ad7 | -8.3239 | -46.9533 | 2025-09-08 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0047fe64-f07e-35fa-b42d-471faa66c90e | -11.0234 | -46.0184 | 2025-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 608f55d8-78dd-3e7e-acbf-6814b429743a | -5.211 | -43.2833 | 2025-09-08 12:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| ca738c7d-29ff-3d28-8c1f-9262fdb3dec0 | -11.0231 | -46.0412 | 2025-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 96a6d4a4-7072-382e-bbcd-28f57d95df70 | -14.4359 | -48.4644 | 2025-09-08 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 84c80db0-3dfd-33a5-98b6-03b31d49519a | -12.2941 | -49.9904 | 2025-09-08 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8a099a3a-afa0-3ae4-8b21-470808183456 | -12.8223 | -52.8806 | 2025-09-08 12:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 7a8677fb-234a-3005-ab3b-09b6091977a4 | -12.8411 | -52.8994 | 2025-09-08 12:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1a7e33ab-1d5c-3a94-a6ab-c40bb4611d13 | -11.282 | -46.5269 | 2025-09-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 7f0a6fa0-e85b-3375-a6b3-0b31ff530ee5 | -15.044 | -50.1118 | 2025-09-08 12:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 4c9b4f91-bad5-3682-99fe-193f27e2f6be | -9.8278 | -53.2976 | 2025-09-08 12:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |


[Clique aqui para ver as próximas entradas](README96.md)
