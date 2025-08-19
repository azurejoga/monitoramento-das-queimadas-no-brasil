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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d34aa837-5d6e-3ff2-90e7-8eef871ff8d4 | -7.29583 | -43.69854 | 2025-08-19 04:25:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d3d145f8-03e1-3606-9ffc-377d9a5576f2 | -6.95512 | -43.60464 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ce8738e-17b0-365b-8c55-403abe50237b | -6.45471 | -44.5598 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2996a188-cab3-397f-892b-d821cad512d9 | -3.98805 | -42.52252 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7b561ca3-78ec-3096-8fb7-248a3b5ecc86 | -7.00708 | -44.24684 | 2025-08-19 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92f50c27-c61c-38db-a748-4102b1231dfb | -3.9814 | -42.51714 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 79024ee1-1bf3-3c47-8391-28eb688a5668 | -5.98448 | -44.10585 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18255d1f-97e9-35eb-a85d-b80163bd3b1e | -3.97775 | -42.51657 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6f5a976c-b9ed-3b7f-93bf-2c875a4e279e | -6.55706 | -43.00723 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e10d935-8a38-35af-b44e-7d8c9be297ae | -7.01748 | -44.27197 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dece4f94-ae05-3002-8529-a385ca533663 | -6.2388 | -44.45873 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e8639a6-4a85-3b2f-9835-5b64d62bc9e4 | -2.90506 | -48.29149 | 2025-08-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cea2aa8e-e997-32a2-80f9-97e24bf7b275 | -7.16709 | -43.42833 | 2025-08-19 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35c4554f-dcec-359a-a838-dbc08f6a862a | -4.95962 | -43.04618 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99e982ec-0309-3a33-b3ed-810940604cff | -7.59201 | -45.42404 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4cc5186-cdc2-3ca2-821f-36694cab8ccf | -6.96347 | -43.59761 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6cc4cfdf-c123-3541-8942-ea112ff19e49 | -7.58756 | -45.43069 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c66d2296-03eb-38a7-becc-04d22567a7af | -3.74219 | -48.93071 | 2025-08-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f689fecd-6b3b-3bd1-bdf7-1cd9d3a567e8 | -5.78653 | -43.60384 | 2025-08-19 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caa7c629-9859-3d39-af9f-97885fd8bc1c | -5.88084 | -48.12084 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4ce432b9-70d0-3268-9694-045dcbe7777d | -7.22612 | -45.17634 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fbfc7d1-42e5-3178-bf14-ea48bd10d6f0 | -6.53479 | -43.43817 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 39138a2a-0dc4-33b0-b703-6d29f74947de | -7.1392 | -44.60011 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 235013bd-039e-38e3-bd71-9e7bb635e1a9 | -3.38154 | -50.00919 | 2025-08-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c05a81f2-7fbf-3119-a876-78cfe9448098 | -6.85409 | -44.4236 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35924cc5-9818-3cdd-8ab2-020b0e105707 | -5.64719 | -43.40131 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65d22e86-c6a0-3dda-8a22-45584691cf5b | -3.25364 | -43.27825 | 2025-08-19 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10facd99-2c34-3f93-884c-899e537c7aeb | -3.65366 | -48.32819 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbbc6ae6-a71e-3e08-9679-e8686efbb6c3 | -7.63401 | -44.92134 | 2025-08-19 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56272d02-2f98-3078-b42a-1c00023fa312 | -6.93249 | -43.60955 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0329becd-d124-3474-ac16-f5a830361730 | -4.91818 | -43.24382 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c2bbc6b-ccb3-3c09-926a-1a4fb380934a | -4.42856 | -47.75752 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67f4ea21-a820-3807-af44-99c7d1c403d8 | -6.24575 | -44.82748 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f4cf800-ab8a-397d-8cdc-0f6236476b08 | -4.02208 | -48.06342 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8e92fa1-07bb-3d8e-8a5a-b86aed2446d2 | -6.48993 | -42.97936 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 084d552f-5390-307b-bbda-a049004b897f | -7.65107 | -45.2639 | 2025-08-19 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bca6b2a-3f41-3dc3-88fc-cc8b1bc5c380 | -4.95959 | -47.59923 | 2025-08-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44470234-5c03-3d1d-ab54-46fcf6a58778 | -6.93203 | -43.5945 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2182173c-9e70-31df-9ffd-e6105ebeab8f | -6.93488 | -43.59325 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ee6d01b4-0541-3c6e-8d06-dedf7638533e | -6.52399 | -43.44569 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 590f6062-d679-337f-ac9b-df4b9dc89216 | -6.95572 | -43.60057 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b24e437b-4be6-37f7-b530-96e62b553bf8 | -5.6532 | -43.3858 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bfa2a3f-77af-399c-b37e-26a1fc0c7496 | -7.14645 | -44.20881 | 2025-08-19 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| daa2dc85-1eb5-356a-a1b7-f0a7163642fb | -6.94677 | -43.61176 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ef6ec87-6761-31ea-8424-1d2f81281875 | -5.36965 | -41.2225 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 428a9cac-f700-3df8-b019-54119013cb75 | -6.93623 | -43.59095 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ad4cf707-21dc-3bbe-a1a8-443481ce06e9 | -5.36212 | -41.21782 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfedb7ca-c5b6-3aee-826e-5b0ab35576a9 | -7.2941 | -43.6857 | 2025-08-19 04:25:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a64ac85-fbea-3476-a281-43ed60868964 | -6.93428 | -43.59735 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 366c9df4-5612-3823-b9be-926956f5374e | -6.93548 | -43.58915 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 69b8442e-ee11-31aa-b25b-923d38db6383 | -7.01055 | -44.24742 | 2025-08-19 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e56b9b-e557-3575-bc91-0f328fcbd28a | -6.61657 | -43.8847 | 2025-08-19 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb829354-a523-3031-8f00-75da2597e225 | -6.56903 | -43.10133 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e941f100-c605-3228-b5e8-27dcc7c8cae3 | -6.56073 | -43.00777 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 292061b5-55b6-35af-a3d6-4e23bfda2bfd | -6.10676 | -44.40474 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fb97922-5c9f-342a-929f-5e51cab0c7e8 | -7.77797 | -45.16796 | 2025-08-19 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d532756-4b04-394a-9f1a-f9604f32c2e2 | -2.54213 | -47.72129 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd2793c7-e719-3585-954e-bddbad576766 | -3.98869 | -42.51827 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2c9897e2-1a7f-34c1-887c-24c7a301b461 | -7.13577 | -44.59963 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01536601-5677-30ce-be95-10f9ffaf6dd4 | -6.0995 | -44.58921 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ce8bac7-8f06-342b-a96d-2608812aeac2 | -3.82947 | -47.75097 | 2025-08-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41748289-8339-3471-bac3-31632f0e6ee5 | -4.01863 | -48.0629 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ff5c4c-5138-34fc-b808-4befe937e535 | -6.36465 | -43.27064 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b09fd233-4ff1-3c92-a8ba-6491bd0d3419 | -5.5475 | -49.07294 | 2025-08-19 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6d41912-aa8e-385f-b28a-499fa21413ae | -3.9917 | -42.52308 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| ef7fdcbe-7a61-37ec-ae77-2713e3cf4ddc | -6.95869 | -43.60519 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1152210-8cd7-35ff-b853-28f6df65c007 | -6.41661 | -42.49646 | 2025-08-19 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f53bcd5-b5dd-3a09-b537-1072baee5141 | -5.37315 | -41.22659 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12d44073-0edd-3886-b088-7ae5909e1923 | -6.93266 | -43.5904 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 006e9bf8-b798-3165-b873-e8701da671d7 | -6.87771 | -45.20811 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7239672-72da-327b-8830-a7f8aa50ef17 | -5.65258 | -43.38983 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e9dc469-16fd-3c58-aa1c-93880f82409c | -7.5803 | -45.43323 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 280dbbaa-e83e-3810-9f28-83530a2e2062 | -6.42084 | -42.51957 | 2025-08-19 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e097ce8b-d2ff-37d2-af1f-7735abf14c1c | -6.93685 | -43.58684 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e7b96101-5463-3dbc-8c43-8fce263a189d | -6.49001 | -42.98132 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95364dce-9d83-3878-aa0c-1559c5948516 | -5.98164 | -44.2823 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6436e35b-e301-3547-bbd5-f05404cbbb6a | -6.93843 | -43.61877 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5042d1e2-4bf7-3ff3-8aee-b1593af3adcd | -6.75076 | -41.56633 | 2025-08-19 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae7d677c-192e-3c53-be13-d04e8a17010b | -14.85728 | -43.88775 | 2025-08-19 04:27:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f0bbd73d-df25-322f-aff2-74112417d5a1 | -12.65876 | -45.80629 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebf3ecf8-d5aa-3786-94e3-3a3949567ce8 | -7.21667 | -49.60707 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30721420-8750-3341-8ef8-22dd1275f3c0 | -9.85555 | -44.68322 | 2025-08-19 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57e83178-26a3-368d-b28d-dbb9bb3c4a69 | -14.73952 | -46.29675 | 2025-08-19 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ed5fd52-62ea-39ef-8e3e-e6c66888e1c6 | -8.82064 | -52.06187 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69919d7e-be8e-3607-9ab0-80838359f854 | -12.9293 | -46.1063 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d44cf201-a699-3b6c-8a87-24ef9795a5ca | -14.86662 | -48.03968 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aaeadce0-9368-39c6-a1b1-41f4c443b237 | -12.63731 | -46.88887 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0486cd1d-8c31-3c0d-943e-2bb66310be78 | -8.70488 | -50.68601 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86c942a7-b974-3a17-88f5-9cab3e411c9c | -11.76426 | -51.73371 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2ca74a6-dc62-3afd-bb37-0176bd71ecdc | -13.18955 | -54.9508 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb1ea509-3e12-3ade-b9f5-38087827549e | -11.76345 | -51.7384 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58712a15-c89f-3616-94e7-8bb2095420dd | -13.3519 | -54.41221 | 2025-08-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d74b4a8f-9bb5-325d-a019-6b03d1430a04 | -12.10421 | -47.91803 | 2025-08-19 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98acaad9-42ef-3e90-829e-b78f7328252f | -13.57781 | -47.00687 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81a5c5b6-0786-3987-b26b-42190cf600a1 | -12.50259 | -45.56317 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e366169c-950e-32fc-820c-0d780de3dcbe | -8.82429 | -52.04021 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f41fa12-717c-33ad-9695-10775f5602bc | -12.99931 | -45.1929 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 117bcc80-27c0-3073-9d26-bbb87ac85bf4 | -12.29492 | -50.01192 | 2025-08-19 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f29e282-c49a-381f-945f-7d371f62b864 | -13.15868 | -54.91587 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e02125b5-75fa-36ad-956c-fb2d4651afec | -13.43167 | -45.90951 | 2025-08-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
