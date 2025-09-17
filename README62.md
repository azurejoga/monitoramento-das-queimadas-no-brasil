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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bce066db-e17a-30ce-b4f9-84349f420d37 | -8.1572 | -46.747 | 2025-09-17 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 0ecafde0-342d-35e3-961d-e864845293ca | -13.9648 | -44.9445 | 2025-09-17 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| c2b43da1-823d-3436-895b-326ffade2a81 | -12.7294 | -47.9845 | 2025-09-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| a11abbe5-8de6-3793-abcb-6bebc5b208dc | -12.0243 | -46.6736 | 2025-09-17 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| e5ba993e-9bbc-3645-8238-4bfee50879ca | -7.4688 | -46.1854 | 2025-09-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c0c0c005-9e54-3189-bb3d-bcd34038b631 | -7.581 | -44.566 | 2025-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| c66bf960-ed90-3bfb-943d-ee08dceb4b15 | -8.6702 | -46.3394 | 2025-09-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a1255672-e3a1-3b39-95a9-da33404c6244 | -13.9653 | -44.921 | 2025-09-17 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 324.6 |
| e725d8b4-a7d2-3b82-b816-66e71f11d8d2 | -8.4279 | -47.6937 | 2025-09-17 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| eeefe21a-791b-3207-937d-a19ff1084885 | -8.4467 | -47.692 | 2025-09-17 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| f928dfd0-4f52-380b-a129-46420b8f986a | -12.0051 | -46.6763 | 2025-09-17 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| b8c27d82-ecde-3817-91a4-0481d6f35a7f | -10.3297 | -46.625 | 2025-09-17 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2f30d0e1-e396-337b-aae1-893e6409012a | -9.1236 | -44.8849 | 2025-09-17 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b41f5ec3-e4f9-3eb4-9ecc-5c04378fa239 | -8.6699 | -46.3618 | 2025-09-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 070c5cd5-1c79-368c-9e20-5d125cc297b3 | -7.45 | -46.1871 | 2025-09-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| c3e865c8-a6ae-3171-bbb7-e155c106f9a4 | -13.9458 | -44.9245 | 2025-09-17 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| bc4480e4-86b7-3373-90e5-3fddf7720080 | -12.7106 | -47.9649 | 2025-09-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| d6dd5068-cb86-369c-880c-44f75fc90cba | -8.4787 | -45.0932 | 2025-09-17 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 213bf72b-fcf6-314a-9cd6-7d7c770d7a85 | -6.6129 | -45.584 | 2025-09-17 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2b948dc0-25bb-35c2-846d-719a6ad0c7d9 | -7.6574 | -44.4667 | 2025-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a146baa6-57fc-32b2-975f-77dc4db8ba3e | -8.992 | -46.2385 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 2dd5cb8e-d2f8-3756-9196-ecf5b5f32c0e | -8.9536 | -46.2874 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| dfb3cec3-526f-351a-b38f-fbf17f599a80 | -12.7102 | -47.9872 | 2025-09-17 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8ca42e85-b260-3b43-943e-fd0cef51c56f | -13.9648 | -44.9445 | 2025-09-17 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 385.2 |
| b9ef90e8-81c8-332b-94de-400db4ac9d9d | -12.0243 | -46.6736 | 2025-09-17 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7c284a70-a961-36a6-8890-e2585c6cb5e2 | -6.1868 | -45.1201 | 2025-09-17 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 548be392-7599-3790-ba93-cded0dfebf1b | -6.6127 | -45.6066 | 2025-09-17 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a5afc200-f9b3-3dac-86a9-5139aad2b0b1 | -10.6925 | -46.4904 | 2025-09-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d87b672e-1a4e-38a5-afd1-6eff48ac2479 | -11.5966 | -48.2902 | 2025-09-17 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 069dc031-bf33-35ee-b577-1f72961e1203 | -7.897 | -48.1787 | 2025-09-17 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 203.4 |
| ea0f32b1-35a0-3555-a33a-f3a1ca08ca5a | -8.9533 | -46.3099 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 872f57dd-b136-3bbc-a0a3-a883917cbea0 | -7.581 | -44.566 | 2025-09-17 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 85f87021-210f-3fe6-bf90-6508eda6b82a | -9.0661 | -44.9374 | 2025-09-17 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 2d98acfa-b1fc-3db0-85cc-9f4473cd3acb | -8.631 | -46.4553 | 2025-09-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5833bc69-ff14-34e6-96c5-58c31f254db9 | -9.4747 | -48.2698 | 2025-09-17 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e4c49120-641f-336f-aa0e-44d847344ebb | -12.0051 | -46.6763 | 2025-09-17 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 169.4 |
| ae4ef017-edc9-32ab-bdf9-23b17fb2054c | -8.9449 | -45.521 | 2025-09-17 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 349.3 |
| a94a8728-9ce5-3a36-8dd8-dcad6e978bb7 | -5.7671 | -43.9392 | 2025-09-17 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f354eb7b-4eed-3afc-8cc6-6b6a439a7432 | -9.0851 | -44.9352 | 2025-09-17 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 16d9e2eb-696c-317d-9774-4deda26b3b25 | -8.8987 | -46.1585 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 07112b06-7f1b-37df-a79b-605bae967595 | -10.6731 | -46.5154 | 2025-09-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 69041b74-0e7f-3c3c-9af0-877a810240e0 | -10.33 | -46.6025 | 2025-09-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 0fdea1c4-8a16-3f92-ac86-fa1429494cdc | -7.8783 | -48.1803 | 2025-09-17 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 96e1cd62-30cd-382e-b969-7ee886b473c5 | -11.1108 | -45.3452 | 2025-09-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| bfcc7a83-fdab-3094-9230-dc588dd3febc | -13.9653 | -44.921 | 2025-09-17 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 404.9 |
| 63c63996-1327-35cc-9988-75fdd754f0e2 | -8.899 | -46.136 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 394ebc03-387d-3358-b375-e30dd1df782d | -8.953 | -46.3324 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 22b57041-082d-3679-9a94-1b4e2a333229 | -5.4897 | -39.426 | 2025-09-17 13:10:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 600a0140-54e6-3a93-9443-84c23b3e8938 | -7.45 | -46.1871 | 2025-09-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a31672e5-b540-3b9a-b04b-b07c79e1c4d8 | -8.6882 | -46.4047 | 2025-09-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 722e92e6-ee88-3d48-a6c7-05ca53cccefe | -7.4109 | -50.0019 | 2025-09-17 13:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| bf50dd6e-d704-3f7c-b649-c33413b7ca3a | -12.7106 | -47.9649 | 2025-09-17 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 929139fd-e396-3e62-8b83-6b536e02031d | -8.8958 | -47.8683 | 2025-09-17 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 2f2b3784-fef2-349d-958b-3b5420430542 | -12.7482 | -48.0041 | 2025-09-17 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 65374377-985c-3ee7-a916-4c56a9bcd3cd | -8.9731 | -46.2405 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 16fefb63-1bb9-3e56-8990-1c53274a95fc | -7.5227 | -44.7321 | 2025-09-17 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8236ca32-8dbb-3e1c-af96-b61f74b17182 | -12.7294 | -47.9845 | 2025-09-17 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| fc4658c8-540b-3236-9d0c-88eb63103808 | -10.6734 | -46.4928 | 2025-09-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 7b30bcc0-07c7-3734-a9c6-06dfe8c446db | -8.9917 | -46.2609 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| d6644628-5b9f-3e65-8709-cf401b6fc3de | -3.8042 | -44.1072 | 2025-09-17 13:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 8b909e16-4533-3e8e-818a-38128422850b | -7.6574 | -44.4667 | 2025-09-17 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ab4243fd-1106-3dd2-98f2-3388893dd4d9 | -8.4467 | -47.692 | 2025-09-17 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 5c057f67-86d5-3692-a96e-a8c41493f1e7 | -11.5779 | -48.2706 | 2025-09-17 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 57adb7b3-61c0-34cf-b207-684aadf197b4 | -8.5609 | -47.5712 | 2025-09-17 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ef042f68-a4b6-3b99-8c9c-45bbe4510fca | -8.9728 | -46.263 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 012c47b1-f570-3933-b84a-9d24aeb8b010 | -12.729 | -48.0068 | 2025-09-17 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 73110af5-ccd3-32b6-aaf4-79eff173ea0d | -8.6885 | -46.3823 | 2025-09-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 201.4 |
| e44b4370-1b08-3f9a-ab7a-ef5415e44eac | -8.0597 | -45.4544 | 2025-09-17 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 39be02ce-f10a-30d3-b952-e038494694ac | -6.8734 | -43.9636 | 2025-09-17 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 6c603996-ca48-3bab-9f1e-2d5f648e9b56 | -8.6887 | -46.3599 | 2025-09-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 599a291c-50f5-3866-9fd2-037d494b37f4 | -7.5807 | -44.589 | 2025-09-17 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| b00d8bc0-d16a-3b0f-8cb0-aed195cf2e64 | -6.2055 | -45.1187 | 2025-09-17 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c8ea90c6-0c97-3111-9cf7-89154f5b24da | -12.0047 | -46.6989 | 2025-09-17 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 512.5 |
| a9c6dd2f-2ecc-367b-a21c-dd2d58d43b75 | -6.6129 | -45.584 | 2025-09-17 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| fed2e3b1-a700-34e9-a0c5-0de09cb73c60 | -11.5775 | -48.2926 | 2025-09-17 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 44800a47-85b1-3f3b-a6d5-d47fd89133a5 | -8.9445 | -45.5438 | 2025-09-17 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 263.2 |
| bfb1dac9-d64b-35b6-aacd-a7d8155bc127 | -15.0549 | -42.4653 | 2025-09-17 13:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 6923fe12-3d34-322a-b88b-f0729b62fb23 | -9.1236 | -44.8849 | 2025-09-17 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 66c9503f-5888-385a-b50f-6389f85d864d | -8.9725 | -46.2854 | 2025-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| ea91e840-cb3b-3477-a995-932793ab1f0d | -9.1236 | -44.8849 | 2025-09-17 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 52296b84-f494-34ab-a91c-679ac446d73b | -8.6699 | -46.3618 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f5af4080-c0b0-3758-b39c-3919beb32658 | -5.7671 | -43.9392 | 2025-09-17 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 0606f756-0269-30a8-9cc3-0def44a253bc | -7.5227 | -44.7321 | 2025-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 53c61178-0907-3139-b19d-1347653dfcf3 | -14.6138 | -46.4036 | 2025-09-17 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2ae3f5aa-e42f-39ef-814b-275a2862cadc | -8.953 | -46.3324 | 2025-09-17 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 278c3862-4dee-3e55-bd0d-4445246fd680 | -12.729 | -48.0068 | 2025-09-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 85c3155e-1e7f-3075-a01d-6a88f1754367 | -12.0243 | -46.6736 | 2025-09-17 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f8e73d25-3f3d-324f-b0ba-0ccb5be22d61 | -15.0549 | -42.4653 | 2025-09-17 13:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 591bea2e-777c-3933-9dae-2d12eeef7e4d | -13.9648 | -44.9445 | 2025-09-17 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 89374c8e-71f3-35af-a50f-30a1d6bb2580 | -8.9449 | -45.521 | 2025-09-17 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 327.7 |
| a0657324-4bb8-3868-8be3-567c6ad02c5f | -3.8042 | -44.1072 | 2025-09-17 13:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 2a182ff8-0d52-31df-a0c1-340ec6277f8f | -6.6127 | -45.6066 | 2025-09-17 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 19f9932a-491c-38fc-a74a-2b603ba4c87c | -8.6885 | -46.3823 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.3 |
| e327ef4c-4e28-3447-8e2f-782c77336ba4 | -12.7482 | -48.0041 | 2025-09-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| e9a359a0-8547-3bb4-90c3-2b83f75b4b1d | -8.1572 | -46.747 | 2025-09-17 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 52feff1c-c5e2-31e4-b5e9-9d7d08e23686 | -8.9259 | -45.5231 | 2025-09-17 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ca43ec5e-9b42-34e5-878c-139966fce487 | -10.33 | -46.6025 | 2025-09-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 0c572b03-49cf-3b23-bc5c-1997410d7145 | -6.6129 | -45.584 | 2025-09-17 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 77ce1959-088e-3b6b-9c3f-164c2ce46b82 | -9.0851 | -44.9352 | 2025-09-17 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| dc20a2c9-cff3-384d-b485-024850d2171b | -7.4688 | -46.1854 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |


[Clique aqui para ver as próximas entradas](README63.md)
