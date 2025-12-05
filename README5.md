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
| 0e586156-a38a-3f62-801d-e338f39c5327 | -5.02527 | -43.25126 | 2025-12-05 03:59:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c186477-ca30-3362-9d40-10eae631eec8 | -5.87172 | -35.38333 | 2025-12-05 03:59:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| dc665b87-2766-36d2-8798-01d2c5f3b017 | -4.6113 | -38.67975 | 2025-12-05 03:59:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 58be95d8-bed7-3de8-846d-07fb762071f7 | -5.18084 | -43.07855 | 2025-12-05 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 60d5f00e-5c5f-3aaa-93d5-1de06e761827 | -2.90205 | -45.23318 | 2025-12-05 03:59:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93b38a75-f7e0-3e04-9f17-89b0c5cabd1b | -5.79414 | -35.37154 | 2025-12-05 03:59:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f28000ca-d1e6-376b-933f-fdf594d725bf | -3.63774 | -42.22777 | 2025-12-05 03:59:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 232b4876-5979-33b8-b87c-af93ce65f63c | -4.50807 | -40.51133 | 2025-12-05 03:59:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c0d584a5-450c-3188-8009-856534b300ad | -3.78213 | -40.55967 | 2025-12-05 03:59:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab36d969-2ddb-3028-8a42-bef87682d872 | -5.00388 | -38.5392 | 2025-12-05 03:59:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3417a73b-26b1-3743-bc0d-7646e23c1a80 | -2.612 | -47.00706 | 2025-12-05 03:59:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db7be20f-554c-31a9-bf30-cad5b42c103f | -1.45716 | -46.72581 | 2025-12-05 03:59:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 780b233f-0515-397d-8f6e-794f304aff69 | -1.45907 | -46.72928 | 2025-12-05 03:59:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46a314d7-e19c-3242-994b-96d3eba19bf1 | -4.50196 | -40.50675 | 2025-12-05 03:59:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 422eba5c-1472-32ea-bff2-d2b468079a87 | -3.66981 | -44.82796 | 2025-12-05 03:59:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e35ae95d-d43e-3aec-8579-3a949b8636e6 | -4.41818 | -45.31861 | 2025-12-05 03:59:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7908bc84-b889-3b6b-a79b-29b454a8d79d | -1.45998 | -46.72382 | 2025-12-05 03:59:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6615f421-775d-3055-98d9-5ae48a0b1cf9 | -4.70714 | -44.56321 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8cbef975-ccd9-3abf-9f84-791f3a49e0cf | -5.47397 | -39.51796 | 2025-12-05 03:59:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77678cb3-2609-3188-9c9b-6b9050c7401d | -4.54466 | -45.63504 | 2025-12-05 03:59:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bedad76-fd3f-3ece-84a1-3bb8c8a85fec | -3.34496 | -42.15518 | 2025-12-05 03:59:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 63352762-deee-353d-af97-d46f15df059a | -4.45948 | -38.38689 | 2025-12-05 03:59:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5823c921-5829-3941-87a2-e8be0b4f2e6e | -5.86698 | -39.1114 | 2025-12-05 03:59:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab98c9e4-b47e-3663-b76e-fca08835cb04 | -3.61877 | -40.94445 | 2025-12-05 03:59:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9a29cdef-ca81-37fb-a143-87207c322a8d | -5.22173 | -39.25895 | 2025-12-05 03:59:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55ac7d3e-d313-3f6e-8201-735d12dde532 | -2.6093 | -47.01027 | 2025-12-05 03:59:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10b8123b-f4d5-345c-affa-9c4057f2d8e3 | -5.3513 | -40.85428 | 2025-12-05 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc6726fe-7e43-3921-9752-8ed3862bb498 | -5.01033 | -37.95008 | 2025-12-05 03:59:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66062eae-8131-3455-924e-163cb54aabe8 | -5.62411 | -37.33229 | 2025-12-05 03:59:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9b6c6d6b-55c9-3160-a8fa-a8e24623b08a | -4.70312 | -44.56257 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea6ff34b-1be2-331d-83dd-1719851e1ff2 | -2.90573 | -45.23795 | 2025-12-05 03:59:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1df8337d-6bc2-3a4e-b3d9-169d61c06cd9 | -2.07052 | -45.35488 | 2025-12-05 03:59:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00459e6d-e184-36f2-b580-2d40bb7474e5 | -2.9014 | -45.23728 | 2025-12-05 03:59:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17b8b46a-87c3-3fd0-87e0-4da3f228e3fd | -4.50251 | -40.50325 | 2025-12-05 03:59:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79b75daf-d987-3b5b-8a06-034e302be7cc | -4.90886 | -44.50776 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67dcb33b-32e4-35fb-8bbb-4eb538205227 | -4.64703 | -38.75675 | 2025-12-05 03:59:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e6b13bb-5edf-3595-85c2-6e8289e7282b | -5.86783 | -35.38281 | 2025-12-05 03:59:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| dc6253e5-08bd-3f4b-b082-0fbf7af4d690 | -2.06982 | -45.35921 | 2025-12-05 03:59:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 713ccf88-d047-3e10-ac12-0de9dc981567 | -3.77934 | -40.55561 | 2025-12-05 03:59:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21cfb776-6d74-395a-94eb-a4e54ffd65a0 | -5.011 | -41.00436 | 2025-12-05 03:59:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 680efbb7-6aa1-374a-8fcc-086b7150b26b | -2.90072 | -41.91618 | 2025-12-05 03:59:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2921769f-1382-3223-af94-8e13ee7ebe46 | -3.85822 | -40.78671 | 2025-12-05 03:59:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff99c402-0e92-3621-9bab-24d1a9c2e6ff | -2.6359 | -46.96951 | 2025-12-05 03:59:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 704f00f0-35df-3ce3-b766-3bb9a945870f | -3.42556 | -39.26229 | 2025-12-05 03:59:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c2cbe0b2-66bb-3d8a-93e3-263ba13c44bd | -3.47446 | -43.8791 | 2025-12-05 03:59:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bc36569-0304-3c77-80c2-6fccf34b13b4 | -4.50474 | -40.51078 | 2025-12-05 03:59:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 970edf0e-c61f-3640-941a-6a767462428b | -2.44167 | -47.15961 | 2025-12-05 03:59:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac929063-ffcb-3772-8352-917b85a43559 | -5.35464 | -40.85479 | 2025-12-05 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07185be2-944f-34a0-a50b-fcb0e381e662 | -4.61076 | -38.68325 | 2025-12-05 03:59:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0217e713-512b-3a39-b914-54872e192e0e | -4.45103 | -42.97612 | 2025-12-05 03:59:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 683b4594-160d-3307-9a03-40800dc290e6 | -2.0654 | -45.35852 | 2025-12-05 03:59:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fadadc8d-63fc-3253-9e78-f13743aee9b1 | -5.62063 | -37.33176 | 2025-12-05 03:59:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e4778aeb-8043-3fe0-857c-51ded5888798 | -5.17876 | -43.09148 | 2025-12-05 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccb6d9c5-66d8-34b4-b9ae-452e24fcb6ec | -5.02826 | -43.25622 | 2025-12-05 03:59:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fba490c-af80-3aae-8496-109e55aa2aa2 | -4.70368 | -44.55914 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbbb6f8e-9d40-3a8f-ae26-f7357e374ea6 | -4.20562 | -44.64222 | 2025-12-05 03:59:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93761a44-b843-3d39-8a7c-3a5676c910e4 | -3.42502 | -39.26572 | 2025-12-05 03:59:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e125e3ba-77d8-31d9-af9b-2145f4a88018 | -5.87246 | -35.37846 | 2025-12-05 03:59:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2d2c28ea-0c8d-3e46-87e5-a1145a9ec6b2 | -5.86947 | -35.38044 | 2025-12-05 03:59:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 302fa030-1226-3876-91ac-77f0dfc0a1fd | -4.60797 | -38.67923 | 2025-12-05 03:59:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7fc3f2e6-42a6-3e81-bf38-79f1f906362e | -5.17945 | -43.08716 | 2025-12-05 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 243e6723-c5c7-3ec9-8f67-f69f8a318aac | -4.7077 | -44.55975 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30b8b320-0706-3b2e-a324-14f92e79f100 | -1.67959 | -45.79485 | 2025-12-05 03:59:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a20cfe03-6445-3b7c-9fd9-a2b59a7460d8 | -2.6062 | -47.01158 | 2025-12-05 03:59:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c885bd41-46a1-3319-9cdb-c03768a52024 | -4.53651 | -44.22768 | 2025-12-05 03:59:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f1fd9a88-a4f4-3d43-ab0a-cddb49d22b29 | -3.45383 | -41.31789 | 2025-12-05 03:59:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20ae79fe-cfa9-38c6-a98c-8cf023b93fb2 | -5.02897 | -43.25183 | 2025-12-05 03:59:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d33b8a7d-ca1d-39a6-819a-78f8e7b7e8ad | -2.80198 | -47.34604 | 2025-12-05 03:59:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 186d43fb-e55b-3000-81b7-29b918be6c55 | -3.34561 | -42.15113 | 2025-12-05 03:59:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c415425e-fa5f-367a-a746-1e03d9d1f945 | -4.7407 | -44.43281 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b888b8f2-e802-30aa-98c0-5ef6842ebce4 | -4.91248 | -43.80101 | 2025-12-05 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 333a8f9f-b80a-3558-8935-cb1f89059eee | -4.71224 | -44.45672 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f9597f05-5644-3627-badf-3e824017e480 | -3.17296 | -45.65351 | 2025-12-05 03:59:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fee91d6f-4f25-3ee6-b2da-71d5bcda12d4 | -5.18015 | -43.08285 | 2025-12-05 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 37c9c4b0-8d5f-397b-a562-9c0e6fe54ffe | -5.06451 | -40.47699 | 2025-12-05 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e56d3a25-5d19-358d-946c-7b836cdf87a7 | -3.66565 | -44.82729 | 2025-12-05 03:59:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ede89db-54a4-3815-a6d8-2323fe6270a5 | -2.90406 | -45.23249 | 2025-12-05 03:59:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3381a02-a84a-3d6a-9426-286d7f977693 | -5.62352 | -37.33617 | 2025-12-05 03:59:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bd2792e0-bd0e-376c-a375-10780c9647ce | -3.6714 | -43.60435 | 2025-12-05 03:59:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2836e94-89f4-369f-a6d7-8ffc7697b8ad | -5.62004 | -37.33564 | 2025-12-05 03:59:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8173779c-e0f4-3f55-9c30-8c24fc2b57ad | -2.63406 | -46.96544 | 2025-12-05 03:59:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3eacbdf7-7cc4-326b-9e25-355eaeefb06f | -4.54969 | -40.13908 | 2025-12-05 03:59:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fef2610f-e018-35e9-a510-2bf622f8e5f9 | -3.49841 | -39.90165 | 2025-12-05 03:59:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3fed59a-b074-3ff4-a681-4178ca4865a4 | -3.06127 | -40.08578 | 2025-12-05 03:59:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c17e1d84-f369-3b84-b04c-ed4673ae9111 | -4.55263 | -45.6406 | 2025-12-05 03:59:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 313f457f-ff9f-353c-a181-b0aec8145aaa | -2.91483 | -39.93463 | 2025-12-05 03:59:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f6547d65-6d0f-3c1a-9f8a-f391aac5850b | -3.37756 | -44.10596 | 2025-12-05 03:59:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5af630d-6971-32b0-9f3d-bcb9b107c333 | -3.34917 | -42.1517 | 2025-12-05 03:59:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0b58238a-d572-332c-bccc-f31a479cdc6c | -3.50687 | -44.52159 | 2025-12-05 03:59:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00d3bfac-a8cf-391c-8504-7da3d3aec1ab | -4.71166 | -44.46026 | 2025-12-05 03:59:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de7fbc0d-ef02-3ed5-901d-be82b9301473 | -5.99731 | -35.38176 | 2025-12-05 03:59:00 | NOAA-21 | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf0d69f4-87b5-3338-976d-1dd8816cc742 | -5.00442 | -38.53567 | 2025-12-05 03:59:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| def67d0e-0e40-3255-944e-0b818e047eaa | -4.42242 | -45.31931 | 2025-12-05 03:59:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a778be2e-a8c0-3934-b1e4-9ed91be01627 | -5.6398 | -39.45606 | 2025-12-05 03:59:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 854778c8-4218-3b76-8c0d-d5a151071670 | -4.60743 | -38.68273 | 2025-12-05 03:59:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ce60bf50-2a28-3573-a5c2-d4620a64e132 | -5.02456 | -43.25564 | 2025-12-05 03:59:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 275bd489-8e9c-35c6-bf26-fb24c2148ce4 | -3.17667 | -45.65853 | 2025-12-05 03:59:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23310448-84f9-3468-923b-8715f923638a | -3.24249 | -46.08242 | 2025-12-05 03:59:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95a1ef58-77f8-3d0d-80c2-ea7125edb3ab | -2.80151 | -47.3489 | 2025-12-05 03:59:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c33ba84-e4e7-33cd-84cd-ca37aa968ea5 | -3.0646 | -40.0863 | 2025-12-05 03:59:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README6.md)
