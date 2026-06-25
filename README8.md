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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b30cd2d4-f37b-3247-8d8f-5de4dc30523f | -8.1267 | -47.88669 | 2026-06-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abdbcb8f-ea8a-3367-bd43-f19035efdd6f | -7.75729 | -44.62101 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 191b6f7f-d65e-35a1-b103-0e072d445806 | -8.67906 | -47.86162 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 487229bc-691b-3410-8955-f6aca01021e4 | -6.48913 | -43.71033 | 2026-06-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc14d440-c6a4-3c1d-a882-cfeb129a43e9 | -9.18779 | -45.31931 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8720da84-2431-398c-a8ef-d81c0eb5c6b7 | -6.76503 | -46.30845 | 2026-06-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbb328be-8cbb-3cac-821a-b9f5563093dd | -9.20413 | -45.32573 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c659110e-0f9f-3b29-a706-53b253abc584 | -9.20752 | -45.32627 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a3d2ee3-8e0c-3a30-9042-54a4bbcd672c | -5.80744 | -45.05665 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c223d67e-f74b-3451-aed6-d42cd7dff0ed | -9.58394 | -49.11954 | 2026-06-25 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 407533f8-4e4a-325a-b5d9-99b552358e1f | -7.02466 | -44.30364 | 2026-06-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbf0c07a-1bd6-3ff2-9a69-19c8937073b0 | -6.99163 | -42.89063 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| d4aaee71-1cd1-39fb-ac51-b37e46b10b18 | -5.51132 | -35.60141 | 2026-06-25 04:14:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 700593ca-e98b-3c0e-9b3d-eddc608dad90 | -7.74944 | -44.6271 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1788c575-bfc8-3bbe-82ef-b61e72b523e1 | -9.21768 | -45.32793 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acbbf897-c309-3ae7-9654-5a73b44024ad | -9.80614 | -48.92043 | 2026-06-25 04:14:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41157486-e605-3b1f-a4b6-5520afa6e215 | -7.74502 | -44.61175 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b4db1b59-908d-37dc-bc10-faa7e526d3fe | -7.96259 | -47.44849 | 2026-06-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89863f47-ed10-3fef-84bd-e86219e16f97 | -7.76178 | -44.6144 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 08b6d10c-25a5-30b0-bc6b-6311b26976c9 | -7.7433 | -44.62249 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b1b2ab1a-1ff1-342f-b668-61e693ccab96 | -6.98779 | -42.89357 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 66abb4b9-14cd-3a11-957a-9d57be1599be | -7.75337 | -44.62405 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa30e342-6fea-3c34-a161-001c6cf3f5b1 | -7.74666 | -44.623 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0882a3f3-041b-36ed-bde2-4d5232929b80 | -9.09606 | -47.52876 | 2026-06-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29903147-cab8-3ccb-b52e-607817cc4554 | -5.81369 | -45.05716 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91131b80-71c9-3897-ad86-783cee3970b1 | -7.73206 | -44.18091 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 326a0a8d-5a11-3eeb-95f4-60010fe32ca5 | -6.50671 | -42.22298 | 2026-06-25 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a985c02b-d047-38cc-9acc-ebf397ba3dd4 | -7.16586 | -42.9749 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 197fcfb0-82e5-3d3c-9105-7cdbe4026c31 | -9.19456 | -45.3204 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| afb82594-a456-30d3-a730-fe689cb26d08 | -6.98833 | -42.89012 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 30781101-3cb9-33aa-ab9a-49b62560b9b2 | -10.03306 | -46.61666 | 2026-06-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb572563-cd61-36db-9a25-9a2c15d12d26 | -7.7478 | -44.61585 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4315bd1c-3cac-3956-8677-b557dac38f10 | -8.68371 | -47.85742 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b2ecc895-9ee7-3a99-9573-bbc60c5a78b6 | -9.6265 | -49.01562 | 2026-06-25 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b761cbf3-65f4-3ff2-85d8-16ecd5912148 | -7.76121 | -44.61797 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d40a304a-7012-3ff2-94ed-9558787d9f53 | -10.29209 | -44.69501 | 2026-06-25 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a9c86ae0-9c99-3dd5-8b05-36e5c30d6ccc | -8.79261 | -44.80946 | 2026-06-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0d776aa-fdc3-3461-9664-de216cb2c2f2 | -6.85792 | -38.35295 | 2026-06-25 04:14:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 92f37972-8fd2-3cb2-93ee-8ebbc1aa488a | -7.63157 | -50.21607 | 2026-06-25 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d0d54a1-dede-32da-a9d7-b6734717f4cf | -7.81096 | -46.4589 | 2026-06-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b243060c-5a6b-3648-90ce-1db28a6d2eda | -7.64486 | -45.29745 | 2026-06-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a403e50-5114-37a4-8203-e631ef672863 | -5.8209 | -43.58654 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adebe55e-21a5-3c5f-92a2-4f3f4a8a3865 | -5.81759 | -43.58603 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01fb54e4-95cf-35e2-a59b-de84242c5ed2 | -5.81267 | -45.04591 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db37dea6-8f14-384a-9e79-ff5bddc7d4e3 | -7.80667 | -46.46255 | 2026-06-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25d37635-1765-3954-8b11-d88f15667f6f | -9.57983 | -49.11884 | 2026-06-25 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f55ee488-fafe-3446-b563-41b2fbabcb52 | -6.31236 | -44.64724 | 2026-06-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77d39d74-c4db-31ca-acd4-1a0c2e6513c2 | -9.10731 | -47.46041 | 2026-06-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bb4f9ea-388f-31d1-b78a-de28601e9356 | -7.73981 | -44.17496 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0011c548-61da-39e2-a756-64b95ba3cc5f | -8.78938 | -47.40744 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c04ee126-80f3-3d86-a3d2-59a8bf1122d1 | -8.68674 | -47.86294 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ac05369f-1f4a-3c10-99a5-260d3201bfd4 | -9.89575 | -47.02857 | 2026-06-25 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a16cb63e-5319-312e-a7c1-fa7f7be73178 | -10.27706 | -47.60576 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4501d546-897b-3289-bfbb-72e97085500f | -7.92955 | -48.29102 | 2026-06-25 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c35657d-ccb3-3bb2-b7ef-b99e52bf37f2 | -7.63614 | -50.21686 | 2026-06-25 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30e2c25d-1f66-3ca7-a6c1-bdf5e9c59297 | -6.30992 | -44.6545 | 2026-06-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38d2af11-e337-30fb-97eb-c0d1ce4f13ea | -9.67917 | -47.02052 | 2026-06-25 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b16d48e-f49f-3813-a054-b76ea408dc3a | -6.99492 | -42.89115 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| c6a50930-a48c-31d3-8a62-71bcfd870158 | -5.81146 | -45.04907 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2cec720-672b-328d-82a9-0f2c8de54241 | -10.29929 | -44.69254 | 2026-06-25 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56a4763d-410a-3949-baf5-490704117d9c | -8.79219 | -47.58092 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9d72ecc-0877-3413-87fc-9b1b350d0f9e | -5.8 | -43.63323 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 305382dd-f27d-38c9-82a5-c50fb950167b | -8.09681 | -46.75394 | 2026-06-25 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 643246e4-1ac1-37b1-9cb9-ca5b9215b5b3 | -10.29985 | -44.689 | 2026-06-25 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5aa78440-d4ae-3588-b239-22ab0db7aadc | -10.29653 | -44.68846 | 2026-06-25 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 372dff76-7606-3f06-bbdb-752372bce823 | -9.19117 | -45.31985 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5c1b6cc-ef9c-3b21-8f9a-34b2d6ed0202 | -10.2778 | -47.60131 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8dac5fe-b5cf-3e2e-958b-feba37e371cc | -6.99439 | -42.8946 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| a23b9c97-e39e-3f46-b6b6-0de937435867 | -5.79669 | -43.63271 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea518a6f-0e71-3abb-ac79-3d766fb3507d | -9.20133 | -45.32151 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ed08fc-cc4d-39e0-b839-168efac1ce7d | -6.98886 | -42.88667 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a17cd049-a116-3a61-b85a-1e9fa4ca8543 | -10.86219 | -43.96888 | 2026-06-25 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6918d6f8-9257-3cb6-90cf-85dc8b11018d | -9.27753 | -47.65445 | 2026-06-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbe04b2d-e32b-393f-b469-c3002d11cdf2 | -9.0407 | -47.26473 | 2026-06-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb7a9059-21ed-3530-a2a2-6d1d109b95e1 | -7.1697 | -42.97197 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de247823-be85-3d5d-a005-cbd17421ad8e | -5.81704 | -43.58952 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abb78a87-c643-32f1-b376-f037d1cdb71f | -9.07575 | -44.74455 | 2026-06-25 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d920b16e-4042-3aac-be78-141e3a450609 | -5.64405 | -36.59211 | 2026-06-25 04:14:00 | NOAA-21 | ANGICOS | RIO GRANDE DO NORTE | Brasil | 2400802 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80281fed-0150-34f0-a432-43dca5cf90b0 | -11.5893 | -47.44028 | 2026-06-25 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a50f2c5e-c96b-3aae-97af-fd15ef894f7b | -11.50616 | -54.50307 | 2026-06-25 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa9f09ea-e7ef-3c11-98a1-76c1864dfa77 | -16.08532 | -45.89692 | 2026-06-25 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 698200d4-c654-3b2b-83e1-a5f663630aa6 | -12.21746 | -55.49159 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c7bfe70-8493-36aa-9a33-697d47507ddd | -11.49764 | -52.92243 | 2026-06-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18e6b7bc-936a-3dc8-a920-f41c2a285fdf | -14.26101 | -52.03874 | 2026-06-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a63e0bec-c8a1-33f4-87d4-5abcf87a9f30 | -12.07847 | -54.61506 | 2026-06-25 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f16a2816-f36b-3518-95d3-1e1d467a3bcd | -9.88677 | -52.43763 | 2026-06-25 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b03009-4fdb-3f21-aa02-e3a49ba476a1 | -13.8354 | -47.02047 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a11ff0a-0e88-3964-9f8c-83746e8b09c0 | -10.59744 | -47.10782 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96524d3b-9a3c-3ad5-9d4c-798951f2dfd3 | -12.31319 | -46.73777 | 2026-06-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c93714e-1757-38ad-be37-2b24b8acdad3 | -11.25409 | -43.32845 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0994de4a-89a8-3a1b-8432-85023673906e | -12.13975 | -48.26025 | 2026-06-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97d2db6d-11b9-3cd5-9bb1-729c0b06ca89 | -15.33486 | -43.69065 | 2026-06-25 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e14a7f46-1c2a-3f51-8c2a-6afbb338b92c | -12.73855 | -44.45936 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ebad70aa-033c-3812-9acf-9825cd8498bd | -13.06033 | -53.35442 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8e695fd-db7f-32cc-a56e-b7b716e6f65d | -12.74185 | -44.45989 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8e9eadfc-de47-35e1-bcf8-1f7abb0c3aec | -10.61993 | -47.1721 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d7885668-2eba-39aa-9187-dc4610603623 | -12.74515 | -44.46043 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eb4e83a2-f9f2-3773-a192-d45be1d4f0cd | -11.49648 | -52.92862 | 2026-06-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38b26a35-2025-30dd-afd2-d38e74784772 | -11.20616 | -43.3533 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4efc5985-9c52-3b58-8e11-173931a3afc5 | -12.22251 | -55.4972 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README9.md)
