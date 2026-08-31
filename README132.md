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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba6bd8fa-4f8d-3894-84cf-e3dbc011c566 | -7.60864 | -44.84314 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 686eee77-4be0-38b8-80fa-9f76372c3cfe | -6.69215 | -44.85106 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cb498c3b-c6c6-320b-afc8-0c5126927848 | -7.63723 | -46.72744 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5b3bcffb-ac9a-3571-ab25-3e57162af3d0 | -5.45101 | -51.41841 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba836a37-4465-35cf-8517-0c5a9993b1c1 | -7.6391 | -44.83086 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89c60eb9-20c9-3e8b-a37f-3cd5347cceab | -3.68962 | -43.07843 | 2026-08-31 16:33:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3375180-558e-3584-965d-e377a127fea9 | -7.10232 | -42.23468 | 2026-08-31 16:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7037eb6d-0034-3cb1-8970-8deaa3f9181c | -1.35989 | -49.26597 | 2026-08-31 16:33:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5eaf99f6-77ec-3fdd-b1b5-5a1950cd46d8 | -7.52458 | -55.33075 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 81039f1e-76bf-326f-a38a-a791dcaa1042 | -7.63652 | -46.72263 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 723b2f8b-8ff4-3bbb-b6ed-ee69bd9ce41e | -7.99223 | -44.27806 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 4cf7ed5e-b672-30a2-b29d-fdbd19e0f15f | -6.6977 | -44.03349 | 2026-08-31 16:33:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c4b50c5a-9a7e-3085-9f52-b1c6ab046b07 | -2.9679 | -44.28244 | 2026-08-31 16:33:00 | NPP-375 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2c15ad0a-adf2-3097-88b2-6639716c4a5f | -5.73268 | -49.13215 | 2026-08-31 16:33:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 5fcf4cb2-d149-3df0-93b4-93f9cf9fbd8f | -7.63559 | -44.83138 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 040b846b-9932-346e-ac1c-8a063dc1e4e5 | -5.859 | -52.09071 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6a15d2c-a3c3-3e61-9e0a-b8ac5e4ea04f | -5.28234 | -47.88511 | 2026-08-31 16:33:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a4c31e49-7501-3b01-a7ca-8d0641bf0872 | -6.42943 | -41.53919 | 2026-08-31 16:33:00 | NPP-375 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 20defcf6-eb5c-3280-b35c-fcca657b53a1 | -8.82674 | -50.59753 | 2026-08-31 16:33:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32657ac7-d6f5-3232-8e6e-f1e5ae7ed78a | -6.4328 | -41.53867 | 2026-08-31 16:33:00 | NPP-375 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0b0ca08f-1798-3a8f-849a-7356b1e15aa8 | -7.1135 | -42.21871 | 2026-08-31 16:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4462e724-7a42-3f3c-97bc-56f82ecf5ea0 | -7.64783 | -46.74272 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d8fb104-596a-3cdb-8d07-fcec17668c3c | -7.96731 | -44.3239 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 761c546d-d9c1-3d37-a1f4-5aa0a2854b23 | -2.46931 | -49.31972 | 2026-08-31 16:33:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3179befa-dca8-3a1a-9144-552999b912a7 | -6.26495 | -53.6485 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf9a9a9a-d1ae-3008-bf97-1124536f46eb | -5.18575 | -42.89169 | 2026-08-31 16:33:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 326e906b-ba12-3449-8be4-d4c4b6c12adb | -5.80308 | -43.64322 | 2026-08-31 16:33:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f379e1b9-1d83-3349-9c63-baa35e0bd1a3 | -7.98512 | -44.32509 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9ca71418-330a-3f41-a85c-4591520b2d3f | -5.86493 | -52.09361 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e394dd6-4151-3694-a395-cb5f69666190 | -6.20713 | -52.99187 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 62880bfc-999f-35ab-bc62-3ec2d9c49bb5 | -5.38642 | -47.71965 | 2026-08-31 16:33:00 | NPP-375 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8e548ba6-2ddb-39ca-b487-56e591edfb1d | -3.42355 | -41.71362 | 2026-08-31 16:33:00 | NPP-375 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dbf77cc5-72ae-3743-871c-d00933994c77 | -7.79204 | -44.0799 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| bb636b4d-6e3c-37da-9f7e-c1b790336414 | -6.99647 | -43.67505 | 2026-08-31 16:33:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93eb07f4-caae-3401-b7c3-c8debc50e875 | -7.61379 | -44.87829 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 60cb9cf7-bd1c-3b15-b662-50847f8bee13 | -7.99193 | -44.34719 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0ca136bf-221d-3979-b4e5-5ff6634ca1e3 | -6.81833 | -43.53959 | 2026-08-31 16:33:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d191ac04-a1d7-33a5-9ab8-be0d92e71719 | -5.58946 | -42.33299 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| abf4616d-f082-309c-9fa1-5e18b8c25156 | -7.49582 | -44.44857 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 949bc4a6-efce-3f4f-8537-f65d2f3c32d7 | -7.68738 | -55.34541 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3b4039b3-8741-3f0a-9355-2b88e763acfa | -7.09499 | -45.78234 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 49040135-889d-3efb-a343-1977b3163059 | -6.84194 | -41.72739 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| e28f993d-f619-3470-8df1-0bc80234d0fe | -3.59469 | -43.7174 | 2026-08-31 16:33:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7952fdc5-c59a-3451-9faa-eea37ab64931 | -3.47861 | -50.59155 | 2026-08-31 16:33:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4754e0e-7710-38a4-a698-4d20102f3de0 | -4.09748 | -50.42681 | 2026-08-31 16:33:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d95ebd62-9cfc-3f6a-ac5e-7e838e840c8b | -5.68859 | -42.73412 | 2026-08-31 16:33:00 | NPP-375 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 09ca852e-f1df-32d3-818f-9d565991e4c0 | -7.10471 | -42.75806 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 572e9119-6471-3696-a17e-7791d3d43125 | -7.10804 | -42.75755 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 32468b22-7938-3d31-8bc8-ca707779d88f | -3.22831 | -52.25912 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f4e3caaf-661f-36fa-b7d7-e1febbf3ade0 | -5.25818 | -55.88889 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2291a792-6226-3876-b734-27458502a1a4 | -6.77356 | -41.17507 | 2026-08-31 16:33:00 | NPP-375 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 755455fa-6ce3-3e23-b082-250dedd1068a | -0.86612 | -47.17373 | 2026-08-31 16:33:00 | NPP-375 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e20adba3-f607-3fcc-97b6-c89879935eac | -7.92307 | -44.23878 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4dce9bf2-37f3-310d-8d7d-55f80d13d6ee | -3.83506 | -55.56983 | 2026-08-31 16:33:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| ad80e919-baa2-3822-b8b4-3a7e635ff235 | -7.0956 | -45.78654 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 83999735-6fdc-3731-a924-2f8f5a741511 | -7.78862 | -44.08041 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 5ffcd9f7-3136-33c2-8757-a84177c0aac5 | -7.7915 | -44.0762 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f47453ee-8600-30d0-a741-c9283a234f23 | -8.82713 | -50.60053 | 2026-08-31 16:33:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0330316f-61f5-3338-8742-c23a9cce4c37 | -6.85277 | -41.6643 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5fc8fc9f-c328-37c6-a628-2ebefe015670 | -5.84822 | -45.22295 | 2026-08-31 16:33:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18a837bd-ce5f-3f24-b5e0-e30bd7572ce3 | -6.94224 | -55.64643 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b2cf2413-d228-364e-bd52-1b175b964fef | -6.21343 | -53.58741 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 658d52b7-ea6a-3e20-aaea-581d34f57bbf | -8.42019 | -47.7233 | 2026-08-31 16:33:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a03b807-7dcc-3611-bc96-d53373f583cb | -2.55958 | -49.11606 | 2026-08-31 16:33:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ba7705a-9e23-3dd7-b952-2356ea1c8af3 | -7.98878 | -44.27858 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| b36f0530-6109-3df7-8812-cb3bd5331c49 | -6.93289 | -55.63253 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0faa6468-62da-38ab-b979-9bb313878bf8 | -7.63969 | -46.71727 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c1fd91f-2e44-3f81-8a3b-1b7b33b605fb | -4.96441 | -55.85287 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 355a3c32-6ef0-3d0a-a0b1-523fa1d32834 | -7.79041 | -44.0688 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09a55e38-a8c8-3d2d-b2b1-fd77dabc1386 | -5.59065 | -42.31854 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 89e543ed-be21-3f96-8fdc-37f84ef4a9c6 | -7.56641 | -44.34175 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b2211df6-9f77-3455-91a6-48517bdb0638 | -7.74391 | -44.73578 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5e1cdcd4-3b59-3206-8d91-deb1aff345fd | -7.10291 | -45.78553 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9546f643-c92b-367e-8a2b-a82abf711e67 | -3.81036 | -38.61481 | 2026-08-31 16:33:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 91553eb3-5621-3e26-b0bd-6c2c29d07f8d | -6.62617 | -53.17366 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d390fef9-40b0-3edc-9082-96c21be93ff0 | -1.60112 | -49.94617 | 2026-08-31 16:33:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 1decc789-e986-38f2-95d3-80978d87e134 | -7.91352 | -44.23666 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 028588fd-c362-3f88-925f-971f56d58900 | -5.58559 | -42.33002 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 72e43b4c-8a9b-3269-a19f-74514d3242a0 | -8.13219 | -45.58067 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e1d67a3b-5ed8-3aa2-bcd3-9d606999f4bd | -6.43842 | -41.53051 | 2026-08-31 16:33:00 | NPP-375 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9c332c8e-1a0a-3035-8be8-19acca801aaf | -5.90404 | -46.12747 | 2026-08-31 16:33:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73314fc3-0834-3eee-9e67-19747fd93279 | -6.06058 | -53.83609 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 10a0d6f0-ba12-3b9c-ad4b-24d59f4205b5 | -2.79607 | -49.58253 | 2026-08-31 16:33:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 61bddea6-3e2f-3c02-88d3-e0ee9afd0ebd | -7.02504 | -55.64071 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 78e8281f-a9b1-3235-b8fb-ad6e7134d9ac | -6.26137 | -44.83647 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1528e9a9-7d0b-3297-ae06-1aadc2295c00 | -3.04338 | -57.41389 | 2026-08-31 16:33:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4115ef11-f770-3331-a099-a5b4248d46e2 | -6.85471 | -43.82551 | 2026-08-31 16:33:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d634bf4-9b3b-3c8e-a338-8d7acbb11143 | -7.11243 | -42.21174 | 2026-08-31 16:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 34b91b4b-4e5a-3b7b-9991-10b65f3f87ab | -7.05398 | -52.71645 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6088468a-d733-33e7-89cd-5f520f91bdba | -7.43818 | -44.95559 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 64401c1b-6961-3b1d-b453-1f46abe952f8 | -8.38985 | -46.46868 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2a466140-7854-38ba-9d6d-bed6d833d564 | -6.97753 | -44.83297 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0773436-dd49-3a13-9a5a-f2555faa2fe8 | -1.72008 | -48.022 | 2026-08-31 16:33:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 4d209067-e0af-31b5-b183-7c8838d852e8 | -4.42218 | -55.43407 | 2026-08-31 16:33:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 64cdf98d-1579-32af-85b2-2c0d7b6814b3 | -1.54541 | -48.26646 | 2026-08-31 16:33:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dc18ed9-a337-323c-8cda-9feffce32f3a | -7.2987 | -46.1805 | 2026-08-31 16:33:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e87431b1-ea7f-3658-bf3b-7b483269c526 | -6.25088 | -53.6753 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b4ac1722-f5f5-38c5-b3e4-a242d7411024 | -6.39147 | -44.9376 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01d1ec25-dab8-3b49-8e25-145b4a22f371 | -3.42048 | -43.37277 | 2026-08-31 16:33:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| bf2a7c4c-8856-32b7-904b-20e1c2c2d72f | -6.53045 | -51.43268 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README133.md)
