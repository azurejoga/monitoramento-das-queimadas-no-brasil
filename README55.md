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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c70359c-2f76-3097-95fb-58441838f1aa | 1.22823 | -50.98782 | 2026-09-20 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ee4deff-0c76-3916-a81b-17b536c14100 | -6.35589 | -43.36902 | 2026-09-20 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02842519-8cc9-3ca6-84a3-380fc1f3ea78 | -6.97571 | -42.17328 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a313211b-edc2-3e4f-8390-b95e5e9349a4 | -3.69205 | -60.5975 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c1e5e1e4-e7e7-3edc-935f-d90c8c215cee | -5.53524 | -45.67558 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f878aedb-632b-30f2-bce4-912d618aad73 | -5.2814 | -49.34936 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e063521e-b94e-3f0e-a187-29fc1ccde667 | -1.25247 | -55.7703 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af2bbfbf-3c8a-39ff-9cc5-1ff87a18d32c | -6.69439 | -43.00753 | 2026-09-20 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f592d8f9-1fda-305d-adc8-ae1e6a5aa7f6 | -2.92871 | -51.93843 | 2026-09-20 04:38:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be6792c0-8668-3a08-8f1f-7004fb64b577 | -5.78029 | -47.366 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffdecb03-8165-3ae7-85b8-cfb1f80c6a29 | -5.66204 | -43.40358 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ae7aa81-3e63-3da5-9af6-72a235f722ee | -5.23737 | -47.55721 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 950148ef-cb1a-3779-89a5-fc322d0cbaaf | -3.16316 | -48.611 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42a6c27c-357d-3c97-94b8-6ea5fe2cea70 | -6.41139 | -42.81536 | 2026-09-20 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 739c9a96-e100-34b7-85fd-55995b53ff18 | -2.90547 | -54.18767 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be43548f-6210-3e99-9d87-9f2a7ba514cc | -3.4448 | -50.60976 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| effea447-8afc-3bb8-86a4-7bb1f33c4196 | -5.82642 | -44.13516 | 2026-09-20 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9292f081-9c9a-335a-b428-8ae8406f0045 | -6.9206 | -42.91075 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57df100b-b7cc-3e3e-bc90-d2193d4a1cf2 | -1.2174 | -55.72089 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9bd3a5b-6eb8-3c0a-9f11-21860798c417 | -6.92007 | -42.9144 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61297fe5-1770-35e5-bc67-b7cf1b775e5d | -6.97768 | -42.17491 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 88f8a85a-56b4-3994-9d07-509dc93cd670 | -3.16595 | -48.61509 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a210a5e9-32c8-38a0-8c7f-2aa40cbe9cb2 | -5.66646 | -43.37424 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4975b59-6195-3b42-9b4b-8fa81fa0f045 | -2.98328 | -54.77336 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a707f1-bb30-3ae8-9c8b-953e0d3d12d0 | -2.87937 | -57.80684 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 004fd97c-e78c-3cd2-b885-643f6bb638bd | -7.30747 | -42.26917 | 2026-09-20 04:38:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fb296755-a4d9-342c-a40f-04bd31580d4d | -4.891 | -45.62959 | 2026-09-20 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f98bd5bf-b777-3d19-97de-dc43d594eadd | -5.56944 | -52.01781 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18cda565-0517-3e4b-a06c-1b27104bdcf2 | -3.89925 | -49.06896 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 2504c4a6-3e89-3ece-8104-d6c621750803 | -3.40641 | -50.40162 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c8bb3aa1-bf12-353f-ab73-7d1b2dcc17e2 | -6.56134 | -45.58717 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dbbc6932-6ce5-335c-a37a-4ba862eaaf8e | -2.71184 | -57.96163 | 2026-09-20 04:38:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e40e7d5-3944-3932-980c-96aed7d36269 | -2.8161 | -54.71659 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9fd157d7-d308-3c0e-9ca5-344b68c7a571 | -5.32955 | -50.09127 | 2026-09-20 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6493c4a3-de55-3173-baee-f19cd45e95dd | -5.57674 | -45.54539 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bc40feb-f9db-3531-99c0-2ca94146d56a | -6.283 | -41.77276 | 2026-09-20 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 628a6a14-24cf-3895-8ff8-9aa31d467f33 | -2.88823 | -57.82556 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 448b386f-9791-30a5-8c88-460d3b5cf2d3 | -6.3225 | -47.63303 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 547ba13b-93e7-35ef-aca6-54456d6a4b79 | -5.40135 | -42.95177 | 2026-09-20 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51aaad0f-d40f-39be-8fda-7d9bc24570d0 | -6.29982 | -47.60459 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf4922e3-78f7-30ce-9d9d-609c1b7b21cb | -3.03896 | -51.3715 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bba425e9-09e3-3f1c-ba57-e29ef33857ce | -6.20411 | -47.52163 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 41650678-3a2c-3351-a3b2-5ff5dceb1618 | -6.25743 | -42.72848 | 2026-09-20 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7afd8433-24a8-3158-af99-df04209858b4 | -3.44253 | -50.60083 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84d37c08-644b-3396-824e-b431a19ce086 | -6.8842 | -42.9311 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4dc3389d-43da-3827-9f8e-7814bcdc398a | -4.36508 | -55.05483 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b7eccf5-df49-3dbf-9303-cdbe2caf2d54 | -3.35084 | -59.87904 | 2026-09-20 04:38:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2d1fa1c-2819-338a-9a13-b874dc9f4ee4 | -3.81986 | -50.74695 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e31919-60db-3cac-ada4-dd992602729c | -3.49197 | -49.50792 | 2026-09-20 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 448fd069-a82f-3f46-8399-cad744a07cf9 | -3.82826 | -51.88788 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5774a2e-da32-3cea-a7de-9a6459a014ee | 1.00658 | -51.1874 | 2026-09-20 04:38:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b80c744-3d48-3f33-9432-fca8babfac32 | -2.82337 | -46.71012 | 2026-09-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21553d5b-73ac-3e10-a975-c566e1ec4bc7 | -6.15064 | -47.51676 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fd634b1-2a73-3b3f-9638-de47377d25b5 | -5.66909 | -43.40962 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c4106d1-612f-36ee-bff1-49829e48fb88 | -3.07436 | -51.20113 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 012090ed-e8f6-3a28-81ab-a4421e02158e | -6.20546 | -47.36143 | 2026-09-20 04:38:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fc9e8d9-635d-3c2f-b126-07583a6618ef | -3.45179 | -58.22157 | 2026-09-20 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b0e92c7-f337-325e-b2e0-7b5775333c01 | -5.7941 | -47.3646 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3eb6a67c-14f1-3294-8b2a-6f6574008f96 | -5.23631 | -47.58533 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e79272a1-6b8f-318e-badd-385d9a5a07d5 | -6.06245 | -46.97345 | 2026-09-20 04:38:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ff52856-0c87-3d84-870d-39982e37fddf | -5.76214 | -47.28835 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93b68414-e475-34dd-bdbf-4f23194953f6 | -6.39755 | -43.19379 | 2026-09-20 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 849bc224-e10b-3817-9306-c3f2f69c5cfb | -5.83965 | -52.02834 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53e0a6fc-ca10-37f5-a089-f40699223588 | -6.19708 | -45.32486 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ee9f059-6d08-3382-a0bd-ec25f605a455 | -3.35744 | -59.88019 | 2026-09-20 04:38:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e3b9e10-5137-3172-b578-f07e94de4cba | -6.19237 | -45.33217 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78af91db-f915-3eeb-9fb7-35425251432b | -6.92523 | -42.90775 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94acc5fc-5c99-32fd-9e83-4850cc5a7280 | -6.31311 | -47.628 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a06227ee-54a9-34a9-996f-6c8fce7901ac | -4.56899 | -42.97283 | 2026-09-20 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d7e5a97-f71d-3594-ba6b-8d37908a0f0d | -4.29892 | -48.63047 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67a3824a-e478-33de-b620-8a0ae39d3120 | -11.47784 | -47.78656 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e97de73b-9459-3687-a78c-30ba21d40e56 | -9.37627 | -45.37442 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1599b327-2450-356e-a8be-26215ed555b2 | -11.86849 | -47.6549 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ba12f66-9f01-356d-9b53-f74bce4b0398 | -12.80952 | -54.0625 | 2026-09-20 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75046018-11bc-3124-929d-b22029988e93 | -10.4632 | -45.0836 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab35efce-61ba-3fb3-ae75-846d0d2a54e3 | -9.1284 | -45.72883 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d1f2dae-0b31-3572-b21e-cf2cccf73de2 | -11.87868 | -47.65649 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58bff5b2-41fc-3874-b4dc-2d7d8dd415de | -9.83066 | -46.39263 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c61e103-1c04-3bcf-9cd7-b8866f0f27de | -11.26959 | -54.11737 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffc24c11-fb90-3f76-8023-984cc56146ef | -12.53048 | -50.03771 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3981f749-d429-32f7-a472-25e036b342ce | -12.29393 | -47.1144 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 603e5f91-36b6-3936-99e8-2e98751356b7 | -7.74315 | -46.70703 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2e53b45-1f7f-36f5-a57d-d5ad248f99a4 | -10.8739 | -54.09221 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b04d9909-98e3-3292-9a55-b4a1e3601d5a | -9.68184 | -54.33718 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7659dd95-3e19-3ee8-9a0e-2a004528dedf | -11.11542 | -54.02558 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| baa950e9-a6f2-3580-a6d9-8c4713ab1241 | -8.67518 | -45.41999 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73c57485-3287-3227-b076-7f96a095cf07 | -14.12176 | -45.59985 | 2026-09-20 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58e16766-2bfd-3755-9de6-0202da8557e5 | -6.64452 | -47.70121 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ab07d14-2298-3edb-b06b-a188e9edf33e | -10.20876 | -54.26033 | 2026-09-20 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d73c612-6ba5-351c-9d25-ba602d260e61 | -8.39252 | -45.62607 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 120b70f1-ba2d-3da0-b15c-7ce6e340a0bf | -11.87714 | -48.99797 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e4f653d-129c-3eef-a028-3e1cbb337112 | -11.50426 | -47.74949 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59dbfbdd-2670-3a26-a70f-1aacccb7c7d8 | -12.90372 | -51.0019 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 237737b4-897c-3422-be2d-46cae8cda4c9 | -8.17078 | -54.76417 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0839e8b-0fc8-311f-95f6-07547acfdcea | -9.28266 | -48.20152 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66c61f04-7aa9-327b-bb74-7ab55618cb2a | -5.85486 | -53.54345 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fee2139-b388-3ff4-afd4-bec28d091388 | -11.8661 | -48.98174 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 339b01c1-9abf-336e-95b1-1ffc783bb396 | -9.75601 | -46.06979 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bafaa09-9f93-3b7e-9874-4815f307b6aa | -7.58016 | -46.73823 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a03ae39-f54c-3e58-bd77-c4f1e4128536 | -11.12914 | -54.01726 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README56.md)
