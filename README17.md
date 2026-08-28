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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55227346-d1eb-320c-8933-f3792a214b4e | -7.88885 | -46.09083 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 593ad48d-9786-38e7-bbbf-5f69f51bbf78 | -6.6494 | -53.18964 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 620d44ee-18e2-3531-a519-c98c309481af | -8.01229 | -48.4039 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1177906b-a301-3bee-b311-d16d71c9efd0 | -4.169 | -42.43591 | 2026-08-28 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 80d23ea5-a822-3ef4-9ab9-23d0224b0be8 | -7.24759 | -45.86263 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e7839e21-5c63-34d4-a47f-cd1a327c8fec | -6.64195 | -53.19165 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 977e29af-4478-336a-8b63-2b64b0ee2575 | -7.27174 | -46.69402 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ee382a0-1608-338e-811f-2f4d6c32f141 | -8.32998 | -47.63352 | 2026-08-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c989a85a-0b2a-3cc3-a4a5-611423fc9315 | -6.75958 | -46.13858 | 2026-08-28 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 325d1fcc-2caf-332c-9eb9-612f6ecedefe | -8.28922 | -39.97207 | 2026-08-28 04:14:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9799cb8c-a23e-37eb-ac05-9635eb00bee7 | -6.24823 | -55.47288 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acc50861-bcf2-327e-8e6d-d4909b5bd3cc | -7.40313 | -44.67247 | 2026-08-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 419acd76-2a95-3cc1-b0aa-a701eaacfeb4 | -8.01722 | -48.01792 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 738be786-2a23-39ce-9ce8-f1cbd61d4f2b | -4.84147 | -45.39116 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad094ccf-b029-344b-a2cf-62a1ee02b9a1 | -5.34193 | -45.16245 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 93afe9f5-e647-371b-be8b-32f10e38e7ae | -3.70067 | -45.24282 | 2026-08-28 04:14:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 167c7593-5a85-385f-bd72-b36efeeec2c5 | -6.61771 | -42.54138 | 2026-08-28 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4fbbd9fa-62b2-374e-b1e6-299dbd9c16e6 | -7.27007 | -45.35649 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d9e39ae8-846d-3dcf-9423-c563edbaac4c | -7.02036 | -42.1124 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6cef1ddc-2e34-3cd6-86a1-3fdbdad7a3ca | -6.85433 | -45.05878 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7acc8523-aeaf-3828-891f-00f9b2ed501f | -7.31372 | -42.96455 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 35b03706-bc2b-3c1f-9d9e-030b42365c8b | -6.75797 | -55.68748 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34551bd7-cf72-3585-b34b-d7c3bca64dc2 | -1.36661 | -54.63588 | 2026-08-28 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b24cac0-baa8-3d16-9622-7ebdc443fbdb | -2.73043 | -47.04248 | 2026-08-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49ad025a-979c-3fc0-a656-fe487743c3cc | -5.87178 | -52.18723 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32a6b240-ade1-37ce-baf9-573c5f5130e9 | -7.31041 | -42.96404 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f03d7dd-4e40-3ce3-be60-8f9d03224bab | -3.76858 | -49.07376 | 2026-08-28 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf377392-4664-370a-8ac3-fc2f3df3bc74 | -7.26217 | -45.86103 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2c54913a-7a16-3f85-84b7-e28b450cc388 | -6.90106 | -43.64785 | 2026-08-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff0e6c0d-4529-3b3a-af61-2df65f431394 | -7.26665 | -45.35593 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd24de16-4141-35b9-a427-6114bb5a8d93 | -5.89641 | -52.10869 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e59a4ca-d102-3637-9c0d-285c1fe0c512 | -6.62715 | -53.18541 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb39cfe2-d03d-358a-b9fc-9a603b86c780 | -7.88537 | -46.09017 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d60fc75a-f092-3a6b-9b99-7a1d92a15bc6 | -6.03409 | -46.76003 | 2026-08-28 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c524c6d-5eae-3af0-9bb1-f252fd5cfac3 | -3.53517 | -48.18224 | 2026-08-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 910bfe96-98ca-3dfd-b064-bee5a24d472f | -8.19086 | -47.53651 | 2026-08-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff76fdd3-cefb-344c-98a9-dd7d0ae19b57 | -6.9329 | -42.67979 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ba2faf48-980c-3bf9-92c3-3054926d0c0a | -8.17357 | -46.17113 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd76f956-38f8-3254-8c10-ac18f9810ca5 | -2.7173 | -49.47557 | 2026-08-28 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b8ed014-44ce-3c97-8a88-7b8f361aa908 | -6.1834 | -45.91135 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89776cdf-9fff-33de-9ec7-5cce48455fec | -7.1009 | -42.18378 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1676f808-00d5-3216-8eb7-0531c24f90f6 | -4.84435 | -45.39561 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f20b20a9-1149-3936-80ac-a56cb588e1b7 | -8.06575 | -45.86868 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9264c4ca-d370-3a31-97bd-c6bf15dea027 | -3.0632 | -48.74939 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37f62a79-ea3e-3ddd-a5bc-1a6ad4d29e23 | -7.0881 | -42.79722 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6e0346fc-5539-3e3e-ae11-ed2b5b2c3e30 | -8.15111 | -46.19287 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f2f8df4-4c70-3cef-91ce-544228af2b37 | -4.8501 | -45.40451 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 30b99e07-64b5-3a5d-9a6d-757f03280252 | -8.06637 | -45.86483 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 019d2655-4794-30f2-ae79-8cee3dbd0682 | -3.4657 | -39.58273 | 2026-08-28 04:14:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| db4a1b33-c924-338d-aa15-f28aab69fff2 | -2.73124 | -47.03747 | 2026-08-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d1946d4-c962-3eba-ab30-d6944ca323e8 | -6.63827 | -53.18755 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce2a8ed9-c429-305c-8d2f-6bf1ab635fea | -6.76341 | -55.69437 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18b799cb-6a38-3c77-af94-98c09d3827c2 | -6.50018 | -53.26236 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af519a6c-eb58-3b4a-84f7-c0954ef5debd | -8.07501 | -45.81116 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e43f9219-9b14-3e66-a431-a09ef5c5e639 | -4.17177 | -42.43986 | 2026-08-28 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d362bff1-74ab-3478-a5b9-05433e1b013f | -7.20226 | -42.73987 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 25aa69e6-cf15-3105-b7d8-feb0e9628f93 | -6.24174 | -55.4718 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0aaa027-1bf5-3906-8b1f-7f5224678d49 | -8.20515 | -47.5201 | 2026-08-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80a7bbaa-a0d5-3f65-82d0-a362f557d018 | -2.88797 | -48.80172 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2ac8834-85ee-3f85-b077-f131115dce34 | -7.3371 | -46.66524 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b9f585a-6e10-3461-83b7-6ef718ce2e2c | -6.27787 | -53.36831 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b6ca238-a3bc-362a-bd9f-adecd637610f | -5.93808 | -52.3624 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30b3545a-09d2-3079-bc20-074e6fcd7e67 | -5.9375 | -52.36567 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d155a6d2-3258-3048-9ec5-7f95650399d4 | -8.16787 | -46.16208 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aa3ad82-e8c2-3fb1-a376-d26fff4d7258 | -7.78159 | -46.14682 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c571971-c93b-30a9-bb2d-3653af5d43d1 | -8.20455 | -42.85326 | 2026-08-28 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 05c9b48b-4475-37b1-92e8-65e9e4f3ef3b | -5.92738 | -52.36066 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bbb8d8d-18cb-3547-bb8c-125a1f67c312 | -7.25805 | -45.86433 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 29901026-0a1f-3e00-892f-15d409495379 | -7.10261 | -42.19498 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9eb31aea-556e-3fe3-94de-23f8696151e1 | -7.06314 | -43.59166 | 2026-08-28 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2125b146-1912-3a39-9990-095fe3b49d4f | -6.82521 | -45.54812 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c41eb9ff-7382-32ce-a744-a489518bfc7f | -6.24076 | -53.47974 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 541899c3-1695-39fe-aeee-eb39579b2029 | -5.87716 | -52.18763 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4c5f22e-3065-3e0d-800e-a33626aba14a | -6.26335 | -53.12094 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf26e21f-b9b3-31a2-b6ad-413cf6a35333 | -7.7401 | -44.73707 | 2026-08-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dddcdd93-675e-3e07-8b7a-2709fbd40a48 | -6.63706 | -53.18689 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfdf9ef8-76e1-3aa0-ad60-f462729591b6 | -7.67206 | -45.69715 | 2026-08-28 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5feca57-056a-3c0c-8327-37c8d7816a40 | -5.49466 | -49.21468 | 2026-08-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1da733d8-114e-3336-9845-a2110dd4ecdb | -6.12961 | -53.5326 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69386622-dcd5-3526-a4e2-721cac2a713d | -7.12183 | -43.17208 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76127995-9a5e-346c-a815-d847d8ca46fb | -6.85773 | -45.0593 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 480453bb-e99f-324e-a6e3-44583972e17b | -7.25742 | -45.8682 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e645d0a7-ed62-3cbe-b7b5-6e6bbb425141 | -7.25931 | -45.85659 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b9bd21e4-c365-3baf-8960-c5259b76ddae | -8.19011 | -47.54097 | 2026-08-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccc2d922-f374-331d-a851-ae9ee1ea78a5 | -6.13034 | -53.52844 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24831495-bf39-3302-8ea3-fe58c30243ee | -5.47159 | -45.12062 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cb2e9e0-d222-3d9c-a71a-e247ea487425 | -6.27121 | -53.14162 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6b16cac-2ea5-3452-a639-f3411f9d4345 | -7.12558 | -42.77449 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab193ed9-fe93-31ac-8a27-ceca88ae34a1 | -7.26412 | -49.84499 | 2026-08-28 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbcb44c7-a3fe-33a7-bf2e-2d6560c8d075 | -7.30457 | -43.02354 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aeb319b8-ef89-3bff-8c04-0957baf5b9db | -5.81039 | -43.6414 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 412ba1e5-e1b4-3a61-97c0-b3808a0f66d1 | -7.88059 | -46.09748 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 83f6f01a-69ea-3f44-ad57-9283dd9444ab | -7.01982 | -42.11594 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| db08f9f8-8180-3762-92c0-45007aa69cfc | -5.99389 | -52.20079 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d81a2179-88fd-3870-b243-9de0590980f7 | -6.93676 | -42.67682 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc01e50c-5574-314b-b18a-7a70c78b8422 | -6.30462 | -46.4143 | 2026-08-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f611e0-7bcb-3d38-b289-f0fce0de403b | -6.87621 | -42.87057 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 38251b22-3684-3fdb-b69c-42fd0666e863 | -7.58893 | -39.51981 | 2026-08-28 04:14:00 | NOAA-21 | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 24c381d5-44bd-3417-85ce-fac2f7d541fb | -5.34598 | -45.15924 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 584bd882-7b04-32d2-938b-dab5bfcf804b | -8.0629 | -45.8643 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
