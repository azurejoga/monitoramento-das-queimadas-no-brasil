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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c23f626-0f62-3d8e-a9ca-d190ac40f1c0 | -11.59515 | -54.67126 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b2544e4-9bcc-36f7-8556-7d1554b80666 | -8.95847 | -60.50891 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c061f995-f4a8-3395-98b0-fd6fe7ad4362 | -11.58583 | -54.66982 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f14f4981-f023-3f26-bae7-737380f5b3ec | -14.42488 | -51.90908 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 68153043-7ff0-3bb8-95e7-4cb5c5685916 | -8.98186 | -60.5343 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5767baa0-8ea4-3776-abae-814ee2d81095 | -14.41367 | -51.90339 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2989475-7df6-3f60-9f08-09bb67659a00 | -8.96126 | -60.51297 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84924b14-f8a9-38a2-8ec8-903d561521ee | -10.41797 | -47.97993 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b0f15485-b39d-3f78-8bc8-3592620e6961 | -8.89666 | -60.56063 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb5a63ef-4a25-32d4-b804-5d9dfa2fc8a6 | -14.7261 | -52.88725 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e178ef1-9488-36a7-8440-6bd4fe3cbe19 | -13.75714 | -53.42289 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6945dc9-e284-3764-81eb-26fba7533a09 | -8.96515 | -60.50997 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f05c432-7291-3c7c-95b8-7c97eb436be2 | -8.89999 | -60.56116 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc8957f0-41e0-3d2b-9ede-73415eb99963 | -13.27166 | -54.19329 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a30eeca8-ef01-340a-b5cf-ff375c433ecc | -8.64856 | -54.69622 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b346a5f-f28f-3b36-8248-466669597876 | -14.32112 | -53.06026 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0459dba9-cb8b-3bb3-b72f-81ed1d0f2d57 | -13.75638 | -53.42911 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cd2a856-0c95-3560-95fe-9c316a1bd865 | -10.41313 | -47.98129 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8a25080c-d962-32de-b5b3-8e318c3db3dd | -13.26495 | -54.19563 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b247f1e-18d2-309b-91d4-09d6c1e6e673 | -11.98837 | -53.45424 | 2026-08-15 05:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ccd4a61-41d3-309f-b66f-35fd9eda4ea5 | -10.40607 | -47.98038 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8070e86b-f00c-3589-9e17-a7e53d5aa3e8 | -11.58784 | -54.69015 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99efbf8c-52df-3f03-a094-11d5b360f7cf | -14.43025 | -51.91402 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 66bf8368-014a-3145-9963-4327b828098b | -14.43214 | -51.89713 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ac26cde9-f338-3fe1-ada1-07f5d735a6c5 | -14.44587 | -51.933 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e31d59bb-8cdf-3464-a850-1fc7534faf08 | -13.23184 | -54.17942 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e948c2b9-76f6-3198-b20b-c9bd432a1015 | -14.42395 | -51.91748 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 576b0295-0bce-35fd-af9d-1b971ed756af | -13.25013 | -54.19361 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df8b07f2-a5fb-3b58-b1f7-0023b150f1ed | -13.28156 | -54.19458 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da9c0a1c-9f0e-36d6-b957-565a3d9d2957 | -14.43798 | -51.89786 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7618e543-7125-3f7f-b0e6-469d83fa31b8 | -14.49297 | -52.03606 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f61ce26-61ac-3d92-a4eb-abccfd025ad8 | -15.15484 | -50.06739 | 2026-08-15 05:36:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4e1d731-4c27-3859-b32f-7ab1b0a432e9 | -7.5871 | -61.22779 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21e7ae08-95c6-3d4c-be73-a20a613bc497 | -8.60279 | -54.68263 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77d329e6-534e-3110-91f5-970485a36b5d | -9.98208 | -53.94969 | 2026-08-15 05:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b47b4eaa-c787-3b74-867a-fa09d2866ce1 | -7.58323 | -61.23074 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41f2d66b-e5d8-3bf0-8a15-0de07a314031 | -13.44622 | -57.04181 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6fa6b0ce-6d67-3cc9-b0c0-b6afda964cf3 | -13.75114 | -53.42837 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05684f23-5bed-3e44-afa4-b3d3faf9c248 | -7.58932 | -61.23528 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72da14dd-112b-38cc-abd0-9a1adccd464a | -11.50691 | -54.61848 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0913a55f-c7af-3716-8eb2-180470c67a89 | -14.43072 | -51.90981 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| e1930c38-0c3d-3931-8578-7e067425634b | -14.45265 | -51.92535 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09f203ff-40b6-3506-8643-cf8b60b3e8fd | -13.80729 | -53.79758 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d93ba89-d37b-3f99-bc4a-57691ac1bb3e | -7.59264 | -61.23582 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 4f8a6e09-1634-3c49-a29a-464c5e54aff9 | -14.45456 | -51.90845 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12d6fd74-a378-3177-8a8c-2380c693d6a8 | -13.42132 | -57.05043 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ce6d49a-49a4-3117-9315-ad4475f108d0 | -11.50627 | -54.62346 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1035f8e5-5e6b-38db-bc0f-ce5840c99dce | -11.49804 | -54.631 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6e7ffa2-9781-3883-8f2f-8ddebba58d2f | -11.49939 | -54.62109 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6a27538-98ec-39db-a28c-f37ea937bb6d | -8.61026 | -54.67678 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e8176e9-4e29-3860-8489-815ce20c55ab | -14.48916 | -53.09001 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8af4384-c570-3701-a0ed-f1cb7412a10a | -14.30449 | -53.06157 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 180609be-3721-3b47-9a0b-136861908b2a | -8.60852 | -54.67449 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1faf8fa-d058-3bd4-bc1f-1805cc489b9a | -9.97729 | -53.94901 | 2026-08-15 05:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6fa18630-2b47-3cd2-b00f-896aaaa4a54f | -11.50408 | -54.62168 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e02dff5-45b8-35da-a4f4-5abea8992050 | -14.4203 | -51.90261 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 113ad7a3-dd3f-340e-b001-dbc949e04b71 | -8.89721 | -60.55711 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5bbafb61-a864-36a5-b677-eb9b22a7fc48 | -12.35271 | -51.21402 | 2026-08-15 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d50049b-cac2-3d3a-92e6-92b932ce5b86 | -11.49871 | -54.62606 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6af22cf-9963-3ce0-b9ed-09fa60877aa6 | -7.586 | -61.23475 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 430c4e4a-12e9-3a72-8ae0-08f48ef81a88 | -11.49069 | -54.61493 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce188453-75b0-3028-87a0-94e2a526f328 | -8.95796 | -60.53411 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74e71c60-b713-320d-bea5-01918ffc3c95 | -11.50475 | -54.61671 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0cc0dd1-1784-32c9-95d3-81e56321bca1 | -10.71801 | -50.55709 | 2026-08-15 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47255786-61af-3767-b867-99a769323e12 | -10.41394 | -47.97453 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ec76f9bd-388a-35e2-8c30-6baf69bcc56e | -9.58619 | -60.50276 | 2026-08-15 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3fb7a96-8443-3c2b-8d75-673600cef36c | -12.69895 | -48.45677 | 2026-08-15 05:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6ca5f4b-7013-38b8-8c68-6ef8b75d64be | -11.59049 | -54.67054 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfe65a2b-f98c-3168-a53c-c1cd30051125 | -13.44212 | -57.04128 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ff3822c7-94c9-3bb8-ac93-644fdd1e68ae | -11.23374 | -54.82691 | 2026-08-15 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66f44309-c2f6-3a20-8634-668b5c4301a7 | -10.41874 | -47.97307 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ff9c0fb8-1c38-33bd-b32f-19ba96987677 | -8.26408 | -57.34375 | 2026-08-15 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cefcdec1-c4b8-3afe-bc6e-31978eb4cc12 | -14.45313 | -51.92112 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a575a0-2237-3056-a477-6f6f852ea040 | -8.60469 | -54.66946 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfecb80a-7721-39df-8778-9bbc010e7ecc | -14.13475 | -53.68187 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52abab2f-020c-352f-9443-7cbfa491f831 | -9.58229 | -60.50578 | 2026-08-15 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df5c16a5-a9b8-3323-b72a-4b042556a975 | -11.5084 | -54.64381 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1eced58-a825-333d-90df-e396a385805b | -14.43609 | -51.91475 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0a84d535-fba3-3926-b8b5-d1e08985f463 | -9.07971 | -61.39623 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c02184ba-7516-3c39-b55d-3db7229d957e | -8.95462 | -60.53358 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 647a27c7-b3c3-39f7-9044-9cec638a4ec8 | -7.58877 | -61.23876 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bfa2244-9ab9-3b5c-91f6-3065c35d842e | -13.42488 | -57.05473 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab0576ea-cf8d-3f51-8442-7cfbd778f086 | -8.94971 | -60.58692 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09b04ba6-42cf-321b-9840-e41a4a51448e | -14.43734 | -51.85054 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86cd8a2c-b750-35b5-9de4-b54fe6fe6fbe | -13.42234 | -57.0431 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3d40c41-1ca8-3c5d-b7d4-8bea809fe3dd | -14.44288 | -51.90704 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3d360425-4e03-3ece-9f29-8df01181bfa8 | -8.9657 | -60.50644 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd944d18-8568-3cb3-b3ce-f063dbeea259 | -7.58489 | -61.2203 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 321becab-c403-36e9-8a5a-2384c486664f | -8.65178 | -54.70575 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 168a20a3-8168-3f61-b9f4-526899989c09 | -14.08864 | -54.52149 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5aa0402-e94a-3ac4-a8a0-53e6727e0a9c | -14.72012 | -52.89058 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3769f003-2ba8-32fd-875b-6b5f73e2ddc2 | -13.91475 | -53.95303 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a3be1f8-b69c-3230-93dd-fd56cae2024a | -14.4193 | -51.91103 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 51679d7c-744e-30fc-b0d7-a1949ab1804b | -10.39901 | -47.97948 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f2d84b6-3d51-35f6-9a66-b66c210a72bc | -8.89332 | -60.56009 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c891ec5a-8bba-3c75-988d-6b7250663672 | -8.65115 | -54.71023 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fd34a92-a37d-30e7-b74e-6771b65bb322 | -13.81914 | -53.7858 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dc8dcb6-6030-34a6-b2f8-5b55ec315e63 | -12.13694 | -57.22359 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da07acf6-20bd-32c6-ab25-fdf4ca869ee1 | -14.4188 | -51.91522 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 114b9835-2a27-3765-afa0-0fe5a8813549 | -8.95792 | -60.51244 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README42.md)
