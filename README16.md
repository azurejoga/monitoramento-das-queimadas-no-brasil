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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dab6e628-b401-335a-9cee-85cab7bd32ac | -8.17402 | -55.10307 | 2026-06-25 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 373ef521-8785-3dd5-87f2-034c7695e68f | -5.78495 | -45.04535 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68039eca-c235-3e84-8b78-1a8862b0e9c5 | -6.76051 | -46.31092 | 2026-06-25 05:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0a98db-5c4d-3206-97e5-904299fdb54d | -7.74888 | -44.62374 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6daac4cc-0101-396c-b5cb-b51b64cb7512 | -9.58286 | -49.11982 | 2026-06-25 05:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1ef7987-37f2-3771-ae1f-a5b9b173c838 | -8.68453 | -47.86274 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecabe743-575c-3e26-ae1c-c4ea45c612f3 | -7.75576 | -44.61966 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 23dd007a-bf0d-3cb0-8f6b-27a461bfb72d | -6.98069 | -42.8899 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 491a9c2a-47b1-3f71-81e1-7d2d4dc271e2 | -9.36846 | -50.54235 | 2026-06-25 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eac2ce40-051a-3ca3-a06a-86fe01e5ede7 | -6.9936 | -42.89772 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 391b7d45-0fde-3e38-bbcc-2b19fd01de79 | -10.29344 | -44.69548 | 2026-06-25 05:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2f45957-638e-3648-a7bc-689b7a410025 | -5.80803 | -45.05273 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3af1de1-1292-3f9f-87a0-5bf976844833 | -9.36635 | -50.53922 | 2026-06-25 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70e33d61-753d-3cc9-90db-58f89538b1be | -6.97385 | -42.88884 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ea5f5dbd-40c6-367a-8627-59e71825a33b | -8.68533 | -47.85673 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db5f3765-aa19-33f1-9d7f-336dff304eb1 | -8.57903 | -46.90681 | 2026-06-25 05:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf836c9b-dd66-3677-81b6-4755a4784af3 | -6.98119 | -42.89026 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| b40bb58c-f9f8-3ba2-97cf-b44a69edce38 | -9.80477 | -48.92218 | 2026-06-25 05:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa573fe6-7601-3fb5-8262-a60c87aac988 | -8.12506 | -47.89005 | 2026-06-25 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aa4f166-ae3b-3e8b-a5e2-168fa44810bb | -5.80679 | -45.06155 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b2c2ed4-4419-3589-bce2-0732458cdce8 | -6.97353 | -42.89562 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f750677b-8d05-3bb0-9f65-df353801752f | -9.45864 | -49.83105 | 2026-06-25 05:08:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f41c016a-fb54-3a51-9424-41277ffb2781 | -6.98671 | -42.89704 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| dc86bc25-a759-322b-8ea5-b8812ada8d72 | -9.37064 | -50.53984 | 2026-06-25 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1a15067-dcab-3025-9649-3d53e631cf6f | -9.5841 | -49.11656 | 2026-06-25 05:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62118fdb-b3b4-34c3-893e-932caad07fa9 | -5.80618 | -45.06586 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a2fee84-896e-3849-b627-5ef67ddb386a | -8.57535 | -46.90285 | 2026-06-25 05:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3ff2aad-0c1b-3a8c-af1c-5c6c6b7c68bb | -8.69005 | -47.86036 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 821f972c-943f-3d45-8044-047400390f1f | -7.74332 | -44.61768 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c0d18fc8-d6cc-3e4b-a107-00413b9fd31d | -7.80747 | -46.46283 | 2026-06-25 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98191429-4215-3069-9c36-164ee0d47643 | -8.574 | -46.90301 | 2026-06-25 05:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71d2975a-9212-33fa-bc33-48a5a2de85bc | -9.80546 | -48.91689 | 2026-06-25 05:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b17a2f47-3d24-3a3f-ad1b-0040014286f2 | -6.98756 | -42.89074 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| beb59aac-4234-3a2b-9ec5-6a0f2f29c5ef | -5.80867 | -45.04823 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb5fdf13-ca81-3e75-9d4d-0e58061449ee | -8.67942 | -47.86208 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7119a3a8-4930-300e-8a31-e175ea39ab9d | -9.19987 | -45.32113 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1572d0df-2ec9-303e-a54f-053bc3932a97 | -7.76266 | -44.61549 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffdaca7d-e618-3bab-9ded-59fb427ee509 | -7.74268 | -44.62263 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 02eb1944-f76a-30e7-8809-c70047b1389f | -9.20535 | -45.32658 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db16039d-0a75-3cb2-a343-83215a72ba61 | -7.73388 | -44.17463 | 2026-06-25 05:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b15e6b0-a223-39ad-bb78-c446065e19f2 | -7.75021 | -44.61353 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3177dbbc-9e85-3e81-a370-66bf6c9e683c | -5.78554 | -45.04108 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74541196-7631-3ab7-9249-646f46fe6fa7 | -6.98806 | -42.89111 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8362cc06-fef6-35ac-8afb-d562ab210cbc | -6.98726 | -42.89741 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 4f873ed4-5688-3ba9-95d0-55c9fb610c39 | -9.36576 | -50.5433 | 2026-06-25 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddfba1e5-d7f6-363f-b4a5-2ac75b5156a4 | -7.76199 | -44.6206 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d94577f5-60eb-3251-a864-7766a4f90e65 | -6.99495 | -42.89181 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4afc7db3-57cc-3620-b86c-9c8683e86251 | -9.74192 | -47.87572 | 2026-06-25 05:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 330678df-c0b8-332b-ba7e-01d5a2333d0d | -8.68965 | -47.86337 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72cdda2a-51ed-39c3-b4d4-0771bb210a92 | -3.51174 | -48.0312 | 2026-06-25 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c812200b-8484-302d-9f7a-baa5cb65099e | -9.21143 | -45.32735 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 695c77e8-0d01-3821-8c93-efd49ac60400 | -7.74201 | -44.62772 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b67cdb66-7d57-338c-b42d-56acb1d55c7c | -7.63509 | -50.21501 | 2026-06-25 05:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ada90979-764e-3634-becc-24f2dd2d81f2 | -9.37005 | -50.54394 | 2026-06-25 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13cca488-24dd-34cd-b063-04f5ee4fb716 | -9.57868 | -49.12095 | 2026-06-25 05:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6c7d621-1845-3939-996e-02279d314b0a | -7.72677 | -44.17907 | 2026-06-25 05:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d342791-84f2-38a6-ace2-68aaed0a742c | -8.67981 | -47.8591 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f0bf9a88-87cb-32b4-95e9-06b78fc60afd | -7.74396 | -44.61274 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0da2c4a0-63f4-3ab9-b038-8be0f9886f29 | -3.51568 | -48.03686 | 2026-06-25 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b3af47a-5338-3800-8b47-d2dc7bac827a | -5.81932 | -43.59442 | 2026-06-25 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f7c68080-e2b4-30c9-8cd3-0640c5a6d546 | -10.29405 | -44.69044 | 2026-06-25 05:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 327651f7-207e-3497-a7df-b9aebff7f7df | -5.82001 | -43.58929 | 2026-06-25 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2380d29d-18a9-3669-87b0-4dc44cd1c8f8 | -9.20644 | -45.32414 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af1def34-59f6-32c1-9d4f-82bea99e7d2f | -9.27874 | -47.65576 | 2026-06-25 05:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dec19621-ca34-3e25-9f06-11653edd8cb9 | -9.21253 | -45.32493 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98a5cbd2-f8f5-3612-ace8-4d4bac3d2fee | -5.81213 | -45.06639 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc26404f-65b2-3001-8556-1df27c82b256 | -7.74034 | -44.17514 | 2026-06-25 05:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8c680ca-729a-3eb2-9848-8395c6b6f25f | -7.63139 | -50.21036 | 2026-06-25 05:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c09e3d57-a468-3e32-b2c5-762538af7b40 | -7.80794 | -46.45931 | 2026-06-25 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a603a24-8869-33da-80a0-bde55ec85679 | -7.73854 | -44.61853 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9891fd6f-fa50-3195-84f4-fe5c651fb6e7 | -10.27961 | -47.60428 | 2026-06-25 05:08:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a086291-6999-3fd5-a660-95c296f27a54 | -6.98888 | -42.88477 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c6f04c49-c15c-37fa-b2f1-a9893741c12c | -8.32366 | -47.12878 | 2026-06-25 05:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fafdef5b-1434-35a9-a3aa-65887b6837f4 | -8.12545 | -47.88716 | 2026-06-25 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 124cb5e0-dca9-364b-ba89-a105cad4cb74 | -9.74152 | -47.87885 | 2026-06-25 05:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d959eee-4e62-3978-83c1-56fc073dcae1 | -8.1256 | -47.89291 | 2026-06-25 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7246c60a-fa37-3496-9f75-ef6199af5084 | -6.99445 | -42.89142 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 4888f1c1-bf9d-3182-9a17-eadc41581c30 | -7.75645 | -44.61436 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 272ed120-a21c-307b-881d-53fdeba007d2 | -9.20035 | -45.32335 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9143c0a-ea6d-3459-8652-4256f607ab03 | -6.76651 | -46.30819 | 2026-06-25 05:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d40829e-264e-389a-8249-debdb54e5d79 | -7.73921 | -44.61367 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ec14a49-a89e-34ac-baa3-7e5e9b63d51e | -7.74823 | -44.62869 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 468ca73c-9bfa-33f5-96f2-eb1956c4cc00 | -7.74953 | -44.61872 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3d0d16a-640c-3005-a374-57d96a3bd036 | -5.82011 | -43.58815 | 2026-06-25 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b510e2c3-3096-3f39-89ee-57e9d8da0f81 | -10.27428 | -47.60366 | 2026-06-25 05:08:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 785fbbc5-cc3c-3d21-842c-3c21600e0c6f | -7.7498 | -44.6184 | 2026-06-25 05:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 461ede04-deff-3da9-bda4-92e6ff1bc933 | -11.8868 | -51.7452 | 2026-06-25 05:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 25a3990a-3fe6-3caa-9a35-0a6842ba54ad | -11.8678 | -51.7473 | 2026-06-25 05:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 996f4c8c-9a02-3030-aa9f-ee3c126e6943 | -11.54132 | -52.77919 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 092480f6-1d66-3169-a489-df90eb60506b | -12.38209 | -54.16549 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2014f44a-9bc1-354c-be64-45a59f1e125f | -12.138 | -48.26554 | 2026-06-25 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a0404aa8-9b02-38a1-890e-a308edaa9744 | -11.8857 | -51.74937 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| a15ee331-e6db-398e-813a-7680eaa64644 | -10.57657 | -57.32055 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0be0d008-5b56-3d6e-af16-02c66a4e8f20 | -11.87748 | -51.7482 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0963fd3e-281a-3307-b3b2-cc7c4656d52b | -12.55729 | -54.59139 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83bdea4d-6e7d-3e8d-9587-f9f561439f84 | -10.61251 | -47.12118 | 2026-06-25 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 508b1b5f-d83f-3222-9e94-160ec4933496 | -10.36507 | -47.348 | 2026-06-25 05:10:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc2e8cad-e7ce-3bc5-8479-15ae6f49a047 | -11.30731 | -54.71235 | 2026-06-25 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe4d4006-443e-388d-b292-284465a1f9f1 | -11.50512 | -54.49746 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab1608cb-006f-3022-bb91-51d9b6ebe0c5 | -12.55437 | -54.58685 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README17.md)
