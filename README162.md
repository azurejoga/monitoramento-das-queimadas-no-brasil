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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 052e17e4-3b93-34fa-a501-3f9ecb8be5e4 | -8.5576 | -46.306 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 92718c37-ad87-386c-a1e0-b2896bfc584e | -12.3914 | -51.094 | 2025-10-05 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 971def73-a54c-3c2f-b28c-05b487e55f22 | -7.9631 | -47.2964 | 2025-10-05 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| bdc33a21-75bd-3ea7-a098-054b688a6900 | -17.9661 | -51.1474 | 2025-10-05 14:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 551387f7-d012-3260-9004-d979a60e89ca | -9.931 | -50.911 | 2025-10-05 14:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| d291b1cf-3f7c-3480-902d-fe88f5e3758e | -7.006 | -47.4651 | 2025-10-05 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 2e7d310d-f60d-32c4-89fb-2d17a0a8257c | -10.3346 | -50.3188 | 2025-10-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| de4f200d-2e26-37bb-89cf-dd3a5a651011 | -17.9605 | -57.5904 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.0 |
| d69e765c-d0fb-3cab-8548-ee3fee5c9ffe | -7.6648 | -45.4471 | 2025-10-05 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| af9e2462-7388-3425-9a8a-17bd2c7afb98 | -6.3055 | -44.4495 | 2025-10-05 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| bdb70f6f-7509-3444-a539-0a7761c21b48 | -6.812 | -39.3987 | 2025-10-05 14:00:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 28d770f9-dd42-3d44-9005-675c4f9a9154 | -13.7473 | -51.3097 | 2025-10-05 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 261.2 |
| c9f89aad-356d-332b-b537-70c3f1106e5f | -7.6622 | -47.367 | 2025-10-05 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 7c5476ca-553a-3314-9ec5-d7390d53e487 | -6.6131 | -43.7085 | 2025-10-05 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4f1ccd5a-daf7-39f7-bf0d-b48c7ccf9209 | -12.5297 | -54.7326 | 2025-10-05 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 30ec2535-04d2-3918-873c-d207f4f44b35 | -8.5407 | -47.6831 | 2025-10-05 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a0e6d7a2-1483-3c13-9c3b-ee4dcc5991db | -17.9404 | -57.6134 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.3 |
| d2a88f71-1989-3314-afca-a8d241625b68 | -10.1497 | -45.9709 | 2025-10-05 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 65d1ec82-c6ec-341e-865e-351f156a06e1 | -6.3889 | -43.6115 | 2025-10-05 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 86ef9768-e6fb-344d-bc60-08f68a28e50e | -13.4445 | -47.7692 | 2025-10-05 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 95811ccd-58a1-39a5-85db-79890cb899f7 | -7.7938 | -42.5607 | 2025-10-05 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| 5f740ce2-99ee-3d93-8acc-9889eb2a5816 | -12.4105 | -51.0917 | 2025-10-05 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| bef055c0-2b5a-3c7c-a135-cb79635f5c8d | -12.5926 | -48.1366 | 2025-10-05 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 83393ff9-922d-3c09-84ed-5b2973a1062e | -8.1891 | -44.1357 | 2025-10-05 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 6f79d95b-5647-3c9d-8e8d-bc899b755b4d | -6.7866 | -41.5882 | 2025-10-05 14:00:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 146.7 |
| a3c323b7-0a74-32b1-a2ce-461a0ab863de | -13.0951 | -47.9323 | 2025-10-05 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a4462a29-30c1-3a21-9edc-5dc018271272 | -17.8417 | -57.6254 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 76a87d80-12a0-3377-98e1-4f7e09d00ca4 | -9.2783 | -46.0047 | 2025-10-05 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 349344e2-649f-3d69-8c2d-b3a69b27502f | -9.0966 | -49.9263 | 2025-10-05 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0edba24c-ac20-3b5f-9021-30548170af89 | -9.2973 | -46.0026 | 2025-10-05 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| bab098c4-e66d-33cb-b6a8-e2a007576a4e | -10.4557 | -48.3827 | 2025-10-05 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 667d74c0-cb86-337f-a732-e7e20c7a1f6f | -17.9609 | -57.5698 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 7be5b20d-1433-37f9-a3c6-8d8555036d85 | -6.0616 | -42.537 | 2025-10-05 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 86e89ddf-00fb-3695-82b5-18216f8b43ba | -7.4669 | -43.0674 | 2025-10-05 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 6b6cb288-6051-39f5-b730-b7cf1ded5b40 | -9.9313 | -50.8898 | 2025-10-05 14:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 8144d2af-5b81-3bda-b2f6-ee7b2f436a54 | -11.5264 | -46.742 | 2025-10-05 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 975affa8-f3ec-3827-8041-67a06deb7ec2 | -11.8033 | -45.0856 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| d7640ce8-6b34-3c6d-a8d5-be969725b4d7 | -12.1461 | -50.9309 | 2025-10-05 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 0afb88db-b969-3edb-b783-f18aad14e20c | -7.8047 | -48.0558 | 2025-10-05 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 608c8744-20c9-386e-b8eb-f4ad6b66e715 | -11.8777 | -56.8769 | 2025-10-05 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0643ed5e-6272-369f-9570-e180fce03aee | -11.1455 | -47.9275 | 2025-10-05 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a16b8f55-58d7-3eae-b288-51d24b77eb4b | -8.5393 | -46.2631 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 33111338-6b1d-3754-9eef-219b788282f4 | -13.7476 | -51.2883 | 2025-10-05 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 3636f37b-ea10-3f07-bf94-57ca49972c53 | -13.7284 | -51.2908 | 2025-10-05 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 220a8c73-3c58-3cd8-b54c-0d8549c33f25 | -9.3941 | -45.8336 | 2025-10-05 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 55f6758a-f0ae-313d-b402-72fa01336b11 | -18.1968 | -53.3638 | 2025-10-05 14:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 33730c94-dccc-30f3-8319-f525dddaef37 | -17.921 | -57.5952 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.4 |
| bbaefbfb-75b2-37e3-acd7-89d634b662d5 | -18.1769 | -53.3669 | 2025-10-05 14:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 46d886a8-b369-32fe-ba7e-e508ed5f07c0 | -11.5301 | -47.6798 | 2025-10-05 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 62765437-68c8-3b9e-93fe-b44a78cc84b9 | -10.386 | -45.4184 | 2025-10-05 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 8e41b23d-5342-3d56-b459-46e6ba1de90b | -6.4179 | -44.4633 | 2025-10-05 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a8f23e6a-33f6-335a-8e82-5f4a0fd6104c | -10.4054 | -45.3931 | 2025-10-05 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 279.1 |
| 5ffc7a4a-8447-3efe-a4ef-3efe8afd8080 | -11.1168 | -49.8492 | 2025-10-05 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0bda2a86-578f-35f8-8a10-d9a80e522976 | -6.2596 | -45.341 | 2025-10-05 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2aea9a37-2832-3a13-9bfe-f76d4821210f | -6.4161 | -44.6466 | 2025-10-05 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c5e6fe48-c226-3012-8fa8-6fd2e0f4c007 | -16.0966 | -51.0829 | 2025-10-05 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 73c5928e-5f51-3878-ad55-ae3c9f41ae61 | -11.8038 | -45.0624 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| dd66973b-797e-3f18-b8a5-735099bc08a1 | -14.1611 | -53.0377 | 2025-10-05 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 209fe607-90c5-3018-81f7-310ccb1b5689 | -8.5578 | -46.2836 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 689111a1-d697-3038-a3cc-dae1751ef041 | -14.0032 | -44.961 | 2025-10-05 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 42f9c1b1-430d-3f0b-be59-d0d5d3db18c9 | -11.0978 | -49.8513 | 2025-10-05 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 372fa069-2487-3db0-80d8-4946bfd01f38 | -17.9408 | -57.5928 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 277fee65-ba11-39c2-b06d-6ea3bd1fcd41 | -15.9829 | -50.905 | 2025-10-05 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e07dc74c-061a-3db5-9f5f-d48f1c705237 | -15.9084 | -48.8254 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 7801ad52-b5a5-3ce7-86c8-25fc217ca071 | -21.6882 | -50.0788 | 2025-10-05 14:00:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.6 |
| f13089fc-26e3-357a-87a8-3044bdd5dd29 | -9.3938 | -45.8562 | 2025-10-05 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f96c155e-4a3a-3c29-bad0-d9c821e4c244 | -10.1766 | -45.4449 | 2025-10-05 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c99dd84b-cb36-300d-868c-61c13f3ec92f | -7.4672 | -43.0438 | 2025-10-05 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 4c7ef351-aba5-3d2c-b075-506d04d43be0 | -7.7743 | -42.6103 | 2025-10-05 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 168.1 |
| a079e0e9-0e31-3dbe-a117-56c893c77171 | -7.5267 | -41.2699 | 2025-10-05 14:00:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 126.0 |
| a37edfbc-d328-32c3-a9b9-8c5ca22639c1 | -8.5953 | -46.3022 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 52492401-33e5-3e91-a880-ca4d2231ead2 | -7.7749 | -42.5628 | 2025-10-05 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 2767ecb5-883b-3958-8ecd-fb592f129667 | -10.6378 | -46.3396 | 2025-10-05 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| f053fe0c-b2ca-34df-b841-c99f891c7ce3 | -10.3907 | -50.3557 | 2025-10-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 52344051-ab29-3539-befb-41808083ec9e | -9.5794 | -46.106 | 2025-10-05 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| d020947a-19ee-3c8b-a3d0-b87089fa3010 | -7.0369 | -42.78 | 2025-10-05 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 172.6 |
| f80f834e-3fab-3c6b-9514-0dfd2bfdeed6 | -16.0021 | -50.9238 | 2025-10-05 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 4e32c782-48f7-361d-b7ff-c8ea4744d44a | -13.728 | -51.3122 | 2025-10-05 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 00da295c-71ab-3196-88b1-75237db97ba1 | -8.5581 | -46.2611 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| b4720d0c-3b0c-3547-a1d7-d90f84048035 | -6.3341 | -41.6309 | 2025-10-05 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| ef320689-5cc3-34ca-8013-6c715aaf6922 | -18.2569 | -53.3329 | 2025-10-05 14:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 69.8 |
| cb139bb0-5b99-30b0-bcbf-873592b7ed13 | -7.4279 | -46.5016 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| bc15b56a-ffc4-3518-b9d4-2b32134ba48d | -8.2787 | -47.5978 | 2025-10-05 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 3a99828c-6462-3c65-8e90-f7a49ee85219 | -12.4673 | -45.4925 | 2025-10-05 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 44857d1a-72f6-3bd9-b641-6b5df47fe456 | -10.1943 | -45.5339 | 2025-10-05 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 37354672-c02b-3cf6-a163-62cfed1a14e1 | -10.0501 | -50.4326 | 2025-10-05 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b757cd11-6d6c-38ce-8e60-f51be23dd133 | -8.5578 | -46.2836 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3953badf-fecf-3e24-90a4-c5ebdd4c4229 | -8.468 | -45.9332 | 2025-10-05 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 44bf4ca9-ed38-3f86-a842-98bbbe9f8ceb | -13.728 | -51.3122 | 2025-10-05 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 245.2 |
| b4ac015b-598d-3ed2-b86a-4e1211537cd8 | -10.1943 | -45.5339 | 2025-10-05 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 3f1688bf-958d-3402-b100-9a2151a57ebd | -8.1888 | -44.1588 | 2025-10-05 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 93a4824d-2d4b-3738-9853-80bc2abd3f5b | -8.854 | -46.7005 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0b28e845-347b-35d3-8374-fcfce221cd58 | -6.2596 | -45.341 | 2025-10-05 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b00f26d4-0a31-3daf-aec7-9a03b1710cb3 | -12.0703 | -45.1612 | 2025-10-05 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 02042c1b-f275-3f13-9e86-a44fc3361699 | -9.5794 | -46.106 | 2025-10-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 6411c624-bd17-386b-a5d1-4bb354d36f9e | -7.7306 | -46.2737 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ac975421-d366-39c4-bc2e-70340c4a7e45 | -12.3917 | -51.0726 | 2025-10-05 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8706873b-7d21-3b3b-a738-40dd0dc5351f | -9.425 | -49.2084 | 2025-10-05 14:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1de89a59-921b-3c1c-848d-a1cc6721de47 | -11.7912 | -48.0448 | 2025-10-05 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 152274e0-3406-3430-b639-0613925ccc8a | -6.4079 | -43.5867 | 2025-10-05 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |


[Clique aqui para ver as próximas entradas](README163.md)
