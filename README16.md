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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a20de31-e6e6-3ca3-9903-a96f6598b026 | -20.29584 | -50.97083 | 2025-11-20 06:20:00 | AQUA_M-M | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 23b963af-7c8e-3eb1-9217-66fb4e00cdbc | -2.92947 | -45.05227 | 2025-11-20 11:57:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 51a830c4-8b8b-370b-bd85-93ccaff5805c | -3.36212 | -41.4839 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b0afdb08-060d-3c11-97ad-e48e1240c3e6 | -6.42534 | -38.33234 | 2025-11-20 11:57:00 | TERRA_M-M | MAJOR SALES | RIO GRANDE DO NORTE | Brasil | 2407252 | 24 | 33 | nan | nan | nan | Caatinga | 20.3 |
| f4f92811-90c6-308b-942a-fc57093f3928 | -3.14183 | -44.10239 | 2025-11-20 11:57:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0efb0441-ce79-33e7-9647-b8456814185a | -3.15437 | -43.25776 | 2025-11-20 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ba87d5ba-0284-3b64-867f-606af7db2aa5 | -3.09501 | -44.1092 | 2025-11-20 11:57:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 51b62f00-20fe-3351-93a2-eed87bebfb81 | -3.42503 | -43.163 | 2025-11-20 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a4796939-9914-3fbe-82b3-a79d3ba532a9 | -3.79242 | -42.34682 | 2025-11-20 11:57:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 48b28c8c-1bd1-3d71-84d6-5f09a1dc5ce1 | -4.59111 | -38.2941 | 2025-11-20 11:57:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 1810cb6a-d6a9-32ee-af9e-11d8de138c72 | -3.34307 | -41.4902 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 180e62aa-90de-3ea4-9cc7-e7efcc7917ca | -6.42363 | -38.34084 | 2025-11-20 11:57:00 | TERRA_M-M | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 9209c740-7f7c-3fa7-9715-aa800c385a99 | -3.1327 | -44.10114 | 2025-11-20 11:57:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| bad9e134-bbbb-3a8b-bcc7-07b7b86c96ef | -4.67225 | -43.22659 | 2025-11-20 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| ac39453c-5390-3b34-8408-dea64680429a | -3.55554 | -43.47581 | 2025-11-20 11:57:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60a98647-08ee-3be5-9978-4c22b97d82e0 | -5.70467 | -38.56462 | 2025-11-20 11:57:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| df7fd75b-ce18-3cda-808e-a3158c6af269 | -4.59513 | -38.28691 | 2025-11-20 11:57:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 13d64cf0-d3fc-3f67-9b07-330860ce5fc8 | -3.43648 | -41.48199 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 4483a0f9-44a4-3bce-8085-8f89b5329cd5 | -5.73553 | -37.99393 | 2025-11-20 11:57:00 | TERRA_M-M | SEVERIANO MELO | RIO GRANDE DO NORTE | Brasil | 2413607 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5ecb6d0f-65e2-326f-b984-aa1f08d342bd | -4.67352 | -43.21778 | 2025-11-20 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8678e490-6e43-3c81-8c0d-06d10fea14ba | -3.32782 | -41.53368 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 4a6e1c94-982b-3e40-89f7-e7ca9afc20a3 | -6.42341 | -38.34716 | 2025-11-20 11:57:00 | TERRA_M-M | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 5f1fd22b-4674-3924-9f40-7cd5f8bed977 | -2.95841 | -40.16178 | 2025-11-20 11:57:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 412aabb4-5497-3ed9-99ec-ecba278e5a01 | -3.48422 | -42.10931 | 2025-11-20 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| baccf33e-b798-3739-b970-7a0fd490ae58 | -3.6815 | -40.60153 | 2025-11-20 11:57:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| deef5b21-b8dd-332d-8fe5-358a80dc3460 | -5.43142 | -39.21776 | 2025-11-20 11:57:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7f413d28-ed29-3891-8972-17bbc3f40ed5 | -3.4822 | -41.5431 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| c946c825-9076-3067-a291-63f81532e7f2 | -2.89675 | -44.01093 | 2025-11-20 11:57:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 9f5ff5b8-7dcf-3670-a5b1-6eb16c30c33c | -3.39123 | -42.50699 | 2025-11-20 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5c829170-dc24-3b8e-9973-46b711a37de2 | -3.79368 | -42.33806 | 2025-11-20 11:57:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 659ec0be-9ae2-305f-9b21-167559f8ae26 | -4.70591 | -39.512 | 2025-11-20 11:57:00 | TERRA_M-M | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 045481b8-d92d-3b92-970b-3d0b8f576411 | -3.37307 | -41.80044 | 2025-11-20 11:57:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 9b526529-c0e9-3f46-9df6-eef38817ba21 | -3.36339 | -41.47498 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| dc54741b-7d0c-3819-9fb7-ed5b4bdf618d | -5.4331 | -39.20548 | 2025-11-20 11:57:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| e6f0b047-341a-308c-8ef0-62fd7ba6dee4 | -3.3418 | -41.49909 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a8a36847-cdf7-3d5f-b396-997e93c11e57 | -3.10474 | -45.31981 | 2025-11-20 11:57:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bddaa3fe-3ffb-3afe-ba2c-ca32c566528b | -3.32654 | -41.54266 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 99d50df7-374b-3fb6-8d04-e2cbb9936588 | -4.68107 | -43.22783 | 2025-11-20 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 69fadaf7-06a0-3093-b725-da7db6121527 | -3.41866 | -41.5435 | 2025-11-20 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ee865e58-129b-3d39-bad5-5f637954c031 | -3.65576 | -39.92539 | 2025-11-20 11:57:00 | TERRA_M-M | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2d67bd1c-9958-3b1e-90da-206da8c95608 | -14.14575 | -45.30952 | 2025-11-20 11:59:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ec854c6a-057c-3c83-ab92-60843150c3bb | -11.90347 | -46.84134 | 2025-11-20 11:59:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b97fdd64-732b-3bbf-91a3-cdea799cdcf0 | -15.46221 | -45.95948 | 2025-11-20 11:59:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2df7807d-9858-3d41-acbb-77e4c26eb15b | -13.94023 | -47.47743 | 2025-11-20 11:59:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 50719c5e-85f6-3461-92e5-52eadcd12e4f | -14.14707 | -45.30044 | 2025-11-20 11:59:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9828bb91-ad71-3dee-a726-868ca561c277 | -13.01742 | -47.8701 | 2025-11-20 11:59:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f39e7957-d347-3ee6-adb1-572458ff2f57 | -14.66628 | -46.5318 | 2025-11-20 11:59:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 4a269390-5a88-3c56-ae32-3f6cefd34b36 | -14.91197 | -47.38792 | 2025-11-20 11:59:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d74c978c-6851-3200-8354-c015039fc280 | -14.13824 | -45.29911 | 2025-11-20 11:59:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 16ad1eb0-ebf8-35ce-a7b1-21cd0951d42b | -16.1885 | -45.15948 | 2025-11-20 11:59:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fb028c62-1aeb-3213-8a41-a84868748964 | -17.14075 | -45.07519 | 2025-11-20 11:59:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a03bd800-2d66-3e32-80b4-a252af66278e | -14.66775 | -46.52184 | 2025-11-20 11:59:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1c1cf259-37c0-3371-b3d3-74a643592537 | -16.1898 | -45.15037 | 2025-11-20 11:59:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b6415619-1f2c-3e37-90ee-770b883e1bc3 | -13.82494 | -43.67845 | 2025-11-20 11:59:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 472a5f5c-453c-362c-a519-7f63781ce013 | -13.27657 | -47.33194 | 2025-11-20 11:59:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e654415-dfd9-3e90-a0c7-685b5020b563 | -15.63429 | -43.24368 | 2025-11-20 11:59:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8e8fd212-2248-3748-aacd-bcd036eb1b30 | -14.90626 | -47.39156 | 2025-11-20 11:59:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 89602ebb-6c9d-3db6-9510-16b1501ace8c | -16.19861 | -45.15169 | 2025-11-20 11:59:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 776a4521-d149-3fb4-b430-ae90cf10ac97 | -17.07553 | -46.59972 | 2025-11-20 11:59:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 5230f991-055b-35d8-9a62-e6652a19d9e2 | -21.20386 | -42.86656 | 2025-11-20 12:01:00 | TERRA_M-T | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 54ef8a70-a1a1-30cd-b6b3-9c799ffc10e1 | -21.45627 | -43.55255 | 2025-11-20 12:01:00 | TERRA_M-T | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e733b880-53c6-313b-bf2c-cd7122f1c996 | -19.88265 | -44.9755 | 2025-11-20 12:01:00 | TERRA_M-T | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93e35907-355b-3c9c-bb34-fb2db5fe6ba3 | -21.54261 | -43.01215 | 2025-11-20 12:01:00 | TERRA_M-T | SÃO JOÃO NEPOMUCENO | MINAS GERAIS | Brasil | 3162906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| fc477a03-b268-3206-abc7-dfead6cbc2e0 | -20.06218 | -43.98092 | 2025-11-20 12:01:00 | TERRA_M-T | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| a6ccbee4-b06c-3dc2-901b-b4ef950c241b | -21.11205 | -44.02242 | 2025-11-20 12:01:00 | TERRA_M-T | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6cb31d3d-783b-3b00-871e-e1689220216c | -19.95684 | -44.36197 | 2025-11-20 12:01:00 | TERRA_M-T | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| cd2f10dc-d3f4-3dfc-8d65-d615fa0b35b5 | -21.40881 | -42.18858 | 2025-11-20 12:01:00 | TERRA_M-T | MIRACEMA | RIO DE JANEIRO | Brasil | 3303005 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| c83a6358-66ca-34dd-b7d8-1e306a8b754f | -20.6827 | -43.78822 | 2025-11-20 12:01:00 | TERRA_M-T | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 95965e56-1bdf-34c5-b357-1d6d94de4a7e | -20.95636 | -43.80237 | 2025-11-20 12:01:00 | TERRA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 6a9dfb92-7d4a-3a5e-b985-e757bcf84b6f | -19.59395 | -42.53824 | 2025-11-20 12:01:00 | TERRA_M-T | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e9f3124f-1b44-3ed8-8cf0-fd4c8c233579 | -21.23715 | -45.76162 | 2025-11-20 12:01:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| df23d0ce-184e-33d4-910f-5cd4e6b0f1cd | -19.59033 | -42.64889 | 2025-11-20 12:01:00 | TERRA_M-T | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a401d29a-52ff-3813-a579-3d807148129a | -29.18288 | -50.87833 | 2025-11-20 12:04:00 | TERRA_M-T | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4199c70b-d654-3a1f-8565-03fb4b71d2eb | -26.21811 | -51.18689 | 2025-11-20 12:04:00 | TERRA_M-T | PORTO VITÓRIA | PARANÁ | Brasil | 4120309 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ea7025c8-a12c-3616-be3e-12f23b1c9ee8 | -17.5373 | -53.6992 | 2025-11-20 13:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ab7ef6bc-81b5-3246-a9bc-6ce50e04b947 | -17.5373 | -53.6992 | 2025-11-20 14:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 98.6 |


