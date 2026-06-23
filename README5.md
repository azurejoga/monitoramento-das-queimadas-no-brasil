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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c4f2394-2642-3d88-a92c-8872b016487b | -9.22192 | -45.32548 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5bd1633-5b9d-3b6f-8ab2-67ec12da7c26 | -5.9426 | -43.46795 | 2026-06-23 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51019fcf-d7c3-3699-9cba-138e2ba71e09 | -8.86519 | -46.9489 | 2026-06-23 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c4201dbd-0a1c-35c4-b552-2899d8e8cd80 | -12.85335 | -44.35589 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b9356b6f-0666-34e7-87d0-5592be5e4939 | -11.80891 | -47.34412 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb0d29ad-3413-3ebc-92a1-ec360a148907 | -14.03011 | -43.8736 | 2026-06-23 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 918ec730-619a-34b1-969c-41ecd53b0d4a | -5.80164 | -43.78968 | 2026-06-23 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e55cf01-c86d-3fb4-ba7f-f8b7d6b9a5c1 | -11.98074 | -47.11889 | 2026-06-23 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3446e0f1-e3c8-3319-9e38-39f782386d29 | -5.82026 | -45.06034 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5f539e5-68be-33fc-af29-994500b511bd | -5.82438 | -45.06287 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 322667c1-198c-360c-a3a5-25825a0115ed | -6.35957 | -43.59972 | 2026-06-23 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bc0c8cc-2709-3a98-aaa1-e1a93dbc8004 | -12.02753 | -47.80333 | 2026-06-23 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d0df384-b6f1-3fec-b4e6-658a02c39a23 | -5.8235 | -45.06765 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5561a75d-937e-30ac-ad7b-deb32f56d250 | -9.21721 | -45.33639 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1a9982e-3e0e-3794-af36-1e8e8fe0e905 | -12.86442 | -44.35482 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 6272b33d-b677-3145-acd0-cc3cc6cde543 | -12.87164 | -44.37328 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd03649f-dc8e-3062-8c8a-0aab1b29b294 | -12.52013 | -48.30116 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad787c18-97a0-365c-a579-fc3e342b2587 | -14.03099 | -43.86831 | 2026-06-23 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7abd8401-bfcd-3a7d-91cb-aa419e3a9921 | -12.84725 | -44.36338 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2942f1e1-e7e1-3a8a-8b76-1e1e47e449eb | -5.82525 | -45.05819 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7bc28ecf-80d0-3e53-ba88-2ede4d437199 | -11.80179 | -47.34514 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0d167b84-81f0-38c7-ad45-222d69b4a128 | -4.05785 | -43.24888 | 2026-06-23 03:47:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deca3520-32bb-3665-a76d-5befa926a55f | -5.79438 | -43.63378 | 2026-06-23 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 175fd92d-71c0-33ce-863a-de5767bc8c50 | -12.02871 | -47.8071 | 2026-06-23 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5bd8832-78c1-31db-8b9c-ef8e35efb50d | -8.07951 | -46.38495 | 2026-06-23 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab886435-7f98-374d-a72b-924aa972ecfc | -11.83592 | -47.07857 | 2026-06-23 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8db9c808-7e39-337e-bb8a-047e896fb7d4 | -12.48354 | -43.72734 | 2026-06-23 03:47:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9dd54ad9-6aa3-34e8-a60d-d1e61be06595 | -7.72125 | -44.56804 | 2026-06-23 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f53d45da-ecb5-3e71-bbf6-3cc5e7bddac2 | -8.08404 | -46.39613 | 2026-06-23 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d6cc2a4-cace-382c-823b-d1dc90a1c456 | -3.86407 | -42.96436 | 2026-06-23 03:47:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a254fd2-eafe-32a0-a8f4-94a9788a5154 | -16.0294 | -43.41785 | 2026-06-23 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c6ea8914-5e55-3710-a696-2744840126ca | -11.80709 | -47.35193 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4322e55d-0fa9-36c1-92b1-e7901935f621 | -12.50219 | -48.2763 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2566591-76d6-3686-aca2-7e47e1a4d0e5 | -15.72592 | -41.35597 | 2026-06-23 03:47:00 | NPP-375D | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fbb4dd30-08e9-345c-bc62-be976d7e6d74 | -12.50889 | -48.2776 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1b28f0e8-ef38-3b86-abd5-c7cac988ee11 | -5.82108 | -45.05569 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 151433ce-43a2-3d34-9d7f-ed2fa8708c7c | -12.87228 | -44.37004 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 791b33d9-d867-39c5-9dfd-de80e59e6bb1 | -11.80138 | -47.34817 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 87deec8c-2642-3e69-ab76-590009365e68 | -13.46474 | -41.76188 | 2026-06-23 03:47:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| db9f11ba-eea4-38b4-a29d-c585fafdc3ec | -11.81567 | -47.34246 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3f5c16a-c7a3-3089-a053-2547b1a7556f | -12.85184 | -44.36773 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5d8dffe7-4578-3732-a4b8-693d41e2b5df | -12.86771 | -44.36567 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9da1f1f8-fd38-31d0-8c0f-5f703f5649aa | -12.86835 | -44.36242 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d64d6061-ecc7-3921-b48c-5fd8950fb480 | -14.02986 | -43.87406 | 2026-06-23 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb7a7236-04fb-3ee1-b48b-3e0f5ffd1f44 | -4.98096 | -37.23429 | 2026-06-23 03:47:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3724dae2-0a43-357e-a1e0-3f7d4492d4ef | -12.85246 | -44.36447 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 093313fb-6c0b-3f94-bcf0-f6f6caa06255 | -12.86579 | -44.37542 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36671570-09c5-3e7c-bf02-2250ef68c10d | -5.82551 | -45.06662 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4de3cdd8-6e3e-3342-999a-3e20661e41ff | -12.85308 | -44.36121 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e2ceaa25-98df-3735-ae2d-da07d6a0c8bc | -6.1875 | -44.86645 | 2026-06-23 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 935db5a4-0ace-3ca7-aa54-3ab0f9f9c572 | -12.92533 | -43.62217 | 2026-06-23 03:47:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bb436f9-83ec-3135-9ea9-60da6dcb998d | -6.18584 | -44.87579 | 2026-06-23 03:47:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5f907ce-91b2-3d86-b21a-b8fb1802462f | -12.64988 | -47.68433 | 2026-06-23 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4fbc6c0-528d-3597-b63c-3992385f4198 | -12.02983 | -47.80167 | 2026-06-23 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96c860f4-2cda-3251-8314-9d7b41b45b57 | -12.5039 | -48.27898 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6690a6ef-fcca-3370-a995-f0f668f0e7a5 | -5.8174 | -45.06617 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69002c21-bada-3717-97d3-8ccfe6fa0ccd | -5.81829 | -45.06139 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 34ff773e-a65a-3477-bc40-cfb740a0071e | -8.12583 | -47.8991 | 2026-06-23 03:47:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a19728f-5439-3c38-92e5-e3fa07e55b97 | -6.37128 | -43.59855 | 2026-06-23 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5816d58c-195f-3b1f-a565-977730e6511d | -9.22621 | -45.33504 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a75251cb-eb9e-3cbf-a65b-728d900ae140 | -12.86378 | -44.35807 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1b280909-3478-37df-9266-ac47ba6140a1 | -6.99483 | -42.90131 | 2026-06-23 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 417c34e2-0d3a-3913-b15b-fe228dd72e96 | -12.87292 | -44.36679 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5589b705-acf7-32e6-8661-bd828487f2b1 | -12.86707 | -44.36893 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09321401-a8fe-34d2-89cf-82183b9c5678 | -4.98471 | -37.2349 | 2026-06-23 03:47:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a281ae2-4fbb-39fc-9452-3694d3a3225b | -12.50516 | -48.27305 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4c44295e-5b74-3666-8b17-1c599fa6bcff | -14.0312 | -43.86784 | 2026-06-23 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b32cb2e5-ebe0-38f8-ae7d-5b65adcdfd36 | -12.48411 | -43.72438 | 2026-06-23 03:47:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f623fed2-fc87-33b4-8680-b49986ac4bbe | -3.86964 | -42.96529 | 2026-06-23 03:47:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f0689bc-375f-3126-b784-aa832048ae46 | -14.41234 | -44.59209 | 2026-06-23 03:47:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4d3932a-1942-3094-977b-ffd989073b6c | -9.22392 | -45.33331 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a89b551b-1f31-364a-b7fc-c448a102244d | -15.38923 | -40.82547 | 2026-06-23 03:47:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1f06fe5-9447-35ae-99ba-e7ea6fd87221 | -11.80778 | -47.34951 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d480f52a-30bc-3c00-b04f-05599332780d | -5.80001 | -43.6348 | 2026-06-23 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b01b040-5751-3b1e-b49f-4cfc47eda743 | -11.81004 | -47.33871 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5382799f-1288-3f93-b555-ac390289b441 | -14.06235 | -39.49148 | 2026-06-23 03:47:00 | NPP-375D | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 38c62e09-aaf8-3914-92ca-fa75cb9500e5 | -7.35949 | -47.02022 | 2026-06-23 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff34cfb6-bc01-3c29-99fb-5ea53d674116 | -12.85143 | -44.36565 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 53175aac-c791-316c-9b6d-f42f35272bc1 | -12.85078 | -44.36891 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c2765b80-3a73-3b62-8495-49daae16b16d | -5.93706 | -43.46686 | 2026-06-23 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ade1688d-2360-315f-bab0-2fc7cfbdc231 | -5.81915 | -45.05674 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 15e335e3-b76a-3327-92aa-541b65d4ca0a | -6.18801 | -44.86832 | 2026-06-23 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f040641-559b-3a73-81dd-3a358867cf89 | -12.85122 | -44.37101 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27376afc-8bff-3f29-959c-77f660f47d80 | -6.50194 | -42.22384 | 2026-06-23 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a16f86dc-2c1b-35df-b392-90792eecb280 | -12.856 | -44.37 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47b715c8-db71-389f-91b3-10cb69928051 | -12.85921 | -44.35373 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 18f960ee-1952-3822-8774-fa499b639a76 | -5.82635 | -45.06186 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 40a1b5de-0f1d-3029-8cf4-4993a229e4da | -12.84621 | -44.36458 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| dafd5fc0-c0cf-31ab-b9ff-c4f4809e979a | -12.48297 | -43.73031 | 2026-06-23 03:47:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7fae038-f2ed-32f8-ba90-c5f761f6cc89 | -6.36511 | -43.60091 | 2026-06-23 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86609794-c966-326b-8ab6-0ece43b90a7f | -11.97446 | -47.11749 | 2026-06-23 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd9c91e6-07ed-35de-8e6c-b5a013027456 | -14.41168 | -44.59533 | 2026-06-23 03:47:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ddff731-3617-3b7d-84ba-2b7247f1427d | -12.86314 | -44.36132 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 1f84f687-4574-392b-b78b-e8b07e971046 | -14.41065 | -44.59446 | 2026-06-23 03:47:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f89a04-431a-3437-89ec-a147f1c6ab86 | -6.50805 | -42.21885 | 2026-06-23 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 81e6c69f-4476-3f7c-a8b6-fa00a1296676 | -12.86899 | -44.35917 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 137d51b2-8d70-397d-9a57-0a8dc7eed7ae | -12.85207 | -44.36239 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 24596f8e-922a-3fa7-9cae-0841dac30ab2 | -12.84663 | -44.36665 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3b8fb880-0d0a-30ab-87b4-42ba8c2ec1a3 | -14.06674 | -39.48995 | 2026-06-23 03:47:00 | NPP-375D | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a0c3f9fc-e643-30f7-9487-2064691626a9 | -12.4785 | -43.72631 | 2026-06-23 03:47:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
