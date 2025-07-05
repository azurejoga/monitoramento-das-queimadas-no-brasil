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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ef164a3-cd1f-354a-880a-6cf01b5486df | -5.06916 | -43.72587 | 2025-07-05 05:44:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3cdf4a96-1944-3584-945a-1a24572aa6ee | -8.09194 | -45.39112 | 2025-07-05 05:44:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7c59f642-2346-38e9-b642-891b48ffce25 | -9.84255 | -46.47146 | 2025-07-05 05:44:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6afc8f8d-4687-36b0-8a35-c4c75557f928 | -7.24935 | -43.0879 | 2025-07-05 05:44:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0d3dcb63-98e9-3b2e-8b84-121b02eeb3bc | -6.80113 | -44.7518 | 2025-07-05 05:44:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 63863b64-5f74-32cb-86c6-51f9ab308c29 | -3.52454 | -48.42857 | 2025-07-05 05:44:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e875306e-cd65-31d0-bf42-2e77edce8ed7 | -4.11247 | -47.93219 | 2025-07-05 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6ab87909-bcf9-3136-96a8-c8c45c37e1d9 | -7.18743 | -45.32332 | 2025-07-05 05:44:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f59d584f-9d16-30ae-8294-10398d2d4778 | -7.24124 | -43.07578 | 2025-07-05 05:44:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 61768883-45fd-379c-8ffc-b1200e985ff7 | -5.06778 | -43.73532 | 2025-07-05 05:44:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c42f46a3-dd7c-3e7b-9b67-b168751a94c8 | -7.89586 | -63.03981 | 2025-07-05 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4067829a-7c8f-38bb-aaf5-5bcc6b745ee3 | -7.89038 | -63.04425 | 2025-07-05 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fc7e7c3-fd2e-3722-b150-b501ecd5fecb | -8.9798 | -68.97429 | 2025-07-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecf7bb0e-c486-335f-b202-3124eeb8f4c4 | -10.30194 | -57.13641 | 2025-07-05 06:01:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d618152-341e-3e19-b113-d3d2192a84fa | -10.75307 | -69.37816 | 2025-07-05 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6ab789e-bebf-3466-af48-b264bcd2f2f3 | -10.20073 | -68.43896 | 2025-07-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9b1b05c4-a5cc-3044-b836-27f1394caa08 | -10.20014 | -68.44292 | 2025-07-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94e5eb77-6e51-36f6-8a9c-ed97d2aa38e4 | -9.51175 | -65.58714 | 2025-07-05 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ad8235-4721-3949-8c5c-1d8ddccbdc48 | -9.91712 | -59.90953 | 2025-07-05 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3eec3334-b2bc-35ba-bfb4-176c47fed058 | -12.0199 | -63.78311 | 2025-07-05 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5b5a17f-4409-39f6-87d0-6fba5d159c2e | -9.79273 | -64.7654 | 2025-07-05 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1740cfe2-67ad-3085-88f3-069aeb9f9bc1 | -9.63243 | -61.46239 | 2025-07-05 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd04adf3-89f2-3e83-8c90-5c5ae3395778 | -9.50766 | -65.58656 | 2025-07-05 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 427addfb-0107-3ae4-b811-a01c701c9d99 | -9.92316 | -59.91027 | 2025-07-05 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d1180bd-add3-3542-a3f7-2c14a853e22a | -9.63196 | -61.46592 | 2025-07-05 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05b9bb52-f335-323b-8d97-bafb016f125f | -22.1473 | -52.9708 | 2025-07-05 09:20:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| 97553116-791e-35c9-9a08-49f9346f66d2 | -22.1473 | -52.9708 | 2025-07-05 09:30:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 157.2 |
| ac7f7389-cbaa-377d-98c2-9a25a3b6b8e5 | -22.1468 | -52.9931 | 2025-07-05 09:30:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| c7b47de8-ba46-3135-8b49-3ab6b1cbf9b0 | -10.4718 | -42.4839 | 2025-07-05 10:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 16bc4977-bbcb-3a94-8abc-39152ed847f0 | -10.4722 | -42.4598 | 2025-07-05 10:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 160.5 |
| 2735c68d-0ee7-3cc6-893e-a463a0cecca6 | -10.4674 | -42.48771 | 2025-07-05 11:30:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 171.3 |
| 7e3bf656-298c-3128-b1ee-db4e81dba897 | -10.46927 | -42.48197 | 2025-07-05 11:30:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 300.0 |
| 2a4f1222-68ec-3de8-bc5e-c382b1eb3332 | -10.48756 | -42.46059 | 2025-07-05 11:30:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 976eb562-28cb-3459-93c4-5c830148121b | -6.68095 | -43.16238 | 2025-07-05 11:30:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 6792ba01-0896-3cdd-979c-5fb31285e716 | -6.48934 | -37.44376 | 2025-07-05 11:30:00 | TERRA_M-M | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 55a1329f-4eec-3bdd-acbb-27d5a020e42c | -8.85627 | -44.15496 | 2025-07-05 11:30:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 4311b05e-3e02-3456-88bd-9ebf41296c9c | -3.4838 | -48.4497 | 2025-07-05 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 0c52bc45-6df0-3e1f-99e6-066de2694c01 | -7.2791 | -44.6633 | 2025-07-05 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 4cafadfb-2b03-3f5b-a396-66117828df8d | -3.4838 | -48.4497 | 2025-07-05 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f42518c1-1b6f-3078-a2dc-10a9a57e2476 | -5.6065 | -45.1852 | 2025-07-05 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 584701f2-0486-3310-93a4-b076802afce2 | -10.4718 | -42.4839 | 2025-07-05 12:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 109.5 |
| ffd31698-3c9c-3794-a6b2-fca258293eef | -5.6065 | -45.1852 | 2025-07-05 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f6a7a498-a2ff-3977-b787-81f650c3e705 | -8.0794 | -45.3844 | 2025-07-05 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| dd6b4f41-e279-3ed2-b4be-5c0b003a1aab | -8.0979 | -45.4053 | 2025-07-05 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| b0ff5adb-f5b6-3855-83a1-9c7aa3878761 | -8.0982 | -45.3826 | 2025-07-05 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 9e177834-02ab-31fc-bbbe-37c8fa0b1909 | -5.6065 | -45.1852 | 2025-07-05 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9e9ce625-c7df-3e27-afe5-71d47be5f140 | -8.0794 | -45.3844 | 2025-07-05 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 392df9c4-beb7-3fef-a724-f77760720250 | -8.8066 | -45.9882 | 2025-07-05 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 1fc312d8-0888-3af5-92c8-75425ee0bc2b | -5.6065 | -45.1852 | 2025-07-05 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| cc5c68fd-0a62-3c52-8434-46d74af3a83e | -8.0982 | -45.3826 | 2025-07-05 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.1 |
| c16d55dc-e868-315a-b6e8-d59f5dd8394c | -8.0979 | -45.4053 | 2025-07-05 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 6663d5b7-94ba-3029-a589-5daf7ae52c7f | -5.6065 | -45.1852 | 2025-07-05 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| e447cd81-360b-35e0-888f-5a6a893339e9 | -8.0982 | -45.3826 | 2025-07-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f49bebff-12d8-376e-936f-3fd847be7578 | -5.6065 | -45.1852 | 2025-07-05 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 9e8d131e-88f5-3f3f-b04f-338e910cf253 | -7.6588 | -44.3515 | 2025-07-05 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 344d53d7-67d8-3236-9a41-e230a2aed5ec | -8.0982 | -45.3826 | 2025-07-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| dbadfccb-eedc-3d06-bdee-9da129f96d5b | -6.7134 | -43.1161 | 2025-07-05 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 50edd358-dd29-35c0-ad42-a41d4d26493a | -8.0794 | -45.3844 | 2025-07-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ab6fc6c1-64b2-33ae-8032-bb7d9d5131c4 | -8.0982 | -45.3826 | 2025-07-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 197.5 |
| da89eb2a-4649-3af7-a7cc-57b24e126702 | -8.0979 | -45.4053 | 2025-07-05 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 07076242-3015-3fbe-82ba-91d4ae13d54f | -5.6067 | -45.1625 | 2025-07-05 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 418e763a-dc6b-322e-8548-a5e1557f7219 | -5.6065 | -45.1852 | 2025-07-05 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 7bcf5dec-106f-3de1-887d-7f20203bb708 | -5.6065 | -45.1852 | 2025-07-05 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| ff8b3feb-2265-3d26-890d-1b015ad8e617 | -8.0982 | -45.3826 | 2025-07-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| bb92c724-1367-3092-87c9-f83036cbad2b | -5.6067 | -45.1625 | 2025-07-05 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9d1870aa-e37e-3140-ab4c-b951962bcdf4 | -8.0982 | -45.3826 | 2025-07-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f32d2fce-f25c-3dba-aeda-ab4eb6de1ea4 | -4.5071 | -47.7998 | 2025-07-05 14:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e7ac2ace-8b88-3865-918e-7b2d1ee29319 | -5.6067 | -45.1625 | 2025-07-05 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9a326ba2-7a53-3e94-9a6c-405952567bff | -5.6065 | -45.1852 | 2025-07-05 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 69aff3c9-c77e-371c-8694-95071d2097b6 | -5.6252 | -45.1839 | 2025-07-05 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |


