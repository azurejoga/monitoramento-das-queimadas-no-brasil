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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2deeb43f-7339-3bd1-81c4-04c324b87e33 | -3.07149 | -54.2418 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5250142-3972-3315-8f71-99d885c77370 | -3.05496 | -54.20939 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29572d17-7bdd-348b-aed3-ed583fb731f5 | -3.05418 | -54.21459 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5d4fc8df-fc32-3efd-9063-40835b5a558a | -6.48387 | -62.85796 | 2026-10-06 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3029d39f-b9e2-3be1-ae4a-36c2b7db63a1 | -4.45847 | -54.96133 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0af0ea3-6cc7-3e67-b52e-06118e814c02 | -4.06246 | -56.3326 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e048e5d0-53ae-34f5-8e1a-06af922fb231 | -4.46347 | -54.95823 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 491762c9-656c-3337-955d-0c8dc7dbb3bf | -3.07244 | -54.18021 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b93546d0-81cf-310f-8903-d48680643190 | -3.17222 | -58.6376 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f46af907-8d97-3643-8329-5491e5364871 | -3.23516 | -53.88126 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e61c676-484d-3e4c-ac40-cba7a9ddeeba | -2.78303 | -57.68195 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a18e26e-00fd-3339-b163-02fb80bfb8c0 | -3.37876 | -58.20256 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8df959e1-7350-35b7-92f4-1f2c4d318caa | -3.02116 | -53.90045 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e044d625-47bd-3137-8d3c-49923e843f5b | -3.68131 | -55.94395 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3a84b15c-1a46-361d-9832-f28fdf2a763a | -2.87204 | -54.1477 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a54e10f-45f4-39b6-9fe0-b2f4c31efb92 | -3.87072 | -55.819 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 556aece5-4081-3887-bc0b-77320f31cf3f | -3.07077 | -54.14767 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff311292-bd4a-32e4-8198-34342dd7f38b | -2.99182 | -54.1035 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09aea124-f63a-3007-a5ee-0e67bcc12be0 | -3.4918 | -54.61967 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7af80969-cefd-3690-a45f-e57171627f35 | -3.09968 | -54.18253 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebff021e-37c3-35cd-b93a-f50ec5e02778 | -3.50216 | -54.63645 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81749939-30b7-3375-b972-a8e4a3092409 | -3.68187 | -55.94001 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58c809f1-0528-36b2-8ef0-1cf0ea528d33 | -1.61825 | -55.11558 | 2026-10-06 05:59:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9118ad2f-d438-3b79-8047-e5a8e6459f9b | -3.10043 | -54.17741 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb311df4-f4f0-3155-9593-d6ae43f5f251 | -4.45654 | -54.96233 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2824facb-de95-34b3-887d-779346a8f064 | -3.07078 | -54.24677 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1c8f7803-6db8-38bd-b7ee-baaf736873b9 | -3.49877 | -54.61592 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f07c800-3f1e-3470-bb42-153b6aa4348f | -3.09932 | -53.73219 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09b58648-3aeb-349f-a5d1-4432dbb655b0 | -3.05825 | -54.2311 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 277bb3ad-9c1d-3c59-94ec-11639cfbe078 | -3.07025 | -54.23816 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e1c13b6-e088-3323-98dc-18c91d48085c | -3.082 | -54.16881 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baeb9572-e2a0-3df8-b3bc-b05238e1b8f9 | -3.00728 | -54.13281 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19f28cfa-0370-37c5-9486-ebcf387b76e1 | -3.0877 | -54.16602 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2afdb59c-ad70-3ee0-92a3-12f7d4ab31ad | -3.69108 | -55.95477 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23c503d0-d38d-3dd3-aa34-8c669d2bac55 | -2.15241 | -59.22437 | 2026-10-06 05:59:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a322f7e1-1e82-30b1-9ad8-762808c4e47d | -2.87527 | -54.16954 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d5b39be-30b5-3230-830c-0f203a24e786 | -3.08355 | -54.15797 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d80cdc7-8c8a-33a7-a5e0-73dfa546399d | -3.02275 | -53.88949 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e33018d0-2329-33ae-9493-99f316242491 | -2.99176 | -54.10288 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfc8bed7-353d-3560-a97f-cf39768c7cbf | -2.92279 | -54.12455 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74a13ab9-2f6d-307c-8272-2796a7e19002 | -2.99445 | -54.13073 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b4f3465-9f30-3770-bc0f-689f21e26a1e | -3.08424 | -54.24392 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7d97b822-b55a-3dfe-acbc-1872dec7b87e | -3.08854 | -54.16052 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c463e6c3-376f-3912-8b7b-4e7bcca93158 | -4.46468 | -54.9623 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f2e40ea-d014-31c5-8b93-59f44d6b12bb | -6.48696 | -62.86316 | 2026-10-06 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35eb4ecf-95c8-315d-b040-114b8489ec95 | -3.38205 | -59.43155 | 2026-10-06 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb1cba72-20fb-39ca-ab5d-6b0fc9582024 | -2.77631 | -54.08555 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a4d6d75-c661-3bca-9f8a-5e2beb1f1226 | -3.68074 | -55.94791 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a801c0e9-c164-3087-9580-25215e83540c | -3.2304 | -53.88041 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e4900b6-2932-3843-8693-d8ac1fef5895 | -3.22386 | -53.87937 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a252107-5ea4-39eb-8046-1359bda963c3 | -3.02982 | -53.89575 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a24e7e96-16c5-3fa7-857c-b9b8f9693f33 | -3.07639 | -54.25311 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd5428ec-09ef-3bc8-bbe5-9b569c75d59c | -3.06951 | -54.24305 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5832cd1f-9c8f-3a46-af83-2407f9346b26 | -3.02413 | -53.88935 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 24796aa9-46d4-3653-9047-ac3043f12560 | -2.78351 | -57.65697 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f60522b-1c9a-3f4a-a685-1482bef870fe | -2.78722 | -57.6666 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f94f864a-8e8c-3636-a669-e2348c84f6ac | -6.758 | -55.46983 | 2026-10-06 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9d456ca-d00e-33c1-9871-143245ba84d6 | -2.9958 | -54.11958 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 886d4600-8ecb-3d44-a079-197e627a1b5e | -3.05185 | -54.23017 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8df7bd87-e779-3702-ba84-a19b4bbc2f70 | -3.08919 | -54.16439 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3ad6a76-d6ca-3fb1-a9f5-6eb08ae0f837 | -3.67609 | -55.93908 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a4cb065-478b-32ba-9745-a1d8cfcb3510 | -2.9446 | -54.15442 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05b81780-5c5d-36d9-bab8-ecda66d7d2a5 | -3.05981 | -54.2207 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed2f8915-9f87-3738-a15c-b308e1068e7f | -3.96055 | -56.054 | 2026-10-06 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9b4505-0ad9-3ea7-93d4-dc583d47784c | -3.00063 | -54.13105 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 219e6a33-73e5-376a-8acc-9c9ba4bded1f | -3.02927 | -53.89046 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f747763b-ac30-3d5b-a9a8-7ecca0a218e1 | -3.07565 | -54.25821 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2614e9d2-1086-398d-a4b7-c5a93d66572c | -2.87118 | -54.16379 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2d635b1-504a-31ac-aece-7f390078a6ab | -3.07487 | -54.16409 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26956c21-328a-3189-bbef-efa8827a287c | -1.61235 | -55.11457 | 2026-10-06 05:59:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80bce744-5459-3374-b341-da28c6d1f1e4 | -3.23123 | -53.87489 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9151108-ef0c-3fa3-b843-6096dcb03617 | -3.37547 | -58.19062 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b90da26e-cb92-3fb2-8d6b-b7f4bf3563cc | -2.15453 | -59.99926 | 2026-10-06 05:59:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d87ad07a-6906-3e95-adc5-c31d9d61e949 | -3.07644 | -54.15366 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bff44aaa-c217-3738-bada-61f71d1857e8 | -2.41805 | -56.53428 | 2026-10-06 05:59:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 177c1652-b656-3e71-94c6-1da5c4388929 | -3.28381 | -54.18256 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbd99c67-7df7-3894-8bee-e1d43b4f4ab7 | -3.06999 | -54.15285 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8af9d235-8215-35ce-bd87-a976bb785bc5 | -3.02195 | -53.89499 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0ae2cfdf-1372-3adc-b347-94bcb2ed5191 | -3.08069 | -54.2555 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8b16497b-a6c9-3b66-b520-72356be680c2 | -2.78305 | -57.65992 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a8c7aec-6e82-3b9f-99e1-53ca97df79d3 | -6.75736 | -55.47459 | 2026-10-06 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7d46fa08-5433-30f5-aa98-f7fae07d31f3 | -2.89043 | -54.15606 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f164038e-b87d-3129-a998-c0c0b14e04c8 | -2.80017 | -54.1419 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03e0be28-2c8b-3efd-b2fa-d7bef8f55a66 | -3.22958 | -53.88586 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 466df0da-2392-358b-8498-26f19743f429 | -3.08279 | -54.1633 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab861457-b351-3584-a200-e4bf0553a719 | -3.05607 | -54.24559 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bea03190-6741-39bc-9ae8-1c51b91b2ee4 | -3.085 | -54.23867 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11fc92a8-6c1b-3446-aa8d-0b77286ba23e | -3.0829 | -54.15436 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80b0feae-22d6-3aa0-9a03-40f08b6c6984 | -3.06277 | -54.15723 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5606f2ea-b26f-3f43-b358-c1358481cf87 | -3.21733 | -53.87835 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e93c4b71-4c38-36ca-a553-e2575cc9bca3 | -3.06921 | -54.15805 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2676e9ec-7613-36c7-92d7-ec1eca333e3f | -2.86792 | -54.13166 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36b02724-252a-33d7-83b8-863b31cf7f8a | -3.09355 | -53.72559 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4d40aec-b6d9-3a33-9e90-289fa2409fe2 | -5.68272 | -53.49692 | 2026-10-06 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cfe8162-a58d-30a6-9a4e-c014123ed522 | -2.87412 | -54.14346 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e2eb290-c28a-335a-b2a8-3ffd258da41e | -3.09325 | -54.18171 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c4085d3-9207-30ca-b5e1-894b7f9852e9 | -2.87759 | -54.16469 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1224e363-02af-3d47-a97a-cf1359142482 | -3.46651 | -54.59188 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 511af5ea-76ad-3c3c-a222-44efa25cbb78 | -3.07222 | -54.23678 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6aa0318-cc39-3c82-973c-aa888d3b62d1 | -2.87132 | -54.15244 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README70.md)
