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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 157641cb-b66c-351d-84d9-66bf3a530bda | -7.94195 | -44.93993 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33108b0d-5f90-37d6-9f63-6e48c1064ad8 | -6.54803 | -43.91158 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6b51758-1d47-3b1a-9b47-1984d7e9c183 | -6.19478 | -44.1865 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90c4ada6-4738-3adf-a83a-a7e5bddf3bf1 | -7.72789 | -44.61716 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d37baf1e-f8bf-3113-9fdd-de3f17e8707a | -5.39273 | -55.90936 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d63a918-5514-34a7-9ae3-58c8eb085d7d | -5.6851 | -45.18196 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2bcc86e-19a6-3be4-97b9-28b74a5b4d48 | -6.05957 | -45.02532 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3456a074-6d11-38ec-a5b7-65151c79c6a1 | -6.5595 | -43.7149 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed1d50b7-b851-3ae8-a461-7c6a315ee382 | -6.79076 | -44.44022 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4dbf723-b212-302d-b3fc-d5176a5813da | -5.69973 | -45.39637 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f9b7f59-cad5-3af8-9ca1-e1a026d1fd05 | -5.53578 | -46.42612 | 2025-09-04 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11b403da-f47f-38fc-a91d-7f35d8378b03 | -5.50439 | -42.6553 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a185565-52cb-3e63-badf-036da9c38bcb | -5.69029 | -45.39133 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7a9bea4-527b-399e-a708-fa99e7fb930e | -6.35272 | -42.56588 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7797bfb-ee92-3fec-929f-1b6cd19b5670 | -5.38278 | -45.94728 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1802ba6-b341-3b93-8b6e-edcf10e339b7 | -6.13156 | -43.33739 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93970712-b28d-3f96-baeb-d0b8fa88eec0 | -5.71202 | -45.25101 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd6e7657-54cb-3e72-88f9-efeb3c7dc34c | -6.0338 | -46.65718 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afab4d9c-ceea-3788-addd-6fdc4eb33f08 | -8.01003 | -44.0355 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d437b3c1-1d47-3c2f-83dd-bd530f2e3b39 | -8.02766 | -44.0629 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92450a34-3514-3d63-8e99-30f01c4fffa3 | -6.19821 | -44.25646 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d4af252-a738-3d26-9f9c-8671c0f8c54b | -8.01651 | -44.04052 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 604e4890-60a4-3bda-8ed6-76dbdb1c1b57 | -4.99275 | -56.25418 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 270ac104-015e-3fb8-9e13-b31ec5f867e2 | -6.88075 | -45.56573 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d7094ff-1719-3e1f-b839-af53399926db | -5.80013 | -45.31896 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc9b2f3b-b110-375b-9eed-05cf982ac7fd | -6.26664 | -43.59237 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8097914-379c-39cb-92ce-d9270cdc5a81 | -6.2538 | -43.29552 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d1120272-c942-356f-b897-abc98fc7501c | -5.3518 | -45.09417 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bfdbc599-4c3a-3c45-aaff-6f7b46e02a69 | -6.2538 | -46.11943 | 2025-09-04 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c49b4161-7e24-35b6-ba99-0b930b103934 | -6.54744 | -43.91552 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf82c6ca-3cc9-3056-898a-9d0a174839b3 | -5.83908 | -42.99505 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1f2ff763-1e08-3b9b-b192-4f63d8e685b0 | -6.27642 | -43.50273 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eace6613-fcc0-3efe-8966-b0757023fb8f | -7.18985 | -44.16732 | 2025-09-04 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 714d7bc0-eee5-314b-9e5c-7325d18438ef | -1.19948 | -46.15431 | 2025-09-04 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28c85bf0-b286-3ac9-b34b-b6bc3b7a1e5e | -7.01295 | -43.22862 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d517ef56-7191-35dd-abcd-baae4a38cff5 | -5.97206 | -44.75094 | 2025-09-04 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd64b5f5-0768-35a4-8b05-8a137feb7ce0 | -7.16553 | -43.8989 | 2025-09-04 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 091b0af2-aa7e-3339-866e-adffde5e1cd9 | -2.14154 | -47.59742 | 2025-09-04 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1e2a6ca-4a28-3f8b-874e-e1b9ddb94ecc | -6.24338 | -42.59748 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b363313a-531b-33c6-9516-40a197f09aac | -6.22944 | -43.55094 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7a25fcd-395f-3151-ba7b-1f29ac46138e | -6.05902 | -45.0289 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a461ce3-6a57-3050-8564-39a4937dcc02 | -5.69695 | -45.9402 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ded76a30-99bf-3dc4-a86d-397f750012e4 | -6.35579 | -42.57094 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 541ba979-3442-3d2a-83ba-a26c687e01c9 | -6.23271 | -43.41018 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d52d0556-bf08-3ffa-bfc6-f3845c1a554e | -8.01762 | -44.13072 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cad378f1-41d9-3874-b3a7-3dd2d6f20ab2 | -5.85818 | -45.64629 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c11232ad-867f-3231-b75d-8f33ec0f6f27 | -6.68288 | -48.41262 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 47a1e6fe-db62-3326-b1a3-fb610b884b56 | -4.295 | -48.60563 | 2025-09-04 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 769b84b0-dc9f-3607-95d0-bfc55b6e7151 | -6.32973 | -47.75918 | 2025-09-04 04:25:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 107d73c3-83d9-3dc2-a1ff-a4231e3a805e | -6.23189 | -43.55793 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe804a6-893f-3b3d-8d27-e0825e6253fd | -6.79251 | -44.08589 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 91866eac-fe5a-3365-9cb6-9c3f1842661d | -7.76687 | -45.44136 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a98c39c-efa7-3cd4-8e0e-ff18f5d8c3ec | -6.67791 | -48.40018 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 17d12215-5524-3a0d-9aa0-cef1f7b1548a | -6.16037 | -43.31672 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9d1827b7-0373-3f70-a94f-3d8577921789 | -5.55214 | -43.09129 | 2025-09-04 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 68da1153-f39b-3562-97ad-39ee08e630eb | -2.78355 | -49.62272 | 2025-09-04 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47143f70-6467-384a-85ae-eceb10b3fcd2 | -8.0522 | -44.1401 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b21b75f-b092-3115-9020-0fc887dbd663 | -7.64153 | -46.55878 | 2025-09-04 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a9b7b48-a8e4-392b-980b-9f8f49671243 | -5.69729 | -45.16941 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9139bf6-16f0-3e44-8837-acf5d89b5e90 | -5.8028 | -45.63045 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f47767b-d28e-351b-977d-da51d5483cdb | -6.22774 | -43.53831 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ceb6750-9217-31f8-a1f8-7ceef22bcb96 | -7.15704 | -45.23026 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c882d5f1-e7ac-3c95-aa0e-d431c852b9bd | -6.30211 | -44.74895 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68a14451-ca9f-371b-b699-28f429023c84 | -6.88461 | -44.241 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62392185-8091-3c88-a7fe-f4321d0c1f98 | -6.22819 | -55.93645 | 2025-09-04 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84200782-7393-34ec-9cad-5e4dd0eedd12 | -6.27296 | -44.4781 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3983f58b-a165-39fd-b499-f193ebe76172 | -6.54621 | -42.94764 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ac6680f-b73d-3cbf-a76a-ae45f5aab84c | -3.35245 | -51.63048 | 2025-09-04 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 338e42bf-fb31-358a-b2ce-8f4f7848af22 | -7.50139 | -44.81715 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74629cc0-5501-3119-9280-50dff75d6495 | -5.96724 | -44.41319 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fad9c4f-dbf0-3518-bc71-f8ba52b71d55 | -5.70506 | -45.1634 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dba850af-f882-30c6-89f8-d5ebdebb4a8b | -5.92735 | -43.20349 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e03a0c60-bc25-315f-ab8b-bcc1de1c7f73 | -6.3226 | -43.77492 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 263275f0-e405-3e00-879e-48960516a2c4 | -6.31786 | -44.48432 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a432031a-2f15-3552-8e26-be8b1ae3378e | -5.8946 | -45.96036 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 342519b3-8a3d-33c9-bef8-94499f249e0d | -6.95807 | -44.95247 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95608917-6b34-3c09-9a15-c804dd80f427 | -6.8922 | -44.32378 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31059171-d374-34ff-93ff-bbc2da78218e | -7.79811 | -45.43134 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1641334d-bb74-36a9-9ace-2697b14f625b | -6.54276 | -43.92283 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61c55437-e221-311d-9be3-2fef4d5b009c | -4.51683 | -41.97003 | 2025-09-04 04:25:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4625959c-4bc1-3c5e-9c7c-441299a33c92 | -6.28583 | -43.51276 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d00d4ccf-97bd-3dd4-8f97-19af317b4c4a | -6.29496 | -43.59673 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eb8a2fc-8a72-3b04-9874-7acfc88ff239 | -5.53908 | -46.42663 | 2025-09-04 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a78987f-4204-336c-ad80-66185436eed3 | -4.83733 | -42.73985 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1e35a65-c617-3e12-a752-9c580fcbffc3 | -6.22046 | -45.04345 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 691551dd-1bc7-3750-9d1f-d64179c326c0 | -6.87566 | -45.19834 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fdef98f-7542-3642-ba18-07934d2a4851 | -6.67851 | -48.39645 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e637cc22-ee20-34b4-a608-417a00c4a46f | -6.26431 | -43.58368 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 842b7c0e-0959-359e-9d9e-fdaf8253edc9 | -6.25489 | -43.3125 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad7f5f8c-2185-3b86-9067-a0736e20122a | -5.73292 | -51.78555 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fca0b7b0-4df1-3930-abac-3320566c6c20 | -6.78087 | -44.09208 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5f7c61b-9b41-34cf-8ca9-335d6c76d382 | -6.89184 | -45.56018 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8a7282f-fe7d-36b2-bbd1-ee712504e29e | -7.93687 | -44.95041 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db3b55a6-cc85-3ac9-b145-02e43c0d0ece | -7.63064 | -42.64533 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd514eae-2c97-3344-b7f5-47021f882f13 | -3.22771 | -47.12486 | 2025-09-04 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c0b7c63-18ad-32cd-a82b-a17a8de3a7a5 | -4.0339 | -48.8987 | 2025-09-04 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7bee1bd-6cb2-31ec-b1f1-9a23ba2f05ed | -6.46902 | -43.97597 | 2025-09-04 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9480c513-7516-3ec9-9b18-0b62b35897ed | -5.84272 | -42.99557 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7550c5e5-d490-394d-872d-9833931ce440 | -6.19907 | -43.34216 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76fe6ce2-0878-3a6b-ad41-67b00595c36c | -7.64207 | -46.55532 | 2025-09-04 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
