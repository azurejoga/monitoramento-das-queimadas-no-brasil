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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70fe2cfe-fd18-3592-ac68-570e1a984c18 | -17.18816 | -56.35807 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 77db0017-641e-37bf-bb52-9ea6ec0c1342 | -20.58247 | -57.08826 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a58aeaa-7934-3ecf-a478-dfb053b0673d | -20.99251 | -50.47104 | 2025-09-26 04:46:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38ecdea5-fcbe-3184-94cd-3586b3024817 | -17.58606 | -51.81821 | 2025-09-26 04:46:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c66c6908-c57d-3173-b109-befce08794cf | -22.35886 | -49.47166 | 2025-09-26 04:46:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d7ed4a4-6641-30d5-91fe-7160c4b9a3f8 | -20.77058 | -57.876 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 90fc80c0-4ce0-3631-a148-b29c5bd1441c | -20.53691 | -57.07893 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a43bcf19-608b-39c2-8b42-e9203b74ee69 | -17.59485 | -52.4902 | 2025-09-26 04:46:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d3c3543-850d-30e4-8c99-a469b0550f8d | -20.99834 | -50.00337 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c127df4b-c5a3-3947-a744-baf0bae203f9 | -18.30398 | -57.10001 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 97da5981-a90f-3135-9247-5617156d2e00 | -20.58626 | -57.08905 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebc50844-d8d6-3bfa-9891-9e67db3d8980 | -21.02957 | -51.13286 | 2025-09-26 04:46:00 | NPP-375D | GUARAÇAÍ | SÃO PAULO | Brasil | 3517802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 1ab49b47-e084-33c6-b9be-098948cb0008 | -21.84266 | -50.57747 | 2025-09-26 04:46:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 14b25e3b-e262-3ceb-b40d-c6cb41605f51 | -19.5136 | -50.60334 | 2025-09-26 04:46:00 | NPP-375D | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b4e5a689-8865-3f22-b7c8-46f2976c617b | -18.29514 | -57.10367 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6ee8849a-ab6c-334d-879e-f84e7756ead2 | -22.25769 | -49.9412 | 2025-09-26 04:46:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 379d4df1-2ea3-35d8-aa36-5a6de020fad4 | -21.00188 | -50.02983 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 56cf2c61-2842-35f4-abd9-02e8c3560ac2 | -20.98843 | -50.47458 | 2025-09-26 04:46:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ca53a8ec-dc10-3b1a-9f97-034e0cdc0957 | -21.04272 | -51.11503 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f557a172-46f3-3eb2-85bf-759b25edb224 | -20.75466 | -57.89504 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d85e89b0-b871-3ad7-8d0a-1d873ad3cda8 | -17.8197 | -51.96905 | 2025-09-26 04:46:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 915f47cf-958d-355f-bc8d-8dd597b706f0 | -22.40593 | -49.63758 | 2025-09-26 04:46:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 939e7396-10aa-3083-9d79-e1f004fd55a6 | -18.18265 | -53.32752 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9abbbd5-a931-3491-a72c-eff4f694ce87 | -20.99714 | -50.01183 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 961a4518-2110-3c0f-875c-e886525a53ff | -20.60868 | -56.7327 | 2025-09-26 04:46:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2ba5781-2782-3a6d-9d34-4eb4afb89dcb | -18.69397 | -52.01484 | 2025-09-26 04:46:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd3a7c6a-ebbb-3cf2-9270-156b947732bb | -18.18476 | -53.3357 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22927bf1-e8bd-3038-a29b-0fdc8864452b | -20.75568 | -57.88964 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0368324d-65e8-3537-8cc2-379cc17ecfd1 | -20.7845 | -56.91648 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a0bbc06-baf2-3a01-abd4-a1ea3399533e | -18.18538 | -53.33192 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4259d681-6a61-3118-a043-d19439a67bee | -18.18202 | -53.33131 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d776aced-f9bd-3bca-aed8-61d997c5f1a4 | -21.04214 | -51.11895 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e6315b22-c9f0-341c-b4e3-da98a71c1425 | -20.99655 | -50.01603 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dfac26dd-6251-3401-9799-ad3c352fba84 | -21.03814 | -51.12229 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| a459aa13-f657-3aa9-aa12-78b42c63e9bf | -18.5474 | -46.9637 | 2025-09-26 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 740330a7-a5d1-3593-b869-cc7b765af481 | -19.92449 | -43.62421 | 2025-09-26 04:46:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a257c037-facd-35cd-8946-1d09c047b8e9 | -20.61155 | -56.73815 | 2025-09-26 04:46:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a36f812d-5550-342e-80ff-47286cb3f955 | -19.74801 | -48.1523 | 2025-09-26 04:46:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 36d267b3-25e2-3757-b141-5a32c74f80b0 | -18.18079 | -53.33884 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7cfb7a1-eaab-30cd-b0b9-d5c084b80036 | -18.60086 | -51.91672 | 2025-09-26 04:46:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1114abf7-a882-3376-9e79-de2d90bfadbb | -20.99358 | -50.01125 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 70b0f341-1b79-3264-b312-86dbf6c0afd2 | -20.56562 | -47.17894 | 2025-09-26 04:46:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6b459ec-38ee-30e1-8835-12a5d4831e11 | -22.41183 | -50.64188 | 2025-09-26 04:46:00 | NPP-375D | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 45cac9b9-8b0a-31a8-aa27-25504e5f49aa | -20.7507 | -57.89421 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| bcc3875e-45be-3bb5-a763-8389ad9d41c8 | -20.99062 | -50.00642 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| af07aac1-c898-3382-9b9c-3aba364b21cc | -21.00544 | -50.03041 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ff5945c-fd62-3d90-838a-432a9a69925e | -21.03357 | -51.12952 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c7e02ee7-3ab9-327c-8c85-9bd76fca3511 | -21.00664 | -50.02192 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8da9b421-e309-3d5f-8b8d-1709a5758d12 | -17.18729 | -56.36301 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e139bbe8-1580-3e86-a6c3-3defcf886eaf | -17.19454 | -56.37217 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 875c097d-73df-3f84-9d46-84fa5b57a763 | -20.99193 | -50.47513 | 2025-09-26 04:46:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 632d5243-5a8e-3550-b440-6da371981688 | -17.5453 | -52.01228 | 2025-09-26 04:46:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc4e5a24-9af0-3b7a-8368-23c490892bd7 | -18.47054 | -50.38322 | 2025-09-26 04:46:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d5958623-210e-3f02-992e-adf67a28d725 | -21.01376 | -50.02312 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6aecc156-15f7-3d3c-bb63-68f599902ac6 | -20.99595 | -50.02023 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8a2817b-7236-3ce2-9fd6-d845a2397090 | -29.47534 | -56.33696 | 2025-09-26 04:46:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 32f75393-e3e3-3249-b63d-abff6d7fc0e9 | -18.47456 | -50.37989 | 2025-09-26 04:46:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 13d00ec9-36cd-370a-ab55-72a273c13ddb | -17.54587 | -52.00865 | 2025-09-26 04:46:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2585f81-5b2e-3f9e-a9da-f7b7e4f0118b | -21.03872 | -51.11837 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 402d4d2a-da22-3f5d-bc23-a9eb06002ce6 | -21.66202 | -46.06515 | 2025-09-26 04:46:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ffefdac1-fd35-3642-92e8-e545b56edf85 | -20.42825 | -43.36344 | 2025-09-26 04:46:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0f740791-9d8c-36f9-999a-9b10792f29b8 | -17.18393 | -56.36498 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c462be77-4167-3ab5-a4b8-a7953bcc368a | -17.94204 | -55.86451 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 199b3fc2-9439-3de7-8097-53d7b840375b | -20.60782 | -56.73742 | 2025-09-26 04:46:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 505b9ec7-38eb-3663-9419-2f351aec2bbf | -22.2006 | -54.84018 | 2025-09-26 04:46:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e36c68d-75d8-3bc0-97c2-aab5b4052d78 | -17.18303 | -56.36992 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2bb4225e-7e7e-39b3-9f26-a5ba82bd468b | -17.19929 | -56.36799 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 396887af-2800-32ec-bec8-c505c9972582 | -17.93958 | -55.8782 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 96b975cc-b560-3c9f-8b55-33e19742434d | -21.00191 | -50.00392 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 54ad2511-7ba9-303a-9b77-8cc0fa38eaf5 | -21.03014 | -51.12894 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 85e8bd2d-e59f-3ec0-bb78-60aa25f9d5d5 | -20.53529 | -57.0767 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4ae5299-900c-3fb8-9ea7-2cb6248cf8a7 | -19.03745 | -46.60157 | 2025-09-26 04:46:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06eed5e0-98e7-30dc-b298-ec713d863173 | -22.13621 | -50.01452 | 2025-09-26 04:46:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0ce34d04-b7f1-301e-8216-4a248c98e6f8 | -30.389 | -54.25078 | 2025-09-26 04:46:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 3d536619-38bf-3241-83a0-35829f2fc93a | -20.53782 | -57.07401 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8542b436-5362-3ce1-9c98-c98f7fd8caaf | -17.58549 | -51.82183 | 2025-09-26 04:46:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4085d84-dcd7-390c-955f-085f821c12d9 | -17.94492 | -55.86979 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 15ddf02d-889b-37dc-889f-20f54a9813c8 | -21.03414 | -51.12562 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 4abf43a5-9251-3e4e-a7cf-396fa7c48fb7 | -22.40654 | -49.63302 | 2025-09-26 04:46:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| eb290f53-92dc-3c57-8e3f-69497cdcace6 | -21.0096 | -50.02678 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8c42fdda-acb5-3bd7-b45b-6bf73cd60280 | -18.18415 | -53.33945 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 033e7468-fe77-3c75-8a4c-4001dc1573a4 | -20.42259 | -43.36628 | 2025-09-26 04:46:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ce513e18-5a1e-303a-b2b9-ac3d5a06061d | -20.75172 | -57.88881 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| efce9e0e-15a3-3e22-8f66-6151692d4bc2 | -18.29908 | -57.10446 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 841be9b5-5683-333f-9501-87404d5d14d7 | -20.99002 | -50.01065 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bab1140a-d03d-3548-9e20-62a68235e9b9 | -17.192 | -56.35882 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 86f34ac7-9676-366d-9aab-10d9e56f48c0 | -20.83776 | -54.80725 | 2025-09-26 04:46:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6bcfa89-bc37-3f81-a31b-1c3ae0f44502 | -18.29611 | -57.09841 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dc62c125-8e52-3589-bee6-3d82a718b315 | -21.83915 | -50.57688 | 2025-09-26 04:46:00 | NPP-375D | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe60dcda-dcec-31bc-bef1-ced01e5f5cb2 | -20.42298 | -43.36252 | 2025-09-26 04:46:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8db5bd00-cab7-3e08-92e5-ecc84ef134de | -18.1814 | -53.33509 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f31bc57-44c2-34a1-94c7-4726a5d99fbb | -20.42783 | -43.36742 | 2025-09-26 04:46:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 25336ebf-38f3-3983-a100-8bb0597ea410 | -18.30301 | -57.10526 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7a017a16-9324-3ec9-a6f1-efe2af0b04fb | -17.93341 | -55.84867 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 16437502-bf64-33be-8500-962108ffaab8 | -21.00071 | -50.01238 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 506d080e-3dff-3d6b-ab91-7dffb345793b | -20.55162 | -57.1486 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9b0fa1d-c605-3f8a-b7f8-1c67e2553c16 | -21.66254 | -46.06055 | 2025-09-26 04:46:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9a1ed12-4140-39d6-a791-402cf99873b4 | -21.03187 | -51.11723 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 371d44d6-0f8f-3faf-af2f-a60cf5d8dda1 | -19.0203 | -51.41139 | 2025-09-26 04:46:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a463b48c-f2d2-385a-beaa-6745256ad96d | -20.97816 | -50.0173 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README39.md)
