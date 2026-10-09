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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daab90d8-f92d-3e9a-ab16-f60b0862413f | -1.09957 | -54.17238 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f1b8777-d9f5-320a-b077-3b3a8caa9d54 | -2.99614 | -54.05711 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4471fd7e-090d-3038-a577-12a8aaf51f57 | -2.98088 | -54.07915 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 765132a2-53c5-3590-bdd3-52027d9bd0f4 | -3.2891 | -49.51394 | 2026-10-09 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b344eb03-a4b0-3b5d-af54-1571d70c406f | -1.1145 | -54.17459 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5c4d129a-8bc2-3f7e-a8a0-2809c0ae284a | -3.98244 | -59.34518 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9515acba-b5b7-3d23-a860-be74366f16e9 | -3.49484 | -59.20747 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c788bb15-dbc6-38a5-80a1-192e577d3cad | -2.88292 | -54.18695 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42c9873d-ea8e-36fc-9541-92bf1ad9b785 | -2.31298 | -57.98281 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c907577-ce2b-3338-885d-003f19e455dd | -2.56321 | -56.16439 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6c5f429-0c63-3c75-b36b-a0eef97ced2b | -3.25031 | -54.02833 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f7563b0e-2f13-37cd-b75c-eae4841266e3 | -3.77194 | -59.25869 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 020abfef-a46e-34c3-b699-6f7dbe99224f | -3.74705 | -60.5963 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5419277e-1f44-323f-8d3c-0d5078003683 | -3.25491 | -54.02415 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b70720dd-d2ac-3710-9c52-9796f1483ea4 | -3.6059 | -60.58278 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89d4e24e-ba2f-3eb2-82c0-4933c7f65ec0 | -3.75028 | -59.41603 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e461cc7a-5841-35c4-b274-f1e70e3071dc | -3.00792 | -54.09524 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f77793d1-bcc9-30de-9418-f1e9ae246748 | -3.47689 | -59.50909 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a546dc2-04a1-3028-99d1-abc1ccb2df3f | -3.04889 | -54.03303 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df6434d3-6354-3df2-bfbb-1868b5c8ce26 | -6.67262 | -63.03405 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07b9fddc-d25e-3eac-a36c-f0f7cea5163f | -3.01464 | -54.06483 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5220d0a3-5fd5-3be2-8eb5-491b93e46c45 | -8.65487 | -54.53723 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4166f07-e5ff-37a1-bbbd-b25d04d26885 | -3.52809 | -59.50999 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c06bbb2f-f2b2-3ff4-8b59-f057c318018c | -3.94146 | -55.85093 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ff238b2-6aed-371d-8dc8-238bdceb8d10 | -3.1041 | -53.95743 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a29fa650-2cf7-3b96-80d8-f980b7acf305 | -3.30826 | -53.69791 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5ac3e73-4e19-3497-8fff-775f031e78b6 | -3.83745 | -55.98532 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9013734-1442-3aa8-af39-90014bfc693b | -3.39109 | -57.99725 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b845104b-4ee4-38e0-9bc4-d57d59825e3c | -2.89866 | -57.65036 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc90c7ed-bba3-3513-a748-b6431408c1b2 | -2.48977 | -56.16068 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1885a761-a805-3b1e-9df0-d71c097838e4 | -3.63324 | -58.99843 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf2035ec-648a-3345-abd9-76d17bfaaa1c | -3.9243 | -56.03339 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 38348bba-3e95-3234-947f-78ec2551a189 | -3.97413 | -59.35457 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 982c5500-9390-3e4e-a840-d3d5c7dcbf8b | -3.25659 | -54.03918 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ae9b1d7f-a51f-3bd7-864a-6c299dbaa93d | -3.71496 | -59.65889 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c69e6dd0-45b9-3420-97d0-a170de017322 | -3.44935 | -59.55896 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 650dcc6a-02a1-31ab-ae9c-cb1e69fe6509 | -1.74097 | -57.17323 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef0b3b7a-31c5-31c4-88ff-d073fd73df16 | -3.5075 | -58.5481 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f57aca-7280-3b26-bbe5-97cdb09acbca | -11.89986 | -46.56849 | 2026-10-09 05:23:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cfbf173-dc23-3b0f-9ad1-df5379ee305a | -3.0923 | -59.25817 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b065797-2a55-3b57-ad69-3af7fc89d805 | -9.26079 | -60.88807 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4804027d-9bb0-3472-bfa6-94aee296bdd4 | -4.32974 | -55.02077 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31b59020-4caa-383b-9049-7a384530fc80 | -2.51099 | -56.16018 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35136883-6ef7-3446-8158-bb1eae1652a3 | -3.12065 | -53.79899 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8eb470a9-8f4a-328c-b6d9-2508db518f62 | -2.58506 | -56.15609 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f908945-8448-3aa7-a2a6-1c1a2cfa32f5 | -3.87133 | -55.99852 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f03d017b-7c6d-3e4e-8331-4b1e19a2772f | -11.31733 | -46.65809 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd543de3-ccba-34b4-8bb9-a9808b90bcea | -3.44835 | -60.25038 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74879b70-1884-3152-b848-bc71e380e913 | -2.98385 | -54.06009 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86df1d3f-a666-3ccc-81ee-177228b0c3d0 | -3.64685 | -60.63146 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 438f5989-3f90-38ee-a6a7-5586a71eeef7 | -3.5249 | -59.33717 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f79b5eff-7ffd-3bc5-bd06-91cf0e99c2c0 | -3.39707 | -60.85392 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d9bb58c-bba1-3589-b757-546103efb813 | -9.7196 | -46.94696 | 2026-10-09 05:23:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d33dfc9-658d-3f6e-b809-b751ae7f5261 | -3.43628 | -57.96893 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abc41cce-1ebd-3de7-ab1d-b65f442babb5 | -10.02273 | -48.03514 | 2026-10-09 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d16244f1-46be-3be2-a1e8-cfb6526d4902 | -3.79189 | -59.32604 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef9102d1-8752-3f1f-98c2-f49ee366250b | -2.93379 | -54.05244 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2fe891-2916-3fb7-a1de-a647f5d6a56b | -11.40384 | -46.68012 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 155d5b51-499c-3481-83bf-c854b321a07a | -4.28254 | -55.72323 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6166668-f121-3ec2-be12-12c26bcef150 | -2.8807 | -54.201 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b97fa25-5f08-3c4f-a420-0e1e2eef62d4 | -3.22084 | -54.30025 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab0c9653-b15c-3345-97cd-96c7f32707bf | -2.07859 | -46.57542 | 2026-10-09 05:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ffdc6ff-41bb-3ab0-84ad-e87f8d86fbd2 | -3.08458 | -59.19977 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fee212ea-b711-3975-823c-8d2d07e2109f | -3.28344 | -60.9953 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e39dda-0161-3a16-b93a-4e8763a9ff2d | -2.8334 | -49.5122 | 2026-10-09 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3909f631-989b-3e09-a33e-43f3d204ab16 | -3.0862 | -53.94471 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64a3b153-41d0-359f-bce8-03bcdafd8df1 | -3.29383 | -51.56946 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5433570d-4fa0-3107-8ff8-a955bb17d9a0 | -3.51863 | -58.02786 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af5501d0-d0a6-31b6-bfe3-3c0a61000819 | -2.57871 | -56.17432 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ee66f90-e163-30c5-9490-7c8f944f2509 | -8.97016 | -45.91598 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a5664ace-16b4-3c86-8959-ef381f711892 | -3.5994 | -61.63992 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6f0c579-6f65-382a-82b3-983d9689d562 | -2.88355 | -54.15814 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0a8c6c1-72d2-3742-9132-c4701586b131 | -6.67784 | -63.02569 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c5ca4f1-6df8-313c-b82c-b3daa0eabed9 | -2.50821 | -56.13279 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f081b77-581f-3677-a624-670a9af0114f | -3.88394 | -51.93695 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08fff010-9674-378a-96b1-2f1a5e9814ca | -1.42089 | -55.71896 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e42f43a7-642d-3d8a-8524-6a2553354dfe | -3.56784 | -54.68398 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a7f28be8-27b9-3561-91f7-7e04a3e369e3 | -11.32437 | -46.65868 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55436310-e79c-3d58-b9ca-caff8f69d579 | -3.26525 | -54.06035 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4f627ae-65ef-3cfb-85b0-d7a03305ef79 | -1.62643 | -55.12814 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57e73004-8452-3624-afb2-e157a4383525 | -3.02185 | -54.18456 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ce750dd9-59a1-3f20-87f0-684b2df23a9e | -2.57511 | -57.13814 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 553759b2-d454-3b43-8064-57f49840e96a | -1.21313 | -54.01753 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 782f8eb4-6729-33c3-826e-d9322aeb6080 | -3.09082 | -53.94051 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac338871-1fc1-3b32-9834-5affc3e42696 | -3.88006 | -55.82639 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24721ec5-176d-3fe5-9a26-9711d7817cab | -3.42743 | -60.22828 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0150280-9805-30c3-91e1-a95f67294c8c | -3.59266 | -58.71998 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f947e33-5c79-389c-b6de-ef264acb2538 | -2.47582 | -56.09757 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d57b197-78d6-3e59-bb71-b0ed58786a2c | -2.62109 | -57.7095 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77640cd3-f1d0-356b-9170-e4662df77b13 | -3.08394 | -53.95935 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f50edb37-31e7-3e98-9c28-fffc31333d9c | -3.18632 | -60.3992 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3febebe9-07c5-32c5-8b06-bb25152bc359 | 0.55449 | -51.66448 | 2026-10-09 05:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abae53b5-1cf1-30ad-bb0f-2284d0668011 | -2.15576 | -60.00078 | 2026-10-09 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3728cbd4-1240-3cc7-9915-36a29051bb90 | -3.85564 | -51.94167 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70a37eaf-b5bf-3bd4-8479-137ae17f0832 | -2.75796 | -54.0934 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e990b099-9ede-3fb7-bd5b-89170e239e34 | -2.13761 | -54.47075 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 97714d22-77d3-3d6e-b9a3-168fbbd224fb | -3.63935 | -60.63411 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5786e1ea-bac9-305d-bf73-1fb43f291c76 | -2.27861 | -56.99439 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73f12008-aedc-34a8-9f0c-bcdf0678bc93 | -9.86934 | -50.49436 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b369c0b6-5874-36fe-a36a-1e4e43ef49a0 | -3.72453 | -57.11208 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README179.md)
