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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5eca7658-0d1f-3ed8-a363-bcc16a06dcaa | -4.1223 | -54.0158 | 2026-09-13 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| c5ba321a-1659-3c61-bd4a-f3faa363f70a | -6.3015 | -59.9387 | 2026-09-13 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 58ed97fd-d8c7-3c09-9751-679a856b4d86 | -6.9367 | -55.636 | 2026-09-13 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b7f91df2-213a-3c3d-832d-a0333518fec5 | -6.7172 | -50.4733 | 2026-09-13 15:40:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 807cf7ee-c6f5-34a4-ade1-45a455492742 | -1.3007 | -49.1464 | 2026-09-13 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ed5cfbba-48dc-3068-8b7f-2232946b8a6d | -13.3754 | -51.7406 | 2026-09-13 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 388264aa-690d-3b28-a8c9-bf7f53bdd131 | -3.354 | -58.1961 | 2026-09-13 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9b776d22-af99-394d-ac00-1a2de6e818d9 | -4.1307 | -56.3434 | 2026-09-13 15:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7b2906ea-3804-38cb-8b61-91d2efc18f03 | -2.6602 | -57.5313 | 2026-09-13 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f65e1099-3960-3db4-9092-a4b67755957a | -7.12 | -42.107 | 2026-09-13 15:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 151.8 |
| ffef1f77-a7a8-3f0f-9d4d-29828a553430 | -7.5394 | -44.9133 | 2026-09-13 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| b5741672-ae5b-3820-a435-21960c66bef5 | -13.4507 | -48.48 | 2026-09-13 15:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 129.9 |
| ddde3625-d8f6-3e85-99fa-4e60451de436 | -3.6076 | -59.0769 | 2026-09-13 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 201.6 |
| 0c7664fe-9e68-3014-9349-d64265c7d61d | -10.8413 | -50.5859 | 2026-09-13 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9ffe8be2-d591-3188-a544-745fa2b7c159 | -9.3763 | -50.1139 | 2026-09-13 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 0c168a65-dbed-3f16-be88-5d0a71bdd8bc | -3.4242 | -59.2151 | 2026-09-13 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 15d66b7d-baf9-3033-8e31-07000811a49f | -2.7149 | -57.608 | 2026-09-13 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ba22ab76-1912-3aa1-9a18-ec51086f0056 | -6.1231 | -55.6359 | 2026-09-13 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 867d7b2c-af0a-3965-8710-1432bde97ee0 | -3.4058 | -59.2538 | 2026-09-13 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 2eb5852e-4ca0-33f8-a3eb-6751beddce9f | -13.4085 | -54.6009 | 2026-09-13 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ee3ba5b6-8ccf-38df-9f2f-48505c5e9e2c | -3.8461 | -58.9178 | 2026-09-13 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 866d8a5d-4433-3bff-aba8-fca2da17a30a | -1.4486 | -49.0166 | 2026-09-13 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7b2a7590-091e-3827-b401-9e936a380573 | -3.4058 | -59.2347 | 2026-09-13 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8266ffbc-584c-3d67-b97b-1f4321176276 | -3.8462 | -58.8985 | 2026-09-13 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 50ac9e9a-4836-37d1-aa5b-6f797548755a | -10.9861 | -49.7131 | 2026-09-13 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 75092aa9-00cc-3a6d-999d-1f86c5e33ed0 | -3.7181 | -58.863 | 2026-09-13 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ff567491-9dd8-3ad3-b184-7a256010a683 | -10.8223 | -50.5879 | 2026-09-13 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| bcf093c9-0d89-36d8-8d33-d38c3acdf7ca | -11.4905 | -50.2581 | 2026-09-13 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8722aafd-d146-3568-ba13-773c67f0a689 | -2.6602 | -57.5119 | 2026-09-13 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 3ac974d5-6364-3acb-bd96-3ef2895bf6aa | -12.6824 | -54.6968 | 2026-09-13 15:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a1e9d310-6101-3dba-971b-67f162e29ed9 | -3.3687 | -59.427 | 2026-09-13 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c0814959-0b09-3675-a6e4-83f9f32019af | -2.6785 | -57.5115 | 2026-09-13 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 3c1ac4d7-3e36-3351-8cbe-7c8394b020cc | -6.8632 | -55.5601 | 2026-09-13 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 76cb0451-9abb-3e8e-a8ba-d35d58e647f7 | 1.0951 | -50.957 | 2026-09-13 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0eab4dc3-2263-30e2-9d67-2b8760c83bbf | -10.6829 | -54.1475 | 2026-09-13 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 487.8 |
| 2248595f-dac2-3d2e-ab29-b251cb2629c1 | -9.376 | -50.1352 | 2026-09-13 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| aa31445a-9042-33dd-a4c2-52f57eebfdd3 | -1.7133 | -54.9521 | 2026-09-13 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 774d8780-df32-3490-a22e-83be47441292 | -7.8715 | -54.7016 | 2026-09-13 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6fac1c83-2439-32e9-a295-0a3e2775c0b7 | -3.6077 | -59.0577 | 2026-09-13 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 55d9d718-2dde-30ab-9fbd-4f3ff0aaf200 | -8.6005 | -44.4378 | 2026-09-13 15:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e83d6943-6551-3013-98f5-6727f7a0bcc9 | -2.7149 | -57.5886 | 2026-09-13 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a24c6b9a-3ac8-36da-b691-6b0bc63ec7b1 | -6.8445 | -55.581 | 2026-09-13 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 275.5 |
| 6010f930-a36b-35c4-9aea-9ef4ac966cb2 | -3.6075 | -59.0961 | 2026-09-13 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| acf83243-912f-324d-8bfd-b18edf71518c | -9.6971 | -47.1668 | 2026-09-13 15:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 729a6a87-446d-3712-aa67-3ef75b27c5ea | -13.3761 | -51.698 | 2026-09-13 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| eaca1109-514c-3690-9eb1-aded15845a96 | -13.3758 | -51.7193 | 2026-09-13 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 78d874dd-461a-34f9-befb-29985803f7e3 | -2.6785 | -57.5115 | 2026-09-13 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 0473aef6-c99a-3c10-b229-09f75323e499 | -3.8096 | -58.8994 | 2026-09-13 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c79dbfdf-f01d-3d1a-ab72-82253945e216 | -2.7332 | -57.6077 | 2026-09-13 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 675cb0a4-6ae4-325d-bac7-7b4799ded99a | -3.8278 | -58.9182 | 2026-09-13 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7101c94d-0208-3c9e-a7bb-2aa9719ef390 | -3.8461 | -58.9178 | 2026-09-13 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| a935c1aa-1910-3999-aff9-c836b8876582 | -8.6383 | -47.3875 | 2026-09-13 16:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 8af2310a-d611-3ca6-a253-2d71a5721897 | -3.1998 | -61.161 | 2026-09-13 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 91a51850-a4c4-38c0-8d62-45d0ad3567a9 | -1.3007 | -49.1464 | 2026-09-13 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 53980233-f0df-37a3-96a5-60abb97c3f49 | -7.5394 | -44.9133 | 2026-09-13 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 015c416a-be9e-3f3c-98f5-80e389469afc | -10.8223 | -50.5879 | 2026-09-13 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 242.4 |
| de625ecc-7e2c-3141-a1a8-84baaa393b0d | -7.12 | -42.107 | 2026-09-13 16:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 236.7 |
| 5ff82930-5203-3059-a1ce-6c5fe7075cf5 | -6.8445 | -55.581 | 2026-09-13 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 6304615e-fc1e-31fa-acf9-aded26103ad4 | -11.4905 | -50.2581 | 2026-09-13 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 184.1 |
| f8efdc25-cbea-3cfe-a64b-ece42ab6bbb1 | -6.7515 | -55.6455 | 2026-09-13 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 02047200-a097-3204-9fcd-3d1628f38445 | -9.3951 | -50.1121 | 2026-09-13 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| ea252744-ac65-3768-81da-9ea744273d03 | -2.7149 | -57.608 | 2026-09-13 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 57d9e23d-2e8a-3113-a5e5-e2201f1d838d | -10.8028 | -50.6326 | 2026-09-13 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 3574d54f-2c6a-31b5-8295-63b22a15d0de | -3.6077 | -59.0577 | 2026-09-13 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2448510c-9c5d-325c-9a21-ce79120f3908 | -3.1697 | -58.6437 | 2026-09-13 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 1a1ca085-0832-319e-bb45-b40cea17b994 | -12.6826 | -54.6763 | 2026-09-13 16:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 2b53e4b6-0416-3534-ada5-e04b09cc1f33 | -3.6076 | -59.0769 | 2026-09-13 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 80349a4f-fc98-35e4-a07e-dd31bca49fcc | -9.3763 | -50.1139 | 2026-09-13 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| e5516a46-3ca3-3c45-b52c-cac53cf7ac98 | -7.8715 | -54.7016 | 2026-09-13 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ad2dffd4-510b-39d2-89f5-135ffb9edd69 | -9.3948 | -50.1334 | 2026-09-13 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 286.2 |
| 6e9398aa-15f8-3eec-97c2-ef4858c16832 | -12.4945 | -47.1694 | 2026-09-13 16:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 70af380f-a40d-3054-8663-a3781eaca15c | 0.1747 | -51.4805 | 2026-09-13 16:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 2a4ec61e-fb7a-3225-abd2-f6bdf7adea2e | -8.0376 | -54.8523 | 2026-09-13 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 59fa6e67-d072-3e56-9d67-d3353b06565b | -4.1307 | -56.3434 | 2026-09-13 16:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 252f3532-b896-38b9-a06e-057b4693e6f6 | -2.7149 | -57.5886 | 2026-09-13 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 66f42847-e37a-323c-a110-bac363d08552 | -13.3391 | -51.6176 | 2026-09-13 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 40730be5-0965-32ef-9f9f-a83197c32d28 | -3.8279 | -58.899 | 2026-09-13 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 28b46818-26e7-322d-bc67-b208be983962 | -3.6998 | -58.8634 | 2026-09-13 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 362f8cd3-1f65-3eb0-9fb6-37ac04d517ba | -2.6602 | -57.5119 | 2026-09-13 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 74042b00-c3ed-32a0-b2fa-b218b0b3f5be | -3.4058 | -59.2347 | 2026-09-13 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 66258570-9638-3a49-bc48-14921401b326 | -2.7331 | -57.6271 | 2026-09-13 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 32ec7800-a989-3c23-b795-21bcf12dd614 | -3.4058 | -59.2538 | 2026-09-13 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 438472c6-7d7e-3f06-a556-a3c05e6de1cb | -10.9861 | -49.7131 | 2026-09-13 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 87edd88f-bbfc-3857-a1e2-cb4bf4b9f5b1 | -9.3765 | -50.0925 | 2026-09-13 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 64fe9bd0-5d1b-38a1-b027-e81e4ae66b6b | -3.4058 | -59.2347 | 2026-09-13 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 61d53166-ab30-3fec-ad69-2307afe8d33b | -7.8715 | -54.7016 | 2026-09-13 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| dca844f2-3ee1-3cd2-89f0-3aadfb1cfcfb | -2.6602 | -57.5119 | 2026-09-13 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 379b8a9c-5252-3132-a03a-6736bebdcd40 | -1.3007 | -49.1464 | 2026-09-13 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| dcc566d0-280d-3648-bf01-2a03fad9fee8 | -13.3387 | -51.6389 | 2026-09-13 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 17eaba40-af1a-31a0-980c-73fccde4fe0c | -10.6431 | -45.9999 | 2026-09-13 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e6783fdb-219e-3ac4-9b0e-63195086693d | -3.8096 | -58.8994 | 2026-09-13 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3c1203a2-4154-35b7-b3a5-0e9055b6dbed | -3.7181 | -58.863 | 2026-09-13 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 0d182b88-46b9-39cf-8913-75309eb61da6 | -3.1814 | -61.1802 | 2026-09-13 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 27bee7e6-28ff-3d97-ba8b-144eab076617 | -6.6334 | -45.4018 | 2026-09-13 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5cf40ebe-172a-37f0-afb1-39a70411ce09 | -7.5703 | -57.6962 | 2026-09-13 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e68819d2-b2b6-38d5-89a9-b7a26c0d36a8 | -13.3391 | -51.6176 | 2026-09-13 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 14e29bde-b222-34ac-8cb5-e15686cd677d | -12.6824 | -54.6968 | 2026-09-13 16:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 9e8742c5-9f37-3c5c-b53b-299468ff7ee3 | -10.8223 | -50.5879 | 2026-09-13 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 84ebebb4-f9b1-3e1b-9817-0277e65bc6b0 | -11.4905 | -50.2581 | 2026-09-13 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 990f8f96-0d2b-39ee-9619-7106a02e3e44 | -9.6755 | -46.0047 | 2026-09-13 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |


[Clique aqui para ver as próximas entradas](README71.md)
