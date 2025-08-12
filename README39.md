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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7728a3d-db48-3da7-b4aa-ad668266844c | -9.92348 | -46.18596 | 2025-08-12 11:53:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2fe63862-b937-3fe1-b310-3b81a39c8521 | -11.34914 | -41.47309 | 2025-08-12 11:53:00 | TERRA_M-M | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| c219d315-b397-3cba-9ab7-25b0ccab6528 | -10.53462 | -42.54979 | 2025-08-12 11:53:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| d95d6fbf-2caf-3a20-9faa-bc28ff983c8a | -5.68202 | -41.40458 | 2025-08-12 11:53:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c5998ce2-0c04-367e-8d53-82689e611ba6 | -8.51766 | -43.30451 | 2025-08-12 11:53:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 72c94089-5b93-3992-95ec-c3dc89c709f9 | -9.22454 | -44.52631 | 2025-08-12 11:53:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d076aa64-cfa8-369a-a3dc-59585b5fb671 | -8.51599 | -43.31548 | 2025-08-12 11:53:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 0ae94c66-d9c1-3dd0-a8fc-e229a8d3325c | -6.09121 | -38.23675 | 2025-08-12 11:53:00 | TERRA_M-M | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 77d6ce97-11d3-346d-b4e0-71db95a984c6 | -7.48792 | -43.93353 | 2025-08-12 11:53:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e8cffed0-50d8-3a5a-b1d1-609e51048757 | -10.63313 | -44.75475 | 2025-08-12 11:53:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ce79d4b0-49c1-3bdf-b0dc-58bb72d7f82a | -8.52575 | -43.31693 | 2025-08-12 11:53:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 94a7e98f-ae53-389e-9740-18c7822b860e | -9.21401 | -44.52491 | 2025-08-12 11:53:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b5940192-90c2-3257-8286-df8d145f1121 | -9.65063 | -48.15316 | 2025-08-12 11:53:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 90dcead0-47d9-331f-ad50-8f7b3f118e38 | -8.82517 | -44.58511 | 2025-08-12 11:53:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 8d6e96fb-b301-37af-a4f7-fea3a010870c | -11.34783 | -41.48206 | 2025-08-12 11:53:00 | TERRA_M-M | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ed3228d9-45b6-37d4-a705-a65d6c186509 | -9.21931 | -44.53175 | 2025-08-12 11:53:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f72d68ab-136e-3bbb-892d-1b2e6c258e11 | -12.68293 | -44.95494 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9d12f6b1-44cb-38cd-be89-8fc55fb3e3cd | -13.63246 | -46.9281 | 2025-08-12 11:55:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| d668ef21-eff0-3f5a-b3cc-53878e489df5 | -13.87622 | -45.57698 | 2025-08-12 11:55:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fda4aa57-3185-3372-bdb2-ad3e66a91c3b | -12.78699 | -45.45715 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 996bddd9-36db-3f38-ae0d-a596d62bbbc0 | -11.75826 | -45.0277 | 2025-08-12 11:55:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6992fc0f-3e1e-392c-a50a-f2aa98256276 | -12.77641 | -45.45539 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| bffc7631-f286-3ce3-b354-b1686ba73f21 | -11.95939 | -43.39024 | 2025-08-12 11:55:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4a7ec4c4-4b4b-3181-9173-29fcb124ef67 | -11.9469 | -43.40934 | 2025-08-12 11:55:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 61a52f24-eae7-3591-9820-59280aae3c3f | -12.5562 | -47.00718 | 2025-08-12 11:55:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d40875fd-d870-3f2f-b7c5-5f815cc8a4c9 | -13.10807 | -46.87303 | 2025-08-12 11:55:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d0a974d2-5ae2-309d-82dd-6fc3ce355eb6 | -12.6849 | -44.9426 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 149f88b7-4673-367a-b951-36040455411b | -12.77426 | -45.46863 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d8ccbf82-795e-39bc-9e30-dcb24f038ce9 | -13.11094 | -46.85591 | 2025-08-12 11:55:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c04b9bee-57ce-3ca6-bf8a-d8efcb3ebc9c | -12.72635 | -45.89938 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d587618c-39dd-3cc0-96f0-ac8ef157a9f6 | -12.77199 | -45.44862 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7204c8ae-3860-33b6-a5f0-f792106953b8 | -13.02983 | -46.66284 | 2025-08-12 11:55:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 60f5c894-9002-39af-b6e0-5bad4958569a | -11.95631 | -43.41067 | 2025-08-12 11:55:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 1caeabb1-509a-3017-9ca5-c19a2fbe2c63 | -12.76992 | -45.46189 | 2025-08-12 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 91379ea7-1ab0-328c-b24e-427f0f9031b5 | -13.62788 | -46.93375 | 2025-08-12 11:55:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 08e3c92c-606b-3b71-b6cd-22da23c641da | -14.55537 | -43.13027 | 2025-08-12 11:55:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f217d7dc-f37f-3f40-80ed-1ee86ab00850 | -11.94535 | -43.41956 | 2025-08-12 11:55:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| ca9efba8-946e-3608-99fb-1d138403b54a | -11.95785 | -43.40044 | 2025-08-12 11:55:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a2d3d047-f948-3d66-9220-a5e2cf4c2355 | -13.02593 | -46.66909 | 2025-08-12 11:55:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f8dbdb35-fb60-386d-90f9-59d5c872b738 | -12.67733 | -46.98037 | 2025-08-12 11:55:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5d2abf12-b488-3aa6-9772-40cb09f77dcd | -14.12 | -44.88936 | 2025-08-12 11:55:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 93b279ce-c2d1-37d3-944b-5a44c4ffb790 | -13.52168 | -42.38857 | 2025-08-12 11:55:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d82bab5a-8a96-3efc-94f4-8948082f8833 | -13.27172 | -40.33894 | 2025-08-12 11:55:00 | TERRA_M-M | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| badd6a1a-8dc3-3f98-ba24-892a41665e4b | -11.66663 | -50.14108 | 2025-08-12 11:55:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0ce2460c-395d-306a-878e-1dd969507448 | -14.56442 | -43.13167 | 2025-08-12 11:55:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f929b24b-e42c-39f0-8d5d-99800f8b816a | -12.55917 | -46.98927 | 2025-08-12 11:55:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| cd013f2d-456a-340d-9fdc-fceed0fa744f | -14.2475 | -43.75396 | 2025-08-12 11:55:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6f18f0bf-2bd1-39f0-896c-92cf185818e8 | -11.95478 | -43.42079 | 2025-08-12 11:55:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 44b185d2-a31f-3265-a540-1cdc7317e3ca | -12.83615 | -39.69065 | 2025-08-12 11:55:00 | TERRA_M-M | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c5348830-56bb-3a8c-8303-72308f588266 | -13.5203 | -42.39785 | 2025-08-12 11:55:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| f1eff0e4-ba3a-36a8-8e22-ffa28090459f | -17.29983 | -46.0568 | 2025-08-12 11:57:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9c70d987-3330-3f01-9e88-c375673e35b5 | -17.30188 | -46.04436 | 2025-08-12 11:57:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4f1d18a1-5b0e-3766-96f1-38e6daf4bde3 | -15.26144 | -44.36287 | 2025-08-12 11:57:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3713de2d-b03d-3692-bd69-e961b8b9b03a | -21.91051 | -41.22623 | 2025-08-12 11:57:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| dae13210-a777-351b-8344-e968e24316cf | -18.63379 | -46.83139 | 2025-08-12 11:57:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 421b6bd8-a799-3bae-86fe-082658d3e5f8 | -18.64064 | -46.82468 | 2025-08-12 11:57:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 17abc062-27b7-33d6-b76e-92e5e4cdde35 | -17.56971 | -45.33649 | 2025-08-12 11:57:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a7c123df-683c-3108-82b4-c8c6a5f6377b | -16.75046 | -45.77739 | 2025-08-12 11:57:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 84b16423-5137-3a78-8326-80e793f27a88 | -19.08393 | -48.13771 | 2025-08-12 11:57:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f264cacd-b7b0-3699-b596-6a7c75c08eef | -15.8232 | -44.69179 | 2025-08-12 11:57:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9d37dcfc-dbe0-3b83-8f45-68d8f1d3570a | -17.29271 | -46.04951 | 2025-08-12 11:57:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 40f15a30-31b4-3f29-b3f5-cda8ccfa2a46 | -19.08105 | -48.15408 | 2025-08-12 11:57:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 37b63ec4-e8b7-37d7-85ed-bb0eccd7cb6e | -17.14236 | -44.80449 | 2025-08-12 11:57:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| da48cde9-745b-3f9e-bbe5-7db8cf71b39e | -17.57148 | -45.32525 | 2025-08-12 11:57:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ba45509c-2642-3ca1-8a34-8c419420f67d | -23.29353 | -46.7987 | 2025-08-12 12:00:00 | TERRA_M-T | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 88b1a52b-ba38-3f6d-9925-6ea34419018a | -12.5738 | -47.0232 | 2025-08-12 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| bae2b6e7-47e6-30f0-a0cd-27b8b5eeed76 | -9.2232 | -44.5283 | 2025-08-12 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e8b227cd-920d-3eab-94d7-456a901f5f28 | -14.1212 | -44.8933 | 2025-08-12 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ee0ffe86-bd6d-3b8c-a432-fc8721023c2f | -11.9493 | -43.4019 | 2025-08-12 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 93ab4918-4da0-3241-9be6-747651606ea2 | -9.2232 | -44.5283 | 2025-08-12 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 53f8c6cc-90c4-393f-b702-acb37f7e870a | -14.1212 | -44.8933 | 2025-08-12 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| d02b8a53-4710-359d-adf1-20628e68445a | -12.555 | -47.0034 | 2025-08-12 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 56d37069-cff0-31d0-9169-2d686ddf3504 | -9.2232 | -44.5283 | 2025-08-12 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 332.8 |
| de68f028-7ed5-31f4-8537-b66f2d6ad442 | -14.1017 | -44.8968 | 2025-08-12 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 36a29af7-a349-327f-b1b9-38c51989e5e4 | -11.9493 | -43.4019 | 2025-08-12 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 8e8e7e16-4f44-31bf-b650-88a3f1f185a7 | -14.1212 | -44.8933 | 2025-08-12 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 825ddff7-7c86-37a0-b3c1-7684a1598ec6 | -9.2042 | -44.5305 | 2025-08-12 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| d084ef9b-dbba-3655-a7b8-0ada55db0282 | -9.2232 | -44.5283 | 2025-08-12 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 6c4dd84c-b999-3d05-ba28-671fd491f5d7 | -14.1212 | -44.8933 | 2025-08-12 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 1f2a8c52-fbd0-301e-aff2-96c1fc919aef | -12.5738 | -47.0232 | 2025-08-12 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 914679e4-b93f-3d6b-9bb3-6693b85f2425 | -9.2042 | -44.5305 | 2025-08-12 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 49303139-ac81-340f-b271-fa61ca116f4e | -14.1017 | -44.8968 | 2025-08-12 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| d946a44f-5c0e-3380-a0fc-d5d1c56e7d57 | -13.8743 | -45.5643 | 2025-08-12 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2c1875a2-a430-39ed-8a19-bf1f186e489a | -11.9493 | -43.4019 | 2025-08-12 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| ab07049a-960c-3cf1-8a77-710f88669c0f | -12.555 | -47.0034 | 2025-08-12 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 612f9153-f4cb-3941-aeb1-9f45bf10484b | -11.9493 | -43.4019 | 2025-08-12 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| f64e613e-7cc1-3200-84c8-4a31a6d7f2da | -11.9489 | -43.4257 | 2025-08-12 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 284.4 |
| 3ae181dd-b402-3a83-890e-d68789caccc3 | -12.6891 | -44.9494 | 2025-08-12 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 46e368b7-bdde-301e-8755-eb6397578873 | -14.1017 | -44.8968 | 2025-08-12 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 90666977-75f4-3627-a02e-381a97817147 | -9.2232 | -44.5283 | 2025-08-12 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 10a57708-8884-3bc2-be9e-63e87deb43d1 | -14.1212 | -44.8933 | 2025-08-12 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 288.0 |
| 809e48a8-047b-3f1a-9bcd-db6eb671f338 | -14.1212 | -44.8933 | 2025-08-12 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 274.6 |
| 0c508fa9-6cef-3df6-8dae-df8646c71893 | -14.1017 | -44.8968 | 2025-08-12 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 1145a41f-e877-32b0-aeaf-e4ac905ee817 | -11.9493 | -43.4019 | 2025-08-12 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 215.9 |
| da49453b-3978-3274-9e6b-11a8b35f89b6 | -9.2232 | -44.5283 | 2025-08-12 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 486.7 |
| 62f7dc4b-2b70-304b-ba2b-44cfe44a75fc | -17.5701 | -45.3346 | 2025-08-12 13:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 79a21790-416c-3d7c-9322-ddaf5daa3d42 | -14.1017 | -44.8968 | 2025-08-12 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 15377181-8b99-3a41-a827-58141f765fa3 | -9.2232 | -44.5283 | 2025-08-12 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 183.2 |
| bfd06921-49e0-35b1-9272-cc4c1a63784c | -12.3565 | -59.8473 | 2025-08-12 13:10:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 2ddebbb0-5dff-3ba5-8211-9a24054167e9 | -17.5701 | -45.3346 | 2025-08-12 13:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 155.4 |


[Clique aqui para ver as próximas entradas](README40.md)
