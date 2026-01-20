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
| 2e4e2668-5d69-3da3-9c5a-366fe86a416f | 2.55033 | -60.58284 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfe1a07e-3b57-38a1-9437-2c80b1b59739 | 1.13058 | -60.52166 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df3b6071-3af6-367f-8f66-4dfd65b6176e | 2.68328 | -60.09056 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20b26027-1b7d-3f55-a3ca-11699290866e | 3.20145 | -60.3817 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef1049ea-74d6-3b1e-8cb8-77689d9721e6 | 2.67174 | -60.08181 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 776a8c2e-6ae8-38e7-9875-cfea3cd04451 | 0.75576 | -59.65593 | 2026-01-20 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 753864d7-6c90-35b9-8c13-83d43735b079 | 2.04857 | -60.87002 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e2bf6d7-970c-37bd-a36b-2f5b74df3eba | 0.75631 | -59.65941 | 2026-01-20 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fc1c451-ec2b-36db-98e8-ddeea5d375df | 2.68437 | -60.09743 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb65bd17-e380-3849-abc5-8d203c62557d | 3.30989 | -59.99163 | 2026-01-20 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9508f07-e3fb-3a6d-b380-3e76a9c566ee | 1.47274 | -59.95647 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f133cd64-ce52-3b68-97fb-d53fd2c7d84a | 1.13334 | -60.51771 | 2026-01-20 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44c84004-999a-36a5-bc5f-ff5e21e67b13 | 2.48903 | -60.4304 | 2026-01-20 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb3d3e2f-e1f6-3f7f-8d42-3bf4326ee795 | -7.71058 | -63.80894 | 2026-01-20 05:31:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ac004e69-291f-3cca-b50f-d45e282adfdb | -19.43184 | -57.22331 | 2026-01-20 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 386ebbb8-96ef-38ca-b8ce-db80aa9b8715 | -19.42698 | -57.22269 | 2026-01-20 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 57653a59-d387-34bf-9e10-68e7643a9f19 | -19.42761 | -57.21708 | 2026-01-20 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 867469ca-403e-303f-b65f-a3f4b3095dac | -20.70448 | -48.81174 | 2026-01-20 06:03:00 | AQUA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 70940596-972f-304e-9ae6-541d28f50d34 | -20.70287 | -48.8218 | 2026-01-20 06:03:00 | AQUA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 00f15ec4-4826-337e-b4da-768c7f5a18e2 | -6.5631 | -51.1126 | 2026-01-20 06:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 336dbf88-6e9e-312e-b207-e3f45e3bfa73 | 1.12571 | -60.52743 | 2026-01-20 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c2add5b-76fa-30bd-819c-640cd05f1e28 | 2.67922 | -60.0883 | 2026-01-20 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0eee2ebd-fa09-3999-9b4d-b9f5c31e817b | 2.68025 | -60.09442 | 2026-01-20 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e9229a8-6610-3523-9b6e-73ac079c2b9e | 2.04937 | -60.86852 | 2026-01-20 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0247fde-718b-3176-ab58-6026294f7a95 | 1.13142 | -60.52037 | 2026-01-20 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a194cec7-941b-3645-b710-52250ce406a8 | 1.12874 | -60.52321 | 2026-01-20 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a277250e-042e-346b-8489-cd157f143e6f | 2.68693 | -60.09308 | 2026-01-20 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63e746f5-b3a6-361c-9c69-def7e5a9b3f4 | 2.68126 | -60.10038 | 2026-01-20 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13d02884-2177-38d0-a035-0ee9eae8b051 | 1.13239 | -60.52623 | 2026-01-20 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc62081c-24e3-3cda-a856-843c4646c89f | 2.68215 | -60.08509 | 2026-01-20 07:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c62e570a-f5f1-315f-a64d-514fa637dd6f | -20.18422 | -50.65081 | 2026-01-20 12:38:00 | TERRA_M-T | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 5c95a603-9cc8-37d6-92a9-7648908692a4 | -19.43685 | -57.22493 | 2026-01-20 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 9c64058b-f0a8-3980-a184-cf20cc119f2f | -19.43119 | -57.26297 | 2026-01-20 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 435e8fac-a821-3a64-ba21-2794dc672bf2 | -22.22003 | -49.65129 | 2026-01-20 12:38:00 | TERRA_M-T | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 668e2f11-0cce-35eb-96b9-78ad69b4e69f | -19.43261 | -57.25345 | 2026-01-20 12:38:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| ec4c7998-37d1-3875-88b0-b930f85f354b | -20.85306 | -53.73946 | 2026-01-20 12:38:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 159db08d-7183-3119-940d-1018ff7ee76c | -20.73762 | -48.90242 | 2026-01-20 12:38:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 3b4434d3-e080-36b4-9553-0a962df6d4e8 | -22.10205 | -50.18942 | 2026-01-20 12:38:00 | TERRA_M-T | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 7e335172-2f99-351c-9386-5f157dc5d444 | -20.85163 | -53.75089 | 2026-01-20 12:38:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7d62ec47-2f01-3223-a9f1-b2f5f80438b7 | -22.20664 | -49.64994 | 2026-01-20 12:38:00 | TERRA_M-T | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| b0c09c51-9d88-3201-875c-b5f8624bccc0 | -27.89566 | -53.31085 | 2026-01-20 12:40:00 | TERRA_M-T | PALMEIRA DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4313706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 64d29740-d2cc-3394-a902-719b0beb8dfc | -28.3056 | -54.2612 | 2026-01-20 12:40:00 | TERRA_M-T | SANTO ÂNGELO | RIO GRANDE DO SUL | Brasil | 4317509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 636f8d94-b7bd-360e-8898-6aa96621b4f7 | -27.17254 | -51.50708 | 2026-01-20 12:40:00 | TERRA_M-T | JOAÇABA | SANTA CATARINA | Brasil | 4209003 | 42 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 87101629-7f3f-3444-93f7-ebeb223a4658 | -27.9475 | -52.92556 | 2026-01-20 12:40:00 | TERRA_M-T | SARANDI | RIO GRANDE DO SUL | Brasil | 4320107 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 418be894-8ec6-3575-a2a0-533d5e22988f | -22.8789 | -52.27655 | 2026-01-20 12:40:00 | TERRA_M-T | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| 162dcd87-a8fc-36ff-a9a1-2863d32c5244 | -25.46069 | -49.53359 | 2026-01-20 12:40:00 | TERRA_M-T | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 655ebc2d-f287-36a0-9e5d-4cf96edcb3ca | -29.22216 | -51.33056 | 2026-01-20 12:40:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| bbade011-8e42-371d-ad67-bef8b50be86d | -25.4561 | -49.52776 | 2026-01-20 12:40:00 | TERRA_M-T | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| bfe4d53c-09d4-3729-b843-4b3d2f31613e | -27.89448 | -52.22332 | 2026-01-20 12:40:00 | TERRA_M-T | GETÚLIO VARGAS | RIO GRANDE DO SUL | Brasil | 4308904 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| a535aff0-7043-3128-b760-9a23e58b8a72 | -27.60529 | -51.46109 | 2026-01-20 12:40:00 | TERRA_M-T | BARRACÃO | RIO GRANDE DO SUL | Brasil | 4301800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 6aef9b2e-84d6-3d2b-a1e5-f86d49a129bf | -25.40608 | -52.41518 | 2026-01-20 12:40:00 | TERRA_M-T | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ddda3c98-5e51-39d4-b090-282caaa88ff8 | -28.97296 | -51.07357 | 2026-01-20 12:40:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 4217a907-23d1-3d7e-bc92-5e24e0feb790 | -23.23335 | -51.65297 | 2026-01-20 12:40:00 | TERRA_M-T | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 9574bf54-b222-3bfb-b0a6-16dcd4ac05ff | -28.50671 | -50.92499 | 2026-01-20 12:40:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| afb3d0ef-6264-3127-96de-1a30637ad74f | -26.35065 | -52.84938 | 2026-01-20 12:40:00 | TERRA_M-T | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 626340d4-b891-3c59-a5f4-58a1e26c90fb | -30.77538 | -53.6454 | 2026-01-20 12:40:00 | TERRA_M-T | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 6.9 |
| ba9fc35e-97ed-35f5-92a9-5b21a11e32c4 | -26.09985 | -51.86953 | 2026-01-20 12:40:00 | TERRA_M-T | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 342bb3a6-cc48-316f-a718-9914cdf21305 | -27.44977 | -53.94016 | 2026-01-20 12:40:00 | TERRA_M-T | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 39d69c88-4507-35f5-adb6-ce923b2cc65a | -29.02779 | -51.18117 | 2026-01-20 12:40:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| b394bf8a-166c-36fd-96ba-6771bbedb386 | -26.7705 | -53.18621 | 2026-01-20 12:40:00 | TERRA_M-T | MARAVILHA | SANTA CATARINA | Brasil | 4210506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| c785f76e-f6fa-397b-b360-84f179690158 | -29.03034 | -51.17471 | 2026-01-20 12:40:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 342719c9-6c9c-3f69-9954-b8930109f06d | -29.35093 | -53.22598 | 2026-01-20 12:40:00 | TERRA_M-T | IBARAMA | RIO GRANDE DO SUL | Brasil | 4309753 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 3e6a9e6c-c53d-39eb-b8cb-eb793f395ef3 | -25.57702 | -54.57304 | 2026-01-20 12:40:00 | TERRA_M-T | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 13c25679-6353-3337-a62a-f9fb49cded63 | -23.01741 | -49.47173 | 2026-01-20 12:40:00 | TERRA_M-T | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| e8a992ea-4c2e-38ac-a433-df1dfe019d3d | -25.78606 | -53.3091 | 2026-01-20 12:40:00 | TERRA_M-T | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 577e74a9-73f1-3529-801c-fcbcd140c559 | -29.25723 | -51.52127 | 2026-01-20 12:40:00 | TERRA_M-T | GARIBALDI | RIO GRANDE DO SUL | Brasil | 4308607 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 48ec71b0-80a7-3e72-9956-35deecaedbdd | -25.08356 | -50.18002 | 2026-01-20 12:40:00 | TERRA_M-T | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 9480d33c-5239-39c2-9c1f-efa622f0fac8 | -27.02153 | -50.9192 | 2026-01-20 12:40:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| e2e22458-c566-3a76-9429-93df96442fc2 | -26.47845 | -48.64187 | 2026-01-20 12:40:00 | TERRA_M-T | BALNEÁRIO BARRA DO SUL | SANTA CATARINA | Brasil | 4202057 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 600563df-f249-368d-b074-ec237a521d52 | -23.10118 | -48.94104 | 2026-01-20 12:40:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 46e0ca2d-1d0b-3aed-9d37-e5f69be2dc34 | -25.46693 | -50.64427 | 2026-01-20 12:40:00 | TERRA_M-T | IRATI | PARANÁ | Brasil | 4110706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 55831792-383b-3b53-98bc-e2cb9375f4c6 | -19.4365 | -57.2354 | 2026-01-20 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 28f52243-c27d-3583-8778-ad7ad2a1b795 | -19.4365 | -57.2354 | 2026-01-20 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 09c93997-6740-3b79-b5a8-a9f5e3cdc1ac | -19.4365 | -57.2354 | 2026-01-20 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| fedbda16-5d18-354e-9aa4-f625b5876483 | -19.4365 | -57.2354 | 2026-01-20 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 9ff73713-1077-334d-aaef-db8268b9bd8b | -19.4361 | -57.2563 | 2026-01-20 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.2 |
| 850c189a-aa42-31f2-b8a7-62a586e49b04 | -19.4365 | -57.2354 | 2026-01-20 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.8 |
| a5b0d90b-1845-3247-95fd-72ff9f3a568f | -19.4361 | -57.2563 | 2026-01-20 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 206.6 |


