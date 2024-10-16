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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7e09895-c7a3-3d52-99ed-019353dbfe39 | -3.57959 | -50.57811 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c404f361-f9a8-3e9a-96b7-0c263b894d99 | -3.57865 | -50.56594 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dff1e542-52ae-3ac4-9253-03adf27bdd18 | -3.57803 | -50.56965 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 667eaeb6-639c-3a9e-9d64-34f5a556782a | -3.57742 | -50.57333 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 449f8a05-6ba0-3f6e-999b-e0a69d4a8f78 | -3.57681 | -50.577 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d14de1d5-aea0-305b-b54c-fac3da2c4785 | -3.57307 | -50.56488 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 824ea4f2-5bf6-3746-9af8-8509acabc88c | -5.23248 | -50.88051 | 2024-10-16 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ed52252-5994-35d4-b5f0-549da1d1db7a | -5.22693 | -50.87945 | 2024-10-16 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7bf902a-d792-3d67-8b55-96e97c961a01 | -4.9945 | -50.88552 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4761e85e-7155-33ef-9d43-86ea0b7070f3 | -2.15375 | -50.89526 | 2024-10-16 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f437d737-29f7-3c59-bafe-2712b00b676c | -2.15252 | -50.89548 | 2024-10-16 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e5b6327-a39f-33c7-8ad2-178a56ed7b8a | -3.58833 | -51.00549 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4621fe0e-2788-3d79-8b81-e251b915678f | -3.58258 | -51.00446 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c5ed43-7a08-3079-9cab-793c136cda6d | -3.54845 | -51.58361 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbad5ee5-bedc-3647-835c-e7f606affd49 | -3.50631 | -51.31227 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6f7e3e5e-f7ac-3c1b-bfd5-aa6abef21b1f | -3.50578 | -52.16285 | 2024-10-16 04:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c07c938-b04f-318b-af91-1c9bd0ff43f9 | -3.28556 | -50.93649 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 43895406-641f-38f6-bf27-f9f7cca9047c | -3.2849 | -50.94043 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 34c84c5a-b9fe-382f-9ab8-9b6ce36f44fb | -3.28119 | -51.52445 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 996a6132-9255-3c14-92d7-7b5124b5ca30 | -3.2798 | -50.93545 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fa82257f-1508-3d59-af32-5eca313b83f7 | -10.2442 | -47.2824 | 2024-10-16 04:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c82582d6-c2da-39e5-bf83-b4c264faf42e | -10.2445 | -47.2601 | 2024-10-16 04:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 414348b7-87fd-30fd-9719-d0fc4ec03815 | -11.6917 | -65.2243 | 2024-10-16 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 194d2334-62d5-32a4-b553-50d83745cb57 | -11.7103 | -65.2424 | 2024-10-16 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 32c30695-77f2-3404-9856-97093603050f | -11.7104 | -65.2235 | 2024-10-16 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3cf27e38-6fc3-308c-bdbf-778c756b3efb | -11.7292 | -65.2227 | 2024-10-16 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f476c324-abc0-35f8-9d6b-9767367c2f1f | -16.9596 | -57.5245 | 2024-10-16 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| da9b22ec-1f1f-3393-833e-5d5c31a39044 | -17.1664 | -56.8439 | 2024-10-16 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.3 |
| 439cbdd4-384e-3449-8a84-0816ba85d588 | -17.1951 | -57.4972 | 2024-10-16 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.1 |
| 612358a9-2b1d-3369-aa64-4134d19c8c15 | -17.1954 | -57.4767 | 2024-10-16 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| ea12b9ff-0e25-3a6d-829b-b4941e8e76fd | -18.254 | -56.6029 | 2024-10-16 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 5337b0ff-716a-3d27-8a80-b9592cb95732 | -18.2544 | -56.5821 | 2024-10-16 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 76e3b875-5da0-3d81-9f6b-cab983ac9fcb | -18.2739 | -56.6003 | 2024-10-16 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 8a67e64c-69f0-388e-8f64-857e3d765ea5 | -18.2742 | -56.5795 | 2024-10-16 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 8d937264-afc4-3958-93b1-42d326125e98 | -19.5812 | -56.9862 | 2024-10-16 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.1 |
| f2539f65-9320-3f86-aa07-a179d07b06b9 | -19.5816 | -56.9653 | 2024-10-16 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.0 |
| 6d33e4c3-3793-31c3-a379-44d31bd4e0b2 | -19.6013 | -56.9834 | 2024-10-16 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 2a3ed786-b6f6-30c3-9c70-a23338b5d56d | -12.09106 | -42.85437 | 2024-10-16 04:08:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2f600601-ad8e-3807-ad8e-74af2fec61db | -13.54207 | -43.30589 | 2024-10-16 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab010c4b-a944-3d86-970d-8a6b78647980 | -13.2619 | -41.95411 | 2024-10-16 04:08:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e09b7a71-b9ef-3624-be4e-faba3c4286d5 | -12.80862 | -42.50708 | 2024-10-16 04:08:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 81dca5ad-de42-37ac-a002-229b94078ffd | -14.31675 | -43.33075 | 2024-10-16 04:08:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eef73377-baaf-37eb-b70a-d0b7403bc05f | -14.31618 | -43.3343 | 2024-10-16 04:08:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d223ef36-db3d-316b-b1ac-dda7ab289c8c | -13.83013 | -43.15224 | 2024-10-16 04:08:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7aa17314-ee29-3288-bebd-919c82faac34 | -15.58549 | -43.21693 | 2024-10-16 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1ee4e5e-6a85-3c2a-84da-fde71f111256 | -15.56547 | -43.25775 | 2024-10-16 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d65c8287-e27e-3429-8e52-55b2d2013d30 | -15.30035 | -43.19997 | 2024-10-16 04:08:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7e16a0eb-2224-3631-9965-3d9cf18b0db8 | -9.68892 | -42.85307 | 2024-10-16 04:08:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 36125912-7591-3041-8361-8ecdd3fd0c7c | -9.60454 | -42.94068 | 2024-10-16 04:08:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a72b9174-bd3e-3c1f-9d17-190053ed78be | -10.54904 | -43.80584 | 2024-10-16 04:08:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dadb0d2-1868-37cd-b4df-8b11bd36742c | -13.92643 | -45.82531 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edafb334-eb4c-3ab4-b48e-e9c0141a1726 | -13.28786 | -43.4352 | 2024-10-16 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b16ea5c-9531-377c-bc91-2affdb99caba | -13.28453 | -43.43465 | 2024-10-16 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 318934f6-73de-3655-8852-eb04dcace9b7 | -13.52933 | -43.70221 | 2024-10-16 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e62bc58-b3f9-3c51-aed2-fc1697f039e4 | -13.26258 | -43.65802 | 2024-10-16 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82fd9416-9728-3310-8231-084b46cc428f | -13.11588 | -44.07711 | 2024-10-16 04:08:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3749825e-7a83-3777-97f0-4f20d822a590 | -13.11535 | -44.07379 | 2024-10-16 04:08:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fe21185-825a-3356-a746-4f9eb541f1c9 | -13.11477 | -44.07742 | 2024-10-16 04:08:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ff7e988-6e8b-30fc-9e74-c9ed3a87fea5 | -13.92505 | -45.83343 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1440b4e-2413-36b8-a7e5-3d660a80483b | -13.9229 | -45.8247 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b45d714-a19b-3873-95b3-a77178d2e66d | -13.9222 | -45.82875 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3db5f51-50cb-373f-8bd4-e9fd941d9438 | -11.99661 | -43.7814 | 2024-10-16 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fbea29e-1f35-3bbf-af6e-c43f3fe75314 | -11.10448 | -45.90839 | 2024-10-16 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44beb851-9b34-36c9-8eba-c85f7ea36513 | -10.06482 | -36.51836 | 2024-10-16 04:08:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8f3e5fbd-7b65-33b4-8064-eabf42e6cfe1 | -16.53766 | -42.3776 | 2024-10-16 04:08:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b0677e9-284e-3c4c-8b70-b7ae51b50b58 | -16.30475 | -42.04559 | 2024-10-16 04:08:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 477d4ba3-7b6f-3ce1-b0bd-a628ca5d8cde | -16.06177 | -42.2721 | 2024-10-16 04:08:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 414a05dc-cfb5-3845-add7-e2827bc7dec3 | -14.55393 | -43.13274 | 2024-10-16 04:08:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38752d9b-667a-39cd-b770-98014e111037 | -15.71094 | -43.64531 | 2024-10-16 04:08:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de9ad0e7-76af-3252-adfb-2cb32ce25996 | -15.5885 | -42.84492 | 2024-10-16 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81d212fe-2e07-3143-8d19-f7805c505d34 | -9.3383 | -43.20853 | 2024-10-16 04:08:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d82f8850-cae7-32fd-8791-ce1dd9db2c32 | -9.33773 | -43.2121 | 2024-10-16 04:08:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 043f99f6-c0e7-3891-a8cb-63ef8d214d52 | -9.11902 | -43.09572 | 2024-10-16 04:08:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7f82827-9ae2-3268-bea8-aff5b7838200 | -9.58795 | -43.50438 | 2024-10-16 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d106615-b561-3b0c-a101-757f7bcdef06 | -9.58515 | -43.50021 | 2024-10-16 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd5eef5d-aa98-30d8-846f-00961f023106 | -13.94124 | -45.82377 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 176e4b0c-f211-3d71-b1f0-351487d09e80 | -13.93771 | -45.82315 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0304de80-78f3-3b9c-8dfa-e62f50498cf4 | -13.93702 | -45.82719 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 667e7b4e-28c5-3c94-af29-44017d2498f9 | -13.93418 | -45.82252 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef2e831a-9e51-309a-92b0-5e26674c563e | -13.93349 | -45.82656 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5e526a6-c1b9-3ec7-bf68-db1ec01cc232 | -13.9328 | -45.83061 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afab575f-c310-3fbe-8ecb-9c12b8a45def | -13.93065 | -45.82189 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| badd2813-5b89-333d-a05b-ea9f40d3d0fb | -13.92996 | -45.82594 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9c01833-9013-3195-9479-4e515958769f | -13.92858 | -45.83405 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f3185c4-c6f5-352b-9e52-31a5679483f4 | -13.92712 | -45.82126 | 2024-10-16 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f24c693e-ca56-3e4a-9765-ac39c3808c47 | -9.17924 | -47.00027 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a1daba7-c042-3907-8231-617f12b3c0a1 | -9.17772 | -47.03289 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93fd8274-4ecb-3c21-b058-da4f97d6ce52 | -9.17371 | -47.03217 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 028643c1-5b6c-31c9-80cc-74ec27269253 | -9.17247 | -47.03929 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b8217b01-0cb0-3777-8e18-b85464edad16 | -9.17185 | -47.04286 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3818f416-3741-3f99-9e9c-be8da11cbbf5 | -9.17061 | -47.05 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 328c678d-147b-305f-88f6-242e55c068bc | -9.15285 | -47.00726 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d22f24c0-26c3-37b7-838a-30b3c5ed1206 | -9.13752 | -47.07376 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8fb4544-4a16-3b8e-8a96-6cb0e7e40e11 | -9.13692 | -47.07736 | 2024-10-16 04:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b84e10b-bf1b-3cd3-a8b3-d850f8b05595 | -8.84646 | -46.92325 | 2024-10-16 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19741910-bb2a-3b03-924c-04e3324a419d | -8.84243 | -46.92262 | 2024-10-16 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed1ef3d3-c85c-3368-a4ca-730e19ad6bdb | -9.96188 | -47.38855 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 974d6732-c614-37fa-ad0d-082fde10d044 | -9.96126 | -47.39222 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e653dba6-aabd-3414-8d10-3f651d7e4dd2 | -9.96106 | -47.38777 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98c5bc0d-3b4d-3a68-945a-5f86ec4e1075 | -9.96042 | -47.39143 | 2024-10-16 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README36.md)
