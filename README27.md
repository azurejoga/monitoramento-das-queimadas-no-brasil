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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49992635-14c4-3290-8be4-383bc613daf1 | -13.22453 | -47.29014 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 434a8b32-e9af-365b-8743-9da34e38d97e | -12.70836 | -47.95244 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 963a029a-58e3-30fe-a811-4f23ff9822e9 | -14.63315 | -46.38617 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6279acab-2184-395a-bc1d-4c0d99ad8d52 | -12.06842 | -46.56886 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b6228d8-f0c2-3a21-b1bb-afaf2945f36e | -10.3227 | -46.62334 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc3fe32b-a298-339b-bf7a-7132965eb68f | -13.7063 | -50.82028 | 2025-09-17 04:12:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 340e667e-c733-3ff5-ad8c-9be2167e4366 | -15.40411 | -46.15047 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a14c08d-0250-374c-b7c4-9c53359138a0 | -15.10091 | -41.06818 | 2025-09-17 04:12:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bae3562f-b7b8-3674-a68b-86cfe4eba8f0 | -11.02853 | -45.06009 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c1c19a6d-9233-3c56-875e-fee6f8a32014 | -14.81038 | -51.70919 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f51f176e-cd67-322c-9492-71f465fcc962 | -15.4133 | -46.16042 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baa31a6f-850e-311e-b7e5-ca1f7cda9556 | -14.6202 | -46.39703 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b98d9e7-29ca-3a25-a190-be70ad9ee484 | -12.69387 | -45.80991 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ffbc342-15fa-3f89-88a9-1c83d0edd6ee | -12.70463 | -47.97385 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5091eb34-bbb1-32fc-9c5d-85390a2c80ef | -15.55348 | -46.7067 | 2025-09-17 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4986961f-c2e9-3e77-8ecb-dd140cbb1768 | -13.91541 | -44.96658 | 2025-09-17 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61006ea3-e693-3cc6-8429-4041dae97a9a | -13.17714 | -44.48328 | 2025-09-17 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f87da84b-7939-39ef-ba8a-cb901df7a4e0 | -13.71093 | -49.85862 | 2025-09-17 04:12:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0769d826-18a8-316d-af39-39f7100db520 | -11.7712 | -44.74326 | 2025-09-17 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8547ed04-d290-3b2a-b03a-5505fe5db3f3 | -10.79004 | -45.97273 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69836a98-00ca-37ba-8f94-7d147baf1282 | -15.98496 | -46.45428 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64c8619b-33c4-3788-a559-8911ce221b51 | -10.79857 | -50.72855 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57b58848-fc31-3219-9a96-591f683f8a62 | -14.60338 | -46.39996 | 2025-09-17 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca124da9-78fb-36fa-8915-8fb2f79fe442 | -11.50623 | -43.63314 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8332c2b4-1757-3915-9b0f-2f2faa514485 | -12.85976 | -47.13381 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 420d95c4-f264-32bf-9f51-d4fd64c89eda | -14.62205 | -46.39862 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd53ed59-3c7e-3283-8965-9e875569a0ce | -12.69724 | -47.96872 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fad03ae4-de71-366d-accc-df59d2485f77 | -10.31422 | -46.62679 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2da4fe42-a0ff-36c5-a1a3-52a466b160db | -12.09611 | -44.83121 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b95896d3-4eb0-3f6d-bb29-f530493e5e2c | -12.10557 | -44.81691 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb41f674-693d-3293-b2cb-5de1c543fd90 | -14.83136 | -46.70959 | 2025-09-17 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a8cd862-7cee-3ab2-b48f-b6c85d6ffe85 | -15.72123 | -39.3188 | 2025-09-17 04:12:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f08195e5-73dd-3da4-9564-a94fc82d9008 | -10.80169 | -50.71141 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1514290b-db58-3397-83b9-b247ea63a12f | -15.12383 | -48.66383 | 2025-09-17 04:12:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58a9db29-75c2-30cc-bebb-56b944a74649 | -15.32264 | -42.05491 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed5ce096-4afb-3968-bd69-2aefd0eeb752 | -10.77478 | -50.71801 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fbb8056-d91a-3da7-997d-b9467cda3dee | -13.65983 | -44.39786 | 2025-09-17 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 617b2ef4-defb-34d9-94e7-c222087bdb14 | -12.00148 | -46.68921 | 2025-09-17 04:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92346551-a950-3ae3-bf6f-b4ae0e6f9f6d | -14.56206 | -47.36858 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a2f58f8-2a31-37da-993a-a7a2b2bf48ef | -11.07219 | -49.76106 | 2025-09-17 04:12:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebdd24b8-1c73-3f8d-a12c-dca6432a85bd | -12.24451 | -46.76105 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c360c2b-7003-3fa8-89de-9177b2dadd1f | -15.43398 | -47.32146 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2bf0904-3125-3b13-b470-69cd99efff30 | -12.44428 | -49.73371 | 2025-09-17 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46422964-948a-3ab8-a611-604edfd1f409 | -10.94428 | -45.50262 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e67ce5a-25df-3220-bbbb-1c0b09fd7450 | -14.2669 | -44.68148 | 2025-09-17 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f2c2669-68c1-3914-96dd-e414d917ec8a | -12.64374 | -44.85878 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b18af781-950f-3311-ae09-3019e5e5cbb3 | -12.71561 | -47.9836 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb6a53ae-1de2-34a7-9da4-adec33d6b90b | -14.54663 | -47.43004 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 068bffa4-6e56-3830-b1f6-ed17a640c64c | -10.95979 | -49.57339 | 2025-09-17 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98788038-486a-3474-98b9-5498e8f90397 | -15.41606 | -46.14388 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcb98cfc-1229-36ca-b3af-99f797a46da8 | -10.87756 | -45.43963 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38f69b8c-2499-3a63-8e26-d1f1214ba0e2 | -15.31747 | -43.66885 | 2025-09-17 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 09778ea2-a352-3941-a1ad-f3e0a4c9154d | -14.80656 | -51.70244 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 145e841b-68c3-366f-ab18-a0321e29cc30 | -15.9274 | -42.63905 | 2025-09-17 04:12:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2996ce3d-5d11-3703-92ee-be445741bc33 | -15.42011 | -46.11965 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b462676-3370-38e8-98a6-63179f59858c | -14.81865 | -48.10923 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4480c943-dc2a-323b-8a3d-fe5c12080a0c | -15.42216 | -46.14859 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4771719f-92b1-328f-86a6-ad29562b8650 | -12.18001 | -44.34407 | 2025-09-17 04:12:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fecd3e34-106a-35c5-a8fe-7fb2126806e8 | -14.82259 | -48.10985 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 817f4a8c-ba0c-32b1-b6c1-e7ec4b1fc5f8 | -13.32682 | -43.1027 | 2025-09-17 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 06c695ce-dbcb-3fc8-be3c-55c123e997f0 | -14.61053 | -46.37945 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 887e4762-b332-3c39-8980-d871fae9afc5 | -12.72928 | -48.02298 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55deba44-0850-3d46-a181-85aea956e957 | -15.42292 | -46.12451 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36f346f6-3c81-3cde-976a-85b11dc65d40 | -11.46564 | -43.55622 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75642bab-ba7d-3372-a8de-c6fcde7ff975 | -11.33174 | -43.4792 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 637d003c-636b-37b3-8076-4c2ddc29a5a4 | -11.50464 | -43.70664 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ae20d81-6df7-3a54-b8df-e2ce84248d18 | -12.74883 | -47.9601 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f48b8eb6-1a41-31c4-8c93-54dc9aa618ff | -14.54287 | -47.42928 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66683ded-e487-318d-8dbf-e1d99579997b | -11.12349 | -45.35395 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6558579c-8043-35c2-908c-8e2a9c1d94fb | -12.86429 | -47.14113 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8708fff4-cf7b-3cf5-a74b-89769a59dadd | -12.9754 | -47.9511 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8380a1cc-b557-30db-9300-10f0bf0ebed2 | -12.97622 | -47.94645 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2f37bfce-1129-3d2d-b956-c0cb6d47bcca | -12.7238 | -48.00725 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a64c8ef-468b-3602-bbd1-4b32df10c07a | -13.28455 | -54.1895 | 2025-09-17 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d9d08ee-76e7-3efb-bb8c-c1586cc862aa | -11.46727 | -43.56749 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05c65587-8a66-3e0e-a7c0-6e9dbb2e5556 | -15.43771 | -47.32206 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03285510-505e-3845-ae92-14304b3e469b | -16.53081 | -43.73768 | 2025-09-17 04:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28d96f0d-be48-301f-ba0f-53281c9e18fb | -15.41943 | -46.12372 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b622e79-dea8-3139-9efb-c796e9982cdd | -14.81385 | -48.1135 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bbcd59f-1f0a-3639-a757-f1e5717a4210 | -11.02502 | -45.05948 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b3d9bc7-77ac-34a1-aeab-b08e73c12e83 | -15.7223 | -39.32112 | 2025-09-17 04:12:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| dc5bdd0d-685f-3fb9-939a-b4ec8f306df8 | -11.59656 | -49.82153 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7be0a487-7b53-355b-98c8-0300b3c8e92a | -11.1369 | -45.33944 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28fa4266-208b-33bd-9258-a7bc5f0eea95 | -12.06699 | -46.55465 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1aee5c2f-6adb-3991-a9ba-5ae13c8ae087 | -12.60319 | -47.98148 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7645cf2-3eb5-3fa2-a5a0-7fda909e0264 | -15.42849 | -46.15388 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7dbb7657-33f8-3a77-8e49-7ba4e9340692 | -13.9548 | -44.91929 | 2025-09-17 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07671cab-6290-3daf-9738-f34c00e2d26e | -12.69955 | -47.76803 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e1fb70a-8abf-3a20-a077-df917f035308 | -16.84863 | -44.07586 | 2025-09-17 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f70fef86-ea00-3a16-aec2-50cf8f1dc9f1 | -12.35735 | -47.06725 | 2025-09-17 04:12:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d22836d-7eb9-39a1-aece-6146dab701ea | -12.94858 | -47.96271 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 031cbe61-db40-3822-ab64-e68fbf156bdc | -12.70803 | -47.97812 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88330b3a-2972-3da6-b4f8-f57a56e1f2ec | -15.414 | -46.15622 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 000d588a-9d61-3725-afef-3695aebca2f3 | -12.72526 | -48.02222 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e87febf-8ce5-3509-898f-865ea59153e9 | -15.21935 | -50.14731 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd5f0ac4-03a4-360d-bd37-8f2ba1f7a4c6 | -14.61417 | -46.40163 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc6a5dba-fd72-338f-a24d-abab23f657c8 | -14.83114 | -51.70973 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d806aee0-9578-3935-8f16-9f5b2f2d658b | -12.96639 | -47.95536 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9692d842-7ea4-3e89-96fc-400f292da18c | -15.40695 | -46.15509 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 382669a6-1f55-387c-b86e-d7873f6700bd | -14.47659 | -46.35746 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README28.md)
