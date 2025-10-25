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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ed85473-ca1d-3c3f-99e3-ff3fba3cc6f5 | -3.23856 | -48.75818 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6068d1bd-203f-3d4f-9b07-f8dda6dd69dd | -4.72399 | -49.08801 | 2025-10-25 04:17:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf423bd5-4fd3-3f27-83f7-09f7837ae0b8 | -4.55461 | -46.67835 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d725c092-bda8-3401-aa40-1d1f294f268a | -5.51678 | -46.41634 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 30dc15a0-8b90-3162-8260-54964ff17902 | -5.56752 | -46.95514 | 2025-10-25 04:17:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3fb17fd-5250-3375-94b8-b36d64c08529 | -6.95708 | -37.51615 | 2025-10-25 04:17:00 | NOAA-20 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7503b634-6e5c-3116-bac6-63e2a9501c92 | -5.21879 | -49.14202 | 2025-10-25 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2246c43f-d0aa-342c-827f-26bfd5b1777e | -5.68342 | -42.76553 | 2025-10-25 04:17:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9035adc5-fb7f-3aee-9d62-1527df9a89f3 | -4.82852 | -50.92919 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a124fe44-aba2-310d-ae68-7b8e69951925 | -2.72205 | -49.16703 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 562cf601-b24d-36d7-aa3a-7a7ec77cb91d | -6.02962 | -39.62312 | 2025-10-25 04:17:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| efc20a24-ff2b-3161-a441-adcd16769fe5 | -2.72263 | -49.79001 | 2025-10-25 04:17:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bdbfdb7-1934-337a-8743-be93350d2d5c | -3.99464 | -48.317 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3519e01f-e3ac-38ca-b9e4-172c5832ff86 | -6.31173 | -40.92041 | 2025-10-25 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5c4d4f84-deea-3e47-9210-d93196d030a9 | -3.98786 | -50.52438 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6b00d99-da13-3026-b615-a3caf709a3a1 | -4.60063 | -49.58504 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad46e561-ab78-3c76-8861-d2e14494d6af | -3.02506 | -45.39792 | 2025-10-25 04:17:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fb2d3a9-09af-31b4-9107-644294fedd99 | -2.69004 | -48.7121 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 290e7af9-5d96-3846-baa6-89d6ee6c266e | -4.70918 | -46.44125 | 2025-10-25 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268adc34-5843-3594-b320-b00eceeb8ece | -4.76297 | -49.53026 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a96b75fb-8284-33df-bef7-73c8c39b10a5 | -4.72741 | -49.09213 | 2025-10-25 04:17:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae778b73-a637-3beb-9b38-d6e016750f59 | -5.57274 | -46.35249 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c547a28-111d-3e2c-98cd-dc6b6adb6781 | -3.70655 | -42.81062 | 2025-10-25 04:17:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fd6ea8b-7b8e-3fe2-9ce3-8aa3a89f50ce | -4.25064 | -44.57613 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2da924b8-8f7b-3e0d-999e-449df15c99a7 | -5.65169 | -45.97297 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a212a9e-3adc-3288-8b35-5c2775f370e0 | -6.43221 | -42.02348 | 2025-10-25 04:17:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b932920f-44e2-36ee-94d4-7e73bde71d9d | -5.69184 | -46.28761 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c869ffd-13eb-3a1d-afc0-a4607b0e4858 | -2.26692 | -47.85791 | 2025-10-25 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b5a8a26-71d4-3a8d-ba7f-f7b6b078a57d | -3.55978 | -39.09291 | 2025-10-25 04:17:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef466c0f-9de7-343a-98fe-0ab9ba8d5e56 | -4.87248 | -47.52871 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 914eecb8-cb27-3eb9-8e2d-9935b57f89ba | -3.7002 | -40.42415 | 2025-10-25 04:17:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 63d3330f-0381-3687-810a-0e313fa37918 | -4.25009 | -44.57959 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beda8467-e896-36ae-b12b-444dfc3916f1 | -2.80841 | -49.14565 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53b54b78-af4f-3454-b096-8701173d7fe6 | -3.13923 | -50.62224 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd714ff6-c36c-334f-bba7-cefc1e82cc98 | -5.37976 | -40.70943 | 2025-10-25 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e37dab68-b64f-3d17-ba1e-27e0bd0cc0ae | -5.45749 | -45.40689 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e7d8e6d-dd75-3cab-82d3-7dabccc9df38 | -5.54301 | -41.38338 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fa67870-b9aa-3bb6-8e1b-a9f5ac216c18 | -2.58156 | -51.34709 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04932ac0-b4aa-3921-9e0c-950a79b7ce28 | -3.1401 | -50.16534 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aac914e6-9686-3079-a793-8e8925514619 | -5.64831 | -45.97243 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11393827-06f8-3b26-a243-3fa90abbfd73 | -2.79086 | -48.89139 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 52389374-a363-34a7-852d-d4a8c5c39644 | -5.68003 | -42.76498 | 2025-10-25 04:17:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1867d9e4-8eb6-3e25-b445-a01ce3b2012a | -5.47097 | -40.87356 | 2025-10-25 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34bc8888-18e1-351c-90ac-4df9ddc931e7 | -6.08925 | -39.19469 | 2025-10-25 04:17:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bbdb6440-3ba7-3b0b-87b6-9910d2bbec1b | -3.43456 | -50.26725 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2413e611-d68d-3351-9e3e-cba333f3258c | -2.78753 | -49.59554 | 2025-10-25 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3273817-cad8-3c1b-8fcc-70d3a40ed449 | -2.81314 | -49.14257 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8550ca25-0bdf-3e80-985d-06fdeb5d1bbe | -6.14071 | -42.46083 | 2025-10-25 04:17:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d31ec6fe-e63c-31c0-a9ef-db678b09ae0e | -4.22704 | -48.61666 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ffdc2b0d-295d-38ed-b823-c78b8bfad2bc | -6.13501 | -42.45222 | 2025-10-25 04:17:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 893a4f75-f75a-39e3-86dd-e927ce4be8e2 | -5.41824 | -46.00674 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae406f2c-f931-35f2-9245-ff11d37dfc00 | -2.74101 | -48.6842 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67d9104d-55f3-3c98-be18-4291abe2ba7e | -4.29128 | -48.26262 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06eac25f-3458-37bf-a874-13d551b1c8fa | -4.55682 | -46.68685 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d9eb2cbf-86dc-3a2c-8de9-043516c2eb4d | -2.80012 | -51.35699 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f6192a9-be87-3b8b-a595-2dd6e6e31985 | -5.03196 | -41.20227 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1724ee9b-3c46-3c9b-9dd5-214855a17a10 | -6.22877 | -41.84083 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd7c77ef-e89d-3327-bae6-5bc0cca700a9 | -3.48059 | -49.89679 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a27d46-0b91-3e8c-b9fc-8f2ecc22e957 | -3.70388 | -40.42468 | 2025-10-25 04:17:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6eed8903-8df2-35e7-ae26-f67beaea1fe0 | -3.14081 | -50.16105 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4a140c1f-aa63-33a6-8370-6fbe17324d98 | -4.61698 | -50.51049 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97ee3c18-6ff2-3d38-8e5f-a4f2a959cacf | -3.08069 | -49.47272 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de523cab-f47c-38e0-b33f-433368e50207 | -6.12589 | -41.73365 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 446738af-9ad2-3014-b95e-4db861648b87 | -3.32363 | -50.22807 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37769798-518b-34d6-9c7e-b6c6297ab537 | -2.72974 | -49.15959 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e365865-712b-35f3-bd06-c985616bf128 | -2.29711 | -48.56897 | 2025-10-25 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61e6c857-4cae-3cdb-9532-6de30162dcf7 | -4.59108 | -50.9732 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a9649bb-7305-357b-bd93-b28e401a7ba2 | -6.28748 | -40.86479 | 2025-10-25 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ec94e8d4-0458-3b78-8bfa-9c854454a4d6 | -4.80099 | -46.74372 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1c7b4cc-d718-3e4a-9402-1e1b107dc8e2 | -5.30736 | -48.7009 | 2025-10-25 04:17:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad118107-8433-3d7f-9e10-7c996c1bb811 | -3.83214 | -42.54949 | 2025-10-25 04:17:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 343b5354-1f12-3755-92e8-a23172ff29bd | -6.24018 | -44.65064 | 2025-10-25 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 885d1066-b74e-3d79-9103-a4675aa9f6cd | -4.27358 | -44.38876 | 2025-10-25 04:17:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a323c3d-79a8-3f74-bac1-4201716e3a0d | -3.21401 | -45.46135 | 2025-10-25 04:17:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3cda1c2-dbb8-3125-8787-93a57153c9a1 | -4.4551 | -38.44418 | 2025-10-25 04:17:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fdffddb8-252d-31ad-86ff-5fd1e5f94b2e | -2.8966 | -48.06572 | 2025-10-25 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75da9e67-ed9d-33f9-aab0-92d3c8af4b08 | 1.43638 | -50.89752 | 2025-10-25 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 205d27e5-b586-364f-92c1-ec49733fb729 | -6.13728 | -42.46028 | 2025-10-25 04:17:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 125cc6bf-5014-3d91-9a5c-8c64d533cc57 | -5.58951 | -41.31924 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11dcf015-48ba-3853-b037-243cada81a80 | -6.06915 | -42.1521 | 2025-10-25 04:17:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a852a3d3-01cf-3025-a80b-763cd580e462 | -5.42629 | -49.58251 | 2025-10-25 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc5b3d27-e8e9-3c5a-98c8-58fc3e2f74d2 | -4.58011 | -48.54973 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4264920e-1078-316a-9c14-6ae7bcabe158 | -4.22395 | -48.61109 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae46b209-1894-36aa-80ef-df1e5b1c17b3 | -4.00028 | -41.02206 | 2025-10-25 04:17:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14556a81-5f56-3ef9-870c-ba4cecffa718 | -4.97241 | -48.36156 | 2025-10-25 04:17:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7dddb2f-f283-37bf-a0fa-ea4bbc2d776d | -6.43351 | -42.33025 | 2025-10-25 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee09330d-4ad8-35c6-9a13-2af2d098f47f | -2.80016 | -49.14427 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d792f46c-1cf5-3b70-854e-96bb13324a6f | -3.91452 | -47.68628 | 2025-10-25 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5be933b2-9a73-3f1d-9ca7-696f87ec08dc | -4.0934 | -51.05389 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55af8d85-9a73-3c66-9a4e-d2cd3e4a8487 | -6.17898 | -42.62264 | 2025-10-25 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7f57747-8b89-32f0-a9a3-9af7ac8c1db6 | -6.54669 | -41.5779 | 2025-10-25 04:17:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 656cab68-7efe-3bfe-8538-81d34e23690f | -5.29836 | -41.14437 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4cd6d2e2-e8c2-31fe-94e9-7ee535747f6e | -2.87021 | -50.71737 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68a94838-0fa7-3b8c-b3fc-af9ba134cc7d | -5.59384 | -45.19136 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 569803d9-69b9-38ce-aba1-bfac3331d13b | -5.60484 | -46.26229 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f596cd4d-48de-30c0-b969-3e32510950f7 | -4.59588 | -49.58813 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86693cc4-d69d-3c08-b25f-19da0cb6a4bc | -3.99231 | -50.52514 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acd056b1-72d1-32e0-a2ef-8c3bad8d8a0c | -5.17536 | -50.12848 | 2025-10-25 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8bdfcd6-31ea-361b-931c-f43c0df4bebc | -4.86776 | -48.40981 | 2025-10-25 04:17:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b50f429-342c-3898-b1fd-8da5a0dd8474 | -5.43353 | -45.86026 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README31.md)
