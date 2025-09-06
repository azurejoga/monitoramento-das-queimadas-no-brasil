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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28c84887-10be-381b-85db-efad4a573d1e | -12.96298 | -54.79761 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d293f6a4-88fe-380a-9019-3bde871b7580 | -13.74595 | -46.9185 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 773c638e-1f5c-3ea3-be11-7f57a8b21f0d | -15.63216 | -41.85746 | 2025-09-06 04:17:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27a5415d-5ab5-3b4c-baeb-1783fbec0d90 | -5.87456 | -46.0384 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 318db8c1-ddaa-32c3-ac29-08ddd717cbb4 | -5.95933 | -44.73624 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dea855c9-04b2-3e19-a29f-5b7f1ffd7f29 | -10.16042 | -46.23714 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 052357a4-d908-312a-bd4c-297c9f58e3be | -6.18763 | -53.25177 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f531f128-6b3d-372b-b927-1a77f538342b | -12.89877 | -48.88666 | 2025-09-06 04:17:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 776fa9af-c46b-3c89-bf57-1b42856774da | -5.85983 | -46.10477 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e6caad0-7538-3910-9223-cd070222fc10 | -12.91804 | -48.01893 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe58ca87-71d2-3fd0-97b6-4d760d32b675 | -4.45459 | -44.13997 | 2025-09-06 04:17:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0fc1eef-97be-333a-b227-ce10eb02648e | -2.78865 | -49.61942 | 2025-09-06 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4c31d75-264c-32e3-afa3-54c4111e6094 | -6.16209 | -43.18045 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da5712fc-4529-3f03-a883-9720354c150c | -6.00905 | -43.6987 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ac4c66c-7158-3ddc-8abe-4874c4aead98 | -6.26593 | -53.44447 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86223bbe-df4b-3ce2-ba71-0814927e7747 | -14.57574 | -48.00895 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7749ab2c-0aad-3cca-b21a-ea91c2777702 | -5.86439 | -46.03251 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 400a0ae4-8ab4-3150-a7bd-67e539d1d95f | -8.6757 | -47.43673 | 2025-09-06 04:17:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d82aeb34-f72b-3a18-b62d-5bc4bfc5872c | -14.18019 | -53.0678 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6c048055-1169-378b-8d12-113bdad9b9be | -5.99561 | -44.16125 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 114bc7fb-8d81-312c-b50d-23eccb94338e | -5.86345 | -46.1054 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81d1cba8-cbeb-3e9c-b03f-5420f7d3965c | -15.54128 | -48.41804 | 2025-09-06 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 156092c6-3a3e-387e-a723-6c1409b6b6a1 | -5.3203 | -44.92694 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 618f2df7-9319-32b5-97a9-461c7ffc8efa | -15.19026 | -48.04665 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff7d65b-c85c-3cac-97cc-1d4cd5165706 | -16.30784 | -45.69195 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4519dacf-b15e-3e21-a420-4e5cb49f00a8 | -10.60005 | -44.33339 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 3f1b4500-f4b1-3c39-a409-9d0b0bf1d6c5 | -14.57864 | -48.03539 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b306359-5b68-3aea-a499-b664d5c7f4c8 | -5.96334 | -44.73313 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d44031e5-d4c6-34dc-b519-a02266d9b206 | -6.60692 | -43.9813 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35927b80-0fd2-3eba-b7f1-bd292995d771 | -6.07381 | -43.35467 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a43ecbf-c603-3b91-8b83-94a3631085b1 | -6.40299 | -46.09285 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d319478e-6b74-3e14-a937-92e83a197b31 | -15.54363 | -49.8198 | 2025-09-06 04:17:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76b7ee21-6219-3832-a484-f2fee7ba5fab | -5.95531 | -44.73939 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b7d413b-105b-3c24-8087-8e25b2883ea2 | -5.92605 | -51.99741 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 612bf75c-11ae-3466-92ed-5933ccbd50f3 | -15.85743 | -52.31028 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 086a0d63-c189-3c1d-aca1-37a90b3c1c59 | -4.50967 | -42.89074 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45b24c80-2b7a-3644-8ffe-2ec803b8aed5 | -8.01925 | -45.43663 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7502c32-177c-382f-9bf6-65a819a032ec | -8.10215 | -45.32965 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| abf85cc4-2f2d-326b-b703-422b28374cc5 | -5.87387 | -46.04255 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a4aae8b-b682-3d2b-a356-b02541f73732 | -12.48999 | -53.85748 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34b58f10-1bee-313d-8a8c-18d73fec013a | -13.01146 | -54.84889 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e81c587e-4662-3487-8133-6be067af43bc | -6.15819 | -43.16204 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49b945d5-9c03-3323-92a3-c7d604a32e36 | -14.58868 | -48.08534 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19e5c44b-dc23-3e78-b0c6-ecf97acdb7c9 | -9.07732 | -47.00708 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 937f95e1-0371-3c39-8564-4cdeb370c33d | -6.11019 | -48.10332 | 2025-09-06 04:17:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 280fa099-2337-3201-872a-5ad212f368a5 | -5.18552 | -43.04297 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4db9acb5-6293-3ab4-bd07-757ef663fc73 | -7.68985 | -50.28806 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5bc8a92a-76cb-31fc-a3c8-4e5866dba79c | -12.89492 | -48.88597 | 2025-09-06 04:17:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f593f95b-9c20-3fcd-a448-284fcff04dff | -8.78023 | -49.634 | 2025-09-06 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58352e1d-059c-3a01-8abd-6c262365905d | -13.73972 | -46.91317 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35f6e2c3-337b-3519-8da2-6b80a4141847 | -5.95074 | -53.80215 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4b8ccf3-b6f2-30e5-ad16-d981b771963d | -12.95177 | -54.81249 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 869a4eeb-226c-33d3-9a91-e9484e6ff5f5 | -6.27026 | -53.45378 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c63b4f3-6b82-32f6-a7d1-3f8b0de6c544 | -3.37526 | -50.84562 | 2025-09-06 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df421d3e-0e51-3162-ad12-1786676a8ebd | -13.71438 | -46.88493 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c39f9e63-df05-3441-94ca-f9029e794635 | -9.24502 | -44.49826 | 2025-09-06 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f14e64ce-bf1f-3e34-9696-1f06fedf3514 | -5.95585 | -53.79683 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f8418cc-898c-3804-974d-d5d907ab5a84 | -5.86508 | -46.02834 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6369b42-c2a6-3439-a007-468d8138b197 | -4.50356 | -42.88623 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 97184112-c7f1-342e-b461-3fab858c1b4f | -3.37425 | -50.85161 | 2025-09-06 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0042bcb4-e653-3147-9f7d-665aca1820ce | -12.48934 | -53.86091 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9735058d-6d08-30c3-9b3a-febe96d4d158 | -14.61915 | -48.98706 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa252f52-ab17-346b-8d4b-9ae72bbdf0ec | -10.60338 | -44.33393 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 907414cf-51b4-3b6e-ae06-9586ed74a0aa | -12.89313 | -48.00988 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f06592f-f8e0-3c60-b5c4-05e6c3e18983 | -5.49236 | -42.15283 | 2025-09-06 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cc190ed-4126-3ff2-99ae-eb1d7e28c897 | -10.31573 | -46.40748 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0988e1c6-6052-3cdd-953d-d20ee8e5d14e | -7.59745 | -44.6661 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 341eb7b0-6a7b-302e-bc5f-f3f04ad4127e | -7.60687 | -44.67825 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 330a0966-5552-3937-a642-eaf0cd4c764d | -7.42041 | -44.94429 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45d78212-6e9a-376f-8e95-6dec59d6899b | -12.92169 | -48.01966 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 598ec497-ada3-30db-909c-7c5cfdb5d119 | -9.08743 | -47.01402 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2fe1bfe-6b1b-3ec4-97f8-64b91a6d0b45 | -15.16699 | -42.59501 | 2025-09-06 04:17:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cdfcbea-a3eb-388e-9e8e-1c0059ce8fd5 | -16.29119 | -45.6891 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76a8c20c-e1df-36fa-b05c-04d440d4662d | -9.68218 | -51.09221 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b1c8174-77ea-3bf7-a060-b735aeb3d457 | -6.15322 | -43.17193 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 47a78ab1-ca11-36c6-81a3-f6f1f2fc65d6 | -3.37937 | -50.85255 | 2025-09-06 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69c127db-9693-39f2-a771-c26050b14e73 | -8.35961 | -48.27929 | 2025-09-06 04:17:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5eda18b-9e12-39e5-9f23-ba32d809f4c5 | -13.92835 | -53.9935 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b7309f9-8b98-3136-bc9e-16b5ff8b875e | -14.15808 | -41.67487 | 2025-09-06 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e4cc0c98-29f7-3dec-96ed-5730275988ba | -9.688 | -51.11358 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd785c50-3ccc-3f8c-a2ad-fb89d38cd118 | -7.60745 | -44.67466 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 934a7321-f83d-316a-93fa-f363eaeb07c3 | -7.72863 | -50.31013 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5756c3fa-11cd-3dab-9dc0-6c0530536d91 | -5.97529 | -53.60001 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c078374-6cc4-32f9-92e3-0123c9178427 | -9.18222 | -46.03428 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08f1fdd0-24f8-37cb-b5ce-2cec50c934fd | -12.98479 | -54.83525 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d64eb7-4d93-33c6-a965-4aa623fde54c | -9.08816 | -47.00971 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dbd8a7c-f756-3cd2-b8eb-daa535a0ff07 | -6.38532 | -43.00916 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c1ccaed-69dd-3ce4-bb15-0c9a2394dc50 | -15.17454 | -52.40659 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 009ca53c-b65b-3c90-b3df-a5821a1c96b4 | -6.14714 | -43.18877 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddf9d302-e674-33c1-ac06-6fd5bb6acffb | -3.75366 | -49.05563 | 2025-09-06 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dacad2c1-02ef-390c-bcb6-60424576a352 | -7.41817 | -44.93645 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58cf311f-ed93-3717-92f0-77e92c572d0c | -13.55171 | -48.11941 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1d8070a-7b80-3462-b7a0-ff92e7bd08eb | -7.40958 | -44.94633 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 809280eb-18aa-3ef6-8724-23f2bc2a084a | -6.99724 | -44.335 | 2025-09-06 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0e6d2a0-6fb3-3509-8d5a-deb143876c7f | -7.333 | -48.49363 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cde4bb3f-aa0e-33d7-acf7-ca107736cb72 | -7.89086 | -45.23127 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16ec1adb-3695-336f-ad98-4e3cd286c216 | -7.00964 | -44.95892 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fd2e32c-bfbe-3a19-8173-a9cb62c166da | -7.72835 | -50.30768 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 62f9b849-8ab7-34c0-be03-e42a4edcf053 | -6.15932 | -43.17645 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a27dfb9e-8dee-30d8-8416-291d1e35bb1f | -5.99504 | -44.16484 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
