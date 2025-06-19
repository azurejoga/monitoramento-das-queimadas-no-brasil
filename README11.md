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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd2a5f01-1bc0-3078-8a10-36787eea4823 | -9.89667 | -48.01982 | 2025-06-19 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2d00b36-320c-3eb9-b43a-85abc95fceac | -14.4402 | -48.90444 | 2025-06-19 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b75d4dd-f8c1-3537-8c54-67e0c91b6a7e | -14.21747 | -45.5102 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0aa97ff6-f00f-3ec4-8125-275fc58b5dff | -10.59062 | -49.46527 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3140882-06b9-3569-9e93-83463804df16 | -10.64167 | -49.45421 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9406c260-fd5c-3ab5-93c0-4adbf05ca803 | -9.79228 | -47.18382 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ebf59d4-7aa0-3bc9-9fb0-a3e8c1e6d69e | -9.4337 | -40.38396 | 2025-06-19 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 738325d2-f6e7-35f4-ab15-53106a2480b2 | -8.96186 | -47.97694 | 2025-06-19 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0aabc1e-c3a3-3525-809c-db12119cdc5b | -9.25226 | -50.0351 | 2025-06-19 03:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9920930e-23e7-3d05-8f32-be161626b61e | -13.08249 | -43.50993 | 2025-06-19 03:57:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 701f921d-a8ab-3276-aa2a-4cf257ffe782 | -14.21614 | -45.51759 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9a94ba3-5896-37de-b2a6-686e3518e038 | -14.21955 | -45.52207 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df637ccb-b117-3ba6-9162-105aa56cad61 | -12.76001 | -44.40737 | 2025-06-19 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c2778a2c-0fb3-37e6-bc7f-13324d967172 | -8.72318 | -47.99494 | 2025-06-19 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03e85e84-c1f0-3c0d-b5b2-a9dde70310a9 | -9.20999 | -45.34204 | 2025-06-19 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cae6d5f-593d-3542-89cf-ec9b39fef37d | -11.91261 | -44.18009 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bf5e7d85-a54f-3657-801f-9a53248dd0e9 | -8.13022 | -49.58617 | 2025-06-19 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed529e37-023d-34c1-bcf6-d908517b7a99 | -10.09537 | -52.73706 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66fc7a9f-0ca7-36aa-9c56-4f1e5ad92770 | -10.09404 | -52.74377 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f25c580-53d3-3da8-bd13-4892b1396ee0 | -9.32855 | -47.83238 | 2025-06-19 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e52f9be-79c6-3f34-aa4b-6974892ce229 | -10.64654 | -49.4592 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad588af4-8ddf-32ee-8944-92d268681855 | -11.62876 | -41.83688 | 2025-06-19 03:57:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1c399a97-cb2e-3ecc-92ac-6a9c573d5766 | -14.43517 | -48.90323 | 2025-06-19 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bad3bd8f-036f-3030-b4a3-d5b1fb8b0a1e | -12.23471 | -44.19683 | 2025-06-19 03:57:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8421059-100a-3c85-86c8-3482446af381 | -11.91224 | -44.18296 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a858074d-9873-3d36-ac16-49dc37e1ca5b | -10.64092 | -49.45806 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c88dbdb4-721e-3ce7-93d0-6253d4c8150d | -11.16374 | -50.08702 | 2025-06-19 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04cc1198-0767-383d-8dd0-36f470529106 | -11.2856 | -48.69259 | 2025-06-19 03:57:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b217175-5fe2-379f-8b23-4dcfdcaa4efe | -10.078 | -52.74724 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad7aab1e-f53e-3088-947a-4b806eb01a0b | -12.39679 | -46.36296 | 2025-06-19 03:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57676bf4-bad4-3157-9515-47bf07229c11 | -10.72211 | -49.56548 | 2025-06-19 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55bee5f9-4242-3b08-8344-2d5262f95b56 | -12.79933 | -48.73192 | 2025-06-19 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80cdfb13-53cd-3a23-b5e5-ba26e22b8f49 | -10.72778 | -49.56651 | 2025-06-19 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e637f29b-ed63-36e6-9c8b-b76307b6153e | -15.2923 | -48.6623 | 2025-06-19 03:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47351d42-db89-3e43-9896-ce46b4c988a2 | -10.50426 | -53.58544 | 2025-06-19 03:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 49f34d76-fbab-306f-a222-e7bb3adc374f | -11.56736 | -47.43106 | 2025-06-19 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eec9bde-96b6-33e2-9b4e-38ba5fe34ec2 | -10.50583 | -53.57783 | 2025-06-19 03:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aaa98dcc-35e0-3b7b-940c-61ab21bcfef6 | -10.59135 | -49.46144 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a007ab16-9b98-3cc8-b9a1-499e6edbcf26 | -11.93426 | -48.42707 | 2025-06-19 03:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a738f34-0366-387f-a7ab-a5d331b3c180 | -9.8961 | -48.02295 | 2025-06-19 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66cb50db-a285-3289-9085-f740b1deb19e | -15.47479 | -41.89218 | 2025-06-19 03:57:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f6359f15-1f10-394d-92fc-195bf0135db0 | -12.75912 | -44.41238 | 2025-06-19 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a57e95e9-1eec-3b0c-a72e-cec345063701 | -12.79726 | -48.73715 | 2025-06-19 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3baa14c4-7d8b-37bc-9761-83936a0bf1e1 | -11.41716 | -41.39853 | 2025-06-19 03:57:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eba801f0-2f28-3683-b859-01b0c207a557 | -8.12713 | -49.58773 | 2025-06-19 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a140a3cb-c2d9-381f-87df-8a2b0a87b05c | -14.43902 | -48.91041 | 2025-06-19 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 94532526-8c5f-3c39-b470-b45da5c9f4da | -12.06676 | -48.46756 | 2025-06-19 03:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2581be12-3f93-3be3-9d82-b6e09b320a75 | -10.69678 | -37.05016 | 2025-06-19 03:57:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1ff8039-18c0-3221-8b68-07198157b3ba | -12.23455 | -44.19844 | 2025-06-19 03:57:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0a19a91-1091-342e-b804-8309b890a35d | -14.21274 | -45.5131 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46451185-df8f-371c-b0d1-6fb85d770c01 | -15.29083 | -48.66571 | 2025-06-19 03:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61b9e0e0-1fcf-337b-abf3-5ef396982291 | -11.93486 | -48.42397 | 2025-06-19 03:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb98a0d-8090-34ad-9c33-5e33ce03f4c3 | -11.33287 | -45.21424 | 2025-06-19 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fdd435a-2f88-39a0-8bc7-bb52a2447116 | -11.9518 | -58.7574 | 2025-06-19 04:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 86119c98-8218-30d4-8611-77f3943226c6 | -7.2405 | -43.0899 | 2025-06-19 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| ccecacc0-227e-3d53-8f49-fa1a937f13a2 | -11.9707 | -58.756 | 2025-06-19 04:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 2a9acc8f-6869-3781-a12e-849d810403a2 | -8.0703 | -43.0981 | 2025-06-19 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 30d05d15-2d91-3b91-8aca-34b97083ff0d | -11.952 | -58.7376 | 2025-06-19 04:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 4ca0d30f-79b3-302d-a271-c2c0b4a70105 | -8.07 | -43.1216 | 2025-06-19 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| bc2ddc61-cd7b-313d-9dd0-627e6c2ec100 | -16.305 | -58.2474 | 2025-06-19 04:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 866cd188-f95c-3389-ab94-18d51c34851c | -11.9709 | -58.7362 | 2025-06-19 04:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 4619ba05-328d-30a4-b864-726b55a1d768 | -21.43197 | -45.08144 | 2025-06-19 04:00:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13f456c0-1422-30c5-b9bd-c2b422e7afd0 | -20.943 | -47.42667 | 2025-06-19 04:00:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec09d263-f53d-388c-b3eb-9307f276f513 | -18.65256 | -55.75327 | 2025-06-19 04:00:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cbb8eab6-56f3-3b1b-ac4c-ea45a4b0e47a | -18.99484 | -52.08263 | 2025-06-19 04:00:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5911d455-2d7b-3408-a076-a52148348fbe | -22.55275 | -42.2037 | 2025-06-19 04:00:00 | NPP-375D | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 10882289-ef58-3ae7-b9c3-b0bd2d933b40 | -19.96966 | -44.21815 | 2025-06-19 04:00:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7c0da87-5f8e-30bc-8336-1356ff583406 | -17.70335 | -46.30049 | 2025-06-19 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aae13968-4f9a-32f4-a8f3-716023f177c5 | -19.12844 | -52.70208 | 2025-06-19 04:00:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2107de3-a304-3995-9544-c7e6c2303c32 | -19.12362 | -52.69614 | 2025-06-19 04:00:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59edf30b-7387-3340-8f28-afc034e3e3dd | -19.84946 | -43.84346 | 2025-06-19 04:00:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7ea37517-10a1-3a71-8dbe-0b5d8d0d0fab | -22.71066 | -43.74457 | 2025-06-19 04:00:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f65c9705-d48b-3ad9-bede-15a51236b89b | -19.98518 | -47.18361 | 2025-06-19 04:00:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b6492a8-c74d-3dee-ada0-35475a54891c | -16.63786 | -48.49298 | 2025-06-19 04:00:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b26374-636e-34b0-9834-be3233a05880 | -18.99391 | -52.08692 | 2025-06-19 04:00:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5da5bffe-912d-3114-9212-4501dfa4b77b | -17.75555 | -52.43074 | 2025-06-19 04:00:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3078433-d5f5-3e24-b46d-5c375147cbdd | -16.31853 | -53.80291 | 2025-06-19 04:00:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c773a91d-1c0e-3d80-9eb1-f1d690567772 | -21.01361 | -44.20939 | 2025-06-19 04:00:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 27d9f947-2c35-3f7e-a522-eed956f965e9 | -20.31246 | -45.58511 | 2025-06-19 04:00:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87a0ce4d-929b-3f34-b01f-3c63be90fee6 | -21.4312 | -45.0858 | 2025-06-19 04:00:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f3d83cfb-0b09-321d-a0d8-3ae92af83a6f | -21.66721 | -41.94807 | 2025-06-19 04:00:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ffae586a-96c7-3824-9b7c-75cfada2fdb4 | -21.08898 | -48.68071 | 2025-06-19 04:00:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c03d4239-c10c-37fd-8145-c8cc0258b5fa | -19.12259 | -52.70068 | 2025-06-19 04:00:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a90773b2-9d3b-33ee-82c0-03d488f96bc0 | -19.98591 | -47.17975 | 2025-06-19 04:00:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a21d676-9f4e-39aa-9157-9927281b0772 | -20.99439 | -51.79342 | 2025-06-19 04:00:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a74edcd6-d707-36b1-8664-8d8c5823d872 | -20.01939 | -44.59633 | 2025-06-19 04:00:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f907dea0-0ed6-30c6-83a4-51c7a9252234 | -16.64255 | -48.49418 | 2025-06-19 04:00:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73949735-7f13-3aac-84ce-10fb9f854dd4 | -19.12434 | -52.70337 | 2025-06-19 04:00:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ed57335-9b4e-3ee1-9e34-d5a124dee779 | -17.75385 | -52.42826 | 2025-06-19 04:00:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c2e6e0d-a0c2-36a3-a628-67a94e62e3c9 | -22.90182 | -43.75191 | 2025-06-19 04:00:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1c56c6e6-521f-3289-9d0c-51a8b8421308 | -18.72647 | -46.87744 | 2025-06-19 04:00:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5f9b8e2-ef36-3979-ab43-f9f69b66f8d8 | -19.71629 | -40.35279 | 2025-06-19 04:00:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1da06e06-f795-3184-92a6-6aeb09961c6b | -20.76458 | -46.77082 | 2025-06-19 04:00:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e0e5722c-0e83-3de1-93bb-84bfaea8baba | -17.75455 | -52.43524 | 2025-06-19 04:00:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0623498-d439-3adc-a410-9eca2a4a9798 | -19.12533 | -52.69881 | 2025-06-19 04:00:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b3f1970-2111-3f31-ae17-36d98b787418 | -21.13197 | -47.80222 | 2025-06-19 04:00:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a12ed5d-9327-3812-b6d1-78c0d4ba935b | -18.65572 | -55.7575 | 2025-06-19 04:00:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a98cc300-6a56-33f6-9105-7422d6b64030 | -20.94226 | -47.43052 | 2025-06-19 04:00:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c63852f6-3eca-396b-a35f-b43a8fc6e6a0 | -19.0005 | -52.08398 | 2025-06-19 04:00:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87c690ed-80cf-37c3-bc74-5c1d01155a8b | -17.76038 | -52.437 | 2025-06-19 04:00:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
