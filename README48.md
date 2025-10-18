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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61936540-0c1d-3743-856a-eecd22c2fae3 | -11.84171 | -38.20081 | 2025-10-18 04:29:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4fcd7a7-8c68-3a39-b295-a224aaded497 | -7.47084 | -47.07298 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 217673e2-01f3-33e4-8556-a8d5e1301464 | -9.26114 | -43.74513 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ca4ea9a-94bb-33d4-851a-16b6f4ee5df4 | -6.03393 | -43.40651 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 282ede0b-0b44-35ec-8ba2-779b97885e16 | -8.3168 | -43.41682 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| add87918-14ac-32e5-b314-c608d58c1797 | -10.08904 | -47.65227 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e801db5-d749-39f7-bd2f-91066e7f7800 | -6.4828 | -44.56342 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2cea445-540b-3c63-826d-b3d15dbfa703 | -5.53504 | -45.31868 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf5878f1-9cfb-333f-8107-f3695b1496eb | -10.49642 | -43.43463 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2593f2d7-9c0e-336e-a281-06a11a17b22f | -7.71668 | -47.85561 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84e15e4e-700b-32ff-b605-6fbb042b9e35 | -5.29767 | -45.47513 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a4bde83-2ffb-3a34-a7bc-34ba6f11dc0a | -7.36473 | -44.22318 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0352829a-aec1-3adc-b492-d66383d47690 | -6.30575 | -44.71298 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e6c42af-4dcd-35b2-9beb-a5847f37f14f | -8.09005 | -45.44841 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40076ccf-b9b2-3f87-9e2b-38af843b70b6 | -6.69031 | -46.70586 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e764648-2d48-3c76-adba-f6d24c576a8f | -10.9828 | -44.32774 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a416bdd-5939-3dcc-9bad-ec6e03a6b593 | -6.89111 | -45.45385 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c87c7e26-d472-39d7-9c7c-319b0f6c818b | -6.23126 | -44.13982 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8bbf697-cec1-3663-a668-90bef7ebdd8e | -5.152 | -46.26951 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5670a3e-2f62-35b7-afe7-0e34ae0d7f88 | -6.69497 | -47.45454 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a00ae6a1-7e20-3600-ab54-b45b52efbedc | -10.50663 | -45.03739 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19f47d67-9b24-3106-bf4a-e3e645c982ff | -10.24423 | -44.0618 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94f7011d-4910-3472-82c3-e22de99e19e6 | -5.923 | -45.44063 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4efdc6a-1225-3b9f-9661-069a933303e4 | -10.3657 | -48.05975 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea3a0a1-ada6-35d7-989e-1bf430e2768a | -6.90444 | -47.99361 | 2025-10-18 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a70761d2-8988-3f45-8743-da863fa45b1f | -6.02239 | -43.72171 | 2025-10-18 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 563275b9-663f-3be3-bde4-b5d011979cee | -6.74278 | -47.37128 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0744986f-7648-3cd5-8978-245da58f538c | -10.70975 | -44.55123 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df07965d-eccb-3b45-91d9-f119323b34ee | -8.2038 | -43.30688 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 06d74acc-375c-353a-919d-c0584dc1a85e | -9.11927 | -46.6172 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dfa71f2-648c-3a6d-abc6-62efe3846194 | -9.27396 | -43.73404 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2112f0a-1cb8-35a6-98c8-f95f51e38be4 | -6.23294 | -44.15181 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67159451-4449-3edc-9c13-b4a30d70103b | -4.73029 | -46.16045 | 2025-10-18 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99f31845-44e7-327a-b410-5e84ba5b24d8 | -4.94207 | -49.76516 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e91be32f-89a8-3610-808f-454c82e80dba | -6.14113 | -44.28794 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 127a8a50-a0de-3a03-b781-06f089c3108f | -5.92523 | -45.44818 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3679d65-9d2f-39bc-a222-860abb3e593d | -8.81469 | -49.68093 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2992ad8a-1910-3c8b-8e6e-c2a25d9a4e5c | -6.43009 | -47.29617 | 2025-10-18 04:29:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb346995-577c-320a-b0b5-0d3680d9165e | -5.21681 | -45.51976 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaf535e0-b9c9-3b5d-846a-d8647688f352 | -5.3562 | -45.03436 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33fbc8f5-1ad6-374e-b490-051a9d50ffad | -4.96811 | -44.60956 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 510ce0a0-9a96-365e-bf4f-2d71f4f77895 | -6.44434 | -43.81165 | 2025-10-18 04:29:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a298dade-6c99-39b9-9ad1-ad830812f82e | -3.81861 | -51.70089 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff0512d3-11a1-3073-a122-3b7d50f62e1a | -10.64205 | -45.31192 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b0729ac-fc5d-39e4-8f2b-12128e7b78ee | -5.01461 | -46.02807 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1ddbe5ec-0309-3705-bbe5-51fae88296a8 | -5.60152 | -47.49765 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 966a8ab4-51f9-3ee7-bd87-eec6f4f93146 | -6.99392 | -45.20321 | 2025-10-18 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ca5d61-bb00-3904-b29a-2092cb30d1c2 | -9.28487 | -43.73574 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 762413de-aa69-3a78-a932-dced5b714fe0 | -8.86185 | -46.02148 | 2025-10-18 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caa3d653-6cee-3edc-94c7-32a9721b47ee | -6.04908 | -46.65358 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 051de60b-a279-315d-a9e4-9c2b436d45de | -5.20782 | -46.19672 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e827d9-fc9d-3ee5-a991-c0f6e2b8bdad | -8.36064 | -46.23869 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c9e6667-cc1e-32e8-b60b-4d972422861f | -8.09522 | -44.10508 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15f6fb24-de93-3c4d-854d-b9ef20ecd5d9 | -5.55863 | -46.37678 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c5910ee-c695-3941-b58d-a47b28c5d820 | -8.8265 | -49.69015 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e023f417-b0a3-3640-9a19-1779a9dfdf98 | -8.10849 | -55.08652 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39be1569-47dd-340f-9515-e136e846975c | -7.48749 | -47.03265 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d18e8df2-deed-3ef4-a90f-86a0447130bc | -7.43574 | -43.75729 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4f21bad4-2cae-34e4-9e14-aa14c0a6ac17 | -10.49886 | -43.44423 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae6f107b-2709-309f-b119-e5553465fc57 | -8.07198 | -43.90554 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 56669d06-53f3-3442-9dc7-9172d3722970 | -8.10434 | -55.08939 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ac41f3-4560-3ab7-b796-39fd6e6b0129 | -7.99165 | -45.15588 | 2025-10-18 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b380fee3-430b-3d8d-980b-e11686b0b2c2 | -5.01625 | -46.01768 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 44b92809-63dd-3d0b-8a61-563cca1729ab | -6.59204 | -44.16539 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 335debaf-d894-3562-be0c-b1b58b03c24f | -6.62249 | -46.19296 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 443fd1f9-7214-3f08-8b15-8aac2e8bf267 | -6.31999 | -44.31092 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d7350b2-5980-39e2-9c6f-863677c7cc5d | -5.15821 | -44.93866 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7efbc44-9dd4-3be3-9af7-a536888c117a | -3.91218 | -52.33827 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a01a4f9-8575-3e2e-82c5-8776eb8a0458 | -5.00796 | -46.02703 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5d46622-a1f3-327f-a6a2-850247bcd902 | -6.85457 | -46.9282 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70d189d9-7052-3287-9ac3-0bcbee44ff43 | -9.19443 | -46.86883 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f7e37bb-67c1-3980-9cf5-47cf6536012c | -6.33886 | -44.0068 | 2025-10-18 04:29:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cc823f5-22d2-38c2-b6f7-50fd30697b93 | -10.23343 | -44.0598 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f29c562-b0dc-3e6a-880c-8dda96142544 | -7.29805 | -47.82923 | 2025-10-18 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7de04b9d-1f0c-3713-b61a-03b8e7593029 | -10.51908 | -43.41098 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50323c9b-9817-338c-a2a9-25b7035ac0e6 | -6.13485 | -44.21361 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7028d9f-5300-3185-8943-eb9521c01469 | -6.43804 | -43.56629 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7935a976-2969-310d-b11a-3c62a53c98ec | -6.94076 | -43.6753 | 2025-10-18 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08e69e66-9b43-3c9c-9d08-9fd8321ee929 | -6.58708 | -47.07605 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2d2a422-4528-37b4-af76-827b95459653 | -6.94382 | -47.76944 | 2025-10-18 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 632e21f2-738d-3643-8d8d-9f18229cc5b2 | -9.75769 | -43.95914 | 2025-10-18 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77766a75-2f6f-3939-ac25-206fbd2822f8 | -7.0134 | -41.83518 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 798b6e4f-dc6d-3865-9656-f01c9b0a4c9e | -7.84868 | -44.14272 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b152676-5be9-3eee-8708-9530f3a4dc7b | -10.41652 | -47.74157 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de340255-2f6b-3951-8d5b-4cde9c2aa655 | -6.74361 | -43.80941 | 2025-10-18 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46c1c64a-00fe-3251-936f-d8b496cf3a87 | -10.49086 | -43.4201 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6af75856-99bf-33eb-9748-8a0ffa69d67a | -3.86158 | -51.90596 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dd95040-11b0-32d1-97b3-84c61053d40d | -7.17122 | -42.36057 | 2025-10-18 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4635633c-d143-3ef8-8ed7-5b57218bba5f | -9.98071 | -48.2424 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 689e232e-a4c8-39c0-9724-233591eacb67 | -9.05202 | -47.02196 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a206d6e0-2f4a-337b-9556-5a513567cda2 | -9.03482 | -47.72058 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25286e6b-2aaa-3b5e-9cc4-9232d1133468 | -4.30548 | -48.06696 | 2025-10-18 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 479cb83a-aec3-3243-aeb7-4b6ae868a2d7 | -7.02372 | -41.81258 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 77789f57-966d-38dd-bfd1-f8a45d17376d | -10.23704 | -44.06039 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64140887-9f6b-3675-af89-e0987aa4a178 | -10.48587 | -43.40149 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b240b2be-bfb8-322b-ad45-3137b6d00c87 | -8.64701 | -47.08234 | 2025-10-18 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89f931fa-e230-38a4-a033-ef263887b32a | -10.07104 | -48.33128 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 242f8f82-87a0-3fd4-87db-d59e1d16c4b9 | -9.50414 | -47.26652 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9ea3cbc1-a2e7-3b7b-b7ef-d96b46f9d602 | -6.10585 | -44.8538 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38c63bcd-4ede-370b-bf08-5e1ab928319e | -7.42861 | -46.89474 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README49.md)
