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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c2d3a36-8154-30ea-a5c9-5eef5db1d1ac | -1.10672 | -54.15318 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c8ef8ff-a188-3ec8-9eb9-91bf4400ffa8 | -6.88725 | -45.02541 | 2026-10-09 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4a67abd-f256-32e6-8f15-d0c937e3a22c | -2.99933 | -54.04949 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59a5c7b2-2e37-3086-a5ee-3becd52e9062 | -3.26629 | -54.01991 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d5715bc-5ddd-346f-a759-f55964384626 | -2.82855 | -54.11534 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dabcae98-4906-3971-9eb4-fe5b99625edb | -2.99693 | -53.90625 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f4abdb21-9cc5-399b-b4c1-4f5ac8aea336 | -3.08047 | -54.29643 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c81b8b2a-3db1-32f2-9bc7-8292700eff2b | -3.78004 | -58.58401 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9d5b6512-3a2b-3b88-9c4c-b3454318a59b | -4.96483 | -42.68429 | 2026-10-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb828d68-3dc4-36c8-999a-ccf0b7ef6406 | -3.29969 | -54.00455 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20e19375-3831-365e-b24c-f4c04a98d34a | -5.59102 | -47.2826 | 2026-10-09 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3d91d09-dacd-3aea-9012-0bbe8dcd4406 | -2.50281 | -56.07175 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| a51e311a-f120-35f2-82ab-1aeeabeb96b9 | -3.43524 | -59.53758 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9bfb680d-fa08-3735-ab34-866567450262 | -2.34051 | -48.87163 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f643f78e-f3e8-314f-8ce5-0a7edb09929a | -6.89328 | -45.89618 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc1a71c4-6a56-36d6-b453-d077e2d99e7c | -3.94546 | -55.84545 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15e04a07-dceb-3066-a125-497803934f79 | -7.0246 | -45.31089 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b16555a1-4869-39d3-ad90-cdc7c746dec8 | -5.41822 | -44.62821 | 2026-10-09 04:25:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce3dc9db-e70d-3266-bb19-acd0fc4b6a65 | -7.4054 | -35.18948 | 2026-10-09 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0cfad092-0fb2-3ebf-81a3-fe60e072abcc | -2.50349 | -56.06765 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| bacdd94a-cd60-3089-8ffc-98c28cf306c9 | -2.83067 | -54.13406 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c47af74-d2c1-38dd-b9bd-d4b8acad4d8f | -2.49712 | -56.17764 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 230c7b97-91fe-33cd-9008-6e1f86338697 | -3.19717 | -50.56609 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2accc2a6-ce2f-36d5-bbc6-4d5c4ffdecc1 | -3.99173 | -59.35937 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 20cbca80-6898-3263-885f-f5288edc2352 | -3.13233 | -54.36438 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e3923be-d078-33cf-96ef-2d82936dbcd8 | -4.04461 | -51.08395 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 540fce86-8407-3faf-9fbd-55accf1572d3 | -2.77969 | -54.07256 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ddd56f-5352-3a26-b767-36266fade469 | -6.15652 | -47.2788 | 2026-10-09 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91f88e57-b2c6-3f1a-97bb-f17c14bb0ac0 | -3.38154 | -59.4301 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 673991fc-a866-3f03-b384-6051b3e0b7cc | -5.48944 | -44.29737 | 2026-10-09 04:25:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 386bff7d-631b-3ebe-b3a4-df9c408f2c1f | -5.71588 | -53.48856 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 77ac3ed6-6746-3131-92d4-2625a8406838 | -1.15414 | -54.22734 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 951d2973-03b0-3deb-85f9-bb69788d5ad7 | -4.82811 | -45.83139 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 73011240-7e13-311e-b7b7-ddbaf97676df | -5.09665 | -42.65372 | 2026-10-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd3a4c45-666d-324d-9877-209ad73725cb | -3.09095 | -53.95969 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40926a0e-072f-34c1-af07-ba20445d6304 | -2.40126 | -51.299 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48fddded-56fd-38a9-a72a-003067cc6539 | -6.19317 | -45.40794 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7261a3d-226b-3ab0-ae60-eae700725e49 | -4.63402 | -50.96114 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c172983f-707b-3989-8c54-311075b625ae | -3.02454 | -54.05361 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea493b0b-18aa-36bc-be28-ad5027ab83a3 | -3.74141 | -59.3732 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a3b29130-8602-3d91-b419-d31e356763e1 | -3.09047 | -53.96256 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a707f101-8f60-35c6-a513-4d8dcacbe41f | -2.39624 | -57.8969 | 2026-10-09 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5155ceba-2a9f-3597-8d5f-9d05336691ee | -5.71516 | -53.49294 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3487dc4e-420a-3620-868f-deedd20e0be9 | -3.09333 | -53.9452 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49582952-fb85-3c5b-a9a6-66186e23851b | -3.17653 | -50.44649 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20cf5af4-4d3d-3825-8d97-7029da575dfa | -3.05623 | -53.92147 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 559dba99-3333-382f-b4d0-0c9e23777d50 | -3.00323 | -54.08943 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6762962e-2b5f-3bb4-901f-a3fbfc5913ac | -2.33586 | -48.87211 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 53d080b3-c811-3797-bb94-4f42493ec88b | -6.88281 | -45.89813 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ebe1d93-3b21-3ba0-bc14-ad969f77c83f | -7.38141 | -39.97559 | 2026-10-09 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1cd72611-a63a-3cd7-9cd7-fdd3e21356ac | -3.01172 | -51.01531 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8730fb46-b64e-3fb7-a6c1-83166204da87 | -3.04214 | -54.09856 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a60c634-ef71-3b96-8709-a5041f8ce899 | -2.78065 | -54.06664 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f313e230-a9bb-3430-a493-fd5fdfa56c9b | -2.88391 | -54.18072 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7a9a3217-3b25-3bd6-92ec-b200270eea42 | -5.70196 | -53.48627 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3f0fff21-cf40-3482-a0a9-be6bd2d476a8 | -3.18688 | -50.5794 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de09c210-a8ba-349b-a82e-b1c3304c7f87 | -6.90869 | -45.88429 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70668b6c-eaf3-33e5-a4fd-0957f047578b | -5.38537 | -44.22104 | 2026-10-09 04:25:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 936f4944-fd45-3535-b002-78f2c3363ea1 | -4.9395 | -45.72868 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d88538c2-7261-3c4a-9bfb-fbaea884e855 | -1.60642 | -55.16306 | 2026-10-09 04:25:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd8859f3-457c-3b4a-9f70-dbc0e061eae8 | -5.43624 | -45.68291 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34f7ec25-4b97-3d35-9bc6-78f04bff7dea | -3.00657 | -54.06876 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bba31b0-cb39-3f13-9218-a07985f823c1 | -3.94083 | -59.79193 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d3d9739-3db2-3ade-a498-2bc2fd56c5b1 | -5.70128 | -53.46169 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41ccbb55-9bc3-3f80-8a6a-d51499580665 | -3.03005 | -54.10876 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26d7b4a3-5ea1-3ead-80b0-35df22682652 | -5.37836 | -45.94606 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 308cba34-8ac3-3245-bd57-1b75d645b2ef | -4.64167 | -48.7388 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c48c4b74-b136-3bf1-98d0-b8bd5f1cee71 | -5.70374 | -49.08392 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b405491-53c3-34dc-b35a-6e3e8197f3d0 | -2.99407 | -54.08192 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 070463b5-11da-36d1-bc6a-e9b85b2a629c | -3.80264 | -49.94388 | 2026-10-09 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74d3c248-6dc2-3882-9ae7-1dd2e85228cb | -3.08443 | -54.28645 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a07c849-3c7f-3a6f-85b7-198b9158fb04 | -4.04783 | -46.90247 | 2026-10-09 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45a3efd7-7659-3f9b-9b5b-55e85c5b26a4 | 0.50583 | -50.78583 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbe31df6-5ac4-37cf-9f74-0cb6d146a2a0 | -3.72752 | -53.69949 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 28e60d54-f38e-3676-884c-7dccf7d8e48a | -3.11008 | -54.19223 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bec8ec67-3ee7-3668-8b4e-30fd322eb455 | -2.89245 | -54.17175 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ce35f1a-2c6f-33ba-be64-93bcb7bcc740 | -2.95971 | -49.17421 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cb7cdd3-8047-38fa-a8a2-9c14f65350f4 | -5.97867 | -44.26376 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55a1f6f5-df35-373d-8d0e-4453054eee46 | -2.99403 | -48.91546 | 2026-10-09 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d4e034a-a50a-3fb3-ae47-bde28f4b9f64 | -5.44008 | -45.67996 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8077f8e4-fe39-3e6f-afbe-3b64d8a409b2 | -3.34832 | -50.47851 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3da175a0-1f88-3431-836e-b62efdb8bed6 | -4.2943 | -54.80557 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef16583d-493b-36ee-816d-d9a31655d52f | -4.26319 | -46.2873 | 2026-10-09 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc678199-c01b-3c43-8822-347cb6cc8960 | -3.18291 | -50.57874 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4db58cf3-69d7-309d-bfa3-1b1e32a03460 | -5.72054 | -41.61909 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e4091631-b963-37cb-859f-364959318a20 | -5.63547 | -45.80211 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 016b21fe-b3cd-394d-9a33-5ccd4433f137 | -3.02945 | -54.08129 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8744ab1-6611-3c35-a0d9-abaca4ef41fe | -3.01281 | -54.0877 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec35a040-bba8-333a-9e12-ed9405923a8a | -1.30556 | -54.19023 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b694ed8-8b89-3330-8423-7db837bb7f4d | -3.26726 | -54.01414 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab325166-4744-3660-88a8-1d91f29e4daa | -4.95009 | -49.41876 | 2026-10-09 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8a40a75-385a-3751-8ffa-d5184863e8ac | -1.89535 | -54.67356 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4561c9e-4f95-3254-b67b-c2b1fe681354 | -6.92318 | -44.55646 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f348c4c0-8768-3460-b94d-59354d39260e | -4.94307 | -45.66207 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85cae138-dac1-3ae2-b295-0f8a2beacb1e | -3.00874 | -54.08103 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 009f8e92-7fea-3b73-923d-05b263337d11 | -3.74284 | -59.44923 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 365f21b8-128e-3705-9e5c-b3ce71948942 | -3.00096 | -54.76455 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11553e70-122b-3141-a5fb-435bf3d0c84b | -5.05871 | -46.18795 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c163737-8f27-319a-83ca-4bc013ca6604 | -2.94037 | -54.15568 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d4d731d-f132-35a3-8425-14761e5935f5 | -6.0082 | -40.97243 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |


[Clique aqui para ver as próximas entradas](README87.md)
