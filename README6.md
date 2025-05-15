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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc2a2ffd-515a-32bb-a8f9-7d704f728e1f | -11.66292 | -54.95278 | 2025-05-15 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96a5e2b3-12b2-3d4c-8ec4-0e1ee4747831 | -14.00781 | -53.00515 | 2025-05-15 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3bfeba9-1ae8-3ddd-b75f-594d13f0dac0 | -12.10789 | -44.74933 | 2025-05-15 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63072e29-8dcc-341f-9e45-3e8acdbb1fe6 | -13.27413 | -45.4331 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc2ee1fb-d03b-3f89-aa00-50ddc3eeedc3 | -11.91198 | -54.4081 | 2025-05-15 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02d7adc8-c996-3faa-8715-5e1dc4f686a4 | -10.34884 | -47.97854 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 115470ab-a9a3-33ac-b5f1-69d2bce0f313 | -13.28165 | -45.43023 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c6b4424-a2f4-3a43-be45-d494b29f878d | -11.78363 | -47.35983 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14b9c4e4-e666-3e71-8a68-e1f27dc74e93 | -10.35329 | -47.972 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34a5b554-479d-30c8-bd9a-42f1712a0838 | -15.26559 | -51.46809 | 2025-05-15 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 314f6bfb-6a45-3091-a65d-23649d2176fb | -10.35661 | -47.97253 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ca17b07-434a-3062-9012-2b836ee11503 | -13.28918 | -45.45146 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f12d608-02d5-3df0-ad00-565c9c2ea8c8 | -10.13037 | -47.09649 | 2025-05-15 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46a195a7-24b4-3ac3-a5a4-e68617d4f7ec | -11.78473 | -47.35283 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28e81a27-2573-38bf-95d9-fe4bbd2bc749 | -13.07708 | -47.81052 | 2025-05-15 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 309bba21-90a7-337f-8ca2-acf5d9308cb5 | -11.51597 | -57.73069 | 2025-05-15 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aecb107-da0e-3732-b0f8-a6e811f122c4 | -14.64448 | -45.10753 | 2025-05-15 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 927915d5-762d-30b4-9726-ff0f0e65eb4a | -13.2747 | -45.42918 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 148beca2-8e5c-3932-814a-cae50c8b65a6 | -13.04704 | -53.71872 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 31096bfc-bed6-3838-bb35-323adbc55633 | -12.14723 | -48.01213 | 2025-05-15 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3fd69f9f-6980-3ff4-bc23-0dc56c576546 | -17.80559 | -44.36026 | 2025-05-15 04:27:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab3244cc-b041-3a05-acd0-79a60c645ee5 | -12.37376 | -47.32536 | 2025-05-15 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4eb59328-baff-315f-a321-5b19d3fbd1af | -13.2718 | -45.42472 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 165c4d89-4eed-3a62-be36-89b6afcb063e | -16.03336 | -43.67824 | 2025-05-15 04:27:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b669ceb-b683-3143-a05a-86a73596e85d | -13.07653 | -47.81404 | 2025-05-15 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0567fbf-85ab-3ca2-bc47-f1d7c74fb432 | -11.78088 | -47.3558 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5caab70-2422-3693-a768-f7a3ae689365 | -11.63108 | -48.47621 | 2025-05-15 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ac5a4c2-cdb0-367f-bcb2-c6db551e7174 | -11.56706 | -47.43934 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9e6b2a89-d979-3574-a5b5-93bae38577c5 | -13.04775 | -53.71473 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e2728ea-ab09-3f56-8b61-ca0e791c2882 | -10.45229 | -49.07513 | 2025-05-15 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 102fbe48-51e9-37d6-bab1-ca247278ff10 | -10.4956 | -46.18904 | 2025-05-15 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9db9a752-4138-3113-a35e-2b69dc7ad38e | -10.71027 | -49.4119 | 2025-05-15 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c6c9c11-25f2-35b7-8e19-392f71739b06 | -10.35718 | -47.96899 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f134607-a2a7-3df5-a507-24b5c987c9fe | -13.21999 | -49.86438 | 2025-05-15 04:27:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b3f75d5-c75b-342e-b5b3-1129175f06f8 | -10.3422 | -47.97748 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cbf8c1a-e84f-3a51-8f43-2b8111f9aa9b | -11.63165 | -48.47264 | 2025-05-15 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c8463c9-f555-3d26-82b1-ff3684cf8fb7 | -11.55727 | -47.60987 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca876395-8417-3971-8b81-0fec8dafe5fc | -12.72736 | -54.96841 | 2025-05-15 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17df8063-f62d-3aa8-9923-3ffeb0285f5d | -13.2776 | -45.43364 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7273c524-1fa8-36d5-b690-e76a2e665ce1 | -10.33614 | -47.97239 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f3aa6e1-7049-30d7-b137-4010a68c6f17 | -12.15054 | -48.01266 | 2025-05-15 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b088530-50ba-3c02-b22f-01ffed2d8d25 | -11.79023 | -47.36089 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56fb5ade-933b-38d7-a7cc-638491b74860 | -11.65961 | -54.95466 | 2025-05-15 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b347706-45a7-3457-8704-9d693ade1f81 | -13.09553 | -52.28934 | 2025-05-15 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1787ec4-ff6d-3965-8f00-f12ea3ac29c2 | -16.40313 | -49.0747 | 2025-05-15 04:27:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67da7efc-53d8-306f-802e-a6887828ccba | -11.41925 | -54.33167 | 2025-05-15 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48aa34e3-9dde-35b3-9ba6-1d5667d0a6f7 | -11.5643 | -47.43531 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e5fac53-63a8-3954-a64c-e4cee1623fda | -11.97016 | -48.12074 | 2025-05-15 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52a20819-5cfe-3029-8792-d8f0ac19e9cb | -14.06554 | -57.11145 | 2025-05-15 04:27:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d050631-36f0-370d-8ecd-1b9491be18ce | -11.60642 | -48.01007 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3281a714-51ec-308c-8658-ef6d414a33ea | -13.27237 | -45.4208 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ecff550-18a3-35e0-8ca7-a283f6b77ca1 | -10.47269 | -49.14408 | 2025-05-15 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de5d328b-ac2a-3e51-a3b3-e1b284e9e287 | -10.33226 | -47.97538 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3482145-1737-35e2-9a7a-62748d431db2 | -14.64865 | -45.10388 | 2025-05-15 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87b401c1-a69c-315d-ab76-3bf78df31f75 | -11.69533 | -48.81896 | 2025-05-15 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73638a12-5455-369c-8e1c-b4a5a42ee1bc | -12.18343 | -48.68463 | 2025-05-15 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 595ed82e-88bc-349c-a777-9abc39ca9fc3 | -10.66848 | -57.63713 | 2025-05-15 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9385b926-5bf3-3cda-bc84-04475803ded0 | -11.40149 | -48.69982 | 2025-05-15 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dfaa420-f283-3ab6-a188-6672e68aca42 | -13.27295 | -45.41687 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b75fcfc-fad1-39b4-8519-90546666b0ca | -11.68412 | -44.84867 | 2025-05-15 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60075926-082e-3c1b-a976-9899817490d9 | -11.62889 | -48.46853 | 2025-05-15 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2be5ecad-40c4-3a3f-b5fe-ada5516a38e6 | -10.47209 | -49.14783 | 2025-05-15 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64c2ca32-2312-3f6a-aca7-a849e17608e4 | -13.05124 | -53.71957 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| eb701a1f-1ad3-34e8-bc52-4bd127301dfa | -11.68115 | -44.86859 | 2025-05-15 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4183d948-21e1-3dee-96a8-a5607dee1d6a | -13.59963 | -47.38237 | 2025-05-15 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5070f25-0629-3b47-bd32-0821402af237 | -11.61249 | -48.01466 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 600e757c-62ac-345f-9965-332d3d591529 | -13.27123 | -45.42864 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20c00697-8535-3833-92bc-3d1da52b0c0b | -11.84044 | -46.64006 | 2025-05-15 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d181ae9-c8f5-3c3b-bbf9-f5f44a815d2e | -11.24289 | -49.4872 | 2025-05-15 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a88470c-02e2-3741-ba93-1dfc3defe5d5 | -11.89238 | -56.41266 | 2025-05-15 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8e28c57-62ba-3d4f-aaec-195c62146fb5 | -14.68354 | -47.2965 | 2025-05-15 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caf4cff2-75d7-3f5d-a798-e7e45a462c84 | -16.61574 | -49.00053 | 2025-05-15 04:27:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ac2aa74-0470-31c2-a372-a5e47a667cc2 | -13.2799 | -45.41792 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44f4601e-5647-3792-8b0a-b5093b203823 | -11.65224 | -48.10834 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63952a7d-1a34-389c-95d4-24a86f7a93ea | -13.04211 | -53.72189 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b33e808-02b7-39ce-8508-714c338f32cb | -11.60754 | -48.00303 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eec48223-b86b-3b7f-8df1-2c7d2bf495ae | -13.04354 | -53.71391 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 324ff414-a77f-34b7-bed5-b47f0494b540 | -17.24776 | -48.10749 | 2025-05-15 04:27:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36f9078e-6d5e-3599-9577-b543dbd60235 | -17.09594 | -43.80595 | 2025-05-15 04:27:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa6b3e24-ee00-3e10-9b4f-8e5849d2c52f | -13.09019 | -54.87324 | 2025-05-15 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d46e8e91-2743-3c9e-bdbd-17667183f505 | -12.16114 | -48.80284 | 2025-05-15 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dfc43c2-b3a3-3348-9480-00772f3992e8 | -11.89297 | -56.40954 | 2025-05-15 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2329adb-d2d1-3e59-9981-1f0b7172e460 | -10.85504 | -42.73159 | 2025-05-15 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5003f6a3-4f4c-3b9e-ad6c-d68daa5d3bbc | -11.55672 | -47.61337 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdd827ff-2ef0-341b-9a90-3922e498c805 | -11.05421 | -56.11202 | 2025-05-15 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d84388b9-519a-3d51-8914-22d4be40dd32 | -14.13161 | -52.12651 | 2025-05-15 04:27:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5e85e9db-d686-31d3-89e4-12706f13691c | -13.28512 | -45.43074 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f3222cf-f3c8-3b40-b47d-b3e6d65a9092 | -13.03861 | -53.71708 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ac520d07-3d7a-3cd5-866d-f44c3b88b893 | -10.33944 | -47.97342 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dae5128e-79db-3aeb-8110-be7e5c96d13d | -13.28744 | -45.43914 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5423e5d2-7901-374e-8bdc-8b025463e102 | -11.42829 | -54.33335 | 2025-05-15 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7259a664-b9f4-36c5-838a-6802ec53a510 | -12.29372 | -52.47191 | 2025-05-15 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bbd884e0-26e1-3ff0-8c7b-da3d5ea73223 | -11.55617 | -47.61687 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ea5eeab-9dc6-3e39-85e0-9d2304bbbde3 | -16.68174 | -43.88353 | 2025-05-15 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cf0969d-8bdd-3d7a-9a80-5dde2312e747 | -10.33888 | -47.97695 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b70985c7-567a-3dc7-97f0-f83cca175e90 | -11.15672 | -48.67442 | 2025-05-15 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41e30b33-3538-3272-b265-30d3ce1d9a3f | -17.00837 | -49.78156 | 2025-05-15 04:27:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41a081d7-7268-39cc-968a-64241c936634 | -10.49506 | -46.19257 | 2025-05-15 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55918f43-f83f-3fb7-8875-7cee690b300a | -11.91281 | -54.40353 | 2025-05-15 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26e3f197-e373-33dc-b955-46ee97e45a23 | -11.68248 | -44.86746 | 2025-05-15 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README7.md)
