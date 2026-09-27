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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3780c2f6-abc7-37d7-b176-f9ec3f555f18 | -12.13529 | -50.33141 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bb4a212-2ad0-3093-adef-d77f691f6eca | -11.85345 | -50.52509 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 113341e1-10c7-37f5-acfb-e8cb14d82ce4 | -9.6142 | -55.10687 | 2026-09-27 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfa1a42d-0e82-3d4b-a1a2-4ee4e4eec0fe | -11.02347 | -54.04356 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 781981fc-c902-334f-9ae2-787009105900 | -12.24958 | -50.70621 | 2026-09-27 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b1f9fa5-bac3-3e51-9bff-483a0fc979df | -10.03995 | -62.45789 | 2026-09-27 05:29:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ce37688-833e-359d-ab5a-3aba18fd2615 | -10.01955 | -50.1459 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e72e69e-5bc0-30ef-9bbe-d14a351ba5b3 | -9.61813 | -55.10744 | 2026-09-27 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e012996-f95e-31db-8aa7-caf7aae1c501 | -10.01862 | -50.15205 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10219292-8c7f-39d7-8948-371ca2f0b0d3 | -12.29094 | -50.27887 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 15959962-614a-3111-8b91-8bdfa86fae43 | -12.28585 | -50.36715 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e55cf3e-5e13-3d6d-a36f-a9e1745e1d85 | -11.94121 | -50.4948 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4ca9ea1a-1b26-3283-a4af-c78f470579e4 | -11.85577 | -50.55118 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af393a9b-047b-31cf-863c-301bcd2a7dd1 | -12.02153 | -50.60915 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c70d562f-05da-39fc-a21f-38e9bdc0e02a | -12.29187 | -50.2712 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7da31c06-4a06-3831-9391-68e7ab9cf496 | -12.47599 | -47.4799 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e62be98-73f4-355a-a5e1-e9bc8b88093a | -10.01771 | -50.15929 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f62cbae5-f354-333c-885a-1d2083334f8a | -12.47146 | -47.48549 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50ad6597-8445-3a1c-832d-7e5f376cfb7e | -12.02197 | -50.60556 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cd952d6c-aee4-33fd-8bfc-dfcb8d81ab99 | -6.89136 | -59.84363 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97001e33-4204-3b0b-8b12-d9a11501d49b | -12.29141 | -50.27504 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d6e1a850-731d-31f4-8832-6e6c35bdb1da | -11.8841 | -50.50214 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2fde488e-2d39-3a07-a6c3-bf42c6659aeb | -12.13913 | -50.33072 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94a74860-3d75-3e28-93f5-f08885740e50 | -10.01639 | -52.09613 | 2026-09-27 05:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93a8eef3-4379-3103-89e3-6b0e8053ab11 | -11.96385 | -50.53858 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d39e5b47-a876-3c49-b498-1cea383e7162 | -11.94076 | -50.49845 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b52826a8-7859-389f-842b-2726ecd9c050 | -12.71117 | -47.31764 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 67e5cf9d-f8f7-3355-bf8c-3071ad4a2575 | -12.2778 | -50.29272 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 44e75950-6a3d-35ba-913b-5825fc451de7 | -10.64875 | -58.77219 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63aba8ad-f722-3f76-94e3-03187091a486 | -9.35823 | -65.75182 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0da54ba-3883-3d84-b925-0ff8a0acf338 | -11.89853 | -50.5236 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dab0acd-0346-341e-a10f-358b442cbcd2 | -13.09805 | -47.41665 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a58270bc-980b-38b5-958d-15b40a654459 | -10.01817 | -50.15566 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 124ff6b9-7c08-3056-8ce7-ac4cc3457d6f | -11.98424 | -57.60668 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ece8f7aa-6621-35cf-bedf-6d47f1e9c988 | -6.87142 | -59.86944 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef18ed8f-0d52-3eb3-bf54-4de2c535de66 | -10.31411 | -54.26828 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c0c390-bdaa-3ce2-babe-3348e53b6516 | -10.21949 | -49.98165 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df86d2ee-786c-3c19-8b56-d06b1e36df4e | -13.87814 | -49.03694 | 2026-09-27 05:29:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ac5c7b0-026c-3294-9ef6-ad9cfec3d88d | -8.6305 | -54.66862 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d201a27-197a-3cf3-9da7-ce6f17163f27 | -6.85012 | -59.9167 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ceee2c69-763f-30cd-b73f-de59d94b1fd7 | -11.274 | -54.43615 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2955dddc-cadf-3735-bcb6-aaa0e9636965 | -12.47212 | -47.47942 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 715a61ab-1585-3d3d-a7b0-a2b25ccffeec | -11.88335 | -50.51056 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d6f97132-a069-3a85-9f6b-98a722053e44 | -11.88981 | -50.50399 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76718fc2-e2f5-39f0-bda3-5564c0efccff | -11.88289 | -50.51419 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f84a41aa-50ca-3de9-9991-4b1afb89d8cd | -11.051 | -54.19117 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 864b6c38-216f-32e6-b8fd-6e71fc743e22 | -12.20783 | -50.37419 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbc61147-8754-3d0f-9c96-beb03341e7c0 | -10.6775 | -57.6307 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f04450a-9202-38c9-9aaf-d224c3dda584 | -11.27454 | -54.43224 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 464888cb-73f2-3f3e-b47c-c564b6cf5e44 | -12.03521 | -50.58894 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 1f65b7be-7679-3828-9109-6e4fe709d5ea | -10.67133 | -57.55384 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0199e077-a972-3ff8-9333-db646124f015 | -11.88934 | -50.50763 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8aa9a5ec-87f1-34e7-808a-1b99c7da9a5a | -11.81706 | -50.50182 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a6714bc9-7dfb-36b9-96b4-4393ce6f3794 | -11.87736 | -50.51347 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 478a3378-44af-3c8c-b918-53120db36560 | -9.10379 | -54.69064 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb932094-f41c-3d90-842d-02e45fa4113e | -11.91639 | -50.51384 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 131335cf-3795-3952-992c-9eb0c14236cb | -10.78917 | -48.72725 | 2026-09-27 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b9681c5-6d17-300f-860f-7bc783cd4033 | -12.30081 | -50.29184 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56ac7dc6-f494-3230-aff4-850b251b1c3f | -7.50021 | -55.02335 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9c9a433-5363-39d6-80b4-2c5c7c392d1d | -12.28436 | -50.2858 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8043d264-64b8-3e94-b2b3-0048dcb89a48 | -13.72193 | -48.81174 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 392a3004-480b-3090-80ce-e4e161bbab3e | -11.24335 | -49.84899 | 2026-09-27 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd84c441-a33f-30fb-8cae-78e2aae7466d | -12.1279 | -50.29967 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 286cc387-dc68-3a4f-8f5f-3c70abb20855 | -13.37668 | -51.31917 | 2026-09-27 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee250943-24b8-3537-8b02-51befe5a8244 | -11.01862 | -54.04708 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1ae87879-952e-379b-9cd8-50493694221e | -11.03695 | -54.04111 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6990597a-285f-3e8b-a70d-caab5546a7d4 | -10.04061 | -62.4539 | 2026-09-27 05:29:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca1b8ee4-d11a-3e81-9895-d010a2c706e8 | -11.92924 | -50.50068 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6dffaa1-c0ab-3f16-acb7-745f0a25e042 | -12.58843 | -51.95207 | 2026-09-27 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80d86aee-22f9-380e-99b0-76b4f73da148 | -11.97031 | -50.57625 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c41160b8-1135-34a1-bb07-b95b41f38a66 | -11.81109 | -50.50473 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3d4e19a5-b633-30bd-b0e7-1f1babee4731 | -12.29987 | -50.29948 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0fc1fa43-f332-337f-b009-f1fe4ff2f4fb | -8.62974 | -54.67377 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 068fa6af-cda5-3f86-8cbd-5776230e3513 | -10.78971 | -48.72285 | 2026-09-27 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 478eba06-9bc9-3ccf-ac5d-434bd096f140 | -13.88181 | -49.03864 | 2026-09-27 05:29:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6913ff0-8098-344a-9f05-109a5c5da7ea | -13.37708 | -51.31578 | 2026-09-27 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4adcbcbe-1588-3bf3-85c9-f749c99eef0e | -6.8636 | -59.87543 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1939f78-6074-331c-80fe-e47e30392975 | -11.98778 | -57.60721 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25b634ee-b355-3841-9b30-5b3ac09a5d3c | -12.27931 | -50.37399 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 394f9ef9-324f-3a0d-9086-14afa6d5d901 | -12.71276 | -47.31762 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aa54230-c708-32bd-bfb1-bcba12546d99 | -11.89806 | -50.52724 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de0604c3-2120-38d2-8580-6c92fca08605 | -12.27124 | -50.29963 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8cde800f-32a3-39db-a9aa-adbeef4fcad7 | -11.09158 | -60.7229 | 2026-09-27 05:29:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 478b1ce5-4697-329f-8ec8-597f38267506 | -11.77159 | -51.0005 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0bd7f9d-e0f7-32d9-a53a-8b789d73cd20 | -11.05067 | -51.32086 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18cc91e5-f5ba-3259-8f3a-f8aa91adb5ca | -11.04951 | -51.32373 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b206ba8-f6b1-3265-8983-9d575d8f2900 | -11.94873 | -50.56975 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bffbc7bf-a0f1-349b-a4af-134e85d18783 | -10.39634 | -61.23609 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7a85e64-c039-3c28-935d-d10918994242 | -12.29047 | -50.2827 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c52171e9-f4ef-324e-9ed6-aa872abe1da6 | -11.77116 | -51.00385 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f9977f8-08c5-3188-93b9-16b2f242ce33 | -12.25595 | -50.69977 | 2026-09-27 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24323937-80dd-33b1-a53a-41bad2b238f5 | -9.57011 | -62.70904 | 2026-09-27 05:29:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1658c5ab-a7a9-33e5-ab6f-6024218c0184 | -10.81985 | -60.73301 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 954a61c3-4d06-308d-a7a3-b06e2920e481 | -10.01907 | -50.14951 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1475ccb-4630-35cb-9602-abbf8e37f750 | -10.60912 | -54.00196 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 925234eb-c929-3216-9713-be25dd7c9773 | -10.1086 | -50.19366 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57de2323-1460-36c9-a582-a72f1cc269f7 | -11.15972 | -62.86698 | 2026-09-27 05:29:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| da1858a5-362e-3965-a083-2f81265b7b86 | -7.39281 | -55.63342 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e03f08-aefa-3423-a072-e86c700ae1b5 | -6.86751 | -59.87243 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 464efc7e-4fb8-3f61-8aa7-84feafd5f178 | -10.29543 | -59.46319 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README47.md)
