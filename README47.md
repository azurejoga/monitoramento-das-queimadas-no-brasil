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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fdee4ac-0c36-3bbf-bd17-92ba07e3c283 | -12.63038 | -57.00461 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eacebacd-d198-35d6-bf8b-fc18fc927ba9 | -11.80213 | -46.47438 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b21ea584-48a1-3ad9-a836-9d65280ead69 | -13.00408 | -48.72935 | 2025-08-31 04:29:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 231b7915-de88-3aaf-bf83-ac3a81ac1ff3 | -13.36578 | -54.38652 | 2025-08-31 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e567f84-6875-39bc-94e2-8f0861f336ad | -11.07353 | -44.62459 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| db50dbea-32d7-3b7b-be75-a3d682a0a14d | -13.34649 | -46.97895 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16a18a73-466f-301c-a8a9-10bb018ba5d2 | -13.50508 | -46.97472 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5777b369-01dc-34be-b49e-889bfe651c68 | -12.82762 | -48.08234 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea3c8e32-7ae6-3619-85a2-388758ed5a7f | -11.26557 | -44.92707 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd871b0b-29e1-35c0-a47b-be74246a1de3 | -13.35857 | -51.74871 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e1cdd70-9915-30d9-948d-8d35ea46133a | -10.71148 | -49.00798 | 2025-08-31 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbf6bf91-ed39-38e7-8221-0addd0f6e0fd | -10.05337 | -48.30822 | 2025-08-31 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 589aae51-301e-3974-a1b2-80f1e0357446 | -13.68736 | -46.89352 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c331153b-ac7b-376c-a334-b7e53793d914 | -13.3476 | -46.97179 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baefb074-b2eb-386b-8fc9-d672d8ec6739 | -13.34148 | -46.98916 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 473c1790-5e20-301e-8ebe-27d735d33267 | -11.84364 | -51.49142 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3bc3d375-9630-381f-8b85-b25d88e5b9c2 | -13.35317 | -51.75731 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ce34332-1d89-3b0f-a82c-db9fa2f50313 | -11.06243 | -52.04847 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 674ef67b-c35c-344e-a968-ef4b2a29aef4 | -10.10675 | -49.28529 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86dbf19d-b851-3aee-bb5f-f59c2f0cb334 | -10.9463 | -50.78658 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b68a7ba-d468-3c2a-8723-6fcf3d6cec34 | -13.03213 | -56.90403 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4181b2d5-5b9d-3990-a1f1-79643b1402f8 | -10.95356 | -50.85626 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 6f992f44-871b-3667-9132-bd30ca489cdc | -10.04156 | -46.02661 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7cad8ae-f3c6-3fff-8d21-cb0ee94d538b | -8.96342 | -50.00816 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e69d8cb6-c476-3587-aaee-4509f49e4fad | -14.26577 | -48.06041 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6d69014-e06c-38b9-aa21-a9ff6c6b98ef | -10.03642 | -48.08288 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c165d61-70db-3230-b1de-a5bb53146ad6 | -11.88042 | -46.72402 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bd5f523-3ca9-3bd7-9c25-d513009faadf | -11.02025 | -46.86642 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eac1a8ed-cbaf-3ef8-a2a5-b542fe3a92d0 | -11.86501 | -46.50237 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5de6e28-edde-3d05-b52c-58e65346587a | -12.56189 | -44.79876 | 2025-08-31 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dc28c33-8aea-3b5d-93e7-f790af1aa052 | -12.63505 | -57.00913 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07e0fbd-b08f-34b4-bc3b-1fb0ef9e514d | -11.82855 | -46.42686 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1d9a0bfb-577c-31e5-ab49-ef476587bb27 | -14.81982 | -46.74506 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd1a73bd-c035-3143-91f5-d49bf3f92cc3 | -12.18217 | -50.11987 | 2025-08-31 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce3e7ea-d599-3ac1-b179-a66380e4ba93 | -12.63506 | -48.20428 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 851cff21-43ea-3269-b0cb-eeb553862949 | -13.68792 | -46.88993 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e19c720a-11f4-3c32-be1e-94425ef719ba | -11.29969 | -43.56142 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995a0878-2b3d-395b-b380-04e2f186a363 | -11.2097 | -45.03767 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff41f08d-f049-3467-a9e6-2476d958a468 | -13.53634 | -46.97218 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c86d7de0-6477-33eb-9988-d5f5e117a575 | -9.47222 | -47.60496 | 2025-08-31 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 065605e9-68d2-3ccd-8316-c1b60d8b734b | -12.6361 | -48.21911 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f4ccd33-0b5b-300e-a7ba-92c3ba0df233 | -11.90016 | -46.43069 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d726aa86-98f5-3823-9c7a-e97e6d92398a | -12.62896 | -48.1996 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13e9d386-86af-3d8b-ad11-dbbdd4a069e6 | -11.00479 | -46.94336 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe663232-e794-3a7f-868b-56f76b2c826b | -13.02359 | -56.8919 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34c3002d-b8ba-347e-b54b-4a81640bf9b8 | -13.02817 | -56.89642 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd9e6fe5-dd7e-372f-a60e-32a695e4fbb9 | -9.80503 | -46.0588 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0c2e0cc-0e7b-3959-b1ee-dbe6a81b33fc | -10.78054 | -48.82059 | 2025-08-31 04:29:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bf2a3a9-3773-3453-8f3d-97e3085e20e3 | -10.60993 | -44.90656 | 2025-08-31 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59a6ffdd-02ab-3310-887d-0b1f869af5a0 | -11.89954 | -46.39021 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 346c0757-5736-3b08-89bb-61f033eb51b7 | -12.31166 | -45.72417 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 453e8c5f-5f66-327d-adff-9b26f8eed4c9 | -11.81463 | -46.45036 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d8d7251-5252-3352-b912-91f09504030f | -13.47163 | -46.96918 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d264fe93-410a-3ab0-a2cd-dc267ae4f3e7 | -13.49225 | -46.9689 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ec77521-2ada-322c-a329-68028fa1fb66 | -11.89324 | -46.72966 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 380d8dfa-2b2d-3566-b827-a1cae1424896 | -14.0441 | -44.54873 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2330db3d-2ae9-3db6-af01-912411df9d2c | -11.31581 | -43.47554 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa0bc6f9-5142-329a-89d4-07cb480dad1a | -11.81331 | -46.4467 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5969acb7-cc2c-3dbd-ae57-e887e0769ed4 | -11.91322 | -46.68907 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d66ee118-cff2-3dc2-897f-1f3bfdc37088 | -9.59049 | -46.00365 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 386dd5e1-2de9-3f8e-b4de-8cfcfc47933c | -13.65838 | -46.92551 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c8f5d7a-2b29-3e6f-b66a-81be18ca1e3b | -11.85544 | -46.45312 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 477e6041-447f-3be8-b2ec-664510b214cc | -14.00166 | -46.32537 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a9e0a77-54a1-3583-83ec-816758562975 | -11.41337 | -44.68468 | 2025-08-31 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 71c60b3c-7a70-345b-80af-c96b1fb8fbe7 | -11.80435 | -46.46008 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e798688-cdbc-3f35-8a58-04d6e2891d7d | -15.96367 | -43.90398 | 2025-08-31 04:29:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c5b597a9-0d2a-32e5-b573-9fa0791dd165 | -12.68242 | -43.16493 | 2025-08-31 04:29:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cffc892b-7dd8-3abb-991f-a65dd6f94068 | -11.89504 | -46.37474 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a11f57d-a1ce-3454-9765-efc8c52ef846 | -12.62438 | -57.00695 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46776587-e8d5-3222-a0bf-ea0ff09c6132 | -13.49615 | -46.96589 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5891072f-2e11-3f0d-9abc-89ce640f6f5e | -11.80883 | -46.45341 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6b10102c-bea4-3752-8b61-57fdfb792263 | -10.75659 | -59.81923 | 2025-08-31 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ca4b558-ff6f-366b-b664-09757b38720d | -10.03134 | -48.0931 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67ee9989-d848-3354-ae9c-1d4a5f915732 | -14.83454 | -46.73931 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edb47924-c4da-3999-a22d-7313f0e71c18 | -9.62046 | -47.80379 | 2025-08-31 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98aac63e-2945-38ee-a37a-b0187f95056e | -9.9959 | -48.38432 | 2025-08-31 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0645e34-6ae8-3748-af95-4f8b55bc703e | -13.48271 | -46.94184 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31586b27-449b-3eaf-b117-4e980948518d | -14.04427 | -44.55076 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65f51166-64d7-36e1-86bd-67d91506ddfe | -12.63667 | -48.21554 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d7885eb-5bf6-388c-8bc2-05ee99766624 | -12.79928 | -48.08861 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e1a9483-3a11-344a-a044-51bd0fb0f4ce | -12.79871 | -48.09217 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 046f61c9-a9ee-3aa5-acda-dee6c210f452 | -10.01974 | -48.36585 | 2025-08-31 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cddd82e-e76d-3a97-9113-20b8cc8a0395 | -11.32509 | -43.67519 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e3f58ce-f77b-37e6-8f2a-eca36b5d44cf | -10.02532 | -48.37425 | 2025-08-31 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfe0f473-e2a9-320b-bc84-5fb115507510 | -10.0287 | -48.37483 | 2025-08-31 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da2c387b-32d5-3baa-95d6-7e866dcc225a | -11.84465 | -46.78791 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 543fa9cb-c09c-3676-b073-d4e1a75a663d | -10.09568 | -49.28735 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 083c3151-a2c0-314e-9e86-0a5d67a341e4 | -11.21896 | -45.02338 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50501167-f3f3-3bcf-a31e-3ccd32b782bf | -11.07745 | -52.05617 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2686234-2837-317e-ac18-1537e6fac135 | -12.4111 | -46.46611 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5348ea0b-57a9-3f41-b6ba-9921c3ff8a9e | -12.93569 | -56.98362 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa656f2-d68f-3c2f-99dd-6d73abfea281 | -11.2881 | -43.64222 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ef93c6b-59d4-303f-b707-85bfeeb032bc | -13.98547 | -46.3158 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35ecbdde-05de-3eff-ad3f-44da05450f9e | -14.54019 | -51.98806 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b974fd4c-dc11-3d4f-a5d6-c1d47392d47b | -11.02192 | -46.87754 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1f012c2-5f23-32a4-8e02-0f29a3f8773e | -14.26788 | -51.90719 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbe8a6ed-5b2c-3ad3-9ee6-3d2f548bcd34 | -13.68905 | -46.88261 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 664d2cf9-c1f8-3797-9fff-426603511518 | -12.83095 | -48.08289 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6218ffea-5b8b-379d-a901-4885d70f090d | -13.51123 | -46.97931 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f8d1f3a-33f6-3a1f-a743-227ba0c385c9 | -12.10122 | -44.72514 | 2025-08-31 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README48.md)
