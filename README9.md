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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fedb19b-0180-3a82-9e4d-a91a93ea96cc | -3.0632 | -54.400902 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53b1dc45-d437-3ff8-be27-077170a49dac | -0.8893 | -52.720402 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a05cf65-9e54-3b76-bf77-c6e89819aca4 | -2.7117 | -51.813801 | 2024-11-18 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aadbfdb-0967-3364-b12f-ea21e8f6646d | -17.3627 | -52.005798 | 2024-11-18 00:49:00 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f301bbde-bba6-3a37-bc75-ea36cd75ec8a | -3.3847 | -53.273602 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66ca58c3-a1f7-30a9-8984-16fe865f9731 | -3.0647 | -54.407799 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20609d84-02f6-34de-8641-9a87ac9ffd7d | -3.3423 | -53.313499 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba863f9b-3806-3da7-a321-7da799cd97ef | -3.3407 | -53.306301 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d6bd96-2bd3-33b0-90bb-eb548a694593 | -1.3051 | -51.741501 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3666cfb-1a08-36e9-adac-689bcc879c3e | -2.6805 | -52.443901 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1844a05e-97f3-35eb-8c50-c3ba44e647dd | -2.2797 | -53.626701 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd78e56b-06a1-3331-aebf-d6d4c1c45f5e | -2.5748 | -51.710999 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e97cb12-96be-3023-8a0e-984b0104b976 | -1.6076 | -52.618301 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e18c868-056d-3b9b-b37d-c8f055605e12 | -1.6943 | -45.8255 | 2024-11-18 00:49:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1045e6bb-df82-3838-929e-771f950bc1c2 | -3.5164 | -50.254002 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f37f2115-7a6e-395f-ad2f-84653a1e6c3f | -3.3275 | -50.5056 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855313f3-06a8-3e9a-af9a-985176136150 | -2.5768 | -51.719501 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7452c6f6-4ff6-360f-bca5-a9ec7c0102c9 | -3.0963 | -53.092899 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc70698-7e30-342b-aca4-411c661c328b | -4.2643 | -50.593399 | 2024-11-18 00:49:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 952eeeff-8008-3ce3-a350-bac4b5cc5159 | -17.7024 | -54.0858 | 2024-11-18 00:49:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f3e962da-271b-3a8c-9123-fa7e2edc3344 | -13.0241 | -56.457699 | 2024-11-18 00:49:00 | METOP-B | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07e99999-a793-386b-83aa-0a495491e599 | -3.0534 | -54.403099 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8feb64ef-6d81-3f49-a39c-589f5f5c8031 | -14.2952 | -57.631901 | 2024-11-18 00:49:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8560d9d0-23ca-3ede-8965-52d338a470fd | -4.5815 | -44.240501 | 2024-11-18 00:49:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbe8b4e2-e856-3420-8ff3-86d871f020ff | -2.8722 | -51.7952 | 2024-11-18 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f141f5e-3677-371c-a4a8-f33dfc238845 | -2.8624 | -51.797401 | 2024-11-18 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d605801-4abc-319e-91ed-1980bc0e38d6 | -0.8875 | -52.712399 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84e7d337-8240-369a-b4c6-e5997de3f148 | -2.5885 | -51.725899 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 737a80c9-18ff-3a73-b29f-733ecd8c4bd0 | -13.0143 | -56.459801 | 2024-11-18 00:49:00 | METOP-B | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4177f59-db82-357d-b9d2-2dc629d27de2 | -3.1852 | -53.257301 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da5575bd-d291-33b8-a3ce-eb549d721497 | -2.5855 | -53.975498 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ac5ea9-1e95-35e3-a8ec-0514e07e6b06 | -3.5782 | -53.716999 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae8602b-e6ed-30fa-b253-ab77036939c3 | -2.193 | -53.653599 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aebebcf9-cc6c-3847-b2dc-19b5ef7b2165 | -2.6493 | -51.721199 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0dca1a-57d1-30ce-947a-79ded6004817 | -3.7507 | -45.965 | 2024-11-18 00:49:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00e35a87-146e-378a-9f1b-574b8be2886d | -1.2964 | -51.7616 | 2024-11-18 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 14747e6d-60e6-301e-be8e-67ae9d646606 | -14.286 | -57.624 | 2024-11-18 00:50:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ebcecd22-05eb-3a8b-9a91-da8eec010739 | -1.6962 | -45.8311 | 2024-11-18 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| d20ec174-e678-3c30-aa47-c893a6f24e99 | -6.5397 | -35.2738 | 2024-11-18 00:50:00 | GOES-16 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 95.8 |
| a327ea42-78da-34ce-83e5-3a9d274f6cd0 | -6.522 | -35.1666 | 2024-11-18 00:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 4a022f38-02dc-33a7-9cf8-ea2e07eb4f32 | -2.8608 | -51.7731 | 2024-11-18 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8984e32e-9880-366a-a77f-0d67cb999c6c | -3.1827 | -45.4514 | 2024-11-18 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| bfb20502-d537-345d-9493-e446c41feedb | -3.0542 | -54.4081 | 2024-11-18 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9574f614-d4fa-3cd8-a2dd-0561b541f166 | -1.3148 | -51.7614 | 2024-11-18 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7544a35b-437e-35f0-96b3-a5e830256c5d | -6.5216 | -35.194 | 2024-11-18 00:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 204.9 |
| 7b2a38b6-7388-3333-b8f0-c3905ab278c1 | -5.5481 | -43.2824 | 2024-11-18 00:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 989c62ad-5520-360d-bf95-b0b0450f1302 | -3.3267 | -50.4923 | 2024-11-18 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4f872187-514e-3818-8f82-519a270c13eb | -1.7138 | -46.1866 | 2024-11-18 00:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 4fa73fc3-c574-337a-a7e6-f66ef12e90be | -1.2964 | -51.7204 | 2024-11-18 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| dc43e01a-9e76-3a88-90c7-830b1399da4d | -3.5678 | -50.2534 | 2024-11-18 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| a7ca02ff-b682-3688-a386-b80237288947 | -1.7147 | -45.8307 | 2024-11-18 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 1e388f23-ff64-3856-a0aa-389d19e38b06 | -2.8792 | -51.7726 | 2024-11-18 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 14eed2fe-f59b-36d2-a35d-dba042010e91 | -3.7563 | -45.9645 | 2024-11-18 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 2db7f225-e000-3445-937a-a557dd0ddbce | -2.766 | -52.5959 | 2024-11-18 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8a8a5327-733b-3326-bcb9-33ffd039145f | -3.7564 | -45.9422 | 2024-11-18 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 1ec1a4bc-fc9d-3a63-813d-f9b92bff259c | -5.9556 | -48.0642 | 2024-11-18 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1598391b-568a-333c-b17e-a6639b303895 | -2.8607 | -51.7937 | 2024-11-18 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 182e9b80-0203-3ad1-b09a-358cbee9fe7b | -2.7659 | -52.6163 | 2024-11-18 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 169.6 |
| d641df3f-4285-30f1-a771-c473167e8843 | -6.5411 | -35.1643 | 2024-11-18 00:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 160.4 |
| 3a7d055b-3fc9-3db2-a1c9-67a04e0cfe33 | -3.6778 | -50.4384 | 2024-11-18 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c81df585-303d-3318-966a-eeed72415363 | -14.2857 | -57.6442 | 2024-11-18 00:50:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 62335ff3-adb4-31ee-abc9-72525cc46be5 | -1.7324 | -46.1862 | 2024-11-18 00:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e1ade1de-cc0e-356d-9d62-6d84e7b1ac1a | -3.4015 | -50.2801 | 2024-11-18 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| e962fbec-847e-3bfb-984b-a7a080cfc132 | -3.3452 | -50.4917 | 2024-11-18 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8331931f-a635-3689-9e67-8eb49f199964 | -3.0764 | -53.2796 | 2024-11-18 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2247a5df-7259-3d6f-b9df-1d308d51f335 | -3.6593 | -50.439 | 2024-11-18 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b51ff7c4-6db5-3319-87e8-aaeb7e1b6027 | -6.54 | -35.2465 | 2024-11-18 00:50:00 | GOES-16 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| 456636bd-5e48-3d07-98ad-456a943d626f | -2.7843 | -52.6158 | 2024-11-18 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 3f0cc8b9-3655-39cf-b643-17370c837c72 | -6.5407 | -35.1917 | 2024-11-18 00:50:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 308.9 |
| 3c756820-09ad-377a-83fa-3c7762382ca2 | -1.2964 | -51.741 | 2024-11-18 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 381.1 |
| 4e271124-d082-3f82-b6b8-abdae29c7add | -2.7475 | -52.6167 | 2024-11-18 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6e0bc9fc-e197-346a-a29e-17720a1d2ca7 | -2.8791 | -51.7932 | 2024-11-18 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 21a2b3c5-a35a-32a3-8c0a-0c95879d29b7 | -3.775 | -45.9413 | 2024-11-18 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 1a1124c8-f0c3-3b06-9c35-3ed06dfdcbad | -2.5847 | -51.7181 | 2024-11-18 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 501b5bcb-3b29-346c-a064-2ab2112c08e7 | -1.3148 | -51.7408 | 2024-11-18 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 03c42cb8-5015-3020-9fd4-5c5a85c323ed | -2.5846 | -51.7387 | 2024-11-18 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 9259b41e-aec3-36bc-a023-daf5d9552406 | -3.0542 | -54.4081 | 2024-11-18 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9b6080fa-64ac-3583-bda0-72c03edec0ae | -1.7138 | -46.1866 | 2024-11-18 01:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 9d4b23bd-3295-391b-801a-e16b159817d3 | -5.9556 | -48.0642 | 2024-11-18 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 814ebab9-14f5-341b-895f-292ec5f9c3b3 | -6.5216 | -35.194 | 2024-11-18 01:00:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| 5240beb5-47d2-36e8-ab47-56aefc4b7a46 | -2.8608 | -51.7731 | 2024-11-18 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| c6570786-9cca-3d96-8817-c70e75c316a6 | -1.3148 | -51.7614 | 2024-11-18 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 8d7dd654-547d-3d78-96e5-5bcc9aa03be2 | -2.5073 | -47.2461 | 2024-11-18 01:00:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 057c341f-ca8b-3965-9b1d-2d51c21c5e53 | -1.2964 | -51.741 | 2024-11-18 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 312.2 |
| c5dd3ebe-62a7-31c6-a31f-c8208f7c5ddd | -6.5407 | -35.1917 | 2024-11-18 01:00:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| f3b5fc23-2bea-3bab-8b9f-948eeeee6766 | -3.7749 | -45.9636 | 2024-11-18 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| a4acfaca-7edf-3b37-8125-efb317fd9058 | -1.6962 | -45.8311 | 2024-11-18 01:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 38f0880c-988a-3cd1-80ab-61f74d5d08f6 | -1.2964 | -51.7204 | 2024-11-18 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| e1f89286-b94a-3e7f-a3ca-2628ecf7eb6c | -3.7564 | -45.9422 | 2024-11-18 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 31d88546-a5b0-3397-b6f1-ac3dbc8915c1 | -2.5847 | -51.7181 | 2024-11-18 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0ab99447-3809-3500-9cf2-0658e923f874 | -2.5074 | -47.2242 | 2024-11-18 01:00:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 9c26d26d-b519-306c-ac1d-1f8f2396af25 | -2.6583 | -51.7163 | 2024-11-18 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 25ca8c30-4fc0-3b26-85a6-6dc17dec4d35 | -3.6593 | -50.439 | 2024-11-18 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1837c19c-14e8-3cd5-b480-8c8b5b5cb58b | -3.3452 | -50.4917 | 2024-11-18 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ec2bf26c-1453-37d0-971d-b44a9a5f0da1 | -1.3148 | -51.7202 | 2024-11-18 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 27cda56c-c2a6-3104-9f41-4af2515418f1 | -2.766 | -52.5959 | 2024-11-18 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 9f1f6e63-6fbe-3bb3-9415-676faffd1e12 | -2.678 | -46.2281 | 2024-11-18 01:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e3361e44-567e-345b-9f87-60d6e02bae80 | -2.7659 | -52.6163 | 2024-11-18 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 50bf99f1-aa49-3dfa-8a29-5ff0f6e5d020 | -1.3148 | -51.7408 | 2024-11-18 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 291.5 |
| c2e25c6a-2a99-312e-991a-43e7f2917431 | -3.3267 | -50.4923 | 2024-11-18 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |


[Clique aqui para ver as próximas entradas](README10.md)
