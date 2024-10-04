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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a330d26c-9a3a-3f4a-8126-377ff4eed2ad | -17.0512 | -56.6932 | 2024-10-04 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| b27dc0f1-05ee-3a0f-b085-75fbfad7b274 | -17.1574 | -57.3993 | 2024-10-04 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 1198f1b7-130b-3c1e-950b-5dc08abf2248 | -17.1771 | -57.3969 | 2024-10-04 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.5 |
| 72dded8c-a34d-32a1-bbab-704509234725 | -17.7307 | -43.8127 | 2024-10-04 02:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e33fe834-d6ba-3b49-8353-b0a206748c88 | -17.7501 | -43.8323 | 2024-10-04 02:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6553f02c-657a-3fd0-9f62-73cee596cfd1 | -17.7508 | -43.8079 | 2024-10-04 02:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 62a5dea1-34fd-3fd6-b914-35ddcf7d7125 | -17.7515 | -43.7835 | 2024-10-04 02:36:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5d8ca408-aa41-33d0-be67-8e085281c8d6 | -18.8606 | -43.6084 | 2024-10-04 02:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| 325c4e72-8468-3621-a755-690c822799c1 | -18.8613 | -43.5837 | 2024-10-04 02:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 161.5 |
| ad1da319-3655-3127-b84a-6a1b7dcdd138 | -18.9081 | -42.0315 | 2024-10-04 02:36:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| ed537344-3066-3573-be54-5d01f63ad8ab | -18.9285 | -42.0259 | 2024-10-04 02:36:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.5 |
| 4adbfd4d-2c2f-3103-8c97-b376db07afe1 | -19.3159 | -42.5976 | 2024-10-04 02:36:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.8 |
| d14f4e3f-a525-34c6-a197-63d44229046f | -19.3167 | -42.5724 | 2024-10-04 02:36:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.3 |
| e1e690ec-645a-3e93-ba0a-7449ac0c8d3c | -19.3363 | -42.592 | 2024-10-04 02:36:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 7958c27a-46a9-30b3-b961-ff93341462dc | -19.4899 | -42.8746 | 2024-10-04 02:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| dabb3271-c037-3fd7-80aa-eb5274a685d2 | -19.8516 | -42.3738 | 2024-10-04 02:36:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 218.0 |
| d1b6c543-4ece-3284-85a5-9b894f5ea1f0 | -19.8524 | -42.3484 | 2024-10-04 02:36:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.7 |
| 4b290a01-b0d5-3ac8-8bf5-f55a00469ee0 | -19.8721 | -42.368 | 2024-10-04 02:36:55 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 5ec91e58-e8c5-3bf6-b499-80685a95a4c7 | -20.121 | -43.5219 | 2024-10-04 02:36:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.9 |
| 2322e397-b363-39d3-9064-85214c987e9e | -19.9901 | -48.7144 | 2024-10-04 02:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0fe9b38d-69c5-32a0-8bbb-c15ded7cea61 | -19.9907 | -48.6913 | 2024-10-04 02:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f6e18bbf-cb8d-3076-b0f4-be3fb42bfe63 | -20.1416 | -43.5162 | 2024-10-04 02:36:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.8 |
| e9e7a346-4242-3b1b-a443-0dd0e36bda2c | -20.0104 | -48.71 | 2024-10-04 02:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2c827ff2-e65b-3b9e-8bbb-78f71e6ec5b9 | -20.0111 | -48.6869 | 2024-10-04 02:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3e5299b0-90ec-319a-9273-de9fcfed132b | -21.7981 | -48.3926 | 2024-10-04 02:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 103.6 |
| a4a84893-0fc4-3394-a8c3-02149ed5ce42 | -21.7988 | -48.3691 | 2024-10-04 02:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 108.7 |
| adb2b5d5-f147-3c8b-8d1b-0a2ca181c206 | -21.8072 | -48.786 | 2024-10-04 02:37:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 8f540cc0-a675-30f6-be6a-9d3531b44ae2 | -21.8079 | -48.7626 | 2024-10-04 02:37:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 87585989-4e98-38f3-813e-3d1d9e6e64ce | -21.8196 | -48.3641 | 2024-10-04 02:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 45222355-8e05-3670-93df-3dbfd8498e1c | -21.839 | -48.4061 | 2024-10-04 02:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9c2d225f-c19a-3199-b72a-2ba2e2cec797 | -21.8397 | -48.3826 | 2024-10-04 02:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 151b1a61-bd11-3669-b57a-4796c3c524a1 | -22.2684 | -51.4941 | 2024-10-04 02:37:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.1 |
| 69c40e6f-358a-3298-9958-3e18a05ea80c | -22.269 | -51.4714 | 2024-10-04 02:37:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.3 |
| ffbb19fc-bb42-3e21-9127-6acb27e92776 | -2.9014 | -50.7142 | 2024-10-04 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b975aa82-4e5d-3488-a7c3-51768429f84e | -3.2534 | -50.3689 | 2024-10-04 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| dd3771e4-c7bc-3187-bd77-1373c72f8d11 | -3.3667 | -42.2875 | 2024-10-04 02:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 66.2 |
| eec80d07-c6d3-396a-b7df-5ca21fc8ac11 | -3.3852 | -42.3103 | 2024-10-04 02:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 58.2 |
| cb459666-0c9d-3251-a347-7b3ac3ba12cd | -3.3854 | -42.2866 | 2024-10-04 02:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3345f59b-05d9-3f1a-9307-f4c8b5ee6197 | -3.2899 | -50.4725 | 2024-10-04 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| aa58d579-0bf9-33a2-b10b-6aab89cc723e | -3.2899 | -50.4516 | 2024-10-04 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 194.0 |
| 06da9916-eeda-377f-8786-f2be18af8e00 | -3.29 | -50.4306 | 2024-10-04 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7efda6c9-7bee-3262-aa9e-01eab6b5aac1 | -3.3083 | -50.4719 | 2024-10-04 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| e63405eb-3b07-3694-a13b-007c9fec0d20 | -3.3084 | -50.451 | 2024-10-04 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 65874107-05a5-3218-8168-3046a22b6376 | -4.0763 | -48.4902 | 2024-10-04 02:45:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 97dea867-ab09-36f8-81a2-e21531246cf5 | -4.0949 | -48.4894 | 2024-10-04 02:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 0349a3d7-a231-3b12-88b7-693705ac1fff | -4.095 | -48.4679 | 2024-10-04 02:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cb67cd42-02ae-37d3-9971-d31ee240ca10 | -4.5375 | -43.304 | 2024-10-04 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 58a3e694-9392-3b3d-a2e2-187330499ab0 | -4.6684 | -45.8961 | 2024-10-04 02:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 105.8 |
| de44ad54-1c4a-3449-a737-3864aace1f8f | -4.6686 | -45.8738 | 2024-10-04 02:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 431e51de-7bf4-3d15-b05a-29a40633498a | -4.687 | -45.8951 | 2024-10-04 02:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 245.7 |
| 406d6bac-4f8c-3e8c-8b97-dc10b5b714d4 | -4.6872 | -45.8727 | 2024-10-04 02:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 393.3 |
| 4995ceff-3a10-3081-898c-6efa5f005264 | -4.6873 | -45.8504 | 2024-10-04 02:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bc4d85b0-4329-3819-b202-144e8241a8bb | -5.8216 | -44.1196 | 2024-10-04 02:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7a02f15d-a666-3bd0-8ee8-4f004670b6fe | -7.0529 | -71.7726 | 2024-10-04 02:45:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 911e62a8-ac2c-3ad8-a046-645be4147b88 | -7.0529 | -71.7544 | 2024-10-04 02:45:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 28451367-4239-3b3b-a362-4e6d69175884 | -7.8164 | -50.543 | 2024-10-04 02:45:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 17677174-62f7-31d9-bcf5-acd3e1b139a4 | -7.8351 | -50.5416 | 2024-10-04 02:45:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e4a9ec9c-a66b-32c2-98af-e47879efac25 | -7.8353 | -50.5204 | 2024-10-04 02:45:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2ff8c072-2e6e-3882-9ecd-2f634e7d0195 | -8.6448 | -50.0518 | 2024-10-04 02:45:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 5787f715-51e5-3b67-84f6-a844e7fe824a | -9.1041 | -50.902 | 2024-10-04 02:45:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f4858932-0030-36f6-a471-c3d1359ca4c1 | -9.3115 | -50.8203 | 2024-10-04 02:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 46cf297f-119f-34cd-a38a-a8c7546b1ff4 | -9.3118 | -50.7991 | 2024-10-04 02:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| d58a3057-623e-352f-8c4b-f4af82ee2296 | -9.3303 | -50.8186 | 2024-10-04 02:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 4e50e514-423b-3a38-9f3d-f12a533fb441 | -9.3306 | -50.7974 | 2024-10-04 02:45:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 233.4 |
| 336376a0-9530-320c-93e9-aaf721eebdeb | -11.0723 | -46.5319 | 2024-10-04 02:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ba27aaa0-c34b-3d33-852a-c6b8978e2290 | -11.0727 | -46.5093 | 2024-10-04 02:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e4c91db0-c5f6-3626-b89d-277413f4a6c1 | -11.0914 | -46.5294 | 2024-10-04 02:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 313.7 |
| ed09ccdb-9df8-3129-90bf-851e3860eac3 | -11.0918 | -46.5069 | 2024-10-04 02:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 61d2c33e-e11e-343f-8453-487b58fb484e | -11.5425 | -65.0607 | 2024-10-04 02:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 30f9bd6c-1754-340c-99e0-71ff847de0ed | -11.5991 | -65.0204 | 2024-10-04 02:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 15f1bfa3-7bff-3559-baea-aeae768a68b0 | -11.5992 | -65.0015 | 2024-10-04 02:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 04541db2-10c1-390f-9fe9-210fe62e5026 | -11.6181 | -64.9818 | 2024-10-04 02:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f82cbe64-29b4-3f0f-bd18-c54482ee77f1 | -11.6369 | -64.981 | 2024-10-04 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f1afe006-0d28-32bc-b2ee-0b13b4992898 | -11.8242 | -56.6009 | 2024-10-04 02:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 043c98d7-80b8-3e96-a06b-fc925791d5f6 | -12.5898 | -53.1359 | 2024-10-04 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7c046ff8-3a92-3d4b-9855-3145235356c2 | -12.5901 | -53.115 | 2024-10-04 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 150.2 |
| d4ff239f-2837-38a8-a521-e3107bd3cb41 | -12.6092 | -53.1129 | 2024-10-04 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 3d379bf7-912c-3766-a6c8-c729c86dfbcb | -14.7012 | -48.7782 | 2024-10-04 02:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1484b6e8-1cfc-324d-8822-9c1bc059d1ba | -14.7939 | -48.0275 | 2024-10-04 02:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6c08cb56-ce06-38e7-bc81-4d01237ceebd | -16.1094 | -50.4489 | 2024-10-04 02:46:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| dd2a7ce4-92e5-32a2-a494-a0e93a9c7a23 | -16.4148 | -57.4028 | 2024-10-04 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 9646c69c-3bfd-3852-8e40-a33b13e2b2e2 | -16.4151 | -57.3823 | 2024-10-04 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 5839c81c-3355-39a0-9208-0180f13336e9 | -16.5935 | -57.1988 | 2024-10-04 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 9fea0552-4358-342e-9d67-9feeca98f444 | -16.5938 | -57.1783 | 2024-10-04 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 4bea95e4-8e62-3f5b-8775-385c53bd7c55 | -16.613 | -57.1965 | 2024-10-04 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 1c1b1e3b-e68e-3049-9310-0b964c26ba76 | -16.6133 | -57.176 | 2024-10-04 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 41297fc5-e72d-3ce6-9d66-5f3f56ae3ae7 | -16.6868 | -57.4741 | 2024-10-04 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| c6c70601-cb2e-3ec1-9b93-a8bc5c77e2c2 | -16.6871 | -57.4536 | 2024-10-04 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 935b56b3-5ffb-3657-ba37-96478d2965b6 | -16.7455 | -57.4674 | 2024-10-04 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 666c72a9-fd13-381e-a11d-9ec207ab0269 | -16.7647 | -57.4856 | 2024-10-04 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| acdf7f00-d700-3ca7-ab34-e454fba9cdd6 | -16.765 | -57.4652 | 2024-10-04 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 198ba993-91ac-3176-bab5-5043dc2cc25e | -16.7843 | -57.4834 | 2024-10-04 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 99c3f38d-6a81-3f85-832c-919f0f1b230f | -16.7859 | -57.3811 | 2024-10-04 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 092f4496-ac52-3408-a0b5-8b740d40f679 | -16.8055 | -57.3788 | 2024-10-04 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 098dc4f3-8aa6-3b1c-8370-ac0113099dc9 | -16.843 | -57.4767 | 2024-10-04 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 9edb2cda-712e-3274-8ebc-8607059c520c | -16.9087 | -55.843 | 2024-10-04 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 7ab61d4f-ff45-30dc-b5c6-88b728430b8b | -16.9283 | -55.8405 | 2024-10-04 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| d852069e-bccc-364a-a1da-a9ac1b9197f1 | -16.9287 | -55.8197 | 2024-10-04 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 4495d663-95d3-3f8d-83e1-edc28fa12e04 | -17.0512 | -56.6932 | 2024-10-04 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 4d98c8e7-7642-3d6e-98fa-53ad220e8313 | -17.1574 | -57.3993 | 2024-10-04 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |


[Clique aqui para ver as próximas entradas](README46.md)
