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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c375c6aa-4fce-3306-be5f-61c0b877e4a0 | -3.897 | -46.652901 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30fb6da6-e15a-334d-ae55-41d2c547d669 | -2.7999 | -53.032902 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9690dae3-a5a8-3aad-ab48-97bd909645f3 | -3.2422 | -50.399399 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608d36e2-e99c-3dc2-9095-dac4acecd956 | -2.6423 | -46.5732 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c0ad6b23-f6db-3bee-84be-87e983d5490e | -4.0494 | -46.597599 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3a66900-9ba8-3b25-a6e8-f158642260b1 | -3.9234 | -52.369598 | 2024-12-04 00:17:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7988af74-6313-3ae8-8790-60de9d4b047b | -4.0449 | -46.806198 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 845442c4-ace8-3d53-b96a-c8b0f9bd3832 | -2.6272 | -45.731998 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cefb4b38-f7ff-3e8e-9ab9-a89d4869c81a | -4.5866 | -45.463799 | 2024-12-04 00:17:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49972449-c4bb-341e-9eb1-1ecd7e1817a0 | -4.069 | -46.593201 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b63d1fc-c9ef-3fa5-929b-33a2db9e2849 | -3.9687 | -46.651299 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 128270bb-eeee-3a5e-b9b0-711b36c60a1a | -2.8069 | -53.0186 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa2fba52-2760-34ef-bf36-e4af133aaae1 | -3.0285 | -49.485699 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd794247-1cbf-33a6-982b-9a213676b899 | -2.678 | -46.594101 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc95538-49de-34a6-9480-106763a4c536 | -2.0959 | -46.572399 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c6db1ad-8cf2-3afd-a785-b5afc964096b | -3.7314 | -47.565601 | 2024-12-04 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d0097b-e5be-3fab-bc1d-5c496335e21d | -3.7981 | -50.961498 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5f5134-c049-3e35-9568-29bfe792ebb8 | -4.0577 | -48.333302 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30d24c31-02ff-31ac-ace0-98a8ca3d60d2 | -3.1082 | -54.570599 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2dab5d8-ecdc-30bb-9a95-70ce927119b4 | -2.826 | -46.747501 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86795c06-3e77-3611-9ad5-86994abd51ca | -3.0184 | -45.503101 | 2024-12-04 00:17:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab4cb1a-805a-381c-8008-1290baefd34a | -3.566 | -50.284 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5caf0a7a-8859-3097-9e51-4bc988a387fa | -4.117 | -46.897701 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f084d48-ad5c-3a57-9575-23ede3d8bcb1 | -2.7227 | -51.806099 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36ecb330-ccb3-38b1-b97b-80ce1a704593 | -3.8153 | -51.6441 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa996d91-08ee-3344-b680-c9d7f485ddf5 | -2.1734 | -46.641499 | 2024-12-04 00:17:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7b829ce-6007-39df-a3f2-f3822fcf0700 | -3.843 | -46.550301 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa04550-a0d0-3e4b-aafd-999b0f099992 | -2.8937 | -51.790199 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 582341c5-b188-3076-b525-1d3448607329 | -3.8423 | -52.139702 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23f83bce-abde-39a1-bd97-8a17e568a668 | -5.5646 | -45.1404 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d58a49ce-a5c0-3b2f-bbbd-4669057fc5a3 | -3.8347 | -50.8951 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09fc5c23-387f-3b4c-a2fc-1147e7e95144 | -2.8167 | -53.016399 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dac73aba-2064-333e-a1bf-f95b5d898367 | -5.8106 | -46.456699 | 2024-12-04 00:17:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43420d8a-a854-385f-b8c0-d4892569a9c1 | -2.647 | -46.5937 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc52e54-e129-3bbe-bc43-99f268621205 | -2.7326 | -46.243099 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afd0ba30-ee18-313c-b92f-b8857e804d57 | -3.7188 | -51.0672 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 372378e3-34e9-396c-bc1a-043bed8b47bb | -4.5309 | -45.900002 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4359107f-f3b9-321c-a497-2cb6c0374d9e | -2.5184 | -45.389 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d010743a-a990-3472-82a6-e6863e21242d | -5.811 | -44.096199 | 2024-12-04 00:17:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5f53453-efcd-3979-bf35-f026cef56487 | -4.0365 | -48.330399 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd78d1a-b5e6-3350-8931-c61bddbd563b | -4.1952 | -45.373901 | 2024-12-04 00:17:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d24708d-169c-32b1-afe0-334d21dd89c3 | -2.4698 | -46.5397 | 2024-12-04 00:17:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8270adb-9d3f-3a94-a68d-3046096c6a16 | -2.4714 | -46.546501 | 2024-12-04 00:17:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08764c79-496f-346f-95f4-3acd7be63b8e | -2.0202 | -46.328999 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d72daf81-134b-3f44-a357-2be213551442 | -4.0645 | -46.8018 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c490692-b4e9-3963-a765-f0bf9e7e023e | -3.6648 | -50.173698 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a816639-0fd7-3288-b03b-dee606230774 | -3.6044 | -50.781898 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b30956ab-d299-3b93-a245-4a555e043251 | -4.5882 | -45.470798 | 2024-12-04 00:17:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44bbf585-8a56-39c0-8287-3f2d17463dea | -4.0523 | -46.976501 | 2024-12-04 00:17:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85062c4a-78f2-3bf6-bf66-c058e6aee7fd | -10.9765 | -44.455601 | 2024-12-04 00:17:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f96514d7-3039-3c2a-b797-1c47f54cd671 | -3.8939 | -46.639198 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19a92ce6-2747-3b90-b85b-42feb538db53 | -3.8242 | -46.604599 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af5df7f1-f807-332a-b410-d15384858dc2 | -3.1019 | -54.588501 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1daf1f11-7666-3310-b68e-1b54cca9be61 | -4.3122 | -48.09 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4428e94e-e1ca-353b-88fe-fb4353ae4c6e | -6.2532 | -43.1502 | 2024-12-04 00:17:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 13664ed6-ae07-336f-989a-e3878c666331 | -5.576 | -45.145199 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e38e8918-379f-36e1-8866-d621d0d3493b | -2.9604 | -44.975601 | 2024-12-04 00:17:00 | METOP-B | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 763666a1-8fff-3f7f-99b4-ff5f2969152d | -4.2952 | -48.198399 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aff500a-121b-3107-9c6a-881daacc356c | -3.7401 | -52.421001 | 2024-12-04 00:17:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb64580b-d1dc-34ef-bb61-d980df428ece | -4.0693 | -46.686199 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39cfd146-50be-3e5b-bc6a-69293beded85 | -1.7016 | -46.195801 | 2024-12-04 00:17:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6546b064-70c5-30c7-abdc-d67191c8c298 | -1.6592 | -52.741798 | 2024-12-04 00:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 050534e6-cdcd-38f3-b9c4-c49ab0b3946d | -4.044 | -46.985401 | 2024-12-04 00:17:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de617b52-a7aa-369e-82ef-564e6948e5a2 | -3.1151 | -54.6022 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0778d8b5-7694-38ef-8b98-0ac118e92faf | -3.2608 | -53.592201 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 098065bb-b1a6-3b1d-879e-0d8095509c33 | -4.9181 | -47.8526 | 2024-12-04 00:17:00 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1a077a7-fb11-3f09-a4f0-1b78d8c2856c | -5.6957 | -45.0364 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08805b5a-8bf3-3d7c-9dad-578d93bee986 | -4.0474 | -46.8629 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 421e0829-93a3-3488-9f23-041fe1feaaf5 | -2.922 | -46.762001 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83047e76-2b69-3eca-89be-7645803dfe93 | -2.6008 | -46.207199 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da7e24f2-325c-378a-84ad-047f86dd0c58 | -4.8099 | -45.1763 | 2024-12-04 00:17:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0079a957-b78e-3e9a-8115-3e084f68c73a | -3.3086 | -50.420898 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74b48ea1-703f-32ec-84dc-49cdfede8fdd | -1.8554 | -46.3293 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10f97de3-9e8c-3580-b370-82892ff3b2db | -2.693 | -46.113899 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc4aa70-d2cb-30ce-82c1-fa44bc1695fd | -4.3083 | -48.210499 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed2bb392-6aca-3beb-b926-9b5c84932b05 | -4.6245 | -48.660198 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb6870a-c50c-38cd-95d9-9fa9da6b719e | -4.3204 | -48.080799 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12024b8f-c9a7-3212-885d-ca05c2edac4f | -2.191 | -48.320702 | 2024-12-04 00:17:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c176a90d-d731-3e21-816c-5755f42a1d96 | -4.0993 | -43.914501 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb78cc4-16be-3562-8376-c1be9a565bdc | -3.171 | -54.299099 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77a62276-6c5d-3a31-ac05-05aa85296260 | -1.244 | -46.5882 | 2024-12-04 00:17:00 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5866166-e9e6-30bc-bb35-cfab7c6f998f | -3.1214 | -54.584301 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57068dd8-0891-3dcc-9d3d-c2ae3725fd29 | -4.3236 | -48.095001 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d11d59-6ca3-3700-86fa-8798685ccfe1 | -2.5651 | -46.186001 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd2354b6-6288-3cba-9f1c-7f7e6f33d1a2 | -2.7901 | -53.035 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b24e36e4-701a-3779-ba1d-3d9fecf71479 | -5.5728 | -45.1311 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54553a38-9549-3cf5-9b33-b7849602855d | -6.0876 | -43.9533 | 2024-12-04 00:17:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0c83bee-c9b1-353d-a3a4-7447027ecff5 | -2.6098 | -45.2467 | 2024-12-04 00:17:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 647fc2c4-f797-33d6-ae05-de508d20f062 | -2.2377 | -46.105801 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0ab374-de1a-3245-b956-dbff9a8503f3 | -3.7231 | -51.226398 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4e505e-2ca1-3e18-8ec7-47e3d8a7bff4 | -2.5348 | -45.370201 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1415d00-ee26-3469-b5f9-dbe6c02e2407 | -4.1207 | -43.917999 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f346fec4-6d3c-36df-912c-d4b2943baae2 | -4.0761 | -46.670399 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 509f1a5e-f639-3148-b79e-07b3ac09af91 | -2.7472 | -45.261799 | 2024-12-04 00:17:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5020e2a-8bcf-31bf-8da8-9d23fbf99fa1 | -3.8954 | -46.646099 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc357b17-15d8-396a-b03a-7895bb5e5efc | -2.2024 | -48.3256 | 2024-12-04 00:17:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3343245a-8d0c-37a8-88b8-0f50134c9d08 | -4.1853 | -45.376099 | 2024-12-04 00:17:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3690c81-3e9e-38c6-b0e7-ffa6e967d9c3 | -3.2896 | -49.180302 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c73104cc-1a83-3dd3-aa16-316145039616 | -3.3337 | -49.747799 | 2024-12-04 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20bd44dc-d816-3e6c-a339-dc5dca7a55d5 | -3.7076 | -51.341801 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
