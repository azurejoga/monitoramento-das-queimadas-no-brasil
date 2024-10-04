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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a85c52f-6760-3dee-a733-43b17e0f958c | -17.1771 | -57.3969 | 2024-10-04 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 3c5b4695-33f2-332b-be2b-a87a384a5eda | -17.7307 | -43.8127 | 2024-10-04 02:46:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2b46ba05-2e77-3a0d-b1e9-7aa831773f90 | -17.7508 | -43.8079 | 2024-10-04 02:46:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 2ed57120-dc48-389c-ad12-0e2ee76542ed | -17.7515 | -43.7835 | 2024-10-04 02:46:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f28b8345-5325-3733-9ac6-7c7e89e6de93 | -18.8606 | -43.6084 | 2024-10-04 02:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 69dc8160-190b-35ee-ad75-75278ba56549 | -18.8613 | -43.5837 | 2024-10-04 02:46:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.8 |
| 31e8b15b-a164-319b-9427-04a60223f1a9 | -19.3159 | -42.5976 | 2024-10-04 02:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 169.3 |
| c93a88e9-a0c4-3906-87ac-7a126fde49c5 | -19.3167 | -42.5724 | 2024-10-04 02:46:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| e74eb863-c036-3c4d-83f4-19f226f7ef3d | -19.3363 | -42.592 | 2024-10-04 02:46:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| 0905636a-4113-31af-a40a-b4bffa252927 | -19.4899 | -42.8746 | 2024-10-04 02:46:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 5146e18a-4b81-3543-a192-e0c83bda0bac | -19.5104 | -42.8691 | 2024-10-04 02:46:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| a7747c16-fff7-332a-be1d-18846ed2ca2a | -19.8516 | -42.3738 | 2024-10-04 02:46:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 185.2 |
| 39513034-1586-370e-bd4f-94febba946a6 | -19.8524 | -42.3484 | 2024-10-04 02:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 322ce47e-b827-3793-9645-8044cca5a9a0 | -20.121 | -43.5219 | 2024-10-04 02:46:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 54b816e8-88c1-358d-b55a-c33231b9c5ed | -19.9901 | -48.7144 | 2024-10-04 02:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 219.3 |
| d8871e5b-f1fc-3050-be05-f8f446ecec39 | -19.9907 | -48.6913 | 2024-10-04 02:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 7e00c218-6c45-3389-b463-7623eea0a824 | -20.0104 | -48.71 | 2024-10-04 02:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 4e0b3f2a-56cb-327a-810a-348fda50eaf8 | -20.0111 | -48.6869 | 2024-10-04 02:46:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 197.4 |
| eaa3b151-6963-3649-acb6-ea433f49fe7f | -21.7981 | -48.3926 | 2024-10-04 02:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 9fd1193f-19c2-3305-9766-a795695faeaf | -21.7988 | -48.3691 | 2024-10-04 02:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b88349c0-df5b-39b3-a057-c21b1265b231 | -21.8189 | -48.3876 | 2024-10-04 02:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 16d6bd41-2b85-38b7-9f52-37b8f3e91926 | -21.8196 | -48.3641 | 2024-10-04 02:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 75.7 |
| dec6ae82-a941-31f9-bad9-6c37d5b06bd3 | -21.839 | -48.4061 | 2024-10-04 02:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 3bc553ee-375d-3552-9d7a-f88c39805751 | -21.8397 | -48.3826 | 2024-10-04 02:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 73046d1c-9271-30a4-901f-65abffcbb8c8 | -22.2684 | -51.4941 | 2024-10-04 02:47:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| 7f0bdf96-9e41-3e89-a3ed-a24ed64f42bb | -22.269 | -51.4714 | 2024-10-04 02:47:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| b8efa436-c980-31f2-8659-e72f5e409703 | -7.04745 | -71.75404 | 2024-10-04 02:49:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 839750bd-03d8-307b-8cf2-5ea73c369bad | -8.26709 | -71.14381 | 2024-10-04 02:49:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 999cffc0-0af7-31ad-8b3e-aaaae8b0ab42 | -7.39414 | -72.50613 | 2024-10-04 02:49:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 47ef6618-da1e-3080-80c1-4d34f4dbfdab | -7.37768 | -72.93662 | 2024-10-04 02:49:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 544f05d5-d73b-3910-bfd5-4c89535abab3 | -7.06069 | -71.76673 | 2024-10-04 02:49:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 2069edb8-f60f-3c62-b958-cfcfaef3bd84 | -7.27471 | -72.72618 | 2024-10-04 02:49:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d2688751-71ca-3656-83a7-98903f950646 | -7.05853 | -71.75235 | 2024-10-04 02:49:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| b82d63fe-44e5-305c-b106-9482e81ad438 | -10.25215 | -68.24769 | 2024-10-04 02:49:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 0dd88978-a5f9-300a-9ab3-d3ca8a7b47f6 | -7.04962 | -71.76844 | 2024-10-04 02:49:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 23b3018d-8fc9-38ee-b71b-16a3d15bbe16 | -7.81673 | -35.22823 | 2024-10-04 02:51:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3c57f99-8537-3c39-a03f-8c766741189c | -7.81564 | -35.23402 | 2024-10-04 02:51:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f906a62-985c-38bd-8df8-cb444d8c701d | -3.3665 | -42.3112 | 2024-10-04 02:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 81.6 |
| e5ae74ac-7c54-3878-9147-33fe587aaee8 | -3.3667 | -42.2875 | 2024-10-04 02:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 137.7 |
| 2555e1c2-0a90-3bc0-a6de-2f6e57d8e093 | -3.3854 | -42.2866 | 2024-10-04 02:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d9e7a9af-00e5-3134-acc8-6fdaf5df5ec4 | -3.404 | -42.2858 | 2024-10-04 02:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 9b2c7a2f-32b0-3801-83de-56f85e28d008 | -3.2899 | -50.4725 | 2024-10-04 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| fa07d577-e6d5-3e65-8b61-148f7b1b4193 | -3.2899 | -50.4516 | 2024-10-04 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 227.6 |
| 2b8d9095-26ef-3008-9e8d-67a678a3445a | -3.29 | -50.4306 | 2024-10-04 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cec2f51f-ee37-3c33-b59a-e37c7e37c2e4 | -3.3083 | -50.4719 | 2024-10-04 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| b9ae9ebe-3018-332f-9c9e-c6160c19819f | -3.3084 | -50.451 | 2024-10-04 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 269.7 |
| 17011143-c304-3f88-b92b-9d565a255611 | -4.0763 | -48.4902 | 2024-10-04 02:55:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| e7e49e09-1ac6-367c-ab89-d51fac4c9a75 | -4.0949 | -48.4894 | 2024-10-04 02:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| bf2c0319-87cb-3d41-b8d2-95a69c769a28 | -4.095 | -48.4679 | 2024-10-04 02:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| add00557-204f-3222-a8ee-8529a14052c2 | -4.5375 | -43.304 | 2024-10-04 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 776240fe-d129-387c-8237-91e9c6e80288 | -4.6684 | -45.8961 | 2024-10-04 02:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| cebd2865-9451-396b-9026-04259c61c15b | -4.6686 | -45.8738 | 2024-10-04 02:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 429c02e7-d04e-37f4-be8c-9095d393e097 | -4.687 | -45.8951 | 2024-10-04 02:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 177.1 |
| fca05505-429b-36a8-a52e-80bc0c87c95a | -4.6872 | -45.8727 | 2024-10-04 02:55:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 374.5 |
| e16e2104-3f70-3421-9cdf-f94a10037a32 | -5.8216 | -44.1196 | 2024-10-04 02:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 6a7bf0a7-478b-314c-a6cf-3a972f0f02d6 | -7.0529 | -71.7726 | 2024-10-04 02:55:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8c6d73d2-0187-333f-bca5-5fcb70761c63 | -7.0529 | -71.7544 | 2024-10-04 02:55:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 5f891de7-4407-3b2e-9daa-4b0acace6e87 | -7.8539 | -45.3611 | 2024-10-04 02:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| bd281115-9cf3-322d-aac5-64f15c165f1e | -9.3115 | -50.8203 | 2024-10-04 02:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 210.3 |
| e31111d6-083c-3f11-a58e-fe55c7da378a | -9.3118 | -50.7991 | 2024-10-04 02:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 313.8 |
| 25b3b9ce-81bc-3205-bcd6-b952b4c3c1a9 | -9.3303 | -50.8186 | 2024-10-04 02:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 237.4 |
| 94d7d95b-620e-377b-a59d-4d76b0f4373f | -9.3306 | -50.7974 | 2024-10-04 02:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 377.6 |
| c8ffbb4b-3d4b-3ee9-a0ef-3ca42acba3f9 | -9.3494 | -50.7957 | 2024-10-04 02:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| b6af9dee-c203-3257-ba52-925d9ca597e2 | -11.0723 | -46.5319 | 2024-10-04 02:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f5433f1b-b747-37b0-be14-c89899d2a723 | -11.0727 | -46.5093 | 2024-10-04 02:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 77ef5b90-2279-3104-8799-e02087731a5e | -11.0914 | -46.5294 | 2024-10-04 02:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 7e793461-2dff-39d0-8640-cbbbed0131df | -11.0918 | -46.5069 | 2024-10-04 02:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| ffe5fbea-db89-3c39-8964-0d653b5fd61c | -11.0921 | -46.4843 | 2024-10-04 02:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| e5463bad-37a5-301d-95f2-9ad7aecbf425 | -11.1112 | -46.4818 | 2024-10-04 02:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 0cafcad4-def3-3325-b72e-e0216172128a | -11.2566 | -60.5825 | 2024-10-04 02:56:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1c26bedc-67f5-3622-9891-7c2b6e2150d5 | -11.5991 | -65.0204 | 2024-10-04 02:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 9840255a-d872-3a8b-b921-a22d4ad0c1c3 | -11.5992 | -65.0015 | 2024-10-04 02:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| dfabeaac-07e8-3aba-826f-dd14ff8a78da | -11.618 | -65.0007 | 2024-10-04 02:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 92b8324c-31da-32d4-b1cf-1e4a3ed317eb | -11.6181 | -64.9818 | 2024-10-04 02:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7dc7484f-2618-33a8-a8f5-d7a740df12b8 | -12.5898 | -53.1359 | 2024-10-04 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 8ad26f9a-2a34-3975-8527-67b23b84ac69 | -12.5901 | -53.115 | 2024-10-04 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 415a4142-6640-31c4-9287-c619b7ff9f8f | -13.0598 | -51.1195 | 2024-10-04 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 32383fb8-7ac2-3530-b794-2c4292762b07 | -13.0786 | -51.1385 | 2024-10-04 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 099ccc41-ed4d-3d18-8fe2-6212c84669f0 | -13.079 | -51.1171 | 2024-10-04 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.0 |
| efb5df33-e1ef-3264-ae30-0821c0615352 | -13.1166 | -51.1551 | 2024-10-04 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 80eaf91b-1257-3786-96e6-bef02aa9525d | -13.117 | -51.1337 | 2024-10-04 02:56:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 54aaf3c2-5335-3d66-8649-313ae17dd213 | -16.1094 | -50.4489 | 2024-10-04 02:56:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 78be246b-7e4c-3909-955b-484bac2fc853 | -16.4148 | -57.4028 | 2024-10-04 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 3270279c-e9f5-3f52-a281-0433baeef92c | -16.4151 | -57.3823 | 2024-10-04 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| dafd9161-8730-3492-8cdc-d909f3f10bf6 | -16.5935 | -57.1988 | 2024-10-04 02:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 78bc5110-fc18-3801-b400-0add128683ff | -16.5938 | -57.1783 | 2024-10-04 02:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 89e06525-2c6f-3376-b3d8-e2d1920f0da5 | -16.613 | -57.1965 | 2024-10-04 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 19c3aba5-2ed3-30d2-8cb9-3767e6fb05b0 | -16.6133 | -57.176 | 2024-10-04 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 18f32e70-4a1a-311e-aa81-82a4f5cb2eb5 | -16.6868 | -57.4741 | 2024-10-04 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| b361ec13-005d-30a3-af81-08c18ecd2411 | -16.6871 | -57.4536 | 2024-10-04 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| ba88b084-cf8f-3f7c-9a35-12ab5b371c3a | -16.7455 | -57.4674 | 2024-10-04 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 9e1c9704-e9de-32ea-8d31-5778aaa45f5e | -16.7647 | -57.4856 | 2024-10-04 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 61a7f2e2-e37e-36a3-b63a-dc8ed66ef738 | -16.765 | -57.4652 | 2024-10-04 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 17023376-1c5a-379e-814f-0892632a8250 | -16.843 | -57.4767 | 2024-10-04 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 2c7453a6-75d6-3b3a-8f15-36494aa18aea | -16.9283 | -55.8405 | 2024-10-04 02:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 156ae839-71c3-3f59-9a1b-faa11a2ae905 | -16.9287 | -55.8197 | 2024-10-04 02:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 8adedcab-014e-3f2f-af60-62091c75532b | -17.1574 | -57.3993 | 2024-10-04 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| db037ad6-0b2e-38cc-929b-058b8a5d66ae | -17.1771 | -57.3969 | 2024-10-04 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 7d5e144d-4f72-3131-83b0-41c0d96f9983 | -17.7573 | -40.1282 | 2024-10-04 02:56:44 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 6d986203-94ae-3120-9754-5ae7d95faa91 | -17.7307 | -43.8127 | 2024-10-04 02:56:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 143.5 |


[Clique aqui para ver as próximas entradas](README47.md)
