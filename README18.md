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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37212617-f7e9-342a-956f-7c329c6548f4 | -12.85775 | -48.05644 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6315a19-b31f-33e4-9e59-8daf644738d8 | -13.69928 | -46.93562 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 1772ad17-5595-3918-a8ae-4bf8efb604c8 | -15.43955 | -43.3145 | 2025-09-02 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45ce4d96-1a04-3580-ad5c-d61186d4fba7 | -9.47699 | -47.60239 | 2025-09-02 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44e8c328-d7fd-3f47-96de-ccd4120371a8 | -10.05581 | -48.09647 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 80311603-a97b-3de8-acc7-1458353a3794 | -13.70504 | -46.93288 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6580e8f1-f519-39f7-9737-d47048bf5faf | -11.0131 | -46.94023 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee7813fd-4997-3576-a60f-9366b55f8eed | -9.83483 | -48.31776 | 2025-09-02 03:51:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fbd22ad-c756-3c10-9fac-8b7a4cf2eaa7 | -7.69139 | -50.2719 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f9f5dead-9dd6-326d-9730-cf5caed8c32b | -7.92505 | -46.43858 | 2025-09-02 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50ced150-950b-30ca-8de4-b97d602f4bdc | -11.37259 | -43.55222 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d53e96c-47d9-33b1-abc2-981d11e9d371 | -8.70486 | -50.43052 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2283677a-0fec-32c3-9a0b-c80be5e52ca6 | -12.99446 | -48.11438 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24d5114c-53ea-3cd9-8eb6-692d0470bec2 | -14.5921 | -48.05381 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5d398b4-f655-3893-aba7-97e31dcfc3bf | -11.82039 | -51.54879 | 2025-09-02 03:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3afd1e28-d949-365d-affb-9f1d0199d0e9 | -12.95853 | -48.09305 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e892e32e-c3c0-3782-99ba-4609a55291d9 | -7.98144 | -46.46734 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3bf404cf-ccec-3efc-a421-6365c9a4aedb | -10.04673 | -48.15205 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a4e6e84-a8fd-39eb-85d5-d24d54c659c1 | -11.36907 | -43.54753 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0716944a-9807-3c65-9b4f-e4d4ff480fe6 | -10.45522 | -49.05828 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8c3b493-947f-3073-9fd7-4c08010f3f21 | -14.05529 | -44.56814 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad283c1f-deb2-3e0d-9417-960e5c796826 | -11.67422 | -52.18665 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 45839e2d-6a46-354c-885a-cf13873cd0ab | -12.94755 | -48.09058 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa64f0df-6e99-3bff-a068-13e4a7f15d1a | -14.92758 | -43.95861 | 2025-09-02 03:51:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea6755bd-53fd-3bab-bdb9-117a6b3841fb | -11.97648 | -45.87637 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2690692d-d8b5-3fe1-bb0d-b5f4eaf80c95 | -9.11945 | -46.05384 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b117fac5-c9c8-34ad-8a2a-1963a1034680 | -12.87911 | -48.06434 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87cf260d-3db9-3f3e-8b92-2db9bb5118c3 | -7.53189 | -45.35587 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdc69016-3c29-3b97-93d1-dde6bf1379af | -12.86556 | -48.04606 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae5b2fb9-20e1-3790-b979-5d912d5e05bb | -10.39507 | -47.13028 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f823a84-0381-31cc-b21c-5692cdc30b67 | -8.15256 | -42.46901 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68fdc843-1f06-390d-9025-a4600b8e3327 | -7.78563 | -45.44993 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15559fcf-16ec-37d1-9a89-96908dcd8cc8 | -10.04506 | -48.1208 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e639d13-a132-3af2-80c2-7a4c02e8d04a | -13.69854 | -46.88459 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18cbfaa9-b31a-3b16-bddf-7975e0da7b42 | -11.78846 | -46.40536 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6edb144-447b-3326-8f8b-841e0df106ee | -12.57689 | -48.25329 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcf1aa5e-7b9f-3871-8a71-74bf61efdcd0 | -9.48697 | -46.51129 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11a51a07-ecd4-31e2-b1c1-d0b48dc4ab8a | -12.88703 | -48.16965 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b3a2b59-de6b-3908-8ec1-605e6c7b5e24 | -11.09999 | -44.6307 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dc6a1972-f3e1-3d35-b978-64d1b450d304 | -11.65837 | -52.19078 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| dfd41c01-e513-308d-87fb-5697b5ee38e6 | -11.37825 | -43.56935 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b6259ce-1801-34ba-bb5d-7dda5a5276eb | -8.88191 | -45.73863 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb5cef09-e357-3d3f-8506-5d1e84e32385 | -11.96885 | -45.86362 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d659122c-fb34-379d-84d9-15b47db06efe | -7.56968 | -45.22799 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f90a290-3268-3dd9-9f30-7dc7b44a1bac | -14.21516 | -48.05642 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d220362-8fc2-358d-b3b5-dc5bd3be821d | -11.02814 | -46.85247 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77d65409-e9f2-36b0-a484-f28ef9f9aa1b | -13.33366 | -46.84926 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f21b4fae-86da-32f9-a376-0d7061c873d3 | -7.92386 | -46.4451 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cb772a9-fcf9-3f98-aba3-12f85e095583 | -7.55693 | -45.70406 | 2025-09-02 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8f2b20a-fca3-3801-8f50-ac2bfbb770ac | -11.6715 | -52.20881 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| d6832339-466a-3787-86f6-d69eea7c9eb7 | -12.78022 | -48.07928 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3538cbc3-e0f1-3588-87a1-2fe16526f0b8 | -7.4822 | -45.37037 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d090d017-dd3c-38c4-9645-bcc4978fb6fb | -14.59269 | -48.05089 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15ddfbe2-33b2-309b-94b1-94f9dfe6fd85 | -12.61357 | -48.18409 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c988c4eb-55e9-3f72-a18b-3cb668d27146 | -13.49946 | -46.93296 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f8c18cf-4711-38b0-b6ca-ff2e939af1bc | -10.83656 | -45.03747 | 2025-09-02 03:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44cae021-ad6a-3838-ab5e-1736cc51a9a2 | -8.01901 | -44.05043 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f77b3bac-67f0-3b2a-9e29-6131f25d2786 | -11.65272 | -52.18199 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 88fcddae-0d87-302f-bfe3-32d7b5be4fda | -11.48306 | -46.78852 | 2025-09-02 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4000e134-9ecc-3bd8-943f-d13a58f42ae7 | -12.46641 | -43.20583 | 2025-09-02 03:51:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d57e089-eeed-3a74-9854-d330fcc54dce | -10.83225 | -47.45197 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0f97aa42-7349-39cf-9c1b-539a394d83c6 | -13.7241 | -46.93144 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c005507-8443-3526-a230-7e3b6c05b220 | -7.78616 | -45.44694 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd7215bd-f1cc-3c5a-bc78-39c9af3d6d6a | -11.05714 | -46.90089 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8525f89-3183-3b7b-b326-2cc7ec7e406a | -11.82179 | -51.54221 | 2025-09-02 03:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c1ac1f11-c76d-3618-855b-60f2eea5e896 | -11.89291 | -46.67268 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81168982-8fd1-38e5-9fd7-5e4bb619a8db | -13.34082 | -46.94845 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b558615f-fe9d-3ece-a7cb-635c19fe3e8a | -8.71038 | -50.43905 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 170c48f8-d55e-3794-be8b-75575fd8af71 | -12.77888 | -47.65047 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da587b6f-6e1b-31a9-969c-ece93e2a326e | -12.78646 | -48.07677 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00be4583-c569-3127-bf6a-92b3acbc158d | -9.11997 | -46.05093 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18db4d6a-17a1-3bae-9523-12c8e8491bcf | -11.6615 | -52.17589 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| dcc2a087-2163-3de4-9dff-2a0311b02f6d | -11.9595 | -45.79351 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5237bc8d-a9c4-30c3-a3ae-ef608b7de9ec | -9.2872 | -47.09055 | 2025-09-02 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46af6621-aae6-3ffb-aedb-4e8d09ccffad | -10.05947 | -48.13983 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8a7e63d1-5090-3dbd-9af4-aad451ee5a17 | -7.70874 | -45.01939 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5975f21a-6fbd-3ae4-8da5-4861676a2a37 | -8.87537 | -45.77414 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3f8f6d0-16e7-3796-bdae-a9795accf602 | -9.73979 | -48.97582 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69c293ff-0740-31db-9497-910a11583a67 | -10.05662 | -48.09233 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f14927a-6084-3a8e-b891-97aa33075844 | -7.48326 | -45.36439 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e4099dd-7298-3db2-b209-6a74f247545a | -11.0078 | -46.9392 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0978997-d827-3d12-9c18-5af5c4ff815c | -12.13451 | -47.19263 | 2025-09-02 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87ac5bf9-aeb4-3c7e-af12-d7db6ac393f6 | -8.81713 | -47.49014 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 094732ed-75ff-3521-8cc8-a0decee9cc29 | -13.69354 | -46.8834 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90c30227-72e1-3beb-8438-6349165fe92d | -13.53224 | -41.83821 | 2025-09-02 03:51:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec9692a0-10e6-3574-887e-fed447fbf210 | -13.6911 | -46.86897 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26a7c44b-4070-3152-8fdb-14ea5509f778 | -12.93669 | -48.08753 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8be7dbdb-7f63-39f6-b2d0-fe2679531c2c | -11.81591 | -51.5406 | 2025-09-02 03:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d35585-272d-37e9-9448-1f338b12a401 | -13.49712 | -46.931 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6a6e7d6-ba7e-37aa-94af-926ec8361b58 | -7.91846 | -46.44403 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3d6568a-9557-34c0-b3cb-1e95e1ef8625 | -13.72126 | -46.93013 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fe7c63a-9e99-311a-81ea-466022628242 | -10.05873 | -48.14363 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c01099da-48ef-39f3-94c7-8e55f7e82b82 | -10.25939 | -47.52259 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9ced48b-d3da-37a2-b511-4d219a58ccd8 | -11.09579 | -44.65424 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 64b515c0-b8f9-3b1f-acd5-b4d2ed301b67 | -14.58614 | -48.05576 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f4acd3f-7507-3aff-85f0-e0bd787103cf | -9.97405 | -46.4145 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fdab9cbe-23c9-3df3-9adc-72b5e77616d0 | -12.61775 | -48.17842 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 03a4f9d9-db15-3fb2-8496-51773fcd68b2 | -12.76228 | -44.69967 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 009f729b-b363-39e7-b688-65d1f1174342 | -11.48246 | -46.79161 | 2025-09-02 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47fd104f-d2da-38aa-a31a-2d2cdd253bd7 | -11.66556 | -52.1922 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |


[Clique aqui para ver as próximas entradas](README19.md)
