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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4831c24e-ec4f-3969-bb67-55a144a90686 | -11.8486 | -49.2218 | 2025-11-14 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 277.0 |
| cab9faf1-2879-3e0b-b382-f7663e722e24 | -6.8854 | -42.8652 | 2025-11-14 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| ce07d8d1-e456-36a6-8b75-4786693f1bea | -4.7018 | -46.4508 | 2025-11-14 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2e14db22-4ea5-3cf2-bca6-185798d95f8c | 3.146 | -60.7075 | 2025-11-14 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fb628b34-1be0-3c2c-93bf-50d55b25203c | -2.9434 | -49.3655 | 2025-11-14 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 0ae42366-6c87-36a4-aac3-fedaed5070c5 | -4.7204 | -46.4497 | 2025-11-14 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 4a325531-c20d-38c0-aad0-58dee35390f7 | -17.7989 | -44.9748 | 2025-11-14 01:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cc036fc7-471a-3f48-a8ee-edeefdb440a0 | -2.9435 | -49.3443 | 2025-11-14 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 23deaffa-7b84-368b-a300-70b6b0539b62 | -11.8677 | -49.2195 | 2025-11-14 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 3bdbf521-fd19-3477-9f95-bedd91c7d654 | -4.221 | -49.1267 | 2025-11-14 01:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 97d56a3e-4a0f-364d-811f-984612bf5f4c | -7.8479 | -44.2865 | 2025-11-14 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| d6d73608-761a-3719-83aa-b15213d5e065 | -6.8856 | -42.8416 | 2025-11-14 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 2524680d-0ec2-33f0-b390-09376c42eff5 | -7.8665 | -44.3077 | 2025-11-14 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 860a5296-f711-34b9-bdb3-71f6e6ad8772 | -7.8476 | -44.3096 | 2025-11-14 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e16fca0d-f139-315b-b147-d66c9ee15f4b | -3.9147 | -44.3309 | 2025-11-14 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 40e928e0-5ea4-3db5-bebe-87bd8e778e27 | -4.7018 | -46.4508 | 2025-11-14 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7aa7a62e-f94f-3044-a2a0-4132a26cfc8c | -11.8677 | -49.2195 | 2025-11-14 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 035879fd-4f2e-3ee5-8567-3ac890ee630a | -17.7989 | -44.9748 | 2025-11-14 02:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| cfac2de3-be43-3df2-9f19-ed100efb209e | 3.146 | -60.7075 | 2025-11-14 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ea7598ab-893f-31ae-a9aa-f2bfa56a9eb3 | -6.8856 | -42.8416 | 2025-11-14 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 4c978655-56f7-32bb-8ad8-fa4ba73344fd | -7.8479 | -44.2865 | 2025-11-14 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| cf74dd1c-1116-381a-ace7-a1d104bf111c | 3.0911 | -60.7653 | 2025-11-14 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 151.4 |
| c26b4ff8-ebe8-3344-9fd1-d179f36d784f | -11.8486 | -49.2218 | 2025-11-14 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 214.6 |
| e92e346c-9194-3524-9adf-176df832334d | -7.8668 | -44.2846 | 2025-11-14 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| bb98c9c5-5ec9-3426-9d06-e5d20a8e493a | 3.1094 | -60.765 | 2025-11-14 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 36cd90a5-e02e-3dc3-8b4f-c0c6e1b039e7 | -6.8854 | -42.8652 | 2025-11-14 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| dd5c4bff-ab09-3bdf-b63c-e4cb69dafd0c | 3.1093 | -60.784 | 2025-11-14 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a696ef6e-b82f-3410-8632-f697c87d7577 | -4.7204 | -46.4497 | 2025-11-14 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3845e365-f3db-3025-907e-b8b81ed82cb4 | 3.1094 | -60.746 | 2025-11-14 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ef6c3029-94d5-3872-8aba-a01eef4a206d | -7.8476 | -44.3096 | 2025-11-14 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 40a9ecfe-d197-3efa-9318-b9608281fb12 | -11.849 | -49.2 | 2025-11-14 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| edc7704f-003a-3f6f-9258-6f7fd6aa78f1 | -11.8677 | -49.2195 | 2025-11-14 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 9bb47f30-5bed-3673-bc74-b2d74d599ade | 3.0911 | -60.7653 | 2025-11-14 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 172.4 |
| e53df2df-783d-3a83-9f3c-bf531bbbf6e2 | -11.8486 | -49.2218 | 2025-11-14 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 219.0 |
| af9d52c8-5ff9-373d-a57f-58313c0028ed | -7.8479 | -44.2865 | 2025-11-14 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 1ddb65d6-5aba-337d-8589-bd29e1478df6 | -6.1606 | -48.0507 | 2025-11-14 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| bff5b8c2-8640-381c-9dfa-d8d5ac8b1a31 | 3.1093 | -60.784 | 2025-11-14 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 3722f8ca-c605-31f1-945c-28fa633d9ee2 | -7.8476 | -44.3096 | 2025-11-14 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8873da66-0761-3a9e-aee1-5ad72fd6d126 | -11.849 | -49.2 | 2025-11-14 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 7a4ed8a8-16bd-3496-8fa5-1a2c616e2f8f | 3.0911 | -60.7843 | 2025-11-14 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 27dc8526-88ea-33e5-a8ca-5bb12f060371 | -2.9434 | -49.3655 | 2025-11-14 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2936df1a-97cf-3afd-9aae-99ece14ac446 | 3.1094 | -60.765 | 2025-11-14 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 11e1fbf2-fd49-3a42-96bb-500bb6212fd2 | -12.6749 | -46.7378 | 2025-11-14 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 0d7369db-849d-3abc-bf07-ee1b1909535f | -4.7018 | -46.4508 | 2025-11-14 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0c218ef6-4c34-3b8e-a1cc-fac151c1760d | -12.6992 | -45.4335 | 2025-11-14 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 41a56596-86d8-3385-b303-6a689ec27897 | -12.6745 | -46.7605 | 2025-11-14 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 9a5e14c0-79ff-3741-b575-1ff1a47862c5 | -11.8486 | -49.2218 | 2025-11-14 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 3a607c41-328c-3d3d-9757-71a7c57530cf | -12.6749 | -46.7378 | 2025-11-14 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ef85fff9-7e4d-35a5-8a23-b127e0353cd9 | -11.849 | -49.2 | 2025-11-14 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c13cd255-9eb8-31eb-a4cc-2e87ebdca990 | -7.8668 | -44.2846 | 2025-11-14 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 42fd6453-5707-30ad-9090-5a042b32b770 | -12.6745 | -46.7605 | 2025-11-14 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ecf48ef2-f855-34eb-8c76-f345d1eadcef | -4.7018 | -46.4508 | 2025-11-14 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c2193bdf-fd59-32c9-87ba-206546d076fe | -4.6116 | -43.3925 | 2025-11-14 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| be14895b-a9ca-322e-ad9d-743498df9bda | 3.1278 | -60.7078 | 2025-11-14 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bdd27cb3-5731-3a9b-8423-20a4bd051727 | -6.1606 | -48.0507 | 2025-11-14 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 52d9a0fd-269c-3120-a9a0-83098740a9b4 | -7.8476 | -44.3096 | 2025-11-14 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 433cfe64-95b0-30ae-a1a1-3355a9028c88 | -17.7989 | -44.9748 | 2025-11-14 02:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b9bfe29c-4074-35a9-85f9-f392db1c57a1 | -11.8677 | -49.2195 | 2025-11-14 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 9a8a9a37-ef42-3a14-8205-ae8efc40ff9a | 3.0911 | -60.7653 | 2025-11-14 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 1c1b6988-e5f5-3994-9653-11629b71960b | -7.8479 | -44.2865 | 2025-11-14 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 2a589a44-809c-393e-aae5-1e54eca43ac2 | -6.8854 | -42.8652 | 2025-11-14 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 5d796266-942d-359c-8596-d241a2563a57 | 3.1094 | -60.765 | 2025-11-14 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 797eabd0-8665-32ff-8b2f-6e058c562b18 | 3.1094 | -60.765 | 2025-11-14 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 164.3 |
| b3237076-2b18-318e-82c7-9b435c62a4f0 | 3.0911 | -60.7653 | 2025-11-14 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 107.2 |
| d3b9d28b-8531-3825-9410-041ab46fc0e5 | -7.8476 | -44.3096 | 2025-11-14 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e1d9a120-ac16-326b-bed4-97459d4e5f97 | -12.6749 | -46.7378 | 2025-11-14 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 85f9cd91-3565-3e3d-b289-e4c1017c6f95 | -11.849 | -49.2 | 2025-11-14 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5a49fbaf-b3a5-33f2-9986-76a68ef0eb72 | 3.1093 | -60.784 | 2025-11-14 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f6eb9dc2-a25d-30bc-898c-fb991970c56f | -7.8479 | -44.2865 | 2025-11-14 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 9076a229-7cb9-352e-a17a-ad265bba4134 | -11.8486 | -49.2218 | 2025-11-14 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 96a1422a-9312-3ba3-b6c5-97000ccda703 | -12.6553 | -46.7633 | 2025-11-14 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| d257fdd5-7eda-34d0-b2fc-3d28aee6e596 | -11.8677 | -49.2195 | 2025-11-14 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| f2953a59-8c02-3b74-9cf0-8b4a0835011a | -12.6745 | -46.7605 | 2025-11-14 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1359e76a-8f4d-3432-83b4-d7ba67297aab | -7.8668 | -44.2846 | 2025-11-14 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 467c5fad-a582-39f4-ba02-bdbc21458c44 | -11.849 | -49.2 | 2025-11-14 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d3cefdbc-f774-30be-a762-747ab910100e | -11.8486 | -49.2218 | 2025-11-14 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 32d08284-b855-3811-992b-54c95f8a0bcd | -11.8677 | -49.2195 | 2025-11-14 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| d9b6a751-4a26-384c-830c-d5b3296e8804 | -7.8479 | -44.2865 | 2025-11-14 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 928e234d-857d-332b-852e-df8026585ecd | 3.1094 | -60.765 | 2025-11-14 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 305b21c2-e6ca-3bb7-9760-a992b92f51fd | 3.1093 | -60.784 | 2025-11-14 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 01f33783-4b80-3e22-b248-d933dfcbcaf7 | -4.7018 | -46.4508 | 2025-11-14 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c6ec1347-3203-35f8-a66b-90f89d245526 | -12.6745 | -46.7605 | 2025-11-14 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 92e3b70b-30ce-3045-8bd8-a14c1d135084 | -7.8476 | -44.3096 | 2025-11-14 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f3cbcc29-2e07-3718-8537-d3cd4275a1ec | -6.1606 | -48.0507 | 2025-11-14 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 81351869-dbc6-3020-bc26-5be0b7260875 | 3.0911 | -60.7653 | 2025-11-14 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 116.3 |
| b1fd18aa-d808-3b39-be2b-bc529c8920f5 | -7.8476 | -44.3096 | 2025-11-14 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8fb2168e-ebfe-3f7e-9c64-342ed51787c5 | 3.0911 | -60.7653 | 2025-11-14 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1e5f303a-fb8c-3ae6-9cc2-2a679b3884a4 | -5.5259 | -43.6794 | 2025-11-14 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 97d6fcc6-9cb5-3047-94da-942a0927d6d3 | 3.1094 | -60.765 | 2025-11-14 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 133.3 |
| fb3889d2-2cf3-3237-894c-61faaf28f8e0 | -7.8479 | -44.2865 | 2025-11-14 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 343dd41c-7d1f-3045-bb26-e78f0543f7f5 | -2.9434 | -49.3655 | 2025-11-14 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 68535d9b-e18a-31d0-9a84-5284876bfca4 | -11.8486 | -49.2218 | 2025-11-14 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 83866e00-5e85-37c5-a560-c9bebbf3d3b9 | 3.1278 | -60.7078 | 2025-11-14 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 86951a08-b9e0-386b-a8f7-803935a777f0 | -11.8677 | -49.2195 | 2025-11-14 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| eae8b151-7425-305a-8f5d-c8b1b5ff6d60 | -11.849 | -49.2 | 2025-11-14 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7ca19c5e-f4a0-340b-a3ef-b00a72c5ecc0 | 3.0911 | -60.7653 | 2025-11-14 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 95f9be3d-3211-35ee-a46d-b101796c24d9 | -11.8486 | -49.2218 | 2025-11-14 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 0fb911c1-7ad6-35c6-b7cf-692e017be558 | 3.1093 | -60.784 | 2025-11-14 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 9da1c0a4-bad2-39c2-89a8-50de72f208d9 | -7.8479 | -44.2865 | 2025-11-14 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 1ef4a58e-422c-3245-8acd-9e10cb23c27b | -2.9434 | -49.3655 | 2025-11-14 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |


[Clique aqui para ver as próximas entradas](README13.md)
