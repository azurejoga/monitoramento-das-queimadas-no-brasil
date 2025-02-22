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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a212f869-5b15-3f05-a752-a44a21471d2e | -15.76457 | -43.23098 | 2025-02-22 04:14:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4cc20ea9-9db6-37db-bf9a-2cebd6218029 | -14.43718 | -45.63175 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf722148-19c9-340c-83ef-51228ce79f8c | -12.81359 | -44.98767 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9031cf96-fc2b-397e-9781-b64f889685d1 | -15.05203 | -42.42568 | 2025-02-22 04:14:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6c241bfa-f35a-3c3f-888b-658ee9c0a154 | -10.36056 | -44.91942 | 2025-02-22 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12454be3-53ec-3e37-a231-80962918c04a | -12.15207 | -54.99709 | 2025-02-22 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c55c2f2-3598-3e5c-9bf6-4495c1967d23 | -10.3578 | -44.91534 | 2025-02-22 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b33e3702-a126-3c3c-baab-0959128c1fcb | -15.7875 | -51.02538 | 2025-02-22 04:14:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db144faf-4ee6-30e0-8ee7-3048f8cf36e2 | -15.28027 | -43.00855 | 2025-02-22 04:14:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4ac39c1-93a6-3f4d-a485-fb7fc9e4ed75 | -10.58633 | -44.6125 | 2025-02-22 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4db201b7-d6a3-36e6-b2de-3c2dbb765472 | -12.09775 | -51.22537 | 2025-02-22 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba8f4879-c555-3778-ae68-7bee9fdcba20 | -14.43443 | -45.62762 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08de0e48-5825-30a8-bae1-3a1812e3e1f2 | -10.42999 | -44.89088 | 2025-02-22 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f9f41c-2eb9-3e45-9f74-84827312e3c6 | -22.05528 | -49.0295 | 2025-02-22 04:16:00 | NOAA-20 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| add32866-56c9-3fb5-a951-8976ea36ab46 | -23.33998 | -46.77285 | 2025-02-22 04:16:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c195c7d-d946-3a8b-a1f4-a1f8a29767a9 | -22.68433 | -50.47507 | 2025-02-22 04:16:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40e0cc60-da60-3031-a814-2316e18c7f25 | -22.90062 | -43.75296 | 2025-02-22 04:16:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a03473da-8ce1-348d-9242-5d363219c10b | -18.86674 | -47.66101 | 2025-02-22 04:16:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9143e59-1a46-3c17-a5ef-b6922fa9b0e4 | -20.61781 | -42.48877 | 2025-02-22 04:16:00 | NOAA-20 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f73bf44b-28e9-3a78-a3fb-87433c07d674 | -20.99525 | -51.79174 | 2025-02-22 04:16:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 96713be3-cf21-3a11-ac74-78780482281c | -22.90001 | -43.7574 | 2025-02-22 04:16:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bde85b17-3abe-30d5-88c0-968d47035db7 | -21.07086 | -56.38863 | 2025-02-22 04:16:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cff1989-cf19-38df-95bc-a4b645bd155d | -20.37772 | -45.60247 | 2025-02-22 04:16:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b268a9ae-4064-3158-af48-69da14826a0d | -22.6853 | -50.47267 | 2025-02-22 04:16:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71318887-95a5-3975-bc10-616e17694c2c | -21.07443 | -56.39011 | 2025-02-22 04:16:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93253e01-640a-39f3-b035-bf56ff49f13f | -23.59199 | -47.43903 | 2025-02-22 04:16:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b2e073a-1a79-34ac-a206-9e5cc6e785f6 | -20.99548 | -44.16293 | 2025-02-22 04:16:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2e6f524c-caed-3865-acb3-6e2048ac2b36 | -15.62928 | -57.31211 | 2025-02-22 04:16:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1826df81-b0d0-3355-a79e-6c15921be6fc | -20.76837 | -45.84288 | 2025-02-22 04:16:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4697c9f2-0279-3d66-bd8a-06315b021d30 | -21.17986 | -44.27488 | 2025-02-22 04:16:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 859c5b9d-ea64-3ae1-8377-24966f520986 | -20.88433 | -46.17033 | 2025-02-22 04:16:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53db8c6d-b12d-3ccd-810d-f14a9c0696e2 | -21.18199 | -44.27399 | 2025-02-22 04:16:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7cd384ee-8dda-380d-b325-fbefc62fb98f | -19.83484 | -40.86575 | 2025-02-22 04:16:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 281671b4-6842-31d2-bd34-e629f07acb6d | -18.8204 | -48.21212 | 2025-02-22 04:16:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7127ad0e-433d-3882-9187-bf11d836ce98 | -20.61848 | -42.4838 | 2025-02-22 04:16:00 | NOAA-20 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| dd7856ff-ac82-3637-82e0-341f1d5ebcba | -19.78038 | -42.09597 | 2025-02-22 04:16:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45eaa344-78cd-344a-be3f-442706d24380 | -19.78566 | -44.29566 | 2025-02-22 04:16:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b19d195-066d-3b7c-b5eb-09de8b0aa9ab | -22.75455 | -43.50924 | 2025-02-22 04:16:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f2bcd86-40d0-3213-aabe-0bfc3bb4956a | -19.7174 | -40.35328 | 2025-02-22 04:16:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6ff8ed8a-8265-397f-b7a0-635e44ba89f2 | -20.1271 | -45.44719 | 2025-02-22 04:16:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c64500af-4814-3e26-a6e2-095d540efd4c | -20.12767 | -45.44349 | 2025-02-22 04:16:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21b9cfeb-e821-39a2-8e51-8d8326783220 | -16.30147 | -58.82884 | 2025-02-22 04:16:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 133df97d-2824-3ed5-be67-61f50a5f9964 | -16.30408 | -58.83575 | 2025-02-22 04:16:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 81fae13f-ecbc-3146-a827-b5daeaec8874 | -20.58 | -44.57526 | 2025-02-22 04:16:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 050d5e86-04b4-30a3-b283-b48818b22742 | -21.06913 | -56.38898 | 2025-02-22 04:16:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4ba2949-4389-3691-a6e0-e7f383ac0cd7 | -20.88763 | -46.17092 | 2025-02-22 04:16:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94c53a4b-1213-3a33-9150-c31ae371c40d | -15.62817 | -57.31731 | 2025-02-22 04:16:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fc6be5f-33d2-3789-88eb-61827923d829 | -22.8556 | -42.98166 | 2025-02-22 04:16:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3144ee37-080f-3b6a-aa1a-9c66b02a938e | -20.34786 | -40.36124 | 2025-02-22 04:16:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ef362acd-2e8f-3c60-82fc-f8b20b86494e | -20.29495 | -40.89037 | 2025-02-22 04:16:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 244ec4e6-d1bc-38df-9fbe-adaaccff58c0 | -23.98611 | -48.91756 | 2025-02-22 04:16:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34247b02-586e-3c0e-9d78-c4c857a63aa8 | -16.30544 | -58.8296 | 2025-02-22 04:16:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 40f5b3df-4239-3b65-b1aa-94b27d12d616 | -20.76894 | -45.83917 | 2025-02-22 04:16:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 29c10a9d-ab85-3d76-b637-be431054db6c | -20.1146 | -40.64806 | 2025-02-22 04:16:00 | NOAA-20 | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b1182738-27ce-329a-9528-74e933f5c1ce | -29.88899 | -51.2348 | 2025-02-22 04:18:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 27aff801-afca-36f9-84b1-ab97bfa7c2bd | -30.2233 | -54.48413 | 2025-02-22 04:18:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 578c796e-f83d-3f89-b9db-abb9803224bb | -30.22216 | -54.4899 | 2025-02-22 04:18:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 072e5164-9a2d-3a3e-a32d-fcd6f4b1bc99 | -29.95218 | -51.61566 | 2025-02-22 04:18:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 4343cc9c-5a06-313a-bd22-6e6cdeb8e090 | -32.00063 | -53.08078 | 2025-02-22 04:21:00 | NOAA-20 | PEDRO OSÓRIO | RIO GRANDE DO SUL | Brasil | 4314209 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 8cc2b962-454d-3bc8-b9d7-304b25b914d9 | 4.78211 | -60.54339 | 2025-02-22 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fa92143-2bba-31bc-a90e-ca7a5e20a640 | -10.43081 | -44.89453 | 2025-02-22 05:03:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d38f4b4a-e671-3636-9806-2f23739ef6c6 | -2.37179 | -51.86901 | 2025-02-22 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb425a8f-e664-34c0-a17f-0b18e79eee5a | -4.12945 | -54.89826 | 2025-02-22 05:03:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2bc96a6-c255-334e-ac21-17d6cb25a767 | -12.81462 | -44.99009 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d4e4651-dedc-3df2-987e-b4b0e858c427 | -9.93199 | -59.93921 | 2025-02-22 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f1255a-3460-3d81-8056-7b798d84c30b | -11.82901 | -58.79964 | 2025-02-22 05:05:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 602e0c83-4433-343f-9b07-ffa58d1ee3f6 | -12.83985 | -44.99836 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ee575be-0bfc-3c47-84a2-ca98ffab44b5 | -12.82048 | -44.99621 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e56f272b-33f1-3ae6-91f1-9fcb0bacc786 | -12.83924 | -45.00375 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b11c640f-70f9-3fb4-978a-bfbbb8fafce1 | -15.29033 | -53.20454 | 2025-02-22 05:05:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94a25109-60cf-36e1-85a5-af422d311caf | -14.43819 | -45.62766 | 2025-02-22 05:05:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec4ef7ac-77e6-35a7-9458-47338321019a | -11.13854 | -54.22638 | 2025-02-22 05:05:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adb51956-6bd2-3d98-bf2f-7268496b6e1d | -12.15646 | -54.99924 | 2025-02-22 05:05:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5fda0a5-e3d6-3d4c-8c78-34a53004238a | -14.44399 | -45.63369 | 2025-02-22 05:05:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40295bf9-acee-3b78-9b4c-cd74937f6651 | -12.82693 | -44.99696 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 969ddf40-0b3e-3f3d-8ec8-64af7c02c0a7 | -12.10016 | -51.22282 | 2025-02-22 05:05:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00826c20-cecd-3c6f-919e-c862f307d7bd | -12.78692 | -54.90224 | 2025-02-22 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a32d27a-b2b9-321a-ac88-884492046249 | -11.82961 | -58.79596 | 2025-02-22 05:05:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea88c2bf-b511-3f23-91eb-dc6886eb457c | -12.81576 | -44.98704 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 943f0560-807f-38a0-b1c9-83df3574113e | -15.28967 | -53.20951 | 2025-02-22 05:05:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abe10d5b-2d75-324b-a9de-020c121c3418 | -15.84248 | -53.55557 | 2025-02-22 05:05:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c489f7ec-9f61-3ac5-8776-74b0abf882a6 | -14.43575 | -45.62241 | 2025-02-22 05:05:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49c03256-2dd0-353a-ba11-3867c0d19d07 | -9.92474 | -59.93798 | 2025-02-22 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6855ef86-b91c-37c6-b6da-aff3182cf394 | -12.82107 | -44.9909 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4551cd38-e250-3ae6-886a-94dfce3ea55e | -9.92683 | -59.90329 | 2025-02-22 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54ad891a-9341-3bc6-8ffa-df30612bc69c | -12.15359 | -54.9949 | 2025-02-22 05:05:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2641d414-cf68-38b7-9226-dfbeb9cdf108 | -12.8152 | -44.99243 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 007318c7-8630-34f1-bda2-b91f2b153d81 | -12.8281 | -44.99401 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2373b43-d3fe-3482-a1a7-1043c06aad8d | -12.82221 | -44.98787 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cae53a73-263c-31e5-9080-ebba44356080 | -12.09962 | -51.22688 | 2025-02-22 05:05:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f63adcfb-2ee3-369f-bcc1-511a1f3b8b6e | -12.83339 | -44.99768 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18277b84-f7b2-3d68-b525-75fb06ea0d50 | -12.84046 | -45.00078 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3831e32-3663-3be9-b3f3-f94a7d06d946 | -12.82753 | -44.99166 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3dcbe14-4aae-3107-80dc-b07b2758fbbe | -12.15702 | -54.99543 | 2025-02-22 05:05:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aba2a35c-7f2e-37f1-839a-b7efae36613a | -12.834 | -45.00005 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5e5c4e5-f27c-39fe-a4fb-2da17918947b | -12.83398 | -44.99237 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ca8d975-a7fd-3f63-a206-758ca6f6faf7 | -12.82867 | -44.98867 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04be1228-e2f4-34c4-9939-cb870ae7d41e | -12.82168 | -44.98549 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89789c6d-b787-3467-b628-d26e572e9505 | -12.83456 | -44.99474 | 2025-02-22 05:05:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fed8c43-c837-3f58-9b5d-7345f4a6ecdb | -11.15264 | -54.49419 | 2025-02-22 05:05:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
