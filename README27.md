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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4df953c5-99a0-3a51-9e4e-8e5e87c3ae05 | -5.8768 | -42.41082 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb2be89b-9d1f-3f9c-a333-cd6b16d7a822 | -6.09541 | -44.37507 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 348efe72-e5b5-3c95-962d-ad9c4162eee1 | -6.02448 | -44.36045 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d465f4b8-aa8f-3716-b3c5-2368752ad5ed | -6.71094 | -44.32518 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 787f1e9d-2570-3ccf-9d0e-e4934a85a0f7 | -6.94581 | -42.8644 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8ae168fc-3453-3f85-96eb-6e2662dee59b | -7.63224 | -45.2473 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9737aae2-989a-3033-bcb9-eebb10e23bf7 | -6.5771 | -44.46257 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a21ccc-5613-390a-bf9f-3daa55c91c47 | -8.84379 | -52.04329 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23ecd594-fc0c-38a5-a0be-e3cb83d8c194 | -7.14988 | -44.63946 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e60ba17-f7cc-31ec-9428-f0a02ab7b77b | -12.08016 | -47.90973 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee85d710-6ff2-3d60-b753-a081a00721c1 | -10.71907 | -48.24383 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9365f9c8-717f-3586-8f9e-5fd0e6f51f19 | -7.99468 | -47.33593 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3728f6f6-5f85-3e45-827f-e26e6eb21374 | -6.01188 | -42.81975 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3e4cd74-490e-3761-8f29-d3572e3e1c99 | -7.14337 | -44.59352 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdf6cbd0-971d-30dd-8387-321bd3299698 | -6.49736 | -42.9781 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8522b253-e65b-3450-a9a5-52cfd89b5b4a | -6.49423 | -43.10559 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9c7abe-b143-3d9a-8afc-fdc67a712192 | -6.5051 | -43.44554 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 84a85e8b-8adc-34ab-9279-154525bfb376 | -6.13081 | -44.71917 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29368d44-828a-349d-9bc0-8e76d5bb2a79 | -7.66188 | -45.25119 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4879c3bc-a57f-3e94-8600-eafea3e27489 | -10.99499 | -45.62331 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 050170d1-fb9f-3dd8-b715-24dd3deaaf8c | -5.79348 | -45.07929 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a2dbd39-58de-3430-8ee5-a3f149fdddef | -11.43477 | -47.3157 | 2025-08-21 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e437ca29-03cb-3115-b738-bbfe10011d51 | -6.95552 | -42.86207 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e3d0300d-2b20-3c0a-9b46-d9be6c39b9f2 | -11.29726 | -44.94685 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eef45c3f-d831-3034-b5ab-55acb6000c08 | -6.45824 | -53.38123 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33423494-8bb0-3aad-9c5e-6f800dbe1ab1 | -6.52923 | -45.46256 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b87658e-d0e2-3bcc-a313-b37ba2d0e877 | -11.30452 | -44.94441 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52048fd9-db50-322e-986c-da42b8157c1a | -6.56405 | -44.47892 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0681b2f7-1dc6-3a79-aad1-b4db696588c3 | -10.28604 | -46.76703 | 2025-08-21 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3794a84f-2567-390f-803b-498490df9145 | -12.64015 | -46.87946 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9f46414-dd30-3456-8418-832da75ae354 | -8.84208 | -52.05287 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c90fba5-8b2f-37f5-9d32-02f6b68aeaba | -12.6395 | -46.88335 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e130a33-7afc-3e87-8c45-4dffdc9935e4 | -12.08466 | -47.90581 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d2c5919-4836-30e6-96d0-8bb2e8532724 | -9.85314 | -44.68995 | 2025-08-21 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab4a759-8085-34a7-8b94-2786ffb16f54 | -6.0213 | -42.82479 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c55f9dee-bac2-39ac-bf40-254e1f9d2805 | -6.07094 | -44.11295 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38441400-e55b-3935-816d-c09f11c723ae | -12.98737 | -45.21418 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fa31ae4a-287a-35f7-b264-32d9bc831b62 | -10.72677 | -48.24521 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e2fdb79-10d5-3a37-bec6-18dd67cbad28 | -7.62169 | -45.26884 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afba4a5a-720b-3bdf-ac04-a89b7657f44b | -6.0462 | -44.11647 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab4d4f25-ec1c-39e0-9a62-fbce87373ecb | -8.16645 | -47.33001 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bde7d918-ccc4-37b1-931a-a344ac81f1ac | -7.1487 | -44.64675 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b11061b7-7fd2-3532-a87b-f52028cfb3c9 | -12.2192 | -45.40123 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f05fd56-b3a9-387c-8379-40f258cfb892 | -11.91168 | -44.87651 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1fd8801-4f79-30a9-9aa4-848151b9cba1 | -6.63452 | -43.90771 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c568cb1d-929f-316b-9443-7b6469c00bf0 | -6.96944 | -44.15707 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43b407f0-5e89-3d87-bb3e-1937b8c12796 | -5.95651 | -44.15018 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cce2b83c-6dd7-3739-9ebe-b462419529f7 | -6.10403 | -45.41296 | 2025-08-21 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfa8995d-3f8c-3fb0-8f8b-27d603e46650 | -7.2763 | -43.67933 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff76b87f-4274-3898-98c0-fd8bcb647be2 | -6.20014 | -43.57195 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc3e7bfe-2e2e-3229-8dda-ce3305040d5d | -8.06909 | -43.67679 | 2025-08-21 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7aa4d8f2-a715-35ca-b846-0b3bdaf5e4b8 | -6.0857 | -44.69651 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c336382-6aef-3774-88d4-d6c11317ef35 | -6.20181 | -43.56147 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ad707ce-7cef-3ba9-9b10-d69a0fb98696 | -7.64809 | -45.24901 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfe87f0b-6124-3596-9606-f966ece0cd49 | -6.04258 | -44.35595 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d1c6e6f-8261-3d29-926c-e18f4e8f176b | -13.01983 | -45.18289 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9417c890-f4e9-33f5-8732-ece05ee10db9 | -8.07297 | -43.67384 | 2025-08-21 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 717a20f1-c8fb-30e0-9927-74fd47ef500f | -7.3864 | -45.9838 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87132bf5-e9f7-33dd-bc70-8d5c6bd9e2f7 | -13.02661 | -45.162 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ef1e51d8-9254-3b53-8e12-91ee865c89e4 | -7.56999 | -44.3994 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6678e2c7-38e2-314d-aac6-179eed0e8979 | -6.2607 | -43.7289 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fac70e9-591b-31ac-a5f9-f160ee0f28d0 | -6.26126 | -43.72536 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87ef84f2-91aa-336a-adee-6251c3e9d508 | -13.0227 | -45.16502 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5ed0621b-1aeb-3f1f-b136-1732c4500983 | -6.0816 | -43.4496 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e124f194-13ff-3d88-b48f-9e2178a518a3 | -8.83525 | -52.06157 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57e33cf8-7a97-3be4-84ec-cac30e478e36 | -8.38592 | -44.59989 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88723423-3366-3e71-9cae-6eb5f4ec1695 | -6.27681 | -43.7283 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f622a7cb-488c-3caa-a759-634f4c0504f7 | -6.94943 | -43.86436 | 2025-08-21 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f508874-7be5-3981-8b49-bcd1c68a8f18 | -6.71431 | -44.32573 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 705e1935-4f81-30db-873c-d22c45d6b336 | -6.21592 | -44.12866 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b0e1b82-d4fe-37cd-a8e8-77208217a880 | -11.8611 | -51.60339 | 2025-08-21 04:17:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a10ec22c-960e-3090-9d8f-79d843e6c5cc | -8.28671 | -47.27918 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e58c1449-4d74-331a-a56a-29b9e1616331 | -9.12086 | -40.30873 | 2025-08-21 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8099f026-2257-3964-a02e-057347c7d3f9 | -5.78079 | -45.06944 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b3dcc3-f18d-321f-abf1-7c8a09dbd511 | -6.95829 | -42.86607 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5fd8c49d-3f14-338a-82cb-e58988f44638 | -10.53857 | -42.54883 | 2025-08-21 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f49ae98-21fb-38de-9725-e507e5b63346 | -12.98012 | -45.21665 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 82ed56e7-d477-386d-979d-3d4d1ffa7487 | -8.80032 | -45.43287 | 2025-08-21 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad95cc8a-d952-3cb8-88cf-a7b509e11c41 | -6.82676 | -44.43536 | 2025-08-21 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35c5b091-6bdd-397e-b2a3-295b8a72da32 | -6.96608 | -44.15654 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab03ebee-2574-3983-806b-bcc09fd86196 | -7.7035 | -44.01725 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79a067b8-8baa-3400-adf8-8b786b89d02f | -6.1968 | -43.57144 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d909de1-5515-3d02-8a1c-f3c35ffa8d45 | -10.27952 | -46.76207 | 2025-08-21 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a7e3309-9feb-320d-8590-9e16b3847127 | -11.17314 | -46.13875 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd3bdd90-3eeb-341d-be35-89284c7d135b | -6.62173 | -43.88033 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a48f5fe-adfa-3904-836b-6d2a79aceced | -6.27017 | -43.71235 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 423cf051-e8bb-3532-918e-afefab69d28f | -6.03242 | -44.35428 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a5db1f9-4fc0-3f3f-9711-c712943567cb | -6.0392 | -44.35538 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8713bc6f-fcbc-371c-8660-49ba1a09d545 | -7.5492 | -44.00655 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2cb2e03-9146-3bef-9da7-b0912b55cceb | -6.17415 | -44.73373 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 368fbbd8-3177-3746-83ab-2b2ec1309dbd | -6.95219 | -42.86155 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fed2c78f-f01a-30f6-91da-2f9844e14664 | -10.71387 | -48.22771 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8587b67a-ce55-36c5-b1e1-fc02d78d7971 | -6.02353 | -42.83224 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 360dd0ff-455d-3a48-ada3-acec2f9542bf | -7.39252 | -48.18959 | 2025-08-21 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c246de6-3f09-34fd-beb0-71a170c4df66 | -8.2163 | -44.4222 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c07096e9-d728-307a-90c1-aaa7043d46eb | -11.81718 | -44.25506 | 2025-08-21 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a1c40ad-48f1-3bca-a103-8e4b3cd5b70a | -5.10842 | -46.1806 | 2025-08-21 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24f89b00-4c26-33f8-9c5d-99b011036532 | -6.71151 | -44.32159 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 129b4a82-9d62-3e1e-b618-893afabdc110 | -7.02979 | -44.62727 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 80ee9a08-bf04-39d0-b864-d4b48f7c5357 | -7.62108 | -45.27257 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
