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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caa2ee33-a9ba-3fb5-80cf-3a911dfc9047 | -3.32752 | -53.24526 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a031794f-7ac5-36ac-a719-3bfbac9180ca | -2.81771 | -53.06959 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50f79764-adc0-344a-9bec-18d93797d518 | -6.91052 | -43.50902 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 08904abb-e6d3-3e81-ac81-12ef45fa6783 | -10.50854 | -44.8737 | 2024-12-11 04:33:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41b48dba-840b-3a98-b16a-199031660c50 | -6.90339 | -43.50282 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 11611f3a-67b3-3059-a12a-79343373b55c | -3.06787 | -53.79852 | 2024-12-11 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1927843-c333-359e-8e3d-dfeddd34263e | -5.98345 | -44.59794 | 2024-12-11 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07b9eb97-8d7e-3eb7-bfc5-d653f37aa860 | -6.94649 | -42.98696 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bf8fb70d-d417-3b3e-a17a-64eddabc2750 | -6.91278 | -43.49385 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 16644af2-138b-3a69-9e98-02951ff3da88 | -6.91127 | -43.50399 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f68e1d96-13f6-3981-b279-e1c9a9f3717a | -6.12305 | -42.52569 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6bd74ac0-6a51-332d-9407-af0f35bb43a9 | -3.12798 | -54.09443 | 2024-12-11 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b56e838-3761-3832-b8cd-71816d74ae5b | -6.97907 | -42.99206 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 36318bc4-00e2-3b64-b52c-d8cdfae25f02 | -2.96255 | -53.72451 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d57bd9a-9048-3acd-ba2f-8eb83c19af5a | -2.6471 | -54.38765 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4f8d93ea-2d3a-341c-9245-349c394f6820 | -9.78138 | -43.99282 | 2024-12-11 04:33:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 447ca387-cd73-3126-a460-f703b11c94c6 | -6.26534 | -43.56223 | 2024-12-11 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| deff5415-eea7-39d1-8eb3-04646462b265 | -6.90534 | -43.51475 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f4bebf47-218b-3bb6-92f2-f71267d40a01 | -6.91597 | -43.49947 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed385a58-d5a2-3e1c-84ba-d235aa45503b | -6.12251 | -42.52943 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7540b2e4-b4e1-35c1-886b-1561b3a0ec62 | -6.96331 | -42.98586 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a937264b-e287-39d5-975f-58a539e8611f | -6.12861 | -42.5459 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 509596e0-fe5b-32e9-affc-40fccf9f77c9 | -6.96738 | -42.98653 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3002c573-5674-3b21-927b-956498969670 | -2.26275 | -53.84781 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eb7055fa-718d-36f5-9c58-7945a6a208a2 | -6.26607 | -43.5572 | 2024-12-11 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40ddfe0e-841a-32e4-82fc-29aa7ef4ef14 | -2.41132 | -53.69775 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19e5a326-593e-34a0-8c1f-3430a4432b96 | -6.90658 | -43.50843 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d81c0b4-f672-3a55-baa4-5728bd6950fa | -6.90462 | -43.51981 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 12cc80af-0455-3a06-bf57-651c07f8433d | -1.47514 | -55.39305 | 2024-12-11 04:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ceb4dc1-3b85-3e05-9eb8-95d8ae59c0db | -6.96172 | -42.99671 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| feec4d23-942d-3bec-9c73-4d2e1d34411b | -5.07132 | -37.71508 | 2024-12-11 04:33:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 06935e29-c469-3ab1-922d-0de7f9b86310 | -3.09561 | -53.7395 | 2024-12-11 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7646be49-00ba-3f74-b21a-82803df6ff6a | -10.54246 | -44.68201 | 2024-12-11 04:33:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a73edab8-4a49-37c8-a916-8018437b4e34 | -3.22281 | -53.13947 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f553a9-99bd-3a77-bd30-80c6b1b842b9 | -5.85587 | -42.42561 | 2024-12-11 04:33:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7662e3b5-205f-3ac8-a4eb-faa3c0901c59 | -3.51502 | -54.17824 | 2024-12-11 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2df7b7d-cb10-3e7c-b4c9-f74332aa271c | -6.9107 | -43.50528 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bfedbfd2-8456-317c-add3-658dad74738f | -6.96986 | -42.99801 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| bcbf1760-f761-32e4-bb45-60ad660d14c4 | -6.90605 | -43.50971 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b2b54243-a8ce-3d74-b1ee-98adbe724bfb | -2.82134 | -53.07331 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d37eae5e-b3df-3a44-81ca-670ced2a9e1b | -7.07229 | -39.78845 | 2024-12-11 04:33:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9017467-aca3-3e02-b15f-2b5bd4f03f73 | -6.90264 | -43.50784 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| ffd07b7e-eb75-3fb4-8410-df08d8fabc3b | -6.94491 | -42.99785 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79541315-9599-392a-b5de-a7e01252b2ce | -2.79024 | -52.86259 | 2024-12-11 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e14b8921-0fb2-3356-8b86-88a99c264af8 | -2.29605 | -53.91137 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79c1e1d3-e0d5-3d99-897b-9da001af6215 | -5.9828 | -44.60221 | 2024-12-11 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3678df8c-3037-3845-8734-783b552e1075 | -6.16292 | -44.42269 | 2024-12-11 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eadd7e89-cb4e-384c-ad84-2ad5aa32b14d | -6.95765 | -42.99609 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 8df51e0d-6e1d-3506-a3d7-2ea565ec5525 | -7.21261 | -39.77481 | 2024-12-11 04:33:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bebebad0-802e-38f7-9652-74cd5df3fc84 | -6.94898 | -42.99847 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f34d15da-4337-3f54-a879-7beac61989f5 | -2.81709 | -53.07353 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f1df271-5796-3512-93ca-fd02625dfc5e | -6.12556 | -42.53765 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 6ae2eedd-db8c-31a6-a64d-c510bfbba41a | -7.8758 | -35.16315 | 2024-12-11 04:33:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3bb4a2da-1474-3082-bbb4-06877e932dca | -6.95358 | -42.99548 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cb6bf3c4-1309-3fdd-a30d-c16a4b700069 | -2.64246 | -54.38686 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2048f2e4-d454-386f-8d40-7aa27459db27 | -6.1025 | -44.04438 | 2024-12-11 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7bb9278-5594-3a9b-8a26-5bba174f7287 | -6.91674 | -43.49438 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd5a483-3dca-3278-b251-b7d16ff5db11 | -6.97253 | -42.97986 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc1aeaed-5d7b-33d3-a1b0-6154e41ff8a8 | -2.96698 | -53.7252 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8c38349-e80b-3bfb-b5a3-d2855d444481 | -6.96225 | -42.9931 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 94283836-8d9c-3a89-8c05-5643cbd9254c | -6.97853 | -42.9957 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c6cdfc11-8731-3b4f-b592-fbc668589cab | -2.26048 | -53.84531 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0937f344-b614-37f4-95c0-d17b18aa1a46 | -6.96933 | -43.00163 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 4ff22916-dda4-391b-b3da-7e49905ae889 | -6.97039 | -42.9944 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| ed319332-e5f0-349d-a14d-d84bdc2d8b44 | -6.90999 | -43.51031 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8df19958-a986-38e4-b4e2-10281508f969 | -9.44008 | -43.21214 | 2024-12-11 04:33:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f57f8c59-6444-3ae9-8027-545f46408112 | -6.90584 | -43.51344 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3c86dcb1-914e-3550-90f5-2e334b53abb6 | -6.91537 | -43.50077 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| de1f0c00-5a35-39e6-85d4-8470c3096107 | -6.95712 | -42.99971 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 80672203-7a66-3e43-88ee-44bf3367b219 | -4.55267 | -48.00762 | 2024-12-11 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2054807d-6143-3678-b08d-fe0a75fcb3a3 | -6.96119 | -43.00034 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| dbb3d6c1-d4e4-3946-b057-428cc0b86674 | -6.96792 | -42.98288 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cd3cb622-41a7-362f-84d2-593ffaa2eddb | -5.69019 | -43.18745 | 2024-12-11 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 735cf7d9-3948-3e84-ae74-2aaa89b6613c | -5.42699 | -39.52683 | 2024-12-11 04:33:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0aaceea8-15ba-302e-a4bb-d45b1012ace2 | -6.95977 | -42.98158 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1e0717c-0548-3ffe-a146-1672fa46b6b0 | -6.12446 | -42.54524 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 168b69e9-ea1c-368e-94c6-60fd70a93340 | -5.34673 | -42.12402 | 2024-12-11 04:33:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eaec126c-7f8c-3276-b298-a6e8ba760bf7 | -2.96184 | -53.72886 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fced3fb6-c3ff-3256-a9f6-e370da91f8c3 | -7.86731 | -43.08878 | 2024-12-11 04:33:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b8c91d1b-9f14-3603-b5e2-383a1caea275 | -2.67601 | -54.26818 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d30cd60-ddcf-3905-91f5-6a412746135d | -6.96685 | -42.99014 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 1197dcea-a33b-3cc0-b860-0a9efef49b62 | -2.45802 | -53.98167 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d73784a-7e53-3978-876c-f7050e7ccb01 | -4.55321 | -48.00417 | 2024-12-11 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb8bccb7-c90d-3074-af93-2fd58db13850 | -6.90068 | -43.51922 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e68ea98-1e35-3471-aef0-ab802fd75796 | -6.9734 | -43.00226 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 0ca9941e-3320-36da-9134-89ac3269c09b | -7.87664 | -35.1564 | 2024-12-11 04:33:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c5291e8f-9865-361b-b9ae-1da99e9c0faf | -6.09872 | -44.04385 | 2024-12-11 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e467a5b1-575d-32e5-8a06-7e9662284f7b | -5.2994 | -43.28041 | 2024-12-11 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f5ff4af-ba30-3d5f-b36d-014f65b536f9 | -3.53158 | -53.9417 | 2024-12-11 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78138af6-8521-3ed0-9ca6-27c2bebb6707 | -6.96385 | -42.98222 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7df6e0b3-cc4b-3a06-b6d4-8d1035d0510b | -6.12392 | -42.54898 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 678ea508-0343-3917-976c-166fc2da6d59 | -2.45076 | -53.70799 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f903e4-b41e-32b5-b212-0342e04a0ee8 | -3.33793 | -53.07057 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d71ae95-1505-3885-a52a-37cb286913ac | -6.91215 | -43.49513 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9a3224b7-7271-3395-89c7-023d8f570c54 | -6.94543 | -42.99424 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 466a7045-1af2-310e-8874-9cc6c7f8bd3f | -2.61383 | -54.2437 | 2024-12-11 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fcce94c-dfc6-3595-b3de-20ecf427a888 | -11.04427 | -41.97998 | 2024-12-11 04:33:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5da1e968-3d22-3a9d-8c9a-f7572a89ef34 | -3.33176 | -53.24602 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 796005dc-1a2d-3af7-b782-81ee2b94caa4 | -2.30927 | -54.00318 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99b6baa3-0d7f-3e6d-a273-1b689c99c9ef | -6.12501 | -42.54145 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |


[Clique aqui para ver as próximas entradas](README16.md)
