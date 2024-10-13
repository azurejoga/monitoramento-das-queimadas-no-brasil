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
| 31d85c86-5695-3007-b74e-a1217f48e320 | -5.12188 | -41.69156 | 2024-10-13 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3fb8c8ab-0e4b-3390-92bd-f7f629140cc8 | -5.11901 | -41.68357 | 2024-10-13 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9e064acb-7a8c-3605-a872-1c553b90083b | -5.1178 | -41.69086 | 2024-10-13 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5a024fa6-808f-35b7-8619-182ec2962690 | -5.11719 | -41.69452 | 2024-10-13 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d7e50d5b-770f-3c79-8edb-ffe9102b5f4e | -5.11493 | -41.68288 | 2024-10-13 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1982987c-5645-3637-972e-2005e5b5df56 | -6.59111 | -42.04168 | 2024-10-13 03:47:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0989e2c7-142d-3c3a-8d42-235dcc86be3a | -7.65854 | -41.52593 | 2024-10-13 03:47:00 | NOAA-20 | VERA MENDES | PIAUÍ | Brasil | 2211506 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b048cc7-20f3-38a9-9f02-3320237eec0d | -7.34287 | -41.11712 | 2024-10-13 03:47:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7666ae27-d0fa-315d-aa2f-01bebe524602 | -7.3421 | -41.12183 | 2024-10-13 03:47:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15b44744-ad87-3e09-b895-85648600576f | -7.34158 | -41.11829 | 2024-10-13 03:47:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b8afa750-299e-3724-a4d7-66d2a6da9bd7 | -7.33722 | -41.1905 | 2024-10-13 03:47:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3b4a2920-9ad1-3269-8962-3a21398ef178 | -6.74277 | -41.10547 | 2024-10-13 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 045740f8-fb90-35de-b464-9307154f5c91 | -6.73893 | -41.10483 | 2024-10-13 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12191145-1549-32a9-ab02-7905d3124ae6 | -8.05868 | -40.94072 | 2024-10-13 03:47:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| aa1728e3-0d22-3ebe-893e-c4736580983a | -8.05792 | -40.94528 | 2024-10-13 03:47:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 77824c73-9b10-362b-ae5a-ad2ef01cd086 | -10.51034 | -42.50831 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d309ed59-aa12-32ac-88b6-13bc84404a09 | -10.50945 | -42.5135 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 818d6b93-c891-31e8-81cd-d50beecf7c70 | -10.50638 | -42.50763 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 6dcc6ef8-69dc-329c-888e-476f68e2be9f | -10.50548 | -42.51282 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 97a7dc38-7236-3859-8595-b921c4e98d1e | -10.50458 | -42.51801 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e06e36e6-5138-335f-bc58-308c857b6b8e | -10.50152 | -42.51213 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 7db2e175-8461-34c5-a3e1-d5d4dde207cd | -10.50062 | -42.51731 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 971f33b8-7844-36a5-88c3-a6028b3cfd5d | -10.49937 | -42.50108 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 317b66f3-6094-3c1c-b693-8f41f7b9629b | -10.49757 | -42.51144 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b962d567-59fa-345d-ae19-2eec72cc2f87 | -10.49632 | -42.49521 | 2024-10-13 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d122f169-666c-3447-bb12-77083069a5ef | -12.11892 | -43.18906 | 2024-10-13 03:47:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d55d1aa7-c3b4-31c9-b546-d058d4306753 | -12.11493 | -43.18815 | 2024-10-13 03:47:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 10749c6f-7ea7-3cb8-92f5-3891cc42b33a | -12.11092 | -43.18728 | 2024-10-13 03:47:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12bf0a74-69ae-3727-ba49-0f04077399fa | -11.65381 | -41.7308 | 2024-10-13 03:47:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0d5967c-633e-39f6-ad5a-4cbb722b3739 | -11.65305 | -41.73529 | 2024-10-13 03:47:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c646784f-b990-389f-9354-9dc9751b3aaf | -11.04192 | -42.01722 | 2024-10-13 03:47:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6397fa10-3efd-3313-8f10-71a91c35e88c | -13.65141 | -43.0951 | 2024-10-13 03:47:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 15663cca-dfb2-3bc3-a349-c1a1aa1d328c | -13.5095 | -43.05412 | 2024-10-13 03:47:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2def8761-0fd8-3825-ba31-7105847843e2 | -13.21188 | -42.25523 | 2024-10-13 03:47:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| be702422-a278-3bc9-a480-0d0498eb110d | -13.14239 | -41.97889 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fa35ac22-fcd1-36b3-b94a-6e105c9b1174 | -13.14162 | -41.9834 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8b62252-bf2e-3eeb-b9c5-b368e01f2c1b | -13.14099 | -41.96477 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 5f27c095-a8ac-3b63-a50e-dedd420b5218 | -13.14023 | -41.96922 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| dd126220-8d77-332f-a84a-c75b723d8606 | -13.13947 | -41.97371 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a0b87846-5f1a-3b22-a541-db32584edcd4 | -13.13869 | -41.97824 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b3550853-afb0-3184-96ce-7be0802873f8 | -13.13731 | -41.96408 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 2507ddf9-7b80-3521-b43d-102eec4ea872 | -13.13655 | -41.96853 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| a21fdeaf-db49-3712-8159-cdcb1ef23eee | -13.51042 | -43.48194 | 2024-10-13 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9287ce5c-44b6-3a97-8b3e-2b35d3c5ebaf | -13.7845 | -42.5415 | 2024-10-13 03:47:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 43b27683-4d3e-3fc0-b3ae-357f2c163373 | -2.84015 | -41.75222 | 2024-10-13 03:47:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 907f02c2-3b63-3078-87ac-38e013e5730f | -5.09294 | -42.20667 | 2024-10-13 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bf699706-6a24-3668-8bdd-0ca2017bd85e | -5.09282 | -42.20814 | 2024-10-13 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8aee03fd-39a5-38f1-a5b3-37a66657c59c | -5.08859 | -42.20745 | 2024-10-13 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d5351bd7-5cae-3411-b09c-326e3e206d35 | -3.71166 | -42.93063 | 2024-10-13 03:47:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9d12619-368f-3aae-8d65-d0db54735a2f | -4.96373 | -41.81329 | 2024-10-13 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b60f8ad-a4d3-3cf6-b08d-fd86b0eb1c21 | -4.9631 | -41.81706 | 2024-10-13 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f156b82e-381e-3bb1-85fd-7d9d99d8582a | -4.96023 | -41.80888 | 2024-10-13 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50790cb1-908f-354a-bc2d-597f5241e63d | -4.95835 | -41.82009 | 2024-10-13 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32e0d984-8f68-3a36-806e-96e9af0f00ee | -4.95423 | -41.81937 | 2024-10-13 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6191775-35be-3b3e-997f-8efa0b6416e1 | -4.9536 | -41.82311 | 2024-10-13 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01bf2f77-727b-3d53-8a33-50a7574a892b | -6.52375 | -42.24081 | 2024-10-13 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 745f1166-9027-3492-90fb-1ff9badb4988 | -6.51962 | -42.24005 | 2024-10-13 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d86c632-22d9-3d5c-b1c7-3229d1354efa | -6.49031 | -42.25134 | 2024-10-13 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f83490a0-20ef-3ea1-a278-7ad6c230e242 | -6.38252 | -42.04176 | 2024-10-13 03:47:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1387cd89-54e6-3e91-a7e3-5755592529f5 | -6.25741 | -42.50532 | 2024-10-13 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4b2615bf-2a67-3abe-a29d-ff38cf61f614 | -6.25317 | -42.50465 | 2024-10-13 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6211b417-9890-3157-a2fe-4268715558a1 | -6.24828 | -42.5078 | 2024-10-13 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 47450b1e-02e2-3925-9cfe-4158f52e3627 | -6.24764 | -42.51156 | 2024-10-13 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 82525558-0386-3527-b2e5-dd75f18df1c5 | -6.24146 | -42.52221 | 2024-10-13 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 51cd8842-3852-397d-a8ac-d9a7000d5048 | -6.23763 | -42.52272 | 2024-10-13 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18a8d410-3fdd-336d-a452-86f70171591c | -6.08102 | -42.39378 | 2024-10-13 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64cb0cac-7085-3ccd-a885-74f9a89ef011 | -6.07748 | -42.38908 | 2024-10-13 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f2e9b3e-6ee1-32f0-98dd-9252bf74840e | -6.07682 | -42.39303 | 2024-10-13 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9e96a0d-1bf8-30cb-8223-88f23aed82d6 | -6.07194 | -42.39624 | 2024-10-13 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ccd3811-d95b-33d4-aa1f-e54625d6c904 | -5.95415 | -43.19844 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 677fa8cf-193e-32d3-9913-9f410fdfaf48 | -5.94969 | -43.1977 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5999568-28d2-3ce4-a580-15cf6f211af2 | -5.94487 | -42.66368 | 2024-10-13 03:47:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbfcf35b-2dd5-3cee-aac1-e44f6f696589 | -5.8734 | -41.94296 | 2024-10-13 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13b37eb9-605e-3f41-8629-97b4d2c0e0b2 | -5.8687 | -41.94591 | 2024-10-13 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8c766fa9-f269-3f37-9edf-e35315602a23 | -5.86459 | -41.94522 | 2024-10-13 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e2600e3-d766-397b-8c9c-315950960541 | -5.85681 | -41.96684 | 2024-10-13 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4e062d4d-fa97-3048-a2b2-b306051e8bd4 | -5.8562 | -41.97053 | 2024-10-13 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92127369-69ce-32ec-ab5d-f31a06f0cede | -5.85268 | -41.96625 | 2024-10-13 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea05737e-86db-3e1a-aab9-f23202994afa | -5.61695 | -42.78683 | 2024-10-13 03:47:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 05b2bf9b-b8d4-3491-b030-9f76617257fd | -5.79555 | -43.22394 | 2024-10-13 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3f38249-d5e7-3099-9c78-4f819767703b | -5.66661 | -43.3073 | 2024-10-13 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e01a9ca-7536-3ebd-8551-ed85cce8d144 | -5.6621 | -43.30652 | 2024-10-13 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d5136d2-bc58-3bc8-9595-1c4176140b74 | -5.32051 | -43.07447 | 2024-10-13 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d7d45e-a826-3e48-b516-24b2cc06ccad | -6.82126 | -42.76665 | 2024-10-13 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3edfe01-75d9-3394-a65f-1d290059e5b1 | -6.81767 | -42.76183 | 2024-10-13 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9bbd9071-5822-334a-989b-a6f85ae99942 | -6.817 | -42.76585 | 2024-10-13 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd0ad61d-d108-3a4f-80f4-f445d3f747d4 | -6.66637 | -42.241 | 2024-10-13 03:47:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ab1e3f78-88a4-3adb-9d78-c839b28c11f2 | -6.63213 | -42.19246 | 2024-10-13 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf7a9011-aef4-3878-a73f-5a5faf8cb4dc | -6.6315 | -42.19618 | 2024-10-13 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 652ae21c-ec61-3123-945f-7f5be784a17c | -6.62737 | -42.19548 | 2024-10-13 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2c24985d-911e-3b5a-920d-369ad03c35e5 | -6.72667 | -43.56082 | 2024-10-13 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e903ed0a-54d0-3001-bcf8-9efb6a0b4bb6 | -6.72217 | -43.55997 | 2024-10-13 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d8c50826-23df-3532-86e4-90ff249dfb53 | -6.61621 | -43.44009 | 2024-10-13 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d698a437-13a1-3f9e-ab1a-46631555f355 | -7.29383 | -42.23152 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 486ca18e-4e88-372c-b903-62ad11974c3e | -7.21806 | -42.28672 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 61c96d12-9d22-380d-8888-a9de84fbfdda | -7.2162 | -42.29787 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c26d874a-a3aa-3266-846b-8f06b4d15914 | -7.21397 | -42.28596 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b450e61a-675d-322f-aeff-9ee0f54ab172 | -7.21335 | -42.28966 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb50ef50-571f-3629-831a-3add3601aa74 | -7.21272 | -42.29341 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a432bc4c-eed7-3e26-a325-7b7185ecb1f6 | -7.20986 | -42.28525 | 2024-10-13 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README39.md)
