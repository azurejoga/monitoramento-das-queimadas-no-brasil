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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31718493-1fc4-3386-bf04-fb40e3db3185 | -6.1109 | -57.684 | 2026-08-31 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c53c18d7-d08d-3451-ae7f-3fcf5b65c753 | -6.6036 | -58.5972 | 2026-08-31 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 315.2 |
| 9ffaa6ba-fa2b-3e23-b8c3-ff772f86cca1 | -7.9239 | -44.2327 | 2026-08-31 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 11ae7b3b-d853-37de-8dc8-0515271d7210 | -10.1531 | -45.7438 | 2026-08-31 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 710782a7-ed48-3a7a-a699-63c272b13513 | -14.4394 | -52.5176 | 2026-08-31 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 9b79f15a-cd6d-34ef-a26e-2702ce5d06b1 | -14.2792 | -52.8758 | 2026-08-31 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| cf218254-4171-3199-aebe-8e479149c691 | -11.2482 | -45.1194 | 2026-08-31 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3d2e4fc7-a3bf-3a3b-8a65-46e3f705f26e | -18.27 | -52.7068 | 2026-08-31 12:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 6a89889c-c58e-37c0-8489-87125e358d7b | -7.9236 | -44.2558 | 2026-08-31 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 0a87d7be-b0f3-32e3-9809-c27a5a73b356 | -7.9605 | -44.3212 | 2026-08-31 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 262.9 |
| e852c807-1ed8-33e6-9fbb-7c7124ea7145 | -5.5831 | -60.2307 | 2026-08-31 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 6a9cb220-bd3b-3b6f-9455-1d538305afad | -14.4007 | -52.5226 | 2026-08-31 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1709c05d-db30-31c1-8205-72ba0ea80cbd | -7.9797 | -44.2962 | 2026-08-31 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| bb757bad-1883-3d58-b464-27a4bb0bc288 | -7.3119 | -60.5706 | 2026-08-31 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d7b57447-0d78-3121-911b-ba1444cc2bae | -11.3423 | -45.1982 | 2026-08-31 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| c13b77fa-dba0-389d-a255-bdc7d39371bd | -11.3767 | -45.423 | 2026-08-31 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 9f50d64c-de09-3d60-a398-654a2f5fc011 | -6.6035 | -58.6166 | 2026-08-31 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 7fee09ba-6db3-3d7e-8070-197fab2568bf | -11.5283 | -45.4933 | 2026-08-31 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| eb0ec01b-cec0-36ce-a3ad-a22c6a62c5a1 | -11.1824 | -50.5706 | 2026-08-31 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 0b2b9756-a80a-3c11-85fd-ce6b0e469736 | -19.154 | -57.3978 | 2026-08-31 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.0 |
| 26242dad-34ca-3d33-beff-2865a45d3e8b | -11.5279 | -45.5162 | 2026-08-31 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 680fab42-2fe3-35bc-8304-655fea3445bc | -18.2695 | -52.7284 | 2026-08-31 12:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| b6316605-c2d6-3178-8ee0-437368c54cbc | -3.5345 | -49.4733 | 2026-08-31 12:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d87df7df-4018-3e33-a7c8-da581d70b5ea | -8.7439 | -46.4661 | 2026-08-31 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| a7802ea9-f88c-3893-a99e-459cd24b0b1c | -11.3236 | -45.1778 | 2026-08-31 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b9db36be-9f13-3d05-b7ba-4b63cbb743a1 | -5.2547 | -55.9105 | 2026-08-31 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| c788cca0-7335-319f-801e-30f5a4760146 | -15.6786 | -45.9332 | 2026-08-31 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 96e12e03-e950-3b09-aad2-23f88d6de611 | -10.7407 | -54.0401 | 2026-08-31 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| eb360e17-c7ed-3eaf-81a1-c24c17197f18 | -10.7407 | -54.0401 | 2026-08-31 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 84ea10df-d924-3562-a05c-3e16d2010571 | -8.7439 | -46.4661 | 2026-08-31 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 217.6 |
| 7e2f34e9-dbc5-37dc-9fbb-4fe015d3071b | -14.4007 | -52.5226 | 2026-08-31 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 347e91be-500b-32d2-b71c-06c82cd9865c | -19.134 | -57.4005 | 2026-08-31 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.0 |
| f16ceda3-1253-38bc-b712-847fce764221 | -18.27 | -52.7068 | 2026-08-31 13:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 5a05bd58-d03d-33a9-869c-198887d3a888 | -11.9378 | -45.0656 | 2026-08-31 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0a69ae47-f8bd-3e5f-ab95-602224db278c | -11.5475 | -45.4906 | 2026-08-31 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 65065238-4a4a-39f6-978d-6833335b0032 | -14.4394 | -52.5176 | 2026-08-31 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| e16e7fcd-8710-376a-866d-49ef83b32a28 | -19.154 | -57.3978 | 2026-08-31 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.9 |
| 5d00bfbd-007f-3137-b568-9353aa6d12fe | -7.3119 | -60.5706 | 2026-08-31 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 4cfddf72-eef3-3173-ae12-27a6fb347c89 | -11.2294 | -45.099 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2cca7489-f4b7-359a-bd2d-29675950d16f | -11.5275 | -45.5392 | 2026-08-31 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| d9b5f951-f6b2-380b-93d7-8b2310dd257f | -6.6036 | -58.5972 | 2026-08-31 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 412.6 |
| cd72fe31-ff9b-3a75-a11d-c99963f77642 | -11.3419 | -45.2212 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| f9235f2d-c632-33f4-ba83-3eee8818ce4a | -11.1824 | -50.5706 | 2026-08-31 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 91d7e9aa-fe18-3173-981b-3c6e540655e2 | -6.9177 | -55.6967 | 2026-08-31 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8275e83a-70be-344d-846f-23cc1e5f3005 | -18.2695 | -52.7284 | 2026-08-31 13:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 551366ed-c3ff-39a0-92e8-77443bb44abc | -11.3232 | -45.2009 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| e7051007-529c-3d00-9f30-e3f89f05df3b | -8.1534 | -45.4904 | 2026-08-31 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9dae6345-4702-38c0-a867-0120fad7f870 | -14.4201 | -52.5201 | 2026-08-31 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| e15fba8e-02d2-3df5-9c81-18a5a849729b | -18.2704 | -52.6851 | 2026-08-31 13:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 41e5d20a-9d92-3730-9d8b-7f49f381ba4a | -8.7442 | -46.4437 | 2026-08-31 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 190.2 |
| a4fc0e33-3539-3928-b8be-8a4e2a24edac | -14.2796 | -52.8547 | 2026-08-31 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| cfb42ff5-718f-312d-aa3a-583c5c312bce | -5.5647 | -60.2312 | 2026-08-31 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 03588448-92a0-352a-ad81-73176c7c9a0f | -14.2792 | -52.8758 | 2026-08-31 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 984b5e2b-d4a7-3728-942c-c343a5ec0b82 | -10.7459 | -47.9757 | 2026-08-31 13:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 376bc2a2-bde8-3b66-9ba2-41bf25219c68 | -11.3767 | -45.423 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 254.1 |
| d929693a-f3c1-3b61-83b1-374c42b8577f | -10.1538 | -45.6982 | 2026-08-31 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 841ddef0-fcf2-335d-87aa-a4da1c1a95f4 | -7.9239 | -44.2327 | 2026-08-31 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| e8949681-8885-3d50-bb05-5c798f9b2a85 | -9.4345 | -45.6477 | 2026-08-31 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7f234d97-4d47-3673-8b56-19dc1b416b10 | -18.2899 | -52.7035 | 2026-08-31 13:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9c8a3bc1-345d-37a9-b632-e8f1ae8fa45c | -5.2547 | -55.9105 | 2026-08-31 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 69410421-85a1-344d-ac70-3d58dff1d807 | -11.3236 | -45.1778 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 05263175-fd9a-30ec-b00a-72ce0faef61c | -7.9236 | -44.2558 | 2026-08-31 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f3f5bc32-710a-3a40-8488-2b17f52f9f5b | -11.3423 | -45.1982 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 260.0 |
| 02b3f297-968c-3b91-8aac-c16244f9923b | -10.1535 | -45.721 | 2026-08-31 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 222d61d1-df06-38a1-ab82-5c010c7edb04 | -19.1344 | -57.3797 | 2026-08-31 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 74798419-8ec8-3639-a5df-91c539a89339 | -8.1537 | -45.4677 | 2026-08-31 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| e27794ad-d4fb-3a2a-9729-03957a7f197d | -5.5831 | -60.2307 | 2026-08-31 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 250.5 |
| e85b22f6-d366-3996-a440-c367d65c00cb | -6.6035 | -58.6166 | 2026-08-31 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c5cd1062-d226-3d5c-b33f-4acc7e55c5b7 | -11.4828 | -58.5159 | 2026-08-31 13:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 44237532-28a5-3d0f-ae7d-48b90b6f528f | -7.3118 | -60.5897 | 2026-08-31 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d1bf3541-266b-3dd6-b43c-913c496cadf8 | -11.2485 | -45.0963 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1cdaf5ff-9add-3b09-b102-1436ff44d750 | -6.1109 | -57.684 | 2026-08-31 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| af858122-9ba5-3dea-bcce-d5ee158a3a96 | -10.7596 | -54.0384 | 2026-08-31 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 7c974141-8cc1-32cf-9c30-59377c398c0a | -11.5283 | -45.4933 | 2026-08-31 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 295.3 |
| 5ecd7a13-50cd-308a-ade9-c97f2b707bd2 | -3.5345 | -49.4733 | 2026-08-31 13:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 128e08fe-1f99-3f19-8266-7055efa8bc75 | -8.1672 | -54.9246 | 2026-08-31 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 58a8e27d-7d99-33a0-9e92-7fab5b6c2311 | -10.1531 | -45.7438 | 2026-08-31 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| a00c65bc-f99e-3dda-89d6-b725be51b39b | -11.5279 | -45.5162 | 2026-08-31 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 562.3 |
| 20be8dab-d942-373c-844c-a8c5e8e15d20 | -18.2904 | -52.6818 | 2026-08-31 13:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 46823c25-6543-33a5-95bd-d597ee9402f0 | -11.1634 | -50.5727 | 2026-08-31 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f4212ecd-8445-3970-80ab-5f30dd4d6607 | -6.1295 | -57.6637 | 2026-08-31 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0657d9b2-80e4-3653-b663-6a66cab72b4b | -7.1126 | -42.749 | 2026-08-31 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 55d51c32-73b3-342a-bf95-ab6878c1002c | -11.3615 | -45.1955 | 2026-08-31 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 64b8ea52-149b-379a-b22e-3eb381f7d1fc | -7.7752 | -44.0628 | 2026-08-31 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2f4cf27f-b8a7-34b6-a1b5-743021a05978 | -14.4201 | -52.5201 | 2026-08-31 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 615973c4-54d5-3d4c-8e0c-122394b2fed8 | -8.1534 | -45.4904 | 2026-08-31 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 5576310f-c95b-3633-a7f7-62db19bf8a22 | -7.1126 | -42.749 | 2026-08-31 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 7436bff5-8f37-3956-94b4-cc2dff73bbf8 | -14.4394 | -52.5176 | 2026-08-31 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 49b24342-2cce-308e-8715-b4ab8704a017 | -18.2899 | -52.7035 | 2026-08-31 13:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5205348e-a954-34ce-8a4e-785179819db9 | -6.6035 | -58.6166 | 2026-08-31 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 39aa7548-223a-317c-912d-6c310cdfa28e | -18.27 | -52.7068 | 2026-08-31 13:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 122.4 |
| aed47ba0-9a0a-3bea-a906-b32abc6506f4 | -19.134 | -57.4005 | 2026-08-31 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 173.2 |
| 68a829f1-8749-33e2-bff0-a52d5870e1eb | -11.3236 | -45.1778 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5e76d25f-6cf2-30e6-b032-2a39172a389e | -8.7439 | -46.4661 | 2026-08-31 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 795370a1-b1ab-379d-a778-1d8b5f835d36 | -19.1344 | -57.3797 | 2026-08-31 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.4 |
| d357cfc3-b2f5-3780-951e-0951af524c39 | -8.1672 | -54.9246 | 2026-08-31 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 50818ae9-0b94-3040-b7df-011b69c8eb3e | -7.3118 | -60.5897 | 2026-08-31 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f0f594bf-51d5-3220-99b5-c08e2839172e | -6.3892 | -45.489 | 2026-08-31 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b4e57efd-30ac-3d03-b419-7507e5ca5601 | -11.2503 | -54.0146 | 2026-08-31 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| b1608299-65b8-3e2b-ade6-b4af8ee2e9e8 | -18.2904 | -52.6818 | 2026-08-31 13:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 136.5 |


[Clique aqui para ver as próximas entradas](README86.md)
