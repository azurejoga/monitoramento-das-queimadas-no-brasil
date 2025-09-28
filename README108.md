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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2f5382c-9497-3cd1-97a7-3d6742ab302d | -13.6263 | -47.3378 | 2025-09-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 278cadc4-cac5-3199-a82f-b9a6f82f4d87 | -11.3642 | -45.0339 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b574db52-ce41-3b0f-b293-953a35be17da | -5.3057 | -43.1599 | 2025-09-28 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 3404ea63-9f22-309b-9fc9-3059b6eef01b | -5.7585 | -42.8211 | 2025-09-28 14:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 9de91873-4717-3b32-9956-9fdcbd742706 | -7.1571 | -45.5158 | 2025-09-28 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 3ac4dc5d-42fc-3c6a-a4cf-11f17d1ce89a | -11.4409 | -45.0229 | 2025-09-28 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 58db5244-07ab-35a9-84b9-d635b4db5d81 | -10.0065 | -45.3976 | 2025-09-28 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 2c585e26-ae4c-3a3f-b0de-9c1684a0b37b | -8.8759 | -45.0274 | 2025-09-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 06de976a-634b-3da5-8a5c-6c115906f75f | -10.9137 | -45.7375 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| f21c7193-61d8-383e-985e-4ade0cca7cd4 | -5.9076 | -42.9268 | 2025-09-28 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| b07cf04f-6341-32bd-872b-45b42e02e796 | -12.9363 | -45.1184 | 2025-09-28 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| f39490e2-2dd2-393c-a8bd-a61c0a9d051d | -7.1574 | -45.4932 | 2025-09-28 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f5177cc1-2e99-3242-823e-e708e52e88e5 | -11.9824 | -48.0197 | 2025-09-28 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| faff7108-deb6-3cb4-9bb9-4d249a8391f4 | -12.2825 | -44.0804 | 2025-09-28 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 326.6 |
| da6496ef-f806-363a-9513-f3b3d7fe15f2 | -12.4162 | -44.1293 | 2025-09-28 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b88a59d5-7f54-392e-8ac4-54bff118b56c | -6.0403 | -44.7675 | 2025-09-28 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3ef9c2b9-3838-3bfc-bfdb-3ef3f386b17d | -12.9544 | -47.2148 | 2025-09-28 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9e4a45c9-7601-3a4d-9c93-73e40953e00e | -8.1614 | -46.3899 | 2025-09-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| a1a66587-44c0-3b4e-9356-52f6837c05d4 | -5.6461 | -44.933 | 2025-09-28 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f79609c5-611a-38ec-b9f7-4fc826f21b3a | -14.885 | -45.5708 | 2025-09-28 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 13ee1481-1bce-3e5d-bc64-b62dcb6868c9 | -6.3105 | -45.8999 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 29cf81c7-7f25-3141-8de1-92ff129b9224 | -12.9156 | -45.1912 | 2025-09-28 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 250ba757-beac-3bb0-a851-a930713e770e | -5.9194 | -43.6729 | 2025-09-28 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 86845b01-d07e-3282-b055-2fae6d04b1ba | -12.4167 | -44.1057 | 2025-09-28 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 59411e88-2f65-3d6a-a1f0-b673ce0f19c1 | -11.964 | -47.9779 | 2025-09-28 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 944c74a8-e6f2-3f3c-80ce-276e99ec2908 | -11.9044 | -44.7928 | 2025-09-28 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 175.1 |
| a1af7567-755b-32f7-b053-3c63390be7e5 | -6.0813 | -42.4407 | 2025-09-28 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 129.1 |
| b7097045-86ca-385e-bfdc-661bb81d1b0b | -12.791 | -47.7533 | 2025-09-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 3f07679c-3070-35c5-8516-2c6b6c2b66e6 | -11.9637 | -48.0001 | 2025-09-28 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a6e39480-2651-3dca-b8fe-45208fda483f | -9.4009 | -54.6781 | 2025-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 294.2 |
| 3847e3b5-6233-315f-84b9-e5f78192bbbd | -12.9547 | -45.1618 | 2025-09-28 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.8 |
| cf12e3fd-b2df-3d70-bff8-b84556a0bf8a | -14.5951 | -48.261 | 2025-09-28 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 398a1547-70e3-3d31-8187-58b4e0dc6df0 | -9.3016 | -45.6855 | 2025-09-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 9b70c714-c346-3d56-ab84-7a919671e32f | -8.1805 | -46.3657 | 2025-09-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a29714fc-ce1a-3935-809c-ab64f930e005 | -13.6267 | -47.3152 | 2025-09-28 14:40:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 869a8c6c-07a6-34c3-a73e-9a17cead9043 | -10.9923 | -45.5901 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 47a5439e-02f9-36f7-97d2-53e36717e4c6 | -9.3013 | -45.7082 | 2025-09-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3121b0d6-b2ad-34a4-9525-a02fae767180 | -6.6192 | -44.9493 | 2025-09-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 62580d3e-5661-3b1f-8fb7-090ca2192d9c | -6.0593 | -44.7432 | 2025-09-28 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 51ab2ef2-c681-3efd-9b2e-75d0b3c1f360 | -8.2856 | -45.4545 | 2025-09-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 161.7 |
| e9c74fc7-c5cd-35fb-ba4e-7d64178a80e0 | -9.3331 | -47.56 | 2025-09-28 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 621ac231-28c8-30b2-b647-2ca276e398e0 | -4.1761 | -44.2716 | 2025-09-28 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5c596b8e-bf38-3384-bfe7-1f064f41a184 | -13.7889 | -47.9181 | 2025-09-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 8734f424-a97d-30ba-9944-eaae89ca57a2 | -9.106 | -47.6275 | 2025-09-28 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 49c60c12-cee6-33aa-ad61-a3f99027ce9c | -8.6631 | -43.991 | 2025-09-28 14:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d0a84ee0-b78c-3660-a98d-c5f6c7de2cbe | -12.0214 | -47.9703 | 2025-09-28 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| cac6f574-61f8-3036-b404-898bf2ede364 | -7.3849 | -47.0157 | 2025-09-28 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 1518809d-68a6-34d7-b193-d84749715ca5 | -15.2212 | -48.0688 | 2025-09-28 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ada149c7-2351-3342-a6a0-84fe12066a90 | -12.2627 | -44.107 | 2025-09-28 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 01a16598-5695-323b-975a-5489a4785966 | -9.4007 | -54.6984 | 2025-09-28 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 652.1 |
| 292284a0-c761-3fe3-b4bb-bf175556789a | -10.8051 | -45.3866 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 5f87526b-3e00-3a44-b199-fd15653d787f | -12.6725 | -46.8737 | 2025-09-28 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 859a1b46-3673-3870-9cd8-5c686562f7d0 | -14.8845 | -45.5941 | 2025-09-28 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| c74dc77e-d643-3e03-a4b0-9d969e21c45a | -4.1386 | -44.2965 | 2025-09-28 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| fa49d625-926e-318c-a020-9c2be2507dd6 | -8.8417 | -46.187 | 2025-09-28 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 8f25689f-2333-3aa7-8fc7-35cfbf9d4342 | -14.4325 | -44.8839 | 2025-09-28 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 4ffef682-4486-3a7f-acc2-65beff3c30e2 | -10.0184 | -48.5401 | 2025-09-28 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7efd24b7-f847-30a7-ad65-758546d7abfd | -11.9794 | -47.0622 | 2025-09-28 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 95b17b35-f7bd-3ec6-9ef5-3503d9fce7d3 | -6.0591 | -44.7661 | 2025-09-28 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b3ca1cf0-6313-341f-a738-1d631c7ed6bb | -8.1619 | -46.3451 | 2025-09-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2b981f12-6693-3484-811b-6a4564b0dfc2 | -13.7704 | -47.8763 | 2025-09-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 99ffa00a-af8e-3342-aba9-ad8b1a690a9b | -13.2966 | -50.7036 | 2025-09-28 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 1fe43c4f-e282-3411-8b9d-2605cbd3f18c | -10.9927 | -45.5673 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 5fba04e6-ee00-35fc-bd12-fcaa6deaca1d | -6.4598 | -44.0226 | 2025-09-28 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 919ab448-4114-30c4-8bef-d8e2ff76977f | -6.5611 | -45.1359 | 2025-09-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 96be5d10-95fb-3611-995c-0e4ba9c8bf35 | -8.6442 | -43.9931 | 2025-09-28 14:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 955ad979-8e13-3265-80c4-ca6cf4af33b9 | -9.0874 | -47.6074 | 2025-09-28 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cedb3292-364a-31d0-b2f3-44c6d7238b4c | -5.8187 | -44.4413 | 2025-09-28 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a59cc28f-a4da-3681-9ecf-cb77fa49e3b3 | -12.7637 | -50.4921 | 2025-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 53bd7757-a5eb-3773-9b9e-2243b3f1488c | -11.4417 | -44.9767 | 2025-09-28 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4a8c127b-6f39-3101-a489-aecfb291d3da | -12.2121 | -43.7383 | 2025-09-28 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 490b04c0-d20a-3868-828d-61cf8067c5b9 | -12.3018 | -44.0773 | 2025-09-28 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1d204edb-2c83-3fa7-acb1-179a6bade78a | -12.2632 | -44.0834 | 2025-09-28 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e500bb25-f1d1-33b7-ab87-98910580cc70 | -14.5955 | -48.2386 | 2025-09-28 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 9b835d4f-6021-3a1b-8b87-9a0689596c0f | -6.2759 | -43.6442 | 2025-09-28 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8083bf9c-784b-313f-9573-c96ee1fb6c36 | -7.2605 | -42.9939 | 2025-09-28 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 22e0cf9c-5fc6-3bc9-aae2-fa03b4da1c26 | -5.6813 | -43.0619 | 2025-09-28 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| cf26cfd4-e4a7-3923-bff8-d25f15841214 | -9.9581 | -43.5987 | 2025-09-28 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| bbb71ba9-11c3-33e1-82ae-81bc68af7a24 | -6.6002 | -44.9736 | 2025-09-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| e1c142d4-fed5-3b92-ac3b-f1dbcf48a572 | -10.9736 | -45.5698 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| d74555a4-838a-3e90-a689-e686b03e93e8 | -12.9552 | -45.1385 | 2025-09-28 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 044328cf-43eb-39c0-8482-d4a1a8b6793a | -8.0224 | -47.0258 | 2025-09-28 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 94ae52aa-ffa6-33fc-9af3-9b897eb434d6 | -9.1102 | -45.8653 | 2025-09-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| fa18f372-e9fd-3aca-ac10-22c49df08473 | -5.7001 | -43.0604 | 2025-09-28 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 60c3270a-3e4f-38f7-ae0a-4a10c2b0524b | -13.6073 | -47.3183 | 2025-09-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 29cc0484-cf50-3b92-920f-a9bbb8855ed7 | -13.7893 | -47.8957 | 2025-09-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 240.7 |
| d14651aa-bc31-3695-a694-56e6e82f059c | -8.8415 | -46.2095 | 2025-09-28 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c36522b3-0caf-391e-acc8-c6cc824c6656 | -10.8242 | -45.3841 | 2025-09-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 480.4 |
| 8b12f46b-941c-33b8-aaa6-7975b3b026ca | -9.0913 | -45.8673 | 2025-09-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a03eea1a-13d5-3d29-8ccb-fdee2a2ff271 | -9.2824 | -45.7104 | 2025-09-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6f72380f-01af-3e6e-801e-2a490b63493c | -11.4413 | -44.9998 | 2025-09-28 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 4e63614e-ebac-30aa-a5fe-0808ba125322 | -5.1887 | -43.7263 | 2025-09-28 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 04893822-44d4-3be5-a104-b485533d18a2 | -6.078 | -44.7418 | 2025-09-28 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 00ee97a1-26e9-34cf-acb7-1cf9f51dd4ce | -5.17 | -43.7276 | 2025-09-28 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 676199a3-00e3-3f06-9df0-f56995fc29fe | -9.4196 | -54.6767 | 2025-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 435.7 |
| bedbe461-fe68-3e00-90f4-c927f24ea567 | -11.946 | -47.9138 | 2025-09-28 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 00d84874-2982-30e7-93d9-0226d5daecf1 | -4.4013 | -44.0755 | 2025-09-28 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 237.0 |
| e670e7c6-b161-3f36-b6c0-c2806c9c3786 | -7.3661 | -47.0173 | 2025-09-28 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e27fc5a4-2e75-3849-b82a-ca44e2c75fc3 | -8.2668 | -45.4564 | 2025-09-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| afabc3ff-4950-3c33-a4ce-336f2df4bb7b | -6.0625 | -42.4422 | 2025-09-28 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |


[Clique aqui para ver as próximas entradas](README109.md)
