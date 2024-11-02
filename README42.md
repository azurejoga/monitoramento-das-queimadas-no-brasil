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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bcdc88f-9f85-3b02-a577-da8c267be25d | -5.48311 | -46.85743 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8134cab1-dceb-3965-843a-65719ea07aa9 | -5.43441 | -46.50663 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d724e00-ed42-38f8-9746-88ad95df9784 | -5.4336 | -46.50502 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca50acfa-2c7b-3d57-9bd9-49a76d84aee0 | -5.43142 | -46.50166 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5dea824-cf46-3767-a87d-0fdc29c66fb7 | -5.43073 | -46.50595 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1bd1920-6aea-3168-adf6-6b9852ffac02 | -5.42992 | -46.50438 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82737ddc-836a-3b7c-a086-fe324075a868 | -5.38895 | -46.67145 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f88ea83f-c67b-32cf-8665-4153853ef1ec | -5.22413 | -46.73468 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8685126-0f72-386f-96ab-391faf607328 | -5.21964 | -46.73857 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2a50a5e-d709-36c4-bd29-fbe4cd655d6c | -5.21439 | -46.7471 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dc7238e-879a-3964-8eb3-68d83c95f0d2 | -7.80659 | -47.47596 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a52af1f-4ebf-336c-9b8e-2ec7ae1b6463 | -7.80281 | -47.47532 | 2024-11-02 04:12:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dbf27346-3a1d-3d2e-a657-34345ffc3224 | -8.9002 | -48.53596 | 2024-11-02 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb98e165-8ae9-316a-81b4-ddf25db4584d | -8.89837 | -48.53737 | 2024-11-02 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 063f3fdf-ea96-3764-b842-3a176cec8e39 | -8.84358 | -47.72875 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1f0f55ab-8100-3fe6-bcb2-58ecbbe79ed6 | -8.84076 | -47.69966 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c95883d1-9aa5-3e76-ba0a-1e0ff487c396 | -8.8398 | -47.7281 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3a6138ed-9e04-3ae0-8cb0-d951006d21e2 | -8.83698 | -47.69902 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 221bc60f-ae90-3b91-bcbb-145d1bc3d560 | -8.8362 | -47.70361 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6654dc4b-7b1d-32eb-a222-cbfae53f4b0e | -8.83243 | -47.70298 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b2553d1-8edc-3090-93e5-bc2024f469b2 | -8.83165 | -47.70758 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6ec2faa-c2db-37de-878c-9cd0a0840933 | -8.82787 | -47.70694 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6cb3b28-8850-349f-b68b-adab8871b8af | -8.82753 | -47.70934 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ce97eb2-6f90-31d5-a445-f2e006cb162a | -8.82709 | -47.71153 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66642241-fafe-34b2-a557-b9cac6ce0a28 | -8.68347 | -47.96167 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 329ce41d-79e3-354b-893e-deba646ea813 | -8.68045 | -47.95621 | 2024-11-02 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2eeb8692-337f-38fa-bb6c-61efd21b83ef | -3.45554 | -47.66865 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| aaf8adcd-ea70-360f-98ce-90bd54b3b967 | -3.45495 | -47.67231 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5faf4386-59bd-3f63-aeff-69984e42da3e | -3.11 | -48.65515 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6609a9fd-8dcc-394a-9e73-fe7fbeaa83e0 | -3.07359 | -47.58178 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc64788e-a7f6-3de1-b5fb-2d31ffdaf46e | -3.06951 | -47.58113 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8126479f-1b5b-3d98-a32f-b8011ae05d2b | -3.06651 | -48.08971 | 2024-11-02 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 710ed33b-2e91-356a-b76e-9792e573474a | -2.94818 | -48.07068 | 2024-11-02 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e45de82-0a1f-3435-ab96-67da072085f3 | -2.94396 | -48.07001 | 2024-11-02 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51556187-29b4-375a-b8ad-8d26839825ca | -2.91891 | -48.61235 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b030300-28d3-35c6-922a-6e66d86d4e3b | -2.91833 | -48.61332 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80213875-f69c-351f-aca1-6631a6753d19 | -2.9182 | -48.61658 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e00a84ff-0011-3d46-b4ca-9ab7d8d0a732 | -2.91524 | -48.60739 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f957c54-d60b-3f11-8ea5-0c3144fbe202 | -2.91327 | -48.61687 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7da53d88-4350-33f2-8c5c-1a1ddd2e2d10 | -2.91311 | -48.62016 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 748c0a1e-b10d-333e-af56-2ce9a3d14e87 | -2.91239 | -48.62445 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80b5d45a-2f9b-3edd-93b5-3503bf085419 | -2.91167 | -48.62876 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98ba29dd-5a22-3880-b14e-6205f927ec55 | -2.9115 | -48.0567 | 2024-11-02 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a38ea7ab-de15-3121-a0b9-2dea42a9dea6 | -2.91121 | -48.62977 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e047091a-9747-3d9a-84a8-efba4a399a4e | -2.90985 | -48.63837 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b103d9ef-4657-3efc-93d7-80df6721ea48 | -2.90888 | -48.61615 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 851b3958-a47c-3acb-bf29-31c5cb16af49 | -2.9082 | -48.62042 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6782815f-bb61-307f-aae6-1324d9bff0cc | -2.90382 | -48.61971 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e248f4ea-97cf-3e06-90b8-3a3146c4bfb2 | -3.08221 | -47.78303 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6228b49-1579-3df0-b1b0-75a630b24234 | -3.06289 | -48.00568 | 2024-11-02 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 393cc012-92ef-35c3-817c-d01066163610 | -2.97742 | -48.63956 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29c67a82-9205-3d88-b7d4-2580ef6387d2 | -2.91765 | -48.61756 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707cc25f-ce1b-3b44-aab8-daa9f5dd366c | -2.91462 | -48.60834 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc3c6bbc-513e-358f-a466-fe9d697a1b18 | -2.91382 | -48.61588 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06c845ac-d46c-3422-90b2-ffc888d425e9 | -2.91258 | -48.62115 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a2f3b28-9661-31a3-a9da-e0885022bf80 | -2.9119 | -48.62546 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c17a47-9f9e-3d2e-84c6-899692653ab6 | -2.91154 | -48.76556 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bf4ce8a-c943-3f95-b98b-27c63f10ac18 | -2.91095 | -48.63305 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55171b5e-4d21-318c-a9c0-9ebff0b0435f | -2.91092 | -48.60336 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe323d8-9a5f-3b62-b473-3bdde3b59d64 | -2.91053 | -48.63409 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44d6a4ec-48c5-39a2-b393-ba3d2f03094c | -2.91023 | -48.63735 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c34c2827-eef2-3184-8ed5-5b048858fabb | -2.7854 | -48.08543 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48c3891b-eb35-3b81-93d6-8a066b36b28e | -2.86553 | -48.66161 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 140bdabb-3613-3629-8722-a2eccc666424 | -2.86227 | -48.4618 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6461b4e-ffb4-33fa-b823-db4c6469a16c | -2.84926 | -48.45964 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1b1a93d-178b-3801-b19c-9baf7100b144 | -2.84858 | -48.46379 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00e1b252-2c7c-3337-a190-6e29a2d39177 | -2.83694 | -48.45339 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 508e4987-1240-3aa4-94aa-d70f2389477a | -2.83608 | -48.45058 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fd1739c-d124-36c0-a230-75bef11f8ef2 | -2.83542 | -48.45474 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9036221b-ba7d-38f5-a507-3418b400e77f | -2.83329 | -48.44855 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d00e5ccd-3ffc-3bfa-bb1d-485f8e4d8b68 | -2.8324 | -48.44572 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 677b7b5e-cdcd-379f-bbea-2bb8664c57fd | -2.82939 | -48.43667 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f0e33bf-83d8-374b-9d0a-db2677f0019f | -2.82891 | -48.35637 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d0fd69d-96f8-3c59-a256-8e305a1c70b1 | -2.82824 | -48.36055 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25dfd452-03d9-30fb-ac7f-d1f3b13307dd | -2.82807 | -48.445 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e60e3d06-8bb4-3cd2-b73a-c155342e0c5f | -2.8274 | -48.44917 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0e30f02-63b4-3527-9e31-d2af3b4a07da | -2.82506 | -48.43597 | 2024-11-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed38db79-92ce-37e9-9c73-d5b7e323ccfa | -2.81304 | -48.57003 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3160182-f124-3411-acaa-339c7acdad7b | -2.81239 | -48.57168 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64cb4111-48d0-3491-bfec-211786e92bee | -2.80392 | -48.6534 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce4f056c-ee12-3aaf-abc5-d1756ff37ab8 | -2.80324 | -48.6577 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9900c2c6-5ea8-3e1d-afbd-1d565fb6baa0 | -2.80324 | -48.6558 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ded06000-ca37-33e6-8fb9-32323d644e33 | -2.79952 | -48.65268 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b651da50-99a3-31be-8b80-147c6337f247 | -2.78478 | -48.57583 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfa703b3-6927-3b3a-bb1b-c163298b50a5 | -2.78108 | -48.57088 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ac464ef-ce6e-3a7b-a099-00155eaf098e | -2.7804 | -48.57512 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00d3c553-c107-3238-891c-3141c08f614d | -2.77972 | -48.57935 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ac588493-038e-35ca-bd7c-4918bb4de08c | -2.77903 | -48.58363 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ad7511f-11e3-3c20-a94a-178da0bddf6d | -2.77602 | -48.57439 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 668d9b95-16fd-3ad5-8480-884be11089f7 | -2.77533 | -48.57864 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 391cd0ee-3c1e-3b47-9239-1cb2068288ad | -2.77527 | -48.7196 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6287b62d-27a8-3cf8-85e5-40f8b7d93215 | -2.77464 | -48.58292 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07a762a8-82c6-3827-81e8-1f3438a6d7cd | -2.77457 | -48.72396 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e6d247e0-9137-36e9-ac54-950161cea49e | -2.77387 | -48.72832 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 69ef4c54-5122-3565-9665-756579dbc955 | -2.77164 | -48.57366 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4355a869-6ea2-35d8-b846-9bba989bed57 | -2.77096 | -48.57792 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4243075f-ecfe-3883-b016-5230d93ebb5d | -2.77084 | -48.71887 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ac224a82-c7ee-3725-9b86-13e40e2eebab | -2.77015 | -48.72322 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5bf3938b-1c6b-3886-8dea-08d45d22c46a | -2.76945 | -48.72758 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8a8cc818-2788-31b2-8fa2-4ab086c7fde3 | -2.76871 | -48.64763 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
