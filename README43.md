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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4ae96b1-4fed-3393-8940-e74107e43343 | -10.06716 | -48.07414 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bed5ea3-57aa-34d0-9551-e016be70d89d | -12.95788 | -54.78104 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bed9c077-4ad4-3c6f-b6c6-062b78417856 | -14.56926 | -48.02514 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c14bcf05-52bd-39aa-ab32-f4b3707914db | -15.16677 | -42.59636 | 2025-09-06 04:17:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2548a421-e49f-31cb-bdc7-1bd6cdc171c2 | -4.56004 | -40.344 | 2025-09-06 04:17:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 58cfbc75-6b6a-3b32-8d7f-6e83d994da6c | -6.42494 | -45.89425 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb7cc227-869e-3da0-a4e2-0138d3b2039f | -6.34876 | -53.44831 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57c8d1b3-b695-3455-9848-3032bb305296 | -12.49852 | -53.85376 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89ce30f6-d20a-3ec0-8d09-12cb9382cf9d | -5.9499 | -53.79568 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c5f00e-f572-3eb7-bcb9-1a24e225eee8 | -6.04889 | -44.41624 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47399b0e-c4b3-3bc0-a4ae-39497cdd66bd | -12.97428 | -54.82905 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50e61127-62df-3b4c-b41d-a08f5f980cab | -6.40601 | -43.81889 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2d90069-455a-3945-9949-6bbb41b341db | -6.5348 | -49.5018 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dd1468f-1af4-34ea-b8c1-1a76ed0efa2d | -6.54831 | -42.94207 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27f9edba-fcb6-3624-93a7-06611efb4c6c | -12.78407 | -48.16246 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e79988ab-2217-3f41-9acb-51b44014354a | -6.61236 | -48.0564 | 2025-09-06 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 637efcdb-9f19-3755-82b0-d0a7508a7314 | -6.15934 | -43.1978 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7cb66988-13c5-3f16-95da-70af793cd42c | -5.68146 | -45.17063 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93977ff1-c4bc-3335-9331-2bbb32b022b9 | -7.33174 | -48.50105 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7770ca5f-a5a0-3d7b-a25e-af8a1ab93261 | -10.60726 | -44.33096 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a5d9bce9-9eb8-3dbd-9454-70ddde19aff6 | -9.84543 | -48.83772 | 2025-09-06 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abce2c2d-6383-3460-bde3-091e655131ed | -4.49691 | -42.88519 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab31af33-8367-3ea2-9082-0d271f85b454 | -5.33847 | -42.7837 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 892b74d1-5d51-3d25-bf26-57203d5dc8ea | -5.84468 | -44.11875 | 2025-09-06 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dac3d30-e8f2-39fb-8827-cb2f670a58d2 | -16.92033 | -45.7514 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c22df16e-8d61-36ba-8ad7-51df44fc3f0e | -5.75377 | -43.13334 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8792e41c-beda-3f60-8e3a-0c4498f4422f | -10.16273 | -46.2383 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9c222b2-f26c-3131-b59a-f9ed8082771a | -12.90007 | -48.01725 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75bc8607-c097-3d44-adfd-a324fe992d70 | -5.92782 | -51.99789 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4e78efa-e66d-3946-baff-29271709d60a | -6.26458 | -43.4958 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6729b7b4-32ed-3d46-8366-8aaa0ec1eba6 | -5.21035 | -43.69862 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0ee6013-b06b-3c0b-89b6-8a9d6f9526b4 | -6.3893 | -43.81626 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50961785-f063-35dc-b7c8-d976a068f113 | -6.16182 | -53.68501 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 995791ff-f957-32f1-aab0-8bc2aa8ee3e2 | -3.75295 | -49.06007 | 2025-09-06 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88f6c0bf-869f-372a-a64b-7c624d3f5b08 | -14.1087 | -51.71975 | 2025-09-06 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb7f53f2-aa09-34ee-9bf4-02a350d57026 | -5.85159 | -44.83698 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05852b1f-1415-319d-9738-9d9975eaaf20 | -3.73996 | -44.37543 | 2025-09-06 04:17:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 818cbbf4-1c3e-3e9f-8247-30a080b2eac2 | -14.57855 | -48.07937 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da9b7bf0-ef83-3fe1-a2e9-4cd16843daf4 | -4.54696 | -41.77253 | 2025-09-06 04:17:00 | NPP-375D | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2667233f-5cfe-31bd-885e-50070de44412 | -4.7964 | -47.26499 | 2025-09-06 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf9566fc-be23-3e9c-a91b-37662d925355 | -7.96802 | -44.94853 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01debbac-3140-363f-aec5-ed394fb5d24f | -9.71279 | -49.49444 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d19e1706-9ca4-371a-b8d0-e7f82dcfbe11 | -15.18684 | -44.0095 | 2025-09-06 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d4619d-8079-3a65-9796-9f8930a1d5cf | -14.58509 | -48.0846 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8bb6a28-f790-3fb2-93cd-cc9976d41097 | -6.03569 | -43.69622 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23a18cca-831a-3235-b86d-70012fe66c32 | -7.17123 | -43.99899 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 481b8ec6-4d6e-3365-986a-d4d763b2b2db | -3.16261 | -48.60334 | 2025-09-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0766d95-8ccf-3ad0-a94b-ed2bfbbcf9d2 | -5.97311 | -53.59282 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d4fde3d-f0b5-34a3-a741-1762476b2c3f | -13.00331 | -54.83074 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e4416eaf-8cca-30d1-a6c1-b11ae4015884 | -6.1563 | -45.0259 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 753028f3-ac8f-31d8-aca6-b0efe70a5081 | -12.98558 | -54.8313 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af9a89ad-e799-3204-941b-a73c3b5c1a6c | -7.83613 | -46.20875 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecac2014-d066-3f38-b422-6dfcfcc38671 | -12.96046 | -54.78105 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcbc098c-df65-3cb5-9e6c-009c92e9243d | -8.87943 | -47.25676 | 2025-09-06 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2f8014c-79d3-3a98-95df-9d7afd6263ec | -8.88254 | -47.91177 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dbe7690-6cd2-30ff-a7c4-d5e843c5843e | -13.28533 | -46.8142 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bbfb433-5398-3e8e-9eb0-97ad0380db21 | -8.8625 | -47.91289 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef3a7952-65b3-3986-a2c9-954dd356b4bb | -9.68511 | -51.10273 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 897bd827-d8eb-3fbd-9f7e-e1aee6c92b1c | -6.22921 | -42.64689 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 27bd0c88-cc8b-37a1-8d19-2fdececc3f43 | -5.92558 | -43.19956 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7b247df-a7bc-346b-956a-bc6309c27ea3 | -15.54754 | -49.82053 | 2025-09-06 04:17:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7348be82-cb0c-3636-9d53-55e84437c5f4 | -8.35492 | -52.51708 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa09099e-b026-38e5-ac87-2fb93cb05be7 | -6.8753 | -45.55052 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 30d638be-60e2-354e-974b-a79e47238360 | -3.3487 | -46.91385 | 2025-09-06 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff5ea888-5b59-3436-a7df-c27de38b1bc2 | -13.05594 | -47.10688 | 2025-09-06 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce24995d-beda-3c78-a2b1-7b872b58dde9 | -7.33707 | -48.49451 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b01077cb-2400-3fa1-a098-b079e889991d | -5.84074 | -44.12178 | 2025-09-06 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed914ca0-872a-3e39-92c5-e72e64eaa662 | -5.7251 | -46.44523 | 2025-09-06 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13628c09-580b-3c15-8971-5e6f790d8048 | -9.74554 | -51.06205 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd0dec26-35d0-366c-abd5-fd07f6d928f8 | -5.72274 | -43.13556 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 285cdb1e-46f1-3e7f-8b4b-906a10c7b3e2 | -5.96845 | -43.41644 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecd44773-8d7b-3e02-bf82-1ba834b90fcc | -8.03617 | -44.094 | 2025-09-06 04:17:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9193fa0b-f2e6-3d7b-8379-294e1fc9ab90 | -12.9533 | -54.78748 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d671abb-23a5-32bb-90fe-a22365753e30 | -15.67 | -45.88857 | 2025-09-06 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fba034b2-cdca-3611-bdd2-b7a230ea3bf0 | -3.10771 | -47.49746 | 2025-09-06 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 663d4946-5e8f-33c1-a5dd-17bad8f3d95a | -6.51196 | -43.06443 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8834e5df-38bb-366a-aa7b-4f749e3b8ee0 | -15.71293 | -46.24775 | 2025-09-06 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fc92b39-4c2b-3ea9-be19-35e7950273da | -5.86768 | -46.03024 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb634ef5-0be8-375e-b2b9-1f1896eac316 | -12.95254 | -54.80852 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d61dc8b-c403-3c4e-ac66-7dda289bc0e4 | -6.48602 | -43.97617 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08495e0a-8eb0-3812-ab2b-9a0e0a4b9fc2 | -15.64371 | -41.85482 | 2025-09-06 04:17:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| efc04164-5d14-38ef-b911-f33a0029c57f | -7.30266 | -43.73257 | 2025-09-06 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d79de049-324a-36ac-9308-dbe48d3d4c02 | -8.90954 | -45.11098 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56e1e244-81ff-335f-8200-61e9e908578f | -12.97022 | -54.82001 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e26515d6-de2e-3d55-800c-05652ed2cd9d | -6.50381 | -42.40728 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da28292e-9440-3c20-b252-a66ff3b71202 | -9.17873 | -46.03372 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45078ec9-d69f-30a6-8d61-4ef9fb01bc5f | -6.14743 | -45.47747 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4599923d-ee5a-30a4-8a9b-8883ffe93652 | -6.07596 | -43.29799 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c4a9780e-2b35-3a8c-bc0a-8f8b5b2efc9d | -14.19117 | -53.06398 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b692f63-1782-346b-9bf0-03dae3ad88a3 | -13.50704 | -50.80917 | 2025-09-06 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9117f4a-c40e-3584-9a09-e8aed644c66e | -12.49248 | -53.85617 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2941aeed-f22b-3e4b-90f1-0e89aba906a0 | -14.57809 | -49.13088 | 2025-09-06 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9886c913-80b7-31a5-bccd-e29042af8dcc | -6.55664 | -42.95406 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0edc11f-9568-3a25-af91-2b3575352d3b | -13.70748 | -46.88358 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41095543-b6b2-3bf0-b742-17c4a803cb14 | -7.05724 | -50.85501 | 2025-09-06 04:17:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76c7d9da-491e-3b0d-80e8-d1551e553289 | -5.96866 | -53.603 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6675df05-041b-3bca-961f-10aa40afda18 | -5.75907 | -45.53515 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e67007c-c1e0-30ac-8413-c4401605facd | -8.01399 | -45.44728 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46b815cc-2139-39f2-9819-f7ed3f1b9eff | -12.967 | -54.80679 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ab54784-a3ca-37ff-817c-922caae2e96e | -8.77089 | -49.63657 | 2025-09-06 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
