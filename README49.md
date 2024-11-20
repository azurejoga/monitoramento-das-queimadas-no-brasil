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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e95c333d-94ab-3e6b-9889-88d71c217615 | -2.85538 | -51.59002 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccc39c5e-6c6d-3dc3-a892-a3e15866efca | -7.21896 | -45.07911 | 2024-11-20 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 359579b0-64c2-3b82-83e3-e3785f8b9be0 | -3.51655 | -50.22624 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e339c849-e8ca-3980-b17c-92af755ee4a3 | -2.76188 | -54.05685 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9efb614-b078-3453-be65-bf9e4706d5dc | -2.65941 | -46.23743 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a953822-7841-3b35-a839-035a92c87314 | -2.53902 | -54.28003 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b41126eb-0bc6-35f8-8da6-5b883d2131fe | -2.02022 | -52.07853 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50150be8-d336-3c7f-88f9-19e7f1a5dc6a | -3.74201 | -52.40488 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f2ba24a-6406-3bb2-a37c-063f7aab2500 | -2.14132 | -50.64491 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71c56a97-6eef-3a98-bc1b-944f8c94ce26 | -1.07748 | -53.18932 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 272b3ee1-84d9-3660-91be-09debd28426e | -2.92174 | -53.07389 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| aa1fc226-82f0-3c47-8bf3-87c07714ab1b | -2.15534 | -50.70789 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32c2e570-a77d-3585-8b5f-20598a68dd6f | -2.74668 | -48.57296 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a5d5f36-4b3f-3b23-a04f-e71679607238 | -1.78983 | -53.60907 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d0ba6d5-a4b9-3119-977e-18f2f11cc8ef | -0.93416 | -51.64589 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0123eb69-3257-34cb-ab61-fc8d6116aa8a | -5.06635 | -44.22568 | 2024-11-20 04:50:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f70f176a-506c-3b78-b8b0-d03f5db9a716 | -1.78636 | -53.60852 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03c672e2-731e-3c31-a8b5-c8e0ffaf407c | -1.78528 | -53.59282 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8d1fb2c-b758-3ea5-ac1d-ef9e5a3788a1 | -3.18501 | -54.32483 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afa9e715-fb29-3803-aefe-49d7dc890a55 | -3.22679 | -53.61693 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 542a02ce-06ee-3fee-b495-f5351587a592 | -2.60719 | -51.79152 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1974b00-463e-3a48-bd88-adcc09e7d8fc | -2.75715 | -54.06403 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4642959f-f63e-39bc-b1bb-d5184d805ab3 | -6.92644 | -41.19934 | 2024-11-20 04:50:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 449359e1-95cb-3ac3-8751-7160e40ef2c0 | -5.97747 | -45.3665 | 2024-11-20 04:50:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9411f986-d88d-341b-adb1-a6bbe56ae330 | -3.59426 | -43.62986 | 2024-11-20 04:50:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a56f76a-0772-3ba9-aed9-71e23f6eb847 | -1.97697 | -53.32681 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb50b33-62b5-3431-a899-b56b19df65b1 | -3.71715 | -53.3043 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f014806-050d-3ba9-bda9-6889b78187a6 | -1.41238 | -52.04718 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59df6cb8-7189-3e72-86ba-18b670ccba20 | -2.19854 | -49.54668 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4b5be00-47af-3e8e-89fd-0729c50d3a7d | -0.66712 | -51.66832 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2df31606-1f3a-3e6d-af0c-6fe998323134 | -1.13915 | -53.66572 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dab52c2-6950-37a5-9606-e41e5323a2d9 | -4.24966 | -53.66636 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2233019-90b9-37fa-bcc4-7d994a484693 | -3.04839 | -54.41308 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49fa9e7f-4cb3-3ca3-bd42-2ea391ba8f41 | -1.35683 | -52.54924 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e4e624d-ff1d-35ed-9eb1-d53c1df0945f | -4.13328 | -47.73545 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 477ab236-94ab-3f97-a4db-6ef439a6257e | -5.45403 | -49.68867 | 2024-11-20 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b05d4a68-3054-3538-8da1-0868ab2366c9 | -2.61606 | -51.79996 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 459d4623-d6d1-3abb-b5f1-c65dd6a8465e | -3.61262 | -52.11177 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9bc7f4d-94e1-3e13-8211-60d2326f3811 | -3.65723 | -49.951 | 2024-11-20 04:50:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 603ed08c-7fda-3c1a-8da9-e3d6979e4c23 | -0.66344 | -52.00919 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e84b92d5-2365-3191-81c9-91827f2d7024 | -2.08289 | -52.10965 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47fb884b-52f6-3e8c-a5fa-1be3b8233ce0 | -1.89897 | -48.51135 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c35a0ef-eccf-3a00-832e-20844ad28a89 | -1.31555 | -51.8722 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ea8def3-7b98-30a2-ba8d-1b118b080d51 | -1.99884 | -46.60078 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c146959c-4cf0-3313-90ae-86d0e6bbea24 | -2.11219 | -49.13563 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31afb42a-6589-396a-a0f8-820af1e24050 | -2.54108 | -54.55676 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3b995c0-ff78-334f-98b5-c122d94a7372 | -4.94686 | -47.80241 | 2024-11-20 04:50:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33538d2d-5b1a-3001-b2ac-3399803062e9 | -2.22029 | -46.48375 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9014877-b03c-39a6-8ccd-05c807a06050 | -1.21999 | -51.78993 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 200cf294-d4ac-3cb0-9959-f2d745911e18 | -3.50663 | -51.02096 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f4c8c6-1051-304e-9324-c3b9feb53a14 | -2.03012 | -51.17842 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65c65480-c308-3a6e-98c9-ca404b439a2e | -1.22041 | -51.74394 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0adf35d-2ea4-32ba-8bd4-6e2a0654433c | -1.53772 | -54.90252 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 867533cb-66b7-3e08-997b-830447f55a33 | -4.10018 | -44.8531 | 2024-11-20 04:50:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80656967-b4af-306d-8bc4-45bd2cb3405e | -2.72594 | -49.3394 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37035723-bb1f-33a4-82d1-7b66c92a78f5 | -2.9525 | -48.32874 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6bfa4d9d-cba5-3a2d-b82f-b0911db864fe | -1.5098 | -51.92719 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3596b117-c953-3aba-8df0-13319a3f61f0 | -4.63355 | -49.54222 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a366b5db-bbbf-3356-aac8-9fe40f44c8dc | -3.08681 | -54.66616 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58652eac-d5f3-388b-9cdd-83ecc69c0783 | -9.17423 | -44.72697 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84da0d12-3807-3e68-80ac-97d846df5fb5 | -0.41089 | -51.61743 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b820fde0-c50f-3172-b139-bf113685cd00 | -3.59469 | -43.62695 | 2024-11-20 04:50:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a8c66c-c008-37c9-9935-8274c48131e6 | -4.10799 | -51.04639 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 498ef785-540e-33a0-9cb1-d0e416a238e5 | -2.61969 | -47.96877 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8516b348-e508-3868-b8c6-3f588bdf3780 | -2.36088 | -46.18957 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 029c3cb0-772f-3bce-85a2-f51c46509a8b | -2.45256 | -49.14637 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3a16de4-2def-3346-966a-f081b26707b0 | -2.55926 | -46.54628 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aa867e6-4126-362a-95ad-b386e2f101ab | -3.29106 | -53.84816 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c28de5a0-8578-335f-a107-39a369069ffc | -1.72583 | -52.80021 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b17cadf3-4b2f-33ef-af43-6635023008b9 | -1.22144 | -51.94994 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c89299e-e280-3d20-b160-c6c0978ee17f | -3.82075 | -52.16536 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47ad13f5-c1e7-3dfc-a7bd-8109e977986e | -4.37007 | -50.73136 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfa68f7b-741b-37ad-8e5e-59f3b44e985d | -3.28076 | -53.83175 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 482e589f-619a-3fbb-9021-633b57a28e06 | -2.74993 | -51.8278 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| c270d7ec-b9e3-336a-bcba-b2d4cd00dd6d | -3.31679 | -52.07563 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a3fc0b2-9810-3cfe-b344-031506e4d189 | -1.58687 | -50.44433 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd79574f-e315-3fda-90c9-25021835af21 | -1.55533 | -51.22773 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 439ff1ec-c551-3cce-8094-8e4ce141d0f6 | -4.11951 | -43.58625 | 2024-11-20 04:50:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71c671a1-dc4b-3703-b0aa-16303cfdf186 | -8.73998 | -44.08804 | 2024-11-20 04:50:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1ee7682-8198-3a00-b55b-2ebcbe249202 | -2.71967 | -47.9731 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a875f60a-16a6-3403-b884-3626512c97af | -2.25695 | -48.9903 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d61462-e5c0-3516-b42e-47e8ef99402b | -4.96837 | -50.47543 | 2024-11-20 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463be317-2cd8-371d-9ac3-fe17a658828a | -2.99813 | -51.45676 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 530621b4-fc2b-37b5-8e7c-8c2302441d16 | -0.93139 | -51.64192 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02bbc9b1-9adf-3b6e-b3e9-9a1d8cd76b66 | -1.68058 | -50.71257 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f413ebd9-0148-3c35-8f28-27434bccbbf7 | -1.63067 | -52.404 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27ec62d3-0eda-368c-8319-8e4efb3424ac | -3.38745 | -44.4348 | 2024-11-20 04:50:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a20fab1f-d818-331e-89df-89b280934464 | -2.94817 | -48.33243 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb0128eb-ad9a-3554-8ae0-8f9b2eaa83e6 | -2.75365 | -54.06348 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21e4f33b-90c9-3d4f-976d-e8f3f4a7d506 | -1.14 | -51.69251 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdd26a1-b3bd-3e62-9794-6b889d4a4b20 | -2.85697 | -48.72684 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3df3e78-ea3e-3285-88f5-0b28cfc02481 | -1.19957 | -53.67455 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 897cde1d-0948-355d-8d05-4aced2a4b803 | -2.77018 | -52.59932 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f46235ba-f511-36f5-9e80-f0d2a1e9848b | -3.00292 | -51.01414 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c73fd4fc-a683-3161-a9ea-3f9970542972 | -1.6464 | -52.76959 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4305ab7-c177-3159-bf75-333d4331d1c4 | -5.59947 | -46.17587 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2763b719-ea26-3eea-b543-e1303a833a90 | -1.92496 | -53.34958 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b276fe2-1178-383c-8252-98af0729b15a | -1.1461 | -51.69699 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbe10446-efe4-3c31-9239-304ca4f0108c | -2.23559 | -53.61813 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81b6ab18-0c35-39b3-9eaa-b45c5ce83995 | -3.09458 | -51.3167 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
