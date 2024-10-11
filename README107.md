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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9393af22-eca1-3046-9e89-a3f177f53cd0 | -6.75151 | -59.32766 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68410a56-3bdc-3081-aeb6-40d45a0a3c15 | -6.75092 | -59.3317 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64a251d2-5727-3b8c-b746-4ceb1b5ecf3e | -6.75033 | -59.33575 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d2b411d-6c77-383c-8604-fcb5e3c1d691 | -6.74779 | -59.32306 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 158e4678-5ca2-3e4f-be97-07288c0b23e9 | -6.74721 | -59.32708 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf760461-a4be-3de6-b89a-046b089a275e | -6.74662 | -59.33112 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8778ceb8-71aa-301b-b5fc-f4858a95351a | -6.7435 | -59.32238 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c62ce262-3633-3b38-8a28-6d1de416c5b2 | -6.7279 | -59.6652 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e33f3924-cbf3-39eb-b5a5-ec9b78c0f34c | -6.7269 | -59.3159 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cd7d2ff-388f-3343-89bf-aa9c3a34ee4c | -6.72632 | -59.31992 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8c364db-bd34-3b4d-927f-ce35de680415 | -6.69406 | -59.86464 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 988c187b-899b-3bdb-9c87-c6980725b889 | -6.68992 | -59.86402 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07448628-1044-35a0-8cef-de890844d502 | -6.68892 | -59.4285 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a739af85-8864-3a9f-94a9-136e5a62fa5f | -6.63562 | -60.06145 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37a0c595-99bb-3734-a949-42dabbb47d9c | -6.61081 | -60.00241 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79f34bac-bb8b-37ce-9179-6a6d9f30b8f7 | -6.6062 | -60.00538 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dca1aba3-4488-3eed-a8d6-bafc00599bc9 | -6.60262 | -60.00116 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f341946-d84e-3887-9750-26932351d0a8 | -6.55407 | -60.02799 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73f6a4dd-cead-370e-80e9-e3cedb4c1ff8 | -6.55354 | -60.03159 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96bbae88-902d-34b0-acdd-b7780d87497d | -6.553 | -60.03517 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 431fa43d-85ba-300f-8647-0a89b2a14a27 | -6.55104 | -60.02024 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d81825-8116-30fe-a1f3-441af3be1be7 | -6.55051 | -60.02385 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91aa9d55-aec4-3daa-987b-df3e0e25225e | -6.54997 | -60.02746 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10fa03e0-40c9-374f-8416-d7416e6a7b85 | -6.54944 | -60.03106 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73e3aca1-92a9-3ab5-8aa9-f9b0b96b8748 | -6.54641 | -60.02331 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f3a39e7-a0c2-3b2a-ac57-a46359ca70f9 | -6.54535 | -60.03053 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5b565c2-d1e7-314e-94f7-5fcdd1452927 | -6.54341 | -60.01538 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab702854-4a19-37aa-a65d-31c96ba31ccf | -6.54183 | -59.76652 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f1ff0b0-ac5a-366f-b90c-2db92b9d6d0a | -6.53822 | -59.76213 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee0c1efb-3dfa-36f3-9dee-7122870a78bd | -6.52426 | -60.06046 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ad7658b-f910-32d7-821f-40bacfee58eb | -6.51664 | -60.05563 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fe13b04-7492-3df6-b04a-58a301bb58a2 | -6.77941 | -60.04516 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4801f40a-39b5-3082-89d6-3a5c15451a75 | -6.77887 | -60.04875 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d4ab073-7cd2-3b38-b68c-92c33ca9a807 | -6.63616 | -60.05781 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a96edff1-2191-3b6c-ba89-ad860307109f | -6.52478 | -60.05695 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6296213-9878-3283-b4df-f14d8878c557 | -6.52123 | -60.05272 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baefba0a-e615-3821-a2f4-fd1af550948c | -6.52071 | -60.05627 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d98ca31-370a-3e46-b31b-71802e3f2221 | -6.5202 | -60.05979 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0552211-44c0-3912-b5cc-6a6167754be2 | -6.51613 | -60.05916 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16ed5267-87bd-3a33-a92a-325746b7e4b0 | -6.51038 | -60.09849 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 440dedf6-6171-33e7-ae99-324655d93e8c | -6.50631 | -60.09787 | 2024-10-11 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56a80c83-204b-372c-bef6-03e4f88922df | 0.83598 | -60.47307 | 2024-10-11 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62db3ae0-ccca-324a-948f-1f168d3b3e32 | 0.816 | -59.84757 | 2024-10-11 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5661864d-295c-3022-b81e-320ec53d5acd | 0.81227 | -59.84816 | 2024-10-11 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f3c251d-c85e-31a0-b6c7-cf7ac1c1616c | -1.44422 | -60.29252 | 2024-10-11 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbe7823f-da48-3931-877e-28f531410479 | -3.08786 | -60.29418 | 2024-10-11 05:40:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43c5d1d9-a91c-3cb5-8702-bd8999481bb2 | -3.11435 | -61.10019 | 2024-10-11 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f703111-815f-32b9-897a-12a31954abc6 | -4.7141 | -60.82034 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3854d9dc-a3f0-3c41-b060-086a80ea7ca0 | -4.71355 | -60.51379 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80d50720-a6a5-3f6b-9637-622f969d5b6d | -4.71031 | -60.81977 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37217bd6-bb03-31df-96d4-b0d56a9d9157 | -3.78112 | -60.12687 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf1d716-89e7-39b8-9fcd-63b84620a1d3 | -3.77771 | -60.1246 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37702b7e-b3b3-3882-991c-794fc17c5c6e | -3.77721 | -60.12626 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54ba6546-ed00-3755-a22a-629ccf7614f8 | -3.77695 | -60.12948 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b92cc1d6-136c-3672-86b2-57a43c6729cb | -1.92194 | -61.73092 | 2024-10-11 05:40:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e604038-9960-3c78-80f2-4804ba95a6e7 | -1.51447 | -61.59283 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aec3f30d-e812-334a-8b67-c8b049c54552 | -1.51096 | -61.5923 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9b5a157-1f49-374b-a252-1651df185c90 | -1.48931 | -61.59294 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8481c62-d6c0-370d-beb8-78a034d71296 | -1.48871 | -61.59682 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b7eb26-b941-3762-baac-ca9bad2785bc | -1.48866 | -61.59307 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6db90f59-fdb1-34d8-9b52-b86395cd5558 | -1.48812 | -61.60068 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac42d83b-6510-3f22-ad67-27319b58aed1 | -1.48805 | -61.59695 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 648ea18c-7e42-3922-acd0-c97bf8677af0 | -1.48744 | -61.60079 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3650f312-22ee-3827-9bd5-0b9b2f426ab3 | -1.48332 | -61.60412 | 2024-10-11 05:40:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a06ad31-1551-3b9a-9851-23fca9ad6d59 | -3.04752 | -61.67825 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f31bb023-fb8e-354b-9ab1-223b5132e93f | -3.04691 | -61.68224 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4551887a-9eeb-3275-ab57-7c5cb5a8bd23 | -3.04336 | -61.68169 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dcc4e69f-7bac-3984-956c-758bcf0c87f6 | -3.04274 | -61.68567 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e96c9d9-708b-3400-a325-29e3cf6b4627 | -3.03981 | -61.68114 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 884932bb-d857-35cb-9177-18bc89bdf5b9 | -3.03919 | -61.68513 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b13b278-7cb6-3d5a-ab6e-316d265de262 | -3.03626 | -61.6806 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2b4edb5-5845-3848-bf49-94c970a5e107 | -2.89462 | -61.87325 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9b11f25-c05c-355c-b921-6da1f48b8f57 | -3.28944 | -61.51103 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33183cc8-aec2-3e19-bac8-5107020eb4ae | -3.04629 | -61.68621 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b7be702-b7ca-317c-bdfb-355196495bf8 | -3.04397 | -61.67771 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d3c5b72f-f1eb-3169-a085-88d75c81686d | -3.04042 | -61.67717 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cd0154ff-3b9f-31d3-bc10-21d4940b53e7 | -3.03858 | -61.68912 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0043250-34a1-308b-97f7-a58a3e8e7e7e | -3.0018 | -61.41654 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c50bd81-430a-38f7-bdec-a3869ac04ec5 | -2.99821 | -61.41599 | 2024-10-11 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a809c3a-2718-32a1-bdab-51d1d437167e | -5.87192 | -63.91131 | 2024-10-11 05:40:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6204762-e159-3657-a765-e2d731503d0c | -8.70318 | -66.99901 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91e4119b-a8a8-31b2-863f-9cf73fada234 | -8.7026 | -67.00262 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3aec71e-e382-3bae-948d-d3987e58d2dc | -8.6998 | -66.99845 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f38ebdc6-5800-3626-8f24-c47b11cc3e40 | -8.69922 | -67.00207 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed32987a-2ef9-3f9d-8621-0aa9caff485e | -10.0993 | -67.35029 | 2024-10-11 05:42:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8908198b-57f7-39c9-a42a-e5b0fd280bdc | -10.0965 | -67.34609 | 2024-10-11 05:42:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55acbd65-20b2-3151-9abd-219f7fbef374 | -10.09192 | -67.13773 | 2024-10-11 05:42:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02247c77-fc61-3c57-94e4-3455bf9714c9 | -10.08856 | -67.13718 | 2024-10-11 05:42:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9499f1a1-1284-33fd-87e2-a1dcea3750e6 | -9.7538 | -67.56498 | 2024-10-11 05:42:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66ec0064-c8c2-3aab-8437-c4c67230cb62 | -10.85635 | -68.2823 | 2024-10-11 05:42:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eac7fa1b-270b-3381-904a-afdc47403ebd | -10.85572 | -68.28613 | 2024-10-11 05:42:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be2500a0-8ee4-3339-a47a-df33f4214ea2 | -10.48512 | -67.79676 | 2024-10-11 05:42:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42863016-8561-3583-9e71-d77f6958d14e | -10.46915 | -68.41407 | 2024-10-11 05:42:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d423717-7b62-3cfc-9684-ca4435007e18 | -9.62506 | -51.76361 | 2024-10-11 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fff06472-68f0-3c3a-bc15-246990ba0dbf | -9.6244 | -51.76585 | 2024-10-11 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 138936bd-c7f3-35f6-8507-b8811d1cd8b3 | -9.62418 | -51.77113 | 2024-10-11 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e7d50df-27b1-37cf-a0db-6404b8ae25d7 | -9.03824 | -52.94383 | 2024-10-11 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e146a3d-11ba-396b-a871-7f9045c0fea5 | -9.03756 | -52.9495 | 2024-10-11 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1afb7e3f-7239-3e33-a282-8e023f165250 | -9.03658 | -52.94409 | 2024-10-11 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f18d54bb-67a4-377b-825c-e63d59404c44 | -9.03588 | -52.94964 | 2024-10-11 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README108.md)
