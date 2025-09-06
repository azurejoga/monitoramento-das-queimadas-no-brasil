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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0681fa39-27ab-3bcc-aa49-a2d7448a0b8d | -5.87025 | -46.04197 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce638502-69c6-377e-9e65-85c6612be50b | -5.65638 | -43.61788 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 727c0b6a-7b42-3fea-8ca9-a3363554601a | -14.55983 | -48.01526 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c335142-cd00-3f84-a1e8-91a239510d08 | -7.58548 | -44.69758 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bddd4cb-0197-3ac6-8b8b-a8ab502bdb0b | -5.34124 | -42.78768 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a1b0209-adea-3b86-b5ef-425673657a60 | -16.5461 | -42.3494 | 2025-09-06 04:17:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0587ae71-c371-350f-a17c-530f384470b1 | -5.95472 | -44.74309 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ead3adbc-ab58-32fc-84d4-ba37dde630aa | -15.3647 | -46.41092 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48ec325f-41df-3739-8cd1-2f53fe92419b | -6.9118 | -44.17151 | 2025-09-06 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3241893-04b0-3be9-95c7-b05eb901a68a | -5.71679 | -43.93799 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cad01f82-f4e4-3555-933c-345104630d08 | -6.60414 | -43.97723 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5665c72b-0736-3d47-b51f-11178f28c558 | -14.78017 | -45.31778 | 2025-09-06 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| cb18379d-023d-3de6-a3a6-6ec5bfc7346b | -7.04809 | -44.35024 | 2025-09-06 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 67afde4a-0e39-3ce9-bf85-f261250c74af | -13.0187 | -54.84198 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1adf189f-1cfb-3468-8986-840ea2d73023 | -14.19006 | -53.06972 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3b34b6b-0dd0-399a-a8c1-f61a7ae136ef | -9.80655 | -48.30333 | 2025-09-06 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 926d2597-1665-316f-8f8b-a3f5fb25481b | -9.87852 | -46.54207 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd138820-cef8-3a4f-86d6-43b7dacf3319 | -6.15431 | -43.16499 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 03f2950d-9817-3d34-a828-164fa34a609e | -5.97819 | -53.59853 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3202e6e-27dc-3d1a-9aa4-f455a68e77a3 | -16.90426 | -45.74492 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 430f8f14-852b-3042-a9ef-ca2e0bf8caa4 | -6.45391 | -44.67753 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45c3166e-dcc9-35a3-b57a-f30183cbc261 | -12.9646 | -54.81878 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc3a3945-481c-35f8-922c-579e903f6019 | -10.06573 | -48.05972 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 963e200b-2e05-32d9-a6cd-831ecaae03aa | -6.33939 | -43.55761 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 071fd975-383c-3467-8b77-3a009096d9a8 | -7.71161 | -50.32648 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42fb1f35-3d36-330e-9faa-ca9358ef6f99 | -6.87468 | -52.79096 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f638420-5a7e-3116-b184-e971b0717ff3 | -13.88896 | -48.02587 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6023b323-7053-3ba8-a763-2a2f39f1ef2c | -10.31093 | -46.41476 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e246473-02ee-3851-9bf2-c3492d5ed5ab | -6.86429 | -52.78541 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2548abfd-17b0-3a6c-80ba-6b0a8cdadda9 | -9.40663 | -40.30825 | 2025-09-06 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 33f61ed5-61e0-3422-9d6f-1812bac22954 | -13.04239 | -56.85968 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f29b3c3a-2d27-3313-a410-27030be6bde8 | -7.73068 | -50.32589 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 929a56cf-6e19-312a-af2d-52e096ad81a4 | -5.74145 | -42.75839 | 2025-09-06 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ceb05dbe-a07c-3116-bfc7-59ead27ae213 | -10.0641 | -48.06905 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257facb4-3b29-31ff-961d-e7d13c3e7923 | -8.02241 | -45.4284 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c35bb1a-6ce5-3b17-81c3-d0e8725f6cf8 | -13.57004 | -48.12254 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 988b7cb8-132a-3b7c-a7d4-84875ec1d115 | -7.00516 | -44.94304 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8490e63b-0cb3-3e2b-a83e-a4dd531f4fb1 | -7.04752 | -44.3538 | 2025-09-06 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 788b5493-8699-3772-abd8-178943991c02 | -12.99922 | -54.82174 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 763983ec-2e02-3673-bd09-27ce99c3b4b2 | -14.58806 | -48.0019 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6626918f-ff9c-358a-acae-2d558bf86284 | -6.15047 | -43.18929 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80e32038-4851-35e7-a3d3-a7dc91b91677 | -9.30746 | -45.41626 | 2025-09-06 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| d3b06114-c020-3f07-94ba-67cc380f3f0b | -6.16439 | -44.30856 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00c4f0bf-334f-3455-803b-5a4aa2663d48 | -5.98275 | -53.59246 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eba8e614-0f4e-3501-a6c2-1341598a4c0f | -8.51331 | -51.32478 | 2025-09-06 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68abe5c9-175b-340e-ae13-7e1262bbd093 | -5.03232 | -49.76208 | 2025-09-06 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dad85ea0-adaf-3142-a0e0-14f24124a190 | -7.72785 | -50.31469 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 74761fe3-4aff-321e-b6b0-1136d9d75564 | -5.6575 | -43.61087 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83c9cd57-8b90-3b40-ba0c-3a69cd280652 | -6.21455 | -43.35942 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26d4d031-0258-377b-ae1f-68923753ebb1 | -6.16104 | -53.68924 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fcced1e-2c97-31c2-83eb-6a4bad8e55e5 | -5.18497 | -43.04643 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2389a3d4-21c0-3f60-a26a-fe7b06bf60f5 | -6.89553 | -43.80027 | 2025-09-06 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 928f3624-ad51-395b-96cc-8af83fb515a3 | -2.7878 | -49.62449 | 2025-09-06 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 086ec40b-bfaf-3b3f-9079-e679c36da51f | -15.84429 | -52.28032 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00f1341e-36d2-3640-8bf3-659226b8b1e9 | -16.28168 | -43.37869 | 2025-09-06 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ba314d7-e0d6-3d35-8f71-b5a61043fe27 | -7.83904 | -46.21338 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bae6a717-7131-31af-b1c7-6cdddc6f3fec | -5.68066 | -45.17135 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42ad8ef9-abb4-30eb-844e-71df884b27f2 | -13.74747 | -46.93068 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21c585db-2a5b-3787-b0ca-4107719d44e2 | -6.54221 | -49.51196 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10d90e53-1427-3320-a14a-e23fdc8aa7a6 | -6.51218 | -42.41935 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bed4f5d7-7b61-3607-bd95-62ac5305b6dc | -5.63019 | -43.65327 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f1099dc-8343-3434-aafd-65ce5e2e396d | -7.83256 | -46.20818 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daf282bc-7cfa-3d94-8d3f-0b6beea7b14a | -13.00015 | -54.84665 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ccaf073-a11e-3981-8999-eee03fe2acec | -10.15987 | -46.23384 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4275485-9ad9-39ce-b4ca-ee872923b0e4 | -14.18512 | -53.06876 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c04edce0-536d-308f-9c2c-7a2ad5f79c5c | -10.0679 | -48.0577 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 135c4a6e-3545-393d-953a-0686cc255e58 | -5.86339 | -46.03383 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f29276d-fca2-3e7a-bd1d-01215bf3b245 | -13.00738 | -54.83981 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4395199f-25c8-3884-878e-26cb57be2e3b | -6.21743 | -43.57768 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39835b86-95d1-3f17-9032-c541287a9823 | -12.90704 | -48.0169 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8b6087f-48a1-34d7-8d07-9b2b0283bb50 | -6.60639 | -43.96302 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c45fc35-1b73-3890-b326-9f54015253dd | -6.15972 | -44.20872 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d726354-9389-3918-8990-6787c9138aaf | -12.98876 | -54.81535 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 622ed6fd-86e5-3dce-ad99-9f310af93b20 | -6.81992 | -52.81102 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db6dcec6-6e90-328a-9097-0c4471c1b53e | -13.56712 | -48.11761 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e95632a-e8d6-371c-9559-ea974af3520a | -12.96377 | -54.79373 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf655559-0793-3920-8946-83991a4301c8 | -9.43444 | -46.75206 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17ae7d5f-3f17-341e-9009-d2386459da36 | -13.00817 | -54.83584 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4033400-dc96-332f-9d2c-c5e3c439fa8f | -7.96462 | -44.94799 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5369065c-62dc-3926-9804-34e0dd10f427 | -6.95667 | -43.95398 | 2025-09-06 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03864bf6-887a-3333-8d8e-04ae483bec4b | -6.2681 | -53.43234 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 823ad8b7-5088-31ae-8c95-4b750b1de37c | -7.23429 | -43.86156 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29ea5cd2-2638-3219-a7d4-054dc06f1612 | -12.95575 | -54.80439 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2680c172-21b5-34e4-b17f-bde1a682dbc7 | -7.97967 | -46.33863 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb148c65-f09e-3d02-94c6-0177c513c303 | -14.57647 | -48.00474 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fff19c59-f9a8-3872-8c2e-6fec2515f47c | -3.31518 | -48.71254 | 2025-09-06 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0d17770-b0e0-3a5f-ad9e-2389d651c40d | -8.36445 | -48.27487 | 2025-09-06 04:17:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 687048e0-eb2e-3f33-8054-00c01c9875b6 | -14.57286 | -48.00418 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17284a28-2068-3ece-9c44-586e2a5037ee | -5.2003 | -43.69703 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eaae93b-b2ff-339c-b335-6f7b0a2e0c17 | -5.96613 | -44.73293 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5750a05c-d2c3-3617-9223-5ae0e5c2c84d | -10.1494 | -46.23212 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8da9470a-96bb-324c-b536-70e202ca6a52 | -5.85197 | -46.10501 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6123e82-c3aa-3178-8dd8-29672af35757 | -14.25658 | -52.18293 | 2025-09-06 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31c16a4d-8b42-3f44-b147-2f7c63364aec | -3.45454 | -47.63054 | 2025-09-06 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d263ff17-96a0-3507-9fdb-198bd4d9244f | -7.34507 | -43.95453 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c31be47f-2701-3b1a-9596-0db80b6c98a6 | -4.82381 | -42.73864 | 2025-09-06 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ce145da-6ccb-331f-9dab-9d2c40fcd76a | -12.5159 | -53.85014 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45131a1a-5a01-3d7b-8946-47982ddb520b | -13.92709 | -53.99994 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a02de325-8f4e-30c6-a50f-2a5e8709d9eb | -6.26791 | -43.49633 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c379c70-feb5-34dd-a84e-fe41e9711a5d | -13.73135 | -46.91154 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README41.md)
