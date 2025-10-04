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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da2ca8e2-293b-301a-b806-7d0865e4f08e | -13.22126 | -47.84057 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b714e01-c29d-3b40-95e8-ddab3fe94cce | -13.33784 | -47.61885 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23a0a6ba-4847-39a2-a4e4-8c02eda8a7e9 | -11.91925 | -46.36562 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6e72726-6f99-38e2-910c-640b41e6e63c | -15.33301 | -47.33379 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01ba5d12-8bd1-37b7-b2bc-d12eba1d5ace | -15.32746 | -46.30215 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f710b6bb-f73f-3dc9-ab31-ca71352022fe | -13.10769 | -47.89786 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b1d46a1-f7f6-35fe-a23f-b714a36c994e | -14.72626 | -48.08051 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34d15730-710e-37d3-b36b-069ce16e58d4 | -12.4022 | -51.08337 | 2025-10-04 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b3f181-fe82-3c84-8a3f-6d3a4b27f4ea | -13.20887 | -47.80579 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0090f868-2fe4-38e4-96ba-8c2b3cdea58b | -11.17008 | -47.75307 | 2025-10-04 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 472088cd-aca2-3f52-b7a4-4e6a486798e0 | -11.82503 | -45.04671 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41564657-8145-3611-b8c3-c98635ac8438 | -11.49525 | -44.98826 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f03f32aa-202f-33c3-a786-784f36d78cc5 | -12.65716 | -46.96972 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52ab1322-afaf-3da4-b794-3239db52285f | -12.27721 | -55.13186 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c794a03-4277-34a2-ad55-7e6b9658d880 | -12.22723 | -43.77386 | 2025-10-04 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28aecf7d-4448-3495-87cd-3b42220fe6d5 | -11.45079 | -49.71363 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db2b1fcb-b5af-3293-9065-dcbd67a5d98d | -12.65673 | -46.97335 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b91ed7a-058f-344b-9430-9700a894285c | -11.92142 | -46.39692 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6682383d-e168-358b-b3c8-ed87aca107b6 | -11.38446 | -54.35168 | 2025-10-04 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1405ee1-34d3-3adc-a2d3-33b2873feebd | -15.2207 | -56.84632 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44d07263-326d-3f51-b926-5d1ffb031db7 | -13.3131 | -47.24303 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5804dfd0-6bbf-3d90-b967-d12df06659dd | -14.88986 | -48.27884 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35158376-f76d-3e66-b18f-45b30e0ef025 | -13.75045 | -48.06002 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a12dab36-cab3-30aa-8fea-65a67a6d1321 | -14.66724 | -48.28714 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a30e520f-e43d-3034-a086-1fe7256eae9e | -15.53019 | -46.80683 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c1fa6d3-8beb-3c5b-8541-c8fea90a925b | -11.86837 | -44.96907 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b45d3abf-ca4f-3ed6-9e1e-505fbece6063 | -13.74842 | -48.05251 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf5bab09-3fc9-3bef-8db8-9fd97d496cb3 | -12.71987 | -48.57029 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21f59c7d-b2c3-3ee5-8a1d-a3c0eda61502 | -11.8844 | -45.00019 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a9274c53-6bee-3e76-ba96-533384231d49 | -11.50084 | -46.74971 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d718e78-a260-3387-8f4c-b0af6d6dfb1e | -12.6444 | -46.97983 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d564828-d7e6-3432-a806-7e7777ddc415 | -13.52452 | -47.27571 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2107e75b-4727-37cd-9530-72baa6fd00b5 | -14.32956 | -45.86409 | 2025-10-04 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94503d47-a821-39ee-b494-46409a85874d | -13.31513 | -47.2458 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f1c5329-3863-33a2-a3e4-398c6c914092 | -15.005 | -56.01889 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea6a73e0-3315-3954-b36c-162f73d44691 | -13.10404 | -47.88268 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3ee4395-61f1-3dec-8174-431a9894cf92 | -13.74125 | -48.09094 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 161f7551-0d0c-3fa4-8f89-8413dc4fec91 | -13.31677 | -47.79678 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79eadddf-42b6-392e-94cb-db1d6ddb50d7 | -10.47343 | -54.63165 | 2025-10-04 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aff3edab-8578-32cb-b8fc-30cca1e1f771 | -14.98377 | -49.97802 | 2025-10-04 05:06:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e9f5d462-a375-30f1-99a0-f02013a68cb9 | -11.87854 | -44.97632 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 820e4818-bcd2-3dbe-813e-2307c0fa7255 | -12.30292 | -55.14755 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc6fe8b1-9aff-35ce-82f0-0d8adcba33a1 | -13.31909 | -47.26063 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 300463c6-a5e7-397a-9d11-ecae88e36350 | -15.98425 | -50.86816 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 949d591d-68fd-33ce-bb0d-7f09ab72c996 | -13.34622 | -47.20402 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8855091b-7460-3a96-ad05-36c815181d8a | -15.3788 | -47.9531 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08afc92c-1568-3268-aa1e-2c019969f8b9 | -15.53302 | -46.8375 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 50357c69-a61a-34ef-8088-f9257064876d | -13.5241 | -47.27922 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a098d192-2337-3976-89b6-dbef19b3c38b | -11.56594 | -47.67253 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b10d488-6f52-3035-ab23-ac3b6fa3ef9a | -14.8939 | -48.38988 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 562ec0d1-06f6-3473-8dbc-5e587a516766 | -11.82568 | -48.06779 | 2025-10-04 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1322b9de-eb7e-30a0-942f-865a6b73fa8a | -14.9225 | -46.87895 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 962d8329-39d0-3c18-8fd0-fe559805c896 | -13.92942 | -48.16535 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91237821-373a-3437-b8e0-41a98f9d0286 | -13.11994 | -47.84201 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 711956e4-3426-3d02-8662-4204081432e4 | -11.10658 | -47.74988 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9a8dfde-5beb-3be0-86e8-0785605bfb44 | -15.1941 | -46.3912 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08dda6ca-a1c2-32d5-9848-b3298a167aeb | -16.03603 | -50.94143 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0cd56e2d-9bb2-32f8-9757-f390f4c7c013 | -12.1973 | -47.77677 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b7f44c2-fe0e-340e-aa4d-5a58f8a17421 | -11.34484 | -55.08539 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c81a23a3-1d6d-3998-9f10-c2f4fb660018 | -13.12184 | -47.93916 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c29272d-bd6e-3143-8466-4fd9742abe26 | -14.67567 | -48.2617 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 548e2960-5cd2-3e0f-b255-b80a39bcaf5d | -13.33778 | -50.95503 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2fdba590-83aa-3a04-9af0-9358a12d5494 | -13.26175 | -47.21183 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edef613d-255c-3f11-bc13-d4b026844c13 | -12.91771 | -54.72939 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2ff8b39-312b-344a-a689-a7cd62c2fbc2 | -10.57097 | -48.69844 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f081b0c7-758a-3eba-bbb7-6eb30f269550 | -11.90788 | -49.93914 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29d67772-a7eb-347d-aa84-55064649328d | -15.60999 | -52.47026 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 111f8a43-0de0-3854-9a93-ef19ef9af82c | -12.39955 | -51.08413 | 2025-10-04 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeb2c5b3-13b8-3983-a706-28f708adddea | -9.92424 | -60.19075 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4daa1e3d-3cce-3a67-b987-37ee55a80a63 | -11.28253 | -47.79424 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63ace737-4b19-356b-bd5d-67ef0ae186e2 | -14.68366 | -48.26601 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f3cdd92-b722-31f7-b443-152ec2388e45 | -11.45253 | -45.13742 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8540d2f7-be72-3436-9be9-4a8b8adb3986 | -11.8896 | -44.99269 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b1241ac2-3b63-360c-b9d4-4d23da7cc2e9 | -11.6895 | -47.49969 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e221bb0-da1a-31b3-a6e1-e0f000105dfa | -11.96711 | -51.4732 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a741796-b55d-3fc1-a14d-8d4bf0a4ebb1 | -9.19956 | -59.40812 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9f9e19b-cdb9-359e-964d-a0935c758a58 | -16.09583 | -51.06603 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 012f19f5-cbf7-3bc7-a865-ac93dcef6c36 | -13.93508 | -48.16349 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7aa75ba9-709c-3761-9e09-b38c2a195e12 | -16.06903 | -50.90069 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20ff79f5-5f72-30de-a51f-d04022a1f232 | -11.06324 | -54.81219 | 2025-10-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63cc6870-835f-3e3d-8a11-6a2642f7e5ea | -16.0245 | -50.84451 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c10d1181-ed0b-37b4-8b81-f98f03210e43 | -12.27132 | -55.12399 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbb9f493-6db7-335e-9f2b-4b098899d288 | -13.25243 | -47.24275 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc71271e-1e75-3f4d-b7bf-bf5e0796b321 | -14.70277 | -48.19236 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e5e6f30-bfbe-3ac3-99f2-86e931e04a15 | -12.92121 | -54.72993 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 142088eb-8338-3d92-b203-8f78c70c498c | -11.89011 | -44.98838 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 78e0f200-553f-3476-a0dd-785a9763fa37 | -12.93797 | -46.43367 | 2025-10-04 05:06:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 986269f0-1034-3a86-8f35-3bd719d99337 | -12.04121 | -45.20402 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef78bdcc-41e2-3ea1-ac7c-ec4abf135800 | -13.11287 | -47.85497 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3bb548ad-2f4a-39e9-ba12-c4a2e648ceb3 | -11.54931 | -47.67454 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19f7a5a9-31ec-3986-9390-0131723500fe | -11.12575 | -47.85021 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ea9c21d-3c95-337a-9478-0d6bbc4aa408 | -14.70521 | -48.19701 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b22ffe2a-8daa-3492-905c-3f19a6cf19e8 | -12.90431 | -54.74773 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86f87a2f-f6c6-3f6b-ada9-b15d36b6b36e | -11.92105 | -46.39357 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9233e4df-b606-351c-b755-aa3d4f4e9af0 | -15.72171 | -46.27842 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85505770-27c0-3c03-8552-78a01f0e6b0c | -14.38895 | -45.94356 | 2025-10-04 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87f00ea2-7abc-39f6-963c-5726f35a8721 | -16.37019 | -49.40653 | 2025-10-04 05:06:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce0fad83-fd0d-334e-9bc5-703c95339fd4 | -10.74029 | -56.59349 | 2025-10-04 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13cbfc44-4dc4-30e2-a84c-11c454c1f4c8 | -13.25601 | -47.26128 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa27c4e3-2491-3cd3-b32c-93c28caefbf9 | -14.70031 | -48.19208 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README120.md)
