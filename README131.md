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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ebbc9fe-c1e8-341f-9381-0fa00f8f1a62 | -11.429 | -43.5307 | 2025-09-12 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a3672681-dd19-3729-9461-b835e6a6af0c | -12.5598 | -44.6677 | 2025-09-12 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cecc0855-61a6-3454-9ee8-bf4a7857c68c | -15.1402 | -50.1628 | 2025-09-12 13:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c94ea2af-2492-3a0c-b863-af4b47f25a54 | -6.1703 | -41.0901 | 2025-09-12 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 506.9 |
| 19fa7c83-4480-3fdc-9ffb-2addf32a8017 | -8.4893 | -47.2694 | 2025-09-12 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 1bfa5518-3c9d-3df3-ab43-b4024f17ac5e | -8.9087 | -49.9433 | 2025-09-12 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 88a13e15-cead-31c4-952a-ae9bc22b2daa | -9.6916 | -47.566 | 2025-09-12 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| fd90a78e-f0c0-347a-b530-e4db9257de8e | -9.0759 | -47.0335 | 2025-09-12 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 60b8a28f-05af-3a62-97d0-650a65424660 | -10.4441 | -50.6059 | 2025-09-12 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 365.4 |
| c52c7a35-5b7f-3d65-9499-fea8a8a17bd8 | -10.6979 | -48.6612 | 2025-09-12 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 288.0 |
| a16604b7-4391-3a84-90eb-0c446ac53195 | -10.4438 | -50.6272 | 2025-09-12 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| edd0e106-e89d-36f4-afdc-59663a85a6ec | -10.0943 | -47.1664 | 2025-09-12 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| c92d89d0-029e-3bfa-ad88-e124e93c45d7 | -11.5425 | -50.5947 | 2025-09-12 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 140b3459-aa62-3710-8aa2-2bb2b1e6d397 | -10.8785 | -45.5597 | 2025-09-12 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 65cb1fee-9945-3c84-8125-7acc8f58aca0 | -14.4394 | -47.3206 | 2025-09-12 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e7f99b24-0d00-3c2b-b681-dcb879a892ef | -6.1891 | -41.0884 | 2025-09-12 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 275.7 |
| cb6be879-5169-35a7-aa0e-b5135913349f | -8.4143 | -47.2545 | 2025-09-12 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c9c55b70-5196-3464-b25e-445f114fe9ee | -14.4588 | -47.3174 | 2025-09-12 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f640a7a6-d973-3664-aa85-743be3ab97c8 | -9.0379 | -47.0597 | 2025-09-12 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d5446be2-df78-389c-a223-f1ae14eb8e12 | -8.9087 | -49.9433 | 2025-09-12 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9d510bdb-7e38-39e4-b297-96814853c26c | -11.9211 | -50.7009 | 2025-09-12 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b54de73d-b5f1-3a58-a2d4-58e684692a8b | -14.2922 | -45.073 | 2025-09-12 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 33448461-8fc2-31b4-9f42-9c531abca54b | -10.8785 | -45.5597 | 2025-09-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5eceb293-de83-3c31-8975-66b27c62a326 | -10.4438 | -50.6272 | 2025-09-12 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 2913a865-f8e0-3092-bf92-19bb556d56fd | -6.1891 | -41.0884 | 2025-09-12 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 383.0 |
| 9a49fcbd-54db-311d-8f0f-970c0669dd6c | -10.679 | -48.6633 | 2025-09-12 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b2eb752b-3ae7-34cf-931a-b267ad73cee4 | -16.08 | -49.9709 | 2025-09-12 13:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 56dcf69b-616c-3ce1-a247-e2a5be0c90f5 | -8.956 | -46.1074 | 2025-09-12 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 208.6 |
| cba42631-ef03-3b3b-bdf6-eba0efed83da | -9.6727 | -47.568 | 2025-09-12 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b024b098-5e8d-34a6-8737-c28e24269f92 | -9.7197 | -46.8972 | 2025-09-12 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 65eddece-5211-3ba0-8079-5f0af7e1adad | -12.9292 | -54.7538 | 2025-09-12 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| d49c796f-105f-3a16-98b7-5d7cbbc19916 | -10.0943 | -47.1664 | 2025-09-12 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 402.5 |
| ae2ddb47-58da-38a1-a4e2-6aaf073e18a2 | -6.1735 | -42.6221 | 2025-09-12 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 437a5f64-b6c6-347a-85ac-216dd9145bbc | -12.5598 | -44.6677 | 2025-09-12 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 64624c20-fa1a-3169-b881-19cfff5e51b5 | -11.5422 | -50.6161 | 2025-09-12 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 171.7 |
| adac5a92-ce50-318b-a809-b6dc3367cb36 | -11.4285 | -43.5544 | 2025-09-12 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 2d526974-f0d9-3189-8ec3-6754e5ed0061 | -7.5641 | -44.4068 | 2025-09-12 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 8062d5ef-aa16-3f6c-a55d-bb13b9924146 | -7.3212 | -49.6255 | 2025-09-12 13:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e80f5fbe-7ac9-3229-b2c4-743b6b9f5dc6 | -10.3504 | -50.5516 | 2025-09-12 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a36ad350-acd0-360f-9d85-86bc6456d273 | -12.9294 | -54.7333 | 2025-09-12 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6e615a35-ef55-33ca-8285-91e9238d1743 | -14.4588 | -47.3174 | 2025-09-12 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a32eb3da-9864-3284-bd19-7432eb50f23e | -14.1907 | -46.2012 | 2025-09-12 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 32adb151-4daa-3ff0-9eb0-ccc3a69ddbfd | -9.9004 | -51.8811 | 2025-09-12 13:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 73863f9d-6c06-3cad-8598-d2cbc15575ce | -8.9371 | -46.1094 | 2025-09-12 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 5d18d699-d179-3be7-bb1f-ce7561ce8405 | -13.1838 | -51.7429 | 2025-09-12 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| e0b5a998-1c1b-321f-84a6-8364726ee555 | -8.1837 | -46.0965 | 2025-09-12 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3418f240-e91d-319a-96c7-4e469fa113fb | -9.72 | -46.8749 | 2025-09-12 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b7c63837-b5f2-34b8-b629-e91d245b8d19 | -6.7501 | -44.9839 | 2025-09-12 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e5435d13-c140-3239-97a3-ab007d95ec13 | -7.5455 | -44.3856 | 2025-09-12 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 283f9f2d-20cc-3762-9327-d526c8f502f7 | -7.5232 | -44.6862 | 2025-09-12 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| b5b83fdd-e074-34a1-8e1a-fd0cfb9bb384 | -7.5452 | -44.4086 | 2025-09-12 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 4dbbacfc-f962-37f7-b5b4-ab9659b9d15e | -11.9713 | -51.164 | 2025-09-12 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| d564125f-68ac-3680-846e-7a7cdc238d62 | -14.2727 | -45.0765 | 2025-09-12 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 195.2 |
| c2dfd1c7-9e80-3f81-8f96-ed848915d427 | -21.6455 | -50.1339 | 2025-09-12 13:40:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 231.9 |
| a0294798-48b3-36ca-92c0-0849ccc397d6 | -15.1058 | -47.9983 | 2025-09-12 13:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2a5dd2b4-525f-3495-8e25-e6dd1ebcc305 | -10.1405 | -47.9133 | 2025-09-12 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b2258f08-7187-36b2-8964-974ff92cde86 | -9.057 | -47.0355 | 2025-09-12 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c7e7ebc8-13ab-3596-8274-91bad3383c33 | -10.8781 | -45.5826 | 2025-09-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| fe0bf07b-57c1-3bbd-8d8c-38dcb8ca8e7d | -11.429 | -43.5307 | 2025-09-12 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 538022b7-bcc6-35b6-9530-c2461bc2ca3b | -6.1703 | -41.0901 | 2025-09-12 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 782.5 |
| 518527a2-fa9a-325d-817f-05289c7c9d64 | -10.1133 | -47.1642 | 2025-09-12 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 564.6 |
| e46dd2df-b184-3066-b5c2-8b107f1b5af2 | -9.9571 | -50.3353 | 2025-09-12 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 67eae713-8a05-3320-bba0-69f9fcaad69c | -9.0376 | -47.0819 | 2025-09-12 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 1b2024cd-fd3f-3a9a-a841-582fef1655b0 | -8.9374 | -46.0869 | 2025-09-12 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 04c38646-0022-36c7-bc75-fe65fae9c599 | -10.8968 | -45.6029 | 2025-09-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8fa285d8-dea6-3625-b974-8f8390c3dd62 | -6.1894 | -41.0641 | 2025-09-12 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 7e9f3122-a05f-3596-8b52-eed8e23736d8 | -12.9101 | -54.7558 | 2025-09-12 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 03465f18-2fc1-322a-a350-15f30c27bf99 | -10.8972 | -45.58 | 2025-09-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 6d650d21-ad85-38bb-baab-6183a7a38ff4 | -9.0382 | -47.0375 | 2025-09-12 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e77f3779-a096-308f-aac2-07d5c062532f | -10.6979 | -48.6612 | 2025-09-12 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| b3a2a690-3db6-32f1-9d4b-ed850734e7bb | -11.4398 | -48.5733 | 2025-09-12 13:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 510.4 |
| 71eeaa16-0567-31be-ab62-60bf9c4620e8 | -14.1717 | -46.1815 | 2025-09-12 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 96ac07b6-8654-3d08-a59d-fee5bd347d32 | -10.0717 | -46.116 | 2025-09-12 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 68a26808-151a-3249-a594-0d617389e4a5 | -8.4331 | -47.2527 | 2025-09-12 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 32d13ab9-c25c-3729-a8e9-5d87e78b23d4 | -14.2732 | -45.053 | 2025-09-12 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 410bd8fa-fe52-3267-a6b5-76abaa55acf6 | -10.4441 | -50.6059 | 2025-09-12 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 597bb5a5-a168-3c9e-b378-5d80c057a15f | -16.4123 | -45.6728 | 2025-09-12 13:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 3ae40ab1-52b1-30e6-860e-14006bc66cb0 | -14.4935 | -53.9181 | 2025-09-12 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 88ac8292-2d3c-3503-b9ce-5e80bb69a1e2 | -9.6827 | -46.8345 | 2025-09-12 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d4508c0c-8730-30c5-ac3e-6073c921733b | -6.5541 | -43.9684 | 2025-09-12 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b5cb8654-ebac-3918-a00b-1a8202740730 | -14.4133 | -52.9221 | 2025-09-12 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| b02b1b86-1bc5-3566-8650-031076b31e25 | -6.3278 | -42.2294 | 2025-09-12 13:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| d6ee4c5f-e60b-36b7-9d5a-074e6ad3d1c7 | -9.0379 | -47.0597 | 2025-09-12 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c6bbd166-608e-338c-8578-f860730807af | -11.486 | -49.2876 | 2025-09-12 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b16bd2d1-9d68-3d29-91b5-08427b2dfe66 | -9.9574 | -50.3139 | 2025-09-12 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 25102b99-ee94-3799-88fc-0ecb447f4305 | -16.4118 | -45.6963 | 2025-09-12 13:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 79de112b-ab34-3ced-98f2-037d5e49a2b3 | -10.3507 | -50.5303 | 2025-09-12 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d9d09d8b-3a90-3d10-ab36-8edbfc30814a | -7.5643 | -44.3838 | 2025-09-12 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 678a4548-074c-36bf-a5f8-e97253830033 | -9.77 | -46.0163 | 2025-09-12 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1b5732c5-fb30-3edc-8aee-7c484c1711d0 | -14.5132 | -53.8949 | 2025-09-12 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 15659da7-57fa-369d-87a3-e3bd70b92cd5 | -6.8184 | -45.6349 | 2025-09-12 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 57d954bb-b66b-324c-8b54-a75d7ff8524d | -8.9563 | -46.0849 | 2025-09-12 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 204.2 |
| d8fecf78-df7d-35df-8521-640b6d59f155 | -11.5425 | -50.5947 | 2025-09-12 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 54bfaf15-5ab2-32db-bb0a-6b7677c0617c | -6.1705 | -41.0658 | 2025-09-12 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 247928e0-9f7f-31a1-a4bf-7836dd1d791d | -6.309 | -42.2311 | 2025-09-12 13:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 6a5908aa-7d01-3a46-9f12-4a1584d8d19b | -10.0754 | -47.1686 | 2025-09-12 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6c080e4c-443d-31fd-9014-b2312f0fec81 | -9.0759 | -47.0335 | 2025-09-12 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 59edf0e9-4c2d-3dda-8008-d8ac96347458 | -14.4394 | -47.3206 | 2025-09-12 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c0a7d57d-b569-3f54-843b-1d591c139e91 | -10.4252 | -50.6078 | 2025-09-12 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| d3267d88-7d90-34d3-a738-ed684951a743 | -6.3226 | -53.4553 | 2025-09-12 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |


[Clique aqui para ver as próximas entradas](README132.md)
